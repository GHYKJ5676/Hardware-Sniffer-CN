# Source: https://github.com/corpnewt/SSDTTime/blob/7b3fb78112bf320a1bc6a7e50dddb2b375cb70b0/Scripts/run.py

import sys, subprocess, time, threading, shlex
try:
    from Queue import Queue, Empty
except:
    from queue import Queue, Empty

ON_POSIX = 'posix' in sys.builtin_module_names

class Run:

    def __init__(self):
        return

    def _read_output(self, pipe, q):
        try:
            for line in iter(lambda: pipe.read(1), b''):
                q.put(line)
        except ValueError:
            pass
        pipe.close()

    def _create_thread(self, output):
        q = Queue()
        t = threading.Thread(target=self._read_output, args=(output, q))
        t.daemon = True
        return (q,t)

    def _stream_output(self, comm, shell = False):
        output = error = ""
        p = None
        try:
            if shell and type(comm) is list:
                comm = " ".join(shlex.quote(x) for x in comm)
            if not shell and type(comm) is str:
                comm = shlex.split(comm)
            p = subprocess.Popen(comm, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0, universal_newlines=True, close_fds=ON_POSIX)
            q,t   = self._create_thread(p.stdout)
            qe,te = self._create_thread(p.stderr)
            t.start()
            te.start()

            while True:
                c = z = ""
                try: c = q.get_nowait()
                except Empty: pass
                else:
                    sys.stdout.write(c)
                    output += c
                    sys.stdout.flush()
                try: z = qe.get_nowait()
                except Empty: pass
                else:
                    sys.stderr.write(z)
                    error += z
                    sys.stderr.flush()
                if not c==z=="": continue
                p.poll()
                if p.returncode != None:
                    break
                time.sleep(0.02)

            o, e = p.communicate()
            return (output+o, error+e, p.returncode)
        except:
            if p:
                try: o, e = p.communicate()
                except: o = e = ""
                return (output+o, error+e, p.returncode)
            return ("", "未找到命令！", 1)

    def _decode(self, value, encoding="utf-8", errors="ignore"):
        if sys.version_info >= (3,0) and isinstance(value, bytes):
            return value.decode(encoding,errors)
        return value

    def _run_command(self, comm, shell = False):
        c = None
        try:
            if shell and type(comm) is list:
                comm = " ".join(shlex.quote(x) for x in comm)
            if not shell and type(comm) is str:
                comm = shlex.split(comm)
            p = subprocess.Popen(comm, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            c = p.communicate()
        except:
            if c == None:
                return ("", "未找到命令！", 1)
        return (self._decode(c[0]), self._decode(c[1]), p.returncode)

    def run(self, command_list, leave_on_fail = False):
        if type(command_list) is dict:
            command_list = [command_list]
        output_list = []
        for comm in command_list:
            args   = comm.get("args",   [])
            shell  = comm.get("shell",  False)
            stream = comm.get("stream", False)
            sudo   = comm.get("sudo",   False)
            stdout = comm.get("stdout", False)
            stderr = comm.get("stderr", False)
            mess   = comm.get("message", None)
            show   = comm.get("show",   False)
            
            if not mess == None:
                print(mess)

            if not len(args):
                continue
            if sudo:
                out = self._run_command(["which", "sudo"])
                if "sudo" in out[0]:
                    if type(args) is list:
                        args.insert(0, out[0].replace("\n", ""))
                    elif type(args) is str:
                        args = out[0].replace("\n", "") + " " + args
            
            if show:
                print(" ".join(args))

            if stream:
                out = self._stream_output(args, shell)
            else:
                out = self._run_command(args, shell)
                if stdout and len(out[0]):
                    print(out[0])
                if stderr and len(out[1]):
                    print(out[1])
            output_list.append(out)
            if leave_on_fail and out[2] != 0:
                break
        if len(output_list) == 1:
            return output_list[0]
        return output_list
import argparse
import HardwareSniffer
import platform
import sys
import os
import traceback

EXIT_SUCCESS = 0
EXIT_INVALID_ARGS = 1
EXIT_UNSUPPORTED_OS = 2
EXIT_HARDWARE_COLLECTION_ERROR = 3
EXIT_REPORT_GENERATION_ERROR = 4
EXIT_ACPI_DUMP_ERROR = 5

def main():
    os_name = platform.system()

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--export", action="store_true", help="导出系统报告")
    parser.add_argument("-o", "--output-dir", default="SysReport", help="自定义输出目录以保存系统报告，默认为 SysReport")
    args = parser.parse_args()

    if not args.export:
        parser.print_help()
        return EXIT_INVALID_ARGS

    if os_name not in ("Windows", "Linux"):
        print(f"不支持的操作系统：{os_name}", file=sys.stderr)
        return EXIT_UNSUPPORTED_OS

    try:
        h = HardwareSniffer.HardwareSniffer(args.output_dir, rich_format=False)

        h.hardware_info.hardware_collector()
    except Exception as e:
        print(f"收集硬件信息时出错：{e}", file=sys.stderr)
        traceback.print_exc()
        return EXIT_HARDWARE_COLLECTION_ERROR

    try:
        h.export_hardware_report()
    except Exception as e:
        print(f"保存报告时出错：{e}", file=sys.stderr)
        traceback.print_exc()
        return EXIT_REPORT_GENERATION_ERROR

    try:
        h.dump_acpi_tables()
    except Exception as e:
        print(f"转储 ACPI 表时出错：{e}", file=sys.stderr)
        traceback.print_exc()
        return EXIT_ACPI_DUMP_ERROR

    h.u.head("硬件嗅探器")
    print("")
    print("完成！请在 `{}` 中查看报告".format(h.result_dir))
    return EXIT_SUCCESS

if __name__ == '__main__':
    sys.exit(main())
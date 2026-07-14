<br/>
<div align="center">
  <h3 align="center">Hardware Sniffer</h3>

  <p align="center">
    它是 <a href="https://github.com/GHYKJ5676/OpCore-Simplify-CN">OpCore Simplify</a> 项目的关键组件，在简化与自动化硬件数据采集和分析过程中发挥着重要作用。其名称强调了“嗅探”出所有相关硬件细节的功能，从而提供系统组件的全面概览。
    <br />
    <br />
    <a href="#-功能特性">功能特性</a> •
    <a href="#-常见问题">常见问题</a> •
    <a href="#-使用方法">使用方法</a> •
    <a href="#-参与贡献">参与贡献</a> •
    <a href="#-许可证">许可证</a> •
    <a href="#-致谢">致谢</a> •
    <a href="#-联系方式">联系方式</a>
  </p>
</div>

> [!NOTE]
> 本项目已签名，以确保安全性和可信度。

<details>
  <summary>目录</summary>
  <ol>
    <li><a href="#-功能特性">功能特性</a></li>
    <li><a href="#-常见问题">常见问题</a></li>
    <li><a href="#-使用方法">使用方法</a></li>
    <li><a href="#-参与贡献">参与贡献</a></li>
    <li><a href="#-许可证">许可证</a></li>
    <li><a href="#-致谢">致谢</a></li>
    <li><a href="#-联系方式">联系方式</a></li>
  </ol>
</details>

---

## ✨ **功能特性**

- **全面的硬件信息采集**： 
  - 使用 WMI 命令行工具 (WMIC) 提取主板、CPU、GPU、显示器、网络适配器、音频设备、USB 控制器、输入设备、存储控制器、生物识别传感器、蓝牙、SD 控制器以及系统设备等信息。
  
- **创新的检测技术**：
  - 📌 **主板芯片组识别**：通过 PCI 设备信息，准确识别 Intel 芯片组型号。
  - 📌 **CPU 代号识别**：通过“Family x Model x Stepping x”识别 CPU 代号，无需查询 Intel ARK 或 AMD 网站。
  - 📌 **GPU 代号识别**：通过设备 ID 确定 GPU 代号。
  - 📌 **输入设备连接类型**：识别输入设备（如触摸板、触摸屏）的连接类型（i2c、PS2、SMBus、USB）。

## ❓ **常见问题**

- **是否支持 macOS 和 Linux？**
  - **macOS**：❌ 不支持。由于 Hackintosh 修改可能导致信息不准确，我们无法保证提供准确的硬件信息。
  - **Linux**：🔄 正在 [add-linux-support](https://github.com/lzhoang2801/Hardware-Sniffer/tree/add-linux-support) 分支中开发中。

## 🚀 **使用方法**

1. **下载**：前往 Hardware Sniffer 的 [Releases](https://github.com/GHYKJ5676/Hardware-Sniffer-CN/releases) 页面，下载最新版本。
   
   ![Releases 标签页](https://i.imgur.com/gAoVphx.png)

2. **运行**：执行 `Hardware-Sniffer.exe`。信息收集过程可能需要片刻时间。

   ![硬件信息收集](https://i.imgur.com/aDB0Wsb.png)

3. **主菜单**：数据收集完成后，将进入主界面，提供三个选项：

   - **T. 切换硬件报告视图**：在简略/完整视图模式间切换
   - **H. 导出硬件报告**：以 JSON 格式保存报告
   - **A. 转储 ACPI 表**：收集并保存 ACPI 表

   ![Hardware Sniffer 主界面](https://i.imgur.com/P0lP9pI.png)

4. **与 OpCore Simplify 配合使用**：依次选择 `导出硬件报告` 和 `转储 ACPI 表` 两个选项。
5. **结果**：输出文件将保存在程序目录下的 `Results` 文件夹中。

   ![结果](https://i.imgur.com/gxV4aLL.png)

## 🤝 **参与贡献**

非常欢迎贡献！如果您有改进此项目的想法，请随意 fork 仓库并提交 pull request，或创建带有“enhancement”标签的 issue。

别忘了 ⭐ 为项目点个星！感谢您的支持！🌟

## 📜 **许可证**

基于 BSD 3-Clause License 分发。详见 `LICENSE` 文件。

## 🙌 **致谢**

- **WMI**：[Microsoft WMIC Utility](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmic) 和 [Python WMI Module](https://github.com/tjguk/wmi)（作者 tjguk）
- **cpuid.py**：[flababah/cpuid.py](https://github.com/flababah/cpuid.py) —— 用于访问 x86 处理器细节的纯 Python 库
- **pci.ids**：[The PCI ID Repository](https://pci-ids.ucw.cz/)
- **usb.ids**：[The USB ID Repository](http://www.linux-usb.org/usb.ids)
- **run.py**：作者 [CorpNewt](https://github.com/corpnewt) —— 通过 `subprocess` 模块管理系统命令执行

## 📞 **联系方式**

**Hoang Hong Quan**
> Facebook（原版） [@macforce2601](https://facebook.com/macforce2601) &nbsp;&middot;&nbsp;
> Telegram(原版) [@lzhoang2601](https://t.me/lzhoang2601) &nbsp;&middot;&nbsp;
> 邮箱：GHYGOCSCP@outlook.com

## 🌟 **Star 历史**

[![Star History Chart](https://api.star-history.com/svg?repos=lzhoang2801/Hardware-Sniffer&type=Date)](https://star-history.com/#lzhoang2801/Hardware-Sniffer&Date)
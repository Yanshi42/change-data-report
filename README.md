# 嫦娥系列数据解析与可视化报告

[在线查看 CE1—CE6 数据目录](https://yanshi42.github.io/change-data-report/)
· [结果浏览](https://yanshi42.github.io/change-data-report/report.html)
· [图像与光谱解读](https://yanshi42.github.io/change-data-report/interpretation-review.html)

按任务、载荷和数据级别列出 CE1—CE6 的80个分类、238个已下载验证样例（235个原抽样产品和3个补充彩色样例）。
点击分类展开可视化、CSV预览、读取方式、结构信息和验证证据。

## 颜色与当前结果

- 蓝色：现有解码工具（Chang-e-PDS CLI、pds4-tools、pdr、rasterio/libarchive）。
- 绿色：自编补充解码器，27个原失败样例通过逐字段字节校验和完整NPZ导出回读验证。
- 黄色：部分结构可读，26个原样例。
- 红色：尚未解码或内容异常，明确区分缺格式说明、读取失败和内容异常。

235个原抽样产品中，198个读取成功，26个部分可读，10个需格式说明，1个内容异常；
当前实际读取失败为0个。这是样例验证结果，不表示整个任务数据目录都已验证。
报告全分类统计另保留3个CE7空目录分类。

## 内容与使用

网页为静态HTML，无需后端。也可下载仓库ZIP，解压后直接打开`index.html`。
保持HTML、`assets/`、`data/`的相对位置即可。PNG和CSV为可视化/表格预览；
仓库不包含原始科学文件、完整解码NPZ、Python环境或认证信息。

`data/`保存逐产品、逐分类汇总和解析证据；`manifest.json`记录发布文件SHA256。
证据中的服务器路径用于追溯，并非在线文件下载地址。
原始记录中的历史读取器报错保留；当前结论以综合报告为准。

“可读”表示实际恢复了科学数组或表格，不等同于物理定标或科学质量验证通过。
雷达/射电预览未据此推断深度或频率，光谱数值也不直接认定为反射率或矿物含量。

工具基础：[FHR2048/Chang-e-PDS-Data-processing](https://github.com/FHR2048/Chang-e-PDS-Data-processing)。
本仓库保存样例解析与可视化分析结果，科学数据来源与产品信息见每个样例的标签和证据记录。
中文字体许可证见`assets/fonts/LICENSE.txt`。

## 发布

GitHub Pages发布源：`main`分支的仓库根目录`/`，`.nojekyll`用于直接发布静态文件。
更新时先在本地完成解析与验证，再重新生成报告并同步发布。

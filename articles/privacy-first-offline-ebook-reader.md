---
layout: default
title: "本地电子书管理朗读器无广告无账号：隐私优先，书籍不出设备，只听不传"
description: "厌倦了上传书籍到云端、强制登录、广告推送、数据挖掘？Ebook Voice Player：纯本地解析 EPUB/PDF/DOCX/TXT/HTML，仅合成语音时发送选中文本到微软 Edge TTS，书籍/书签/笔记/进度全留本地。无账号体系、无遥测上报、无启动广告、卸载干净无残留。附隐私对比表与数据流向图解。"
lang: zh-Hans
hreflang_en: "/articles/privacy-first-offline-ebook-reader/"
og_title: "本地电子书管理朗读器无广告无账号：隐私优先，书籍不出设备"
og_description: "隐私党实测：书籍本地解析、仅合成文本上云、无账号无遥测无广告。对比主流阅读APP隐私政策，附数据流向图解。保护版权书、内部资料、个人笔记不泄露。"
---

<section class="page-hero">
  <div class="container">
    <p class="eyebrow"><span class="dot" aria-hidden="true"></span> 隐私深度测评</p>
    <h1>本地电子书管理朗读器无广告无账号：隐私优先，书籍不出设备，只听不传</h1>
    <p>把版权书、内部资料、个人日记上传到阅读 APP 云端？强制登录、广告推送、阅读画像被卖？Ebook Voice Player：书籍本地解析，仅“选中朗读的文本”发给微软 TTS 合成语音，书签笔记进度全留本地。无账号、无遥测、无广告、卸载干净。隐私党实测对比，附数据流向图解。</p>
  </div>
</section>

<section class="page-body">
  <div class="container">
    <div class="prose">
      <h2>主流阅读 APP 的隐私「三宗罪」</h2>
      <table class="facts-table">
        <caption>主流阅读/听书 APP 常见隐私风险点</caption>
        <thead>
          <tr><th>风险点</th><th>典型表现</th><th>后果</th></tr>
        </thead>
        <tbody>
          <tr><td>书籍强制上传</td><td>导入书籍自动同步云端、无本地模式、或本地模式功能阉割</td><td>版权书侵权风险、内部机密泄露、个人隐私读物暴露</td></tr>
          <tr><td>强制账号体系</td><td>不登录/不绑定手机/微信/苹果 ID 无法使用核心功能</td><td>身份关联、画像建立、换设备麻烦、注销困难</td></tr>
          <tr><td>广告/推荐/埋点</td><td>启动广告、阅读中插屏、基于阅读习惯推送商品/小说</td><td>注意力被收割、阅读偏好商业化、恶心体验</td></tr>
          <tr><td>遥测/统计/上报</td><td>阅读时长、翻页速度、点击热力、设备指纹、剪贴板监听</td><td>行为数据被收集、可能共享第三方、GDPR/个保法合规存疑</td></tr>
          <tr><td>数据不可导出/删除</td><td>书签笔记进度锁在云端、导出格式专有、注销账号数据不删</td><td>数据被绑架、迁移成本极高、遗产继承困难</td></tr>
        </tbody>
      </table>

      <h2>Ebook Voice Player 的隐私架构：本地优先，最小权限</h2>

      <h3>数据流向图解（文字版）</h3>
      <pre style="background:#1e1e1e;color:#d4d4d4;padding:1rem;border-radius:8px;overflow:auto;font-size:0.8rem;line-height:1.6;"><code>┌─────────────────────────────────────────────────────────────────┐
│                      用户设备                                     │
│  ┌──────────────┐    ┌──────────────────────────────────────┐   │
│  │  电子书文件   │───▶│  Ebook Voice Player (本地进程)        │   │
│  │  (EPUB/PDF/  │    │  • 解析文档结构、提取文本              │   │
│  │   DOCX/TXT/  │    │  • 章节识别、书签笔记、进度管理        │   │
│  │   HTML)       │    │  • 语音列表渲染、播放控制              │   │
│  └──────────────┘    │  • 设置存储 (%APPDATA%\EbookVoicePlayer)│   │
│         │            └──────────────┬────────────────────────┘   │
│         │                           │                            │
│         │      仅「选中朗读的文本」  │                            │
│         │      + 语音参数(语音名/语速)│                            │
│         ▼                           ▼                            │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │              网络请求 (HTTPS, TLS 1.2+)                       │  │
│  │  POST https://edgeservices.azure.com/cognitiveservices/...   │  │
│  │  Body: {text: "...", voice: "zh-CN-Xiaoxiao", rate: "1.0"}  │  │
│  └────────────────────────────┬────────────────────────────────┘  │
│                               │                                   │
│                               ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │         微软 Edge TTS 云端服务                                │  │
│  │  • 神经网络语音合成                                           │  │
│  │  • 返回 MP3/WAV 音频流                                        │  │
│  │  • 不存储请求文本（按微软隐私声明）                           │  │
│  └────────────────────────────┬────────────────────────────────┘  │
│                               │                                   │
│              音频流 (MP3)    │                                   │
│                               ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │         本地播放 / 缓存 (%APPDATA%\...\Cache) / 导出 MP3      │  │
│  └────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘</code></pre>

      <h3>关键点：什么上云、什么留本地</h3>
      <table class="facts-table">
        <caption>数据归属对照表</caption>
        <thead>
          <tr><th>数据类型</th><th>存储位置</th><th>是否上云</th><th>用途</th><th>用户可控性</th></tr>
        </thead>
        <tbody>
          <tr><td>电子书文件原件</td><td>用户原始路径（不复制、不移动）</td><td>❌ 从不</td><td>本地解析、阅读</td><td>完全掌控，软件只读不写</td></tr>
          <tr><td>解析后的文本/章节结构</td><td>内存 + %APPDATA%\Cache</td><td>❌ 从不</td><td>阅读渲染、章节跳转</td><td>可随时清理缓存</td></tr>
          <tr><td>阅读进度/书签/笔记</td><td>%APPDATA%\EbookVoicePlayer\data.json</td><td>❌ 从不</td><td>跨会话恢复、导出笔记</td><td>可导出 JSON/MD、可删除</td></tr>
          <tr><td>设置偏好(语音/语速/字号/主题)</td><td>%APPDATA%\EbookVoicePlayer\settings.json</td><td>❌ 从不</td><td>个性化体验</td><td>可重置/导出/导入</td></tr>
          <tr><td>音频缓存(已合成段落)</td><td>%APPDATA%\EbookVoicePlayer\Cache\</td><td>❌ 从不</td><td>二次播放不重复合成、省流量</td><td>可设置大小/清理/禁用</td></tr>
          <tr><td>「选中朗读」的文本片段</td><td>内存 → 网络请求 Body</td><td>✅ 仅合成瞬间</td><td>调用微软 Edge TTS 生成语音</td><td>用户主动触发、不可关闭(核心功能)</td></tr>
          <tr><td>导出的 MP3 文件</td><td>用户指定输出文件夹</td><td>❌ 从不</td><td>离线听书、分享、归档</td><td>完全掌控，软件不访问输出后文件</td></tr>
        </tbody>
      </table>

      <h2>横向对比：Ebook Voice Player vs 主流阅读/听书 APP</h2>

      <table class="facts-table">
        <caption>隐私维度对比（2026年10月实测）</caption>
        <thead>
          <tr><th>维度</th><th>Ebook Voice Player</th><th>微信读书/Kindle/得到/喜马拉雅</th><th>典型开源阅读器(KOReader/FBReader)</th></tr>
        </thead>
        <tbody>
          <tr><td>账号体系</td><td>❌ 无账号、无登录、无注册</td><td>✅ 必须登录、绑定手机/社交账号</td><td>❌ 可无账号使用</td></tr>
          <tr><td>书籍上传</td><td>❌ 从不上传、本地解析</td><td>✅ 默认同步云端、或强制上传</td><td>❌ 本地文件、可选同步</td></tr>
          <tr><td>广告/推荐</td><td>❌ 无广告、无推荐、无推送</td><td>✅ 启动广告、阅读中插屏、算法推荐</td><td>❌ 无广告</td></tr>
          <tr><td>遥测/统计</td><td>❌ 无任何遥测上报</td><td>✅ 完整埋点体系(时长/翻页/点击/设备)</td><td>⚠️ 部分可选遥测(可关)</td></tr>
          <tr><td>语音合成</td><td>☁️ 仅选中文本发微软 TTS</td><td>☁️ 自建/第三方 TTS，全文上传合成</td><td>💻 本地 TTS(离线)或云端可选</td></tr>
          <tr><td>数据导出</td><td>✅ 笔记/书签/设置一键导出 JSON/MD</td><td>❌ 通常不支持/格式专有/需会员</td><td>✅ 支持标准格式导出</td></tr>
          <tr><td>卸载清理</td><td>✅ 删 %APPDATA% 文件夹即干净</td><td>⚠️ 注销账号流程繁琐、残留云端数据</td><td>✅ 便携版无残留/删文件夹即净</td></tr>
          <tr><td>网络请求</td><td>仅 TTS 合成 + 检查更新(可关)</td><td>持续心跳、同步、推送、统计、广告拉取</td><td>仅检查更新/同步(可全关)</td></tr>
        </tbody>
      </table>

      <h2>微软 Edge TTS 隐私条款关键点（官方文档摘录）</h2>
      <ul>
        <li><strong>数据最小化</strong>：仅接收合成所需文本、语音参数，不接收用户身份、设备指纹、书籍元数据</li>
        <li><strong>不存储输入文本</strong>：合成完成即丢弃请求文本，不建立用户语音画像</li>
        <li><strong>不训练模型</strong>：用户请求数据不用于改进/训练微软语音模型</li>
        <li><strong>企业级合规</strong>：ISO 27001/27018、SOC 1/2/3、GDPR、HIPAA、中国个保法合规</li>
        <li><strong>数据驻留</strong>：可选区域端点（中国区走 Azure 中国/世纪互联），数据不出境</li>
      </ul>
      <p>完整条款见：<a href="https://learn.microsoft.com/zh-cn/legal/cognitive-services/speech-service/privacy" rel="noopener">微软认知服务语音隐私声明</a> | <a href="https://privacy.microsoft.com/zh-cn/privacystatement" rel="noopener">微软隐私声明</a></p>

      <h2>隐私敏感场景实操建议</h2>

      <h3>场景 1：阅读版权电子书（购买的 Kindle/Kobo/Google Play 书籍）</h3>
      <ol>
        <li>去除 DRM（仅限个人合法购买、个人使用，勿传播） → 得到无保护 EPUB</li>
        <li>拖入 Ebook Voice Player → 本地解析、本地阅读、本地朗读</li>
        <li>书籍文件始终在你的加密磁盘/隐藏文件夹/离线存储中，从未经过任何网络</li>
      </ol>

      <h3>场景 2：处理单位内部文档/机密报告/未公开论文</h3>
      <ol>
        <li>断网环境下导入 DOCX/PDF → 章节结构、书签笔记全本地生成</li>
        <li>需朗读时：临时接网 → 合成语音 → 断网 → 继续阅读（缓存复用）</li>
        <li>或：导出 MP3 → 断网设备播放 → 全程无网络痕迹</li>
      </ol>

      <h3>场景 3：个人隐私日记/心理治疗记录/遗书草稿</h3>
      <ol>
        <li>存为加密容器/加密磁盘/Veracrypt 卷 → 挂载后导入软件阅读</li>
        <li>软件仅读取挂载后的明文路径，不复制、不索引、不上传</li>
        <li>用完卸载软件、卸载挂载点、加密卷落锁，零痕迹</li>
      </ol>

      <h3>场景 4：给不懂技术的长辈/家人用（防误触上传/广告诈骗）</h3>
      <ol>
        <li>帮长辈配置好：大字、慢速、晓伊语音、护眼模式</li>
        <li>把常听书导出 MP3 传给长辈老人机/MP3 播放器</li>
        <li>长辈设备全程离线、无账号、无广告、无联网、无误触风险</li>
      </ol>

      <h2>如何验证「真·无上传」？（极客自查清单）</h2>
      <ol>
        <li><strong>抓包</strong>：Wireshark/Fiddler/Charles 抓包，过滤进程 <code>EbookVoicePlayer.exe</code>，仅见 <code>edgeservices.azure.com</code> TTS 请求，无其他域名</li>
        <li><strong>防火墙</strong>：Windows Defender 防火墙 → 出站规则 → 仅允许 <code>*.azure.com</code>、<code>*.microsoft.com</code>，拒绝其余 → 软件核心功能（阅读/书签/导出）全正常，仅失去在线 TTS</li>
        <li><strong>进程监控</strong>：Process Monitor 监控文件操作，仅见读取用户书籍路径、读写 <code>%APPDATA%\EbookVoicePlayer</code>，无遍历用户目录、无读取浏览器历史记录/剪贴板/通讯录</li>
        <li><strong>网络日志</strong>：路由器/软路由日志，仅见设备对微软 Azure IP 段的 HTTPS 连接，无其他异常流量</li>
      </ol>

      <h2>常见问题快答</h2>
      <details class="faq-item">
        <summary>软件会不会偷偷扫描我全盘的电子书？</summary>
        <div class="faq-answer"><p>不会。只有用户主动点击「文件→打开书籍」或「添加文件夹」指定路径时，软件才会读取该路径下的文件。无后台扫描、无文件系统监视器、无定时索引。</p></div>
      </details>
      <details class="faq-item">
        <summary>检查更新会上传我的设备信息吗？</summary>
      <div class="faq-answer"><p>检查更新仅请求 GitHub Releases API / 微软商店 API，获取最新版本号。不上传设备指纹、用户 ID、书籍列表、使用统计。可在设置中关闭「自动检查更新」。</p></div>
      </details>
      <details class="faq-item">
        <summary>导出的 MP3 里会不会嵌入我的个人信息水印？</summary>
      <div class="faq-answer"><p>不会。ID3 标签仅含：书名、章节名、作者(来自书籍元数据)、封面图、流派=Audiobook。无用户名、设备 ID、时间戳(除文件系统创建时间)、无隐形水印。</p></div>
      </details>
      <details class="faq-item">
        <summary>如果微软 TTS 服务挂了/被墙了，软件还能用吗？</summary>
      <div class="faq-answer"><p>阅读/书签/笔记/导出 MP3(已缓存段落)/设置/章节跳转/搜索全正常。仅「新文本合成语音」和「实时朗读」不可用。建议：提前把常听书批量导出 MP3 离线备用。</p></div>
      </details>
      <details class="faq-item">
        <summary>软件开源吗？代码审计过吗？</summary>
      <div class="faq-answer"><p>核心引擎闭源（商业软件），但架构透明：本地解析、最小权限、仅 TTS 上云。微软商店上架需通过安全审查。如需完全开源可审计方案，建议用 KOReader + 本地 TTS(piper/coqui)。</p></div>
      </details>

      <h2>总结：你的书，你的声，你的规矩</h2>
      <ul>
        <li>📚 <strong>书籍</strong>：躺在你的硬盘里，软件只读不传</li>
        <li>🗣️ <strong>语音</strong>：只把「你点播放的那段文本」发给微软合成，合成完即扔</li>
        <li>📝 <strong>笔记/书签/进度</strong>：存在你的 <code>%APPDATA%</code> 里，想导出导出、想删就删</li>
        <li>🚫 <strong>账号/广告/遥测/推送</strong>：统统没有</li>
        <li>🗑️ <strong>卸载</strong>：删个文件夹走人，不留痕迹</li>
      </ul>
      <p>微软商店搜 <strong>Ebook Voice Player</strong>，免费试用全功能。不放心？装上、断网、导入本地书、阅读、加书签、导出笔记、卸载、查文件夹——全程无网络、无账号、无广告、无残留。隐私不妥协，听书不将就。</p>

      <div class="cta-actions" style="margin-top: 2rem;">
        <a class="store-badge" href="https://apps.microsoft.com/store/detail/9NLHLN1SJNBR?cid=DevShareMCLPCS" rel="noopener" aria-label="从 Microsoft Store 获取 Ebook Voice Player">
          <svg class="store-badge-icon" aria-hidden="true"><use href="#i-store"/></svg>
          <span class="store-badge-text">
            <span class="store-badge-kicker">免费试用</span>
            <span class="store-badge-name">Microsoft Store</span>
          </span>
        </a>
      </div>
    </div>
  </div>
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "本地电子书管理朗读器无广告无账号：隐私优先，书籍不出设备，只听不传",
  "description": "隐私党实测：书籍本地解析、仅合成文本上云、无账号无遥测无广告。对比主流阅读APP隐私政策，附数据流向图解。保护版权书、内部资料、个人笔记不泄露。",
  "datePublished": "2026-10-27",
  "author": { "@type": "Person", "name": "Ebook Voice Player Team" },
  "keywords": "隐私优先阅读器, 无账号电子书软件, 本地TTS朗读, 数据不上传, 微软Edge TTS隐私"
}
</script>
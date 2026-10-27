---
layout: default
title: "Privacy-First Offline Ebook Reader: Books Never Leave Device, Only Synthesis Text to Cloud"
description: "Privacy test: Ebook Voice Player parses EPUB/PDF/DOCX/TXT/HTML locally. Only selected narration text sent to Microsoft Edge TTS. Bookmarks/Notes/Progress stay local. No Account, No Telemetry, No Ads. Data Flow Diagram Included. Protects Copyright Books, Internal Docs, Private Journals."
lang: en
hreflang_zh: "/articles/privacy-first-offline-ebook-reader/"
og_title: "Privacy-First Offline Ebook Reader: Books Stay Local, Only Synthesis to Cloud"
og_description: "Privacy deep-dive: Local Parse, Only Synthesis Text to Cloud, No Account/Telemetry/Ads. Vs Mainstream Apps Privacy Policies. Data Flow Diagram. Protects Copyright Books, Internal Docs, Private Notes."
---

<section class="page-hero">
  <div class="container">
    <p class="eyebrow"><span class="dot" aria-hidden="true"></span> Privacy Deep-Dive</p>
    <h1>Privacy-First Offline Ebook Reader: Books Never Leave Device, Only Synthesis Text to Cloud</h1>
    <p>Uploading copyrighted books, internal docs, personal journals to reading app clouds? Forced Login, Ad Push, Reading Profiling? Ebook Voice Player: Local Parse, Only "Selected Narration Text" to Microsoft TTS. Bookmarks/Notes/Progress All Local. No Account, No Telemetry, No Ads, Clean Uninstall. Privacy Test with Data Flow Diagram.</p>
  </div>
</section>

<section class="page-body">
  <div class="container">
    <div class="prose">
      <h2>Mainstream Reading Apps' Privacy "Three Sins"</h2>
      <table class="facts-table">
        <caption>Common Privacy Risks in Popular Reading/Listener Apps</caption>
        <thead>
          <tr><th>Risk</th><th>Typical Behavior</th><th>Consequence</th></tr>
        </thead>
        <tbody>
          <tr><td>Forced Book Upload</td><td>Auto-Sync to Cloud, No Local Mode, or Local Mode Crippled</td><td>Copyright Infringement Risk, Internal Leak, Private Reading Exposed</td></tr>
          <tr><td>Mandatory Account</td><td>Core Features Locked Behind Phone/WeChat/Apple ID Bind</td><td>Identity Link, Profiling, Device Switch Hassle, Hard Delete</td></tr>
          <tr><td>Ads/Recs/Tracking</td><td>Launch Ads, In-Read Interstitials, Algo Recs Based on Habits</td><td>Attention Harvested, Reading Taste Monetized, UX Degraded</td></tr>
          <tr><td>Telemetry/Analytics</td><td>Read Duration, Page Turn Speed, Click Heatmap, Device Fingerprint, Clipboard Snoop</td><td>Behavior Data Collected, Third-Party Sharing Possible, GDPR/PIPL Compliance Dubious</td></tr>
          <tr><td>Data Lock-in</td><td>Bookmarks/Notes/Progress Cloud-Locked, Proprietary Export, Account Delete ≠ Data Delete</td><td>Data Hostage, Migration Cost Extreme, Digital Inheritance Hard</td></tr>
        </tbody>
      </table>

      <h2>Ebook Voice Player Privacy Architecture: Local-First, Minimal Permissions</h2>

      <h3>Data Flow Diagram (Text Version)</h3>
      <pre style="background:#1e1e1e;color:#d4d4d4;padding:1rem;border-radius:8px;overflow:auto;font-size:0.8rem;line-height:1.6;"><code>┌─────────────────────────────────────────────────────────────────┐
│                      User Device                                   │
│  ┌──────────────┐    ┌──────────────────────────────────────┐   │
│  │  Ebook Files  │───▶│  Ebook Voice Player (Local Process)   │   │
│  │  (EPUB/PDF/   │    │  • Parse Structure, Extract Text       │   │
│  │   DOCX/TXT/   │    │  • Chapter Detect, Bookmarks, Notes,   │   │
│  │   HTML)        │    │    Progress Management                │   │
│  └──────────────┘    │  • Voice List Render, Playback Control   │   │
│         │            │  • Settings Storage (%APPDATA%\EVP)      │   │
│         │            └──────────────┬────────────────────────┘   │
│         │                           │                            │
│         │      Only "Selected       │                            │
│         │      Narration Text"      │                            │
│         │      + Voice Params       │                            │
│         ▼                           ▼                            │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │              Network Request (HTTPS, TLS 1.2+)              │  │
│  │  POST https://edgeservices.azure.com/cognitiveservices/...  │  │
│  │  Body: {text: "...", voice: "zh-CN-Xiaoxiao", rate: "1.0"}  │  │
│  └────────────────────────────┬────────────────────────────────┘  │
│                               │                                   │
│                               ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │         Microsoft Edge TTS Cloud Service                     │  │
│  │  • Neural Speech Synthesis                                   │  │
│  │  • Returns MP3/WAV Audio Stream                              │  │
│  │  • Does Not Store Request Text (Per Microsoft Privacy)       │  │
│  └────────────────────────────┬────────────────────────────────┘  │
│                               │                                   │
│              Audio Stream (MP3)│                                   │
│                               ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │         Local Playback / Cache (%APPDATA%\...\Cache) / Export MP3│  │
│  └────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘</code></pre>

      <h3>Key: What Goes to Cloud vs Stays Local</h3>
      <table class="facts-table">
        <caption>Data Ownership Matrix</caption>
        <thead>
          <tr><th>Data Type</th><th>Location</th><th>To Cloud?</th><th>Purpose</th><th>User Control</th></tr>
        </thead>
        <tbody>
          <tr><td>Original Ebook Files</td><td>User's Original Path (No Copy/Move)</td><td>❌ Never</td><td>Local Parse, Read</td><td>Full Control, App Read-Only</td></tr>
          <tr><td>Parsed Text/Chapters</td><td>Memory + %APPDATA%\Cache</td><td>❌ Never</td><td>Render, Chapter Jump</td><td>Clear Cache Anytime</td></tr>
          <tr><td>Progress/Bookmarks/Notes</td><td>%APPDATA%\EbookVoicePlayer\data.json</td><td>❌ Never</td><td>Resume, Export Notes</td><td>Export JSON/MD, Delete</td></tr>
          <tr><td>Preferences (Voice/Speed/Font/Theme)</td><td>%APPDATA%\EbookVoicePlayer\settings.json</td><td>❌ Never</td><td>Personalization</td><td>Reset/Export/Import</td></tr>
          <tr><td>Audio Cache (Synthesized Segments)</td><td>%APPDATA%\EbookVoicePlayer\Cache\</td><td>❌ Never</td><td>Replay Without Re-Synth, Save BW</td><td>Size Limit/Clear/Disable</td></tr>
          <tr><td>"Selected Narration" Text Chunks</td><td>Memory → Request Body</td><td>✅ Only At Synthesis Moment</td><td>Call Microsoft Edge TTS for Speech</td><td>User-Initiated, Non-Disablable (Core Feature)</td></tr>
          <tr><td>Exported MP3 Files</td><td>User-Chosen Output Folder</td><td>❌ Never</td><td>Offline Listen, Share, Archive</td><td>Full Control, App Doesn't Touch Post-Export</td></tr>
        </tbody>
      </table>

      <h2>Side-by-Side: Ebook Voice Player vs Mainstream Apps</h2>

      <table class="facts-table">
        <caption>Privacy Dimension Comparison (Oct 2026)</caption>
        <thead>
          <tr><th>Dimension</th><th>Ebook Voice Player</th><th>WeRead/Kindle/Dede/Ximalaya</th><th>Typical Open Source (KOReader/FBReader)</th></tr>
        </thead>
        <tbody>
          <tr><td>Account System</td><td>❌ No Account, No Login, No Register</td><td>✅ Must Login, Bind Phone/Social</td><td>❌ Optional Accountless</td></tr>
          <tr><td>Book Upload</td><td>❌ Never Upload, Local Parse</td><td>✅ Default Cloud Sync, or Forced Upload</td><td>❌ Local Files, Optional Sync</td></tr>
          <tr><td>Ads/Recommendations</td><td>❌ No Ads, No Recs, No Push</td><td>✅ Launch Ads, In-Read Interstitials, Algo Recs</td><td>❌ No Ads</td></tr>
          <tr><td>Telemetry/Analytics</td><td>❌ Zero Telemetry</td><td>✅ Full Tracking (Duration/Pages/Clicks/Device)</td><td>⚠️ Optional Telemetry (Disableable)</td></tr>
          <tr><td>TTS Synthesis</td><td>☁️ Only Selected Text to Microsoft TTS</td><td>☁️ Self-Hosted/3rd Party TTS, Full Text Upload</td><td>💻 Local TTS (Piper/Coqui) or Cloud Optional</td></tr>
          <tr><td>Data Export</td><td>✅ One-Click Notes/Bookmarks/Settings → JSON/MD</td><td>❌ Usually No / Proprietary / Paid Tier</td><td>✅ Standard Format Export</td></tr>
          <tr><td>Uninstall Cleanup</td><td>✅ Delete %APPDATA% Folder = Clean</td><td>⚠️ Account Delete Flow Tedious, Cloud Residue</td><td>✅ Portable = Clean / Delete Folder</td></tr>
          <tr><td>Network Requests</td><td>Only TTS Synthesis + Update Check (Disableable)</td><td>Constant Heartbeat, Sync, Push, Stats, Ad Fetch</td><td>Only Update/Sync (Fully Disableable)</td></tr>
        </tbody>
      </table>

      <h2>Microsoft Edge TTS Privacy Highlights (Official Docs Summary)</h2>
      <ul>
        <li><strong>Data Minimization</strong>: Receives Only Synthesis Text + Voice Params. No User Identity, Device Fingerprint, Book Metadata.</li>
        <li><strong>No Input Storage</strong>: Request Text Discarded Post-Synthesis. No User Voice Profile Built.</li>
        <li><strong>No Model Training</strong>: User Requests Not Used to Improve/Train Microsoft Speech Models.</li>
        <li><strong>Enterprise Compliance</strong>: ISO 27001/27018, SOC 1/2/3, GDPR, HIPAA, China PIPL Compliant.</li>
        <li><strong>Data Residency</strong>: Regional Endpoints Selectable (China via Azure/21Vianet). Data Stays In-Region.</li>
      </ul>
      <p>Full: <a href="https://learn.microsoft.com/zh-cn/legal/cognitive-services/speech-service/privacy" rel="noopener">Microsoft Cognitive Services Speech Privacy</a> | <a href="https://privacy.microsoft.com/zh-cn/privacystatement" rel="noopener">Microsoft Privacy Statement</a></p>

      <h2>Privacy-Sensitive Scenarios: Practical Guides</h2>

      <h3>Scenario 1: Reading Copyrighted Ebooks (Purchased Kindle/Kobo/Google Play)</h3>
      <ol>
        <li>Remove DRM (Personal Legal Purchase Only, Personal Use, No Sharing) → DRM-Free EPUB</li>
        <li>Drag into Ebook Voice Player → Local Parse, Local Read, Local Narrate</li>
        <li>File Stays on Your Encrypted Drive/Hidden Folder/Offline Storage. Zero Network Touch.</li>
      </ol>

      <h3>Scenario 2: Internal Corporate Docs / Confidential Reports / Unpublished Papers</h3>
      <ol>
        <li>Air-Gapped Env Import DOCX/PDF → Chapter Structure, Bookmarks, Notes All Local</li>
        <li>Need Narration: Temp Online → Synthesize → Offline → Continue (Cache Reuse)</li>
        <li>Or: Export MP3 → Offline Device Playback → Zero Network Trace</li>
      </ol>

      <h3>Scenario 3: Personal Private Diary / Therapy Notes / Draft Will</h3>
      <ol>
        <li>Store in Encrypted Container/Veracrypt Volume → Mount → Import for Reading</li>
        <li>App Only Reads Mounted Cleartext Path. No Copy, No Index, No Upload.</li>
        <li>Done → Uninstall App, Dismount, Volume Locked. Zero Trace.</li>
      </ol>

      <h3>Scenario 4: Non-Tech Elderly/Family (Prevent Accidental Upload/Ad Scams)</h3>
      <ol>
        <li>Configure for Elder: Large Font, Slow Speed, Xiaoyi Voice, Eye-Care Mode</li>
        <li>Export Frequent Books as MP3 → Transfer to Feature Phone/MP3 Player</li>
        <li>Elder Device: Fully Offline, No Account, No Ads, No Net, No Mis-Touch Risk</li>
      </ol>

      <h2>How to Verify "Truly No Upload" (Geek Self-Audit Checklist)</h2>
      <ol>
        <li><strong>Packet Capture</strong>: Wireshark/Fiddler/Charles Filter Process <code>EbookVoicePlayer.exe</code>. Only <code>edgeservices.azure.com</code> TTS Requests. Zero Other Domains.</li>
        <li><strong>Firewall</strong>: Windows Defender Outbound → Allow Only <code>*.azure.com</code>, <code>*.microsoft.com</code>, Block Rest → Core Features (Read/Bookmarks/Export) Work. Only Online TTS Lost.</li>
        <li><strong>Process Monitor</strong>: ProcMon File Ops → Only Reads User Book Paths, R/W <code>%APPDATA%\EbookVoicePlayer</code>. No User Dir Walk, No Browser History/Clipboard/Contacts Access.</li>
        <li><strong>Router Logs</strong>: Device → Only Microsoft Azure IP Ranges HTTPS. Zero Anomalous Traffic.</li>
      </ol>

      <h2>Quick FAQ</h2>
      <details class="faq-item">
        <summary>Does App Secretly Scan All My Ebooks?</summary>
        <div class="faq-answer"><p>No. Only Reads Paths User Explicitly Opens via "File→Open Book" or "Add Folder". No Background Scan, No FS Watcher, No Scheduled Index.</p></div>
      </details>
      <details class="faq-item">
        <summary>Update Check Uploads Device Info?</summary>
      <div class="faq-answer"><p>Update Check Hits GitHub Releases API / Microsoft Store API for Latest Version Only. No Device Fingerprint, User ID, Book List, Usage Stats. Disable "Auto Check Updates" in Settings.</p></div>
      </details>
      <details class="faq-item">
        <summary>Exported MP3 Contains Personal Info Watermark?</summary>
      <div class="faq-answer"><p>No. ID3 Only: Title, Chapter, Author (From Book Metadata), Cover, Genre=Audiobook. No Username, Device ID, Timestamp (Except FS Create Time), No Steganographic Watermark.</p></div>
      </details>
      <details class="faq-item">
        <summary>If Microsoft TTS Down / Blocked, App Still Works?</summary>
      <div class="faq-answer"><p>Read/Bookmarks/Notes/Export MP3 (Cached Segments)/Settings/Chapter Jump/Search All Work. Only "New Text Synthesis" and "Real-Time Playback" Unavailable. Advice: Pre-Export Frequent Books as MP3 Offline Backup.</p></div>
      </details>
      <details class="faq-item">
        <summary>Is It Open Source? Audited?</summary>
      <div class="faq-answer"><p>Core Engine Closed (Commercial). Architecture Transparent: Local Parse, Minimal Perms, TTS-Only Cloud. Microsoft Store Listing Passed Security Review. For Fully Auditable Open Source: KOReader + Local TTS (Piper/Coqui).</p></div>
      </details>

      <h2>Summary: Your Books, Your Voice, Your Rules</h2>
      <ul>
        <li>📚 <strong>Books</strong>: On Your Disk. App Reads, Never Sends.</li>
        <li>🗣️ <strong>Voice</strong>: Only "Paragraph You Hit Play" Sent to Microsoft. Synthesis Done → Discarded.</li>
        <li>📝 <strong>Notes/Bookmarks/Progress</strong>: In Your <code>%APPDATA%</code>. Export Anytime, Delete Anytime.</li>
        <li>🚫 <strong>Account/Ads/Telemetry/Push</strong>: None.</li>
        <li>🗑️ <strong>Uninstall</strong>: Delete One Folder. Walk Away Clean.</li>
      </ul>
      <p>Microsoft Store Search <strong>Ebook Voice Player</strong>, Free Trial Full Features. Skeptical? Install → Disconnect Net → Import Local Book → Read → Bookmark → Export Notes → Uninstall → Check Folder. Zero Net, Zero Account, Zero Ads, Zero Residue. Privacy No Compromise, Listening No Settling.</p>

      <div class="cta-actions" style="margin-top: 2rem;">
        <a class="store-badge" href="https://apps.microsoft.com/store/detail/9NLHLN1SJNBR?cid=DevShareMCLPCS" rel="noopener" aria-label="Get Ebook Voice Player from Microsoft Store">
          <svg class="store-badge-icon" aria-hidden="true"><use href="#i-store"/></svg>
          <span class="store-badge-text">
            <span class="store-badge-kicker">Free Trial</span>
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
  "headline": "Privacy-First Offline Ebook Reader: Books Never Leave Device, Only Synthesis Text to Cloud",
  "description": "Privacy test: Local Parse, Only Synthesis Text to Cloud, No Account/Telemetry/Ads. Vs Mainstream Apps. Data Flow Diagram. Protects Copyright Books, Internal Docs, Private Notes.",
  "datePublished": "2026-10-27",
  "author": { "@type": "Person", "name": "Ebook Voice Player Team" },
  "keywords": "Privacy-First Ebook Reader, No Account Ebook Software, Local TTS Reading, Data Not Uploaded, Microsoft Edge TTS Privacy"
}
</script>
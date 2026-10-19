# Ebook Voice Player

> **Open a 200,000-word novel and hear it read aloud—in a voice you picked.**  
> **229 voices, 56 languages and regional accents; auto chapter detection, read-along highlighting, full-book MP3 export.**  
> **¥7 one-time purchase. No subscription, no ads. Install on Windows 10/11 and go.**

[**Get it on Microsoft Store (free trial included) →**](https://apps.microsoft.com/store/detail/9NLHLN1SJNBR?cid=DevShareMCLPCS)

`Available on Microsoft Store` · `Windows 10/11` · `x64` · `~194 MB` · `229 voices` · `56 languages & regional accents` · `¥7 in China, free trial`

[中文](README.md) | [English](README.en.md)

---

You know the moment: you find a novel you want to read, but it is a TXT file. You try the built-in narrator and get two robotic voices. You switch to an online TTS page and face copy-paste limits, ads, broken sentence pauses, and no way to save your place. Eventually, you give up.

**Ebook Voice Player is not another online TTS page, and not a 4 GB offline model.** It is a Windows desktop reader: open the book, detect the chapters, pick a voice, and start from any paragraph.

## The short version

| It is for you if… | It may not be for you if… |
|---|---|
| You want to turn web novels, TXT, PDF, and EPUB into audiobooks | You need 100% offline synthesis with no internet at all |
| You want to read and listen on Windows with automatic follow-along highlighting | You mainly use a phone and do not want a desktop app |
| You need Chinese dialects, multiple accents, and different character voices | You need OCR for scanned PDFs |
| You want to export a whole book as MP3 for commutes or chores | You need to remove DRM from ebooks |
| You prefer a one-time purchase without subscriptions or ads | You need multi-track editing from a professional dubbing suite |

## 5 frustrations you already know

| Pain point | What usually happens | How Ebook Voice Player solves it |
|---|---|---|
| **Robotic voices** | System TTS gives you a few mechanical voices; two chapters in, you are done | 229 neural voices, including Mandarin, Cantonese, Northeastern, Shaanxi, and Taiwanese accents, plus English, Japanese, Korean, French, German, Spanish, Russian, Arabic, Thai, Vietnamese, and more |
| **No chapters in long novels** | You can only start from the beginning; jumping means dragging a progress bar | Detects “Chapter/Volume/Part/Section” in Chinese and English; a chapter dropdown takes you straight there |
| **Listening and reading drift apart** | You lose track of where the narrator is and have to scroll manually | Current paragraph highlight + auto-scroll + progress percentage + estimated time remaining |
| **Split volumes must be opened one by one** | Dozens of TXT files in one folder, switched by hand | Treats an entire folder as one book; previous/next file switches with one click |
| **Character and place names are mispronounced** | Every book forces you to endure strange pronunciations | Drop a `名词转换.txt` term map with “original → replacement” pairs; longest matches win |

## 8 reasons to download

### 1. 229 voices, not one robot reading everything

The catalog covers 56 languages and regional accents across 75 regions. Chinese is not just Mandarin: Cantonese, Northeastern, Shaanxi, and Taiwanese accents are clearly labeled. English covers US, UK, Australian, Canadian, and Indian accents. Japanese, Korean, French, German, Spanish, Russian, Arabic, Thai, Vietnamese, and more are included.

Search the voice list, preview a voice, and switch voices during playback—the current paragraph finishes, then the new voice takes over.

### 2. Four major formats, plus automatic encoding detection

Supports **TXT, DOCX, PDF, and EPUB**, and also handles HTML. TXT files are tried against UTF-8, GBK, GB2312, GB18030, Big5, UTF-16, Shift-JIS, EUC-JP, and more, reducing the “open the file and see garbage characters” problem.

> Scanned PDFs have no text layer and must be OCR'd first. This is a shared limitation of text-based readers.

### 3. Auto chapters, and start from any paragraph

Chinese “第 X 章/卷/篇/话/节/集” and English Chapter/Part/Section/Volume headings are detected; secondary headings are not duplicated as chapters. You can:

- jump directly with the chapter dropdown;
- click any paragraph in the book to start reading from there;
- nudge playback with previous/next paragraph;
- resume from your last position automatically next time.

### 4. Real read-along

While playing, the current paragraph is highlighted and the reading pane follows automatically. The status bar shows progress percentage, current paragraph / total paragraphs, and an estimate of time remaining based on your actual listening speed. Chapter switches keep playback and display in sync—no manual searching.

### 5. Engineering built for long books

- Background parallel synthesis with 3 concurrent workers; playback starts while later paragraphs are generated;
- Cache keys built from `text + voice + rate` with SHA-256, so repeated paragraphs open instantly;
- The reading pane renders 32 paragraphs per frame with GC control, so a 10,000-paragraph book does not freeze the UI in one giant build;
- A playback watchdog handles unreliable Windows/SDL2 end-of-audio events, preventing “it stops after the first paragraph”;
- A chunked render pipeline keeps very large documents from blocking the interface.

### 6. Term replacement for names, places, and invented techniques

Put a `名词转换.txt` file in the book's folder, one “original + Tab + replacement” pair per line. Replacements are applied longest-first, so `索菲莉亚` is not stolen by `索菲`; use `（空白符）` as the replacement to delete unwanted symbols.

```text
# original<Tab>replacement
索菲	索菲娅
萧炎	萧焱
系统	金手指
```

The file only affects narration, never modifies the book, and is shared automatically by every book in the same folder.

### 7. A reading workflow, not just a play button

Bookmarks, paragraph notes, full-text search, F3 find-next, sleep timer, font size, line spacing, dark/light themes, fullscreen reading, recent files, reading statistics, Chinese/English UI, and keyboard shortcuts—all in one window for finding, reading, listening, noting, and exporting.

### 8. Export a whole book as MP3 for offline listening

Export the current book as numbered MP3 files, starting at `段落_0001.mp3`, ready for a phone, MP3 player, or car USB drive. Synthesized audio is cached locally and can be cleared at any time to free space.

## How it compares

> Comparison based on public product pages and Microsoft Store information as of October 2026; prices, features, and sizes may change between versions.

| Product | Price | Voices & languages | Offline | Read-along / chapters | MP3 export | Platform & size |
|---|---|---|---|---|---|---|
| **Ebook Voice Player (this app)** | **¥7 one-time, free trial** | **229 / 56 languages & regional accents** | Internet required for synthesis | **Paragraph highlight + auto-scroll / auto chapters** | **Yes** | Windows 10/11, ~194 MB |
| Ebook to Audio | $24.99 | 9 languages | Fully offline | Yes / Yes | Yes | Windows, ~3.8 GB |
| NaturalReader | Limited free tier; subscription | 150+ / 20+ languages | Mostly online | Yes / Partial | Paid | Windows / Web / mobile |
| Speechify | Subscription | Multilingual premium voices, strongest in English | Online | Yes / Partial | Paid | Multi-platform |
| @Voice Aloud Reader | Free + ads/premium | System TTS; quality depends on engine | Depends on engine | Yes / Yes | WAV | Android |
| Balabolka | Free | System SAPI voices | Offline | Limited / Limited | Yes | Windows |
| Edge Read Aloud | Free | 40+ languages | Partially offline | Yes / No library | No | Browser |

### One-line choice

- Want **fully offline, 9 languages, and willing to accept 3.8 GB and $24.99**? Ebook to Audio is a good fit.
- Want **to read web pages in your browser**? Edge Read Aloud is lighter.
- Want **system TTS on Android**? @Voice Aloud Reader is the right tool.
- Want **229 voices, Chinese dialects, chapter follow-along, full-book export, a ¥7 one-time purchase, and a Windows desktop app**? Choose Ebook Voice Player.

### Where we win

**Price:** ¥7 one-time, versus $24.99 upfront or a monthly subscription. Very low cost to try.

**Voice coverage:** 229 voices versus 9 languages; Chinese dialects are labeled separately, so you do not have to guess among dozens of “Chinese female” entries.

**Size and barrier to entry:** About 194 MB, runs on CPU, no GPU and no multi-gigabyte local model download. It installs on older PCs too.

**Workflow completeness:** Many tools stop at “text to MP3.” We cover the whole chain: open book → split chapters → pick voice → read along → take notes → search → sleep timer → export.

**Chinese-language details:** Chinese chapter regex, dialect labels, GBK/Big5 detection, term replacement, and a bilingual UI. These details decide whether a Chinese novel is usable for the long haul.

### Boundaries we admit

- **Internet is required to synthesize new paragraphs:** voices come from Microsoft Edge TTS. Cached paragraphs can play offline, but new paragraphs cannot be generated without a connection.
- **No OCR for scanned PDFs:** only PDFs with a text layer can be extracted directly.
- **No DRM ebooks:** use personal, DRM-free files.
- **Not a native mobile app:** the Microsoft Store listing is the Windows desktop version. The UI adapts to narrow screens, but phones are not the primary target.
- **The voice list may change:** the 229 voices are provided by edge-tts and may change with Microsoft's service.

## Up and running in 3 minutes

1. Install from [Microsoft Store](https://apps.microsoft.com/store/detail/9NLHLN1SJNBR?cid=DevShareMCLPCS) and open the app.
2. Choose `File → Open File` for one book, or `File → Open Folder Library` to treat a whole folder as one book.
3. Search or preview voices in the right-hand panel and pick one.
4. Click any paragraph, or press `▶` at the bottom to start; `Space` pauses/resumes.
5. To listen offline later, use `Tools → Export to Audio Files` to export MP3s.

## Keyboard shortcuts

| Shortcut | Action |
|---|---|
| `Space` | Play / pause |
| `Ctrl + O` | Open file |
| `Ctrl + D` | Open folder library |
| `Ctrl + ← / →` | Previous / next file |
| `Ctrl + ↑ / ↓` | Previous / next paragraph |
| `Ctrl + F` / `F3` | Search / find next |
| `Ctrl + B` | Add bookmark |
| `Ctrl + Shift + B` | View bookmarks |
| `Ctrl + Shift + N` | Add note |
| `Ctrl + Shift + M` | View notes |
| `Ctrl + + / -` | Increase / decrease font size |
| `F11` / `Esc` | Fullscreen / exit fullscreen |

## Tech stack

- **UI:** Python 3 + Kivy 2.3, responsive desktop/narrow-screen layout
- **Speech:** edge-tts (Microsoft Edge neural voices), asyncio parallel synthesis
- **Document parsing:** PyMuPDF / pdfplumber, python-docx, EbookLib, BeautifulSoup
- **Caching:** SHA-256 content addressing, MP3 validity checks
- **Performance:** chunked rendering, GC control, playback watchdog, background threads + semaphores
- **Testing:** pytest coverage for the reader, TTS engine, voice manager, UI components, and responsive layout
- **Distribution:** MSIX package for Windows 10 version 17763+ / Windows 11, x64

## Privacy and boundaries

- Book files are opened locally and are not uploaded to any self-hosted content server; the app has no account system.
- Text to be narrated is sent to Microsoft Edge TTS for speech synthesis.
- Synthesized audio is cached on your device and can be deleted via `Tools → Clear Audio Cache`.
- Only narrate files you have the right to use; this app does not provide DRM circumvention or copyrighted content downloads.

## Download and pricing

[**Microsoft Store: Ebook Voice Player - Text To Speech Ebook Reader →**](https://apps.microsoft.com/store/detail/9NLHLN1SJNBR?cid=DevShareMCLPCS)

- China Store price: **¥7**, with a **free trial**; prices in other regions follow the Store listing.
- Requirements: Windows 10 version 17763 or later / Windows 11, x64.
- Install size: about **194 MB**.

---

> **You do not need to wait for another “when I have time” evening.**  
> Install now and turn your next book into company for the commute, the chores, or bedtime.  
> [**Get Ebook Voice Player →**](https://apps.microsoft.com/store/detail/9NLHLN1SJNBR?cid=DevShareMCLPCS)

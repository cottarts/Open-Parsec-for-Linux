# Linux client decoder compatibility

If the official Linux Parsec client connects but reports -17, inspect its local log for a video-decoder initialization failure. A working host encoder does not establish that the client's decoder libraries can load.

The Parsec 150-105c Linux build tested with this release tries to resolve avcodec_close even when loading libavcodec.so.62. FFmpeg 8 removed this symbol; a machine with only FFmpeg 8 may therefore fail before decoding its first frame. A compatible FFmpeg 7 runtime (libavcodec.so.61 and libavutil.so.59) resolved this on the tested Ubuntu 26.04 client. This observation is specific to that client build.

Use an official package for your distribution when available, or build the corresponding FFmpeg 7 release into a separate prefix. Keep the system FFmpeg version installed. Do not rename or symlink a newer major-version library to an older SONAME: the ABI differs. Restart Parsec after installing the compatible runtime and verify its log reports FFMPEG 7 Software. This software-decoder path does not promise hardware acceleration.

References: [FFmpeg removal of avcodec_close](https://ffmpeg.org/pipermail/ffmpeg-cvslog/2025-March/147911.html), [Parsec error -17](https://support.parsec.app/hc/en-us/articles/34984639667092-Error-Codes-17-Your-device-had-trouble-using-the-video-decoder).

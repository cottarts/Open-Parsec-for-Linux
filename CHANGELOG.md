# 0.1.1 — 2026-10-13

This corrective release fixes empty/green video surfaces on older Intel GPUs and keeps the selected encoder when changing the host name.

- Query VAAPI surface-memory capabilities before importing converted frames. Use the legacy PRIME descriptor on drivers such as i965 that do not support PRIME_2; reject unsupported layouts rather than silently encoding an empty surface.
- Correct the DRM memory-type constants from libva's DRM headers.
- Add VAAPI to the encoder selector and configuration validation, preserve explicit encoder arguments, and default new configurations to automatic selection.
- Add regression tests for renaming a VAAPI host and automatic encoder selection.
- Allow the hardware capture test to select its conversion backend through LOWLAT_CONVERT. Log the first video header after encoder initialization for diagnosis.

## Validation and limits

Validated on Ubuntu 24.04 with Intel HD Graphics 4400 / i965: 30 encoder unit tests, 8 control-panel tests, and independent decoding of 400 real capture frames through each of Vulkan and OpenGL. A real Parsec client on Ubuntu 26.04 connected and the user confirmed working video after the fixes. Service restart was verified; a full machine reboot and a fresh-machine installation have not been validated for this release.

The Linux client needed FFmpeg 7 compatibility libraries. Its installed Parsec build required avcodec_close, which FFmpeg 8 removes. This is a client runtime issue; see CLIENT-COMPATIBILITY.md. The host archive does not install compatibility libraries on client computers.

The archive contains the Ubuntu 24.04 x86_64 host binaries and matching source, with existing license notices. EDID overrides, virtual-screen setup, credentials and user settings are excluded.

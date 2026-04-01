# This is where AI training actually happens. Remote

| Command | What It Does | AI-Specific Use |
|---------|--------------|-----------------|
| `ssh` | Secure shell | Connect to GPU servers |
| `scp` | Secure copy | Transfer files: `scp model.pt server:/models/` |
| `rsync` | Sync files | Efficiently sync large datasets |
| `tmux`/`screen` | Terminal multiplexer | Keep sessions alive, multiple windows |

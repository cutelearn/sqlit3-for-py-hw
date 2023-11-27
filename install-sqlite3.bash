#!/bin/bash

# 更新套件列表
apt-get update

# 安裝 SQLite3
apt-get install -y sqlite3

# 驗證安裝
sqlite3 --version

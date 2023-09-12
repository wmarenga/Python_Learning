"""
echo $SHELL
#!/bin/bash

# Updating packages:
sudo apt update -y
sudo apt upgrade -y

# Only the Python:
sudo apt install python3.11-full python3.11-dev -y

# Installing packages:
sudo apt install git curl build-essential dkms perl wget -y
sudo apt install gcc make default-libmysqlclient-dev libssl-dev -y
sudo apt install -y zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm \
  libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git

# Pyenv
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
# Follow the instruction of Pyenv

# Download and install VSCode: https://code.visualstudio.com/download

# Download everything is optional:

# Instal and configure ZSH
sudo apt install zsh -y
chsh -s /bin/zsh
zsh

Improve the visualization of zsh terminal
# Install Oh-my-zsh! -> https://ohmyz.sh/
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Install Spaceship Prompt
https://github.com/spaceship-prompt/spaceship-prompt
git clone https://github.com/spaceship-prompt/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"

# Change ~/.zshrc -> ZSH_THEME="spaceship"

# Install Zsh Autosuggestions
https://github.com/zsh-users/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Install Zsh Syntax Highlighting
https://github.com/zsh-users/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
\zsh
nano ~/.zshrc
ZSH_THEME="spaceship"
Ctrl+O (Save)
Ctrl+X (Exit)

# Change plugins
zsh
nano ~/.zshrc
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
Ctrl+O (Save)
Ctrl+X (Exit)

pyenv Commands (at the end)
zsh
nano ~/.zshrc
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
Ctrl+O (Save)
Ctrl+X (Exit)

Exit zsh shell:
$ exec SHELL

$ zsh
$ pyenv update

Definition of the Python's global version:
$ pyenv global 3.11.0

# Font optional (https://github.com/pdf/ubuntu-mono-powerline-ttf)
mkdir -p ~/.fonts
git clone https://github.com/pdf/ubuntu-mono-powerline-ttf.git ~/.fonts/ubuntu-mono-powerline-ttf
fc-cache -vf

# REBOOT!!!!!!!!!!!!!!!!!!!!!
"""

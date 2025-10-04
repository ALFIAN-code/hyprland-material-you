# HyprYou

> This project is not affiliated with or sponsored by Google.

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/koeqaife/hyprland-material-you?style=for-the-badge&labelColor=%23424242&color=%23B2FF59)
![GitHub repo size](https://img.shields.io/github/repo-size/koeqaife/hyprland-material-you?style=for-the-badge&labelColor=%23424242&color=%2384FFFF)
![GitHub Repo stars](https://img.shields.io/github/stars/koeqaife/hyprland-material-you?style=for-the-badge&labelColor=%23424242&color=%23B9F6CA)
![GitHub contributors](https://img.shields.io/github/contributors/koeqaife/hyprland-material-you?style=for-the-badge&labelColor=%23424242&color=%23FFAB40)
![GitHub License](https://img.shields.io/github/license/koeqaife/hyprland-material-you?style=for-the-badge&labelColor=%23424242&color=%23FF9E80)

HyprYou (hyprland-material-you v2). It aims to provide a modern, feature-rich, and visually appealing desktop configuration. Here are some key features:

- **Material You Colors**: The project generates colors for your apps based on you wallpapers or settings.
- **Fluid Animations**: Expect natural and fluid animations throughout the desktop experience.
- **Design**: The design wherever possible is made by [Material 3 design](https://m3.material.io/)
- **Settings**: Almost all settings are possible to configure in settings! You don't need to change hyprland.conf unless you need something specific.
- **Clean home folder**: I made everything so won't have any unnecessary files in home. And from settings you can enable configs for terminals or anything else.

## Preview

- **Demo video:** [Reddit post](https://www.reddit.com/r/unixporn/comments/1mj2p6x/hyprland_hyprland_material_you_v2_hypryou/)  
- **Screenshot:** [![Screenshot](assets/screenshot.png "Screenshot")](assets/screenshot.png)

> [!TIP]
> When you run HyprYou as DE session (from SDDM, Greetd, etc.) it doesn't use `~/.config/hypr/hyprland.conf`  
> For any custom variables/configs look for `~/.config/hypryou/hyprland.conf`  
> I made that so you can have different dotfiles on one system  
> If you don't have Display Manager you can use `hyprland --config /usr/share/hypryou/configs/hyprland/main.conf`

> [!NOTE]
> I'm doing everything by myself and **for free**.  
> If you want to support me, you can buy me a coffee on [**ko-fi**](https://ko-fi.com/koeqaife).

> [!NOTE]
> If you want to talk or to check devlogs go to our Discord server  
> <https://discord.gg/nCK3sh8mNU>

## Packages info

- `hypryou` - The main package, should be installed before anything else
- `hypryou-utils` - Replacement of `hypryou-qtutils`, uses gtk4 for hyprland dialogs instead of qt
- `hypryou-greeter` - Configs for greetd, so it's replacement of SDDM or anything like that. With Material 3 theme.

## How to install (Arch)

> [!TIP]
> If you have an error like "cannot resolve dependency" you should install packages that are named there with `yay` or any other AUR helpers.  
> For very new people to ArchLinux, check this: <https://itsfoss.com/install-yay-arch-linux/>  
> Also if AUR is down (it happens sometimes) you can check for Chaotic AUR: <https://aur.chaotic.cx/>  
> And if you have errors like `Config error in file /....` just try using `hyprctl reload`

<details>
    <summary>Manual installation</summary>
    
- Install chaotic aur first, <https://aur.chaotic.cx/>
- Clone repository: `git clone --depth=1 https://github.com/koeqaife/hyprland-material-you.git`
- Install all dependencies from depends.txt
- Build Cython code by using `build.sh` in `hypryou/`
- Then copy `hypryou` to `/usr/lib/hypryou` and copy `hypryou-assets` to `/usr/share/hypryou`
- Then use `build.sh` in `build`
- Move `hypryouctl`, `hypryou-start`, `hypryou-crash-dialog` to `/usr/bin`
- Copy `assets/hypryou.desktop` to `/usr/share/wayland-sessions/`
- And run it as `HyprYou` from your display manager (Not `Hyprland`!!)
- Optional:
  - You can build `hypryou-utils` or `hypryou-greeter` if you want  
    > By using `makepkg -si` in `greeter` for `hypryou-greeter` or in `hypryou-utils`

</details>
<details>
    <summary>Automatic installation</summary>
    
  - Install chaotic aur first, <https://aur.chaotic.cx/>
 <br> then : <br>

**Build manually:**
  - `hypryou` - Use `makepkg -si`
  - `hypryou-greeter` - Use `makepkg -si` in `greeter/`
  - `hypryou-utils` - Use `makepkg -si` in `hypryou-utils/`

> Coming soon to `AUR`!

</details>

## Updating & Troubleshooting (jika perubahan lokal tidak muncul)

Jika kamu mengubah kode lokal dan setelah `makepkg -si` perubahan tidak muncul di sistem, ikuti panduan ini supaya tidak perlu menghapus konfigurasi sistem setiap kali.

1) Gunakan source lokal saat ingin build dari working tree

- Edit `PKGBUILD` dan ubah `source` menjadi `git+file://$PWD`, serta naikkan `pkgrel` untuk memaksa paket baru:

```bash
# contoh bagian di PKGBUILD
pkgver=2.1.4
pkgrel=2
source=("$_pkgname::git+file://$PWD")
sha256sums('SKIP')
```

2) Bersihkan hasil build / clone lama sebelum membangun

Jalankan dari folder yang berisi `PKGBUILD`:

```bash
rm -rf src/ pkg/ *.pkg.tar.* "${_pkgname}"*
# commit snapshot lokal (opsional)
git add .; and git commit -m "local snapshot"; or true
```

3) Hapus instalasi lama sementara (opsional, berguna untuk debugging)

```bash
sudo rm -rf /usr/lib/hypryou /usr/share/hypryou /usr/bin/hypryou* /usr/share/wayland-sessions/hypryou.desktop
```

4) Build & install paket baru

```bash
makepkg -si
```

5) Jika `makepkg` mengeluh bahwa folder bukan git repo

- Pilih salah satu:

  - Rename folder yang menghalangi supaya makepkg bisa clone remote:

  ```bash
  cd /home/alfian/alfianSpace/gitDownload
  mv hyprland-material-you hyprland-material-you.bak
  makepkg -si
  ```

  - Atur remote repository pada folder lokal jika folder tersebut memang git repo tapi remote berbeda:

  ```bash
  cd hyprland-material-you
  git remote set-url origin https://github.com/ALFIAN-code/hyprland-material-you.git
  cd ..
  makepkg -si
  ```

  - Buat clone lokal yang pasti adalah repo git dan pakai itu sebagai source:

  ```bash
  git clone --local --no-hardlinks "$PWD" /tmp/hyprland-material-you-git
  # lalu ubah PKGBUILD: source=("$_pkgname::git+file:///tmp/hyprland-material-you-git")
  makepkg -si
  ```

6) Hapus cache Python yang mungkin menyebabkan kode lama masih dipakai

```bash
sudo find /usr/lib/hypryou -name '__pycache__' -exec rm -rf {} +; or true
sudo find /usr/lib/hypryou -name '*.pyc' -delete
```

(Di dalam `PKGBUILD` kamu juga bisa tambahkan langkah menghapus `__pycache__`/`.pyc` di dalam `package()` sebelum menyalin file.)

7) Cara cepat (tanpa paket) untuk menguji perubahan lokal

```bash
sudo rm -rf /usr/lib/hypryou
sudo cp -a ./hypryou /usr/lib/hypryou
```

8) Verifikasi bahwa file yang terpasang sama dengan file lokal

```bash
md5sum /usr/lib/hypryou/src/services/hyprland_keybinds/workspaces.py \
       ./hypryou/src/services/hyprland_keybinds/workspaces.py
# atau tampilkan beberapa baris teratas
head -n 40 /usr/lib/hypryou/src/services/hyprland_keybinds/workspaces.py
head -n 40 ./hypryou/src/services/hyprland_keybinds/workspaces.py
```

Catatan penting

- Kamu tidak perlu menghapus konfigurasi sistem setiap update. Yang perlu dipastikan adalah paket baru benar-benar berisi perubahanmu.
- Naikkan `pkgrel` ketika membangun ulang dari source lokal agar package manager mengenali versi baru.
- Bersihkan folder `src/`/cache dan `.pyc` jika perubahan tidak muncul.
- Jika masih ada masalah, lampirkan output `makepkg -si` (khususnya langkah clone/copy) dan hasil `md5sum`/`head` seperti di atas agar bisa ditelaah lebih lanjut.

## Thanks to

- All people from my discord server
- All Sponsors (I love y'all!)
- [Astal](https://github.com/Aylur/astal): For Bluetooth and WirePlumber services
- [Gtk4LayerShell](https://github.com/wmww/gtk4-layer-shell): For LayerShell
- [Hyprland](https://github.com/hyprwm/Hyprland): For the best TWM I've ever seen
- Maybe that's it

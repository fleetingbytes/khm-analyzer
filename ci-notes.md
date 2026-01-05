echo "===== Switch to the Latest Ports Branch, Disable SRV Mirror Types ====="
mkdir -p /usr/local/etc/pkg/repos
cat > /usr/local/etc/pkg/repos/FreeBSD.conf <<'EOF'
FreeBSD: {
  url: "https://pkg.FreeBSD.org/${ABI}/latest",
  mirror_type: "none",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
EOF
pkg update -f
pkg upgrade -y
echo "===== Install Packages ====="
pkg install -y libxml2 libxslt ${{ matrix.python-data.pkg }} rust uv


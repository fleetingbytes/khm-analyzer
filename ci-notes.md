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
pkg install -y pcre2
pkg install -y git libxml2 libxslt python314 rust uv
mkdir -p /home/work/khm-analyzer; cd /home/work/khm-analyzer
git clone https://github.com/fleetingbytes/khm-analyzer
cd khm-analyzer
git switch words-sentences
uv sync --no-managed-python --locked --verbose --group test --python 3.14


# in git project:
pkg install -y libxml2 libxslt python314 rust uv
uv init --app --package minimal-example
cd minimal-example
uv add --verbose lxml

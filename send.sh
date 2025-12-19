rsync -avzc --delete --exclude .direnv/ --exclude .git/ --exclude .venv/ \
  . robo@roboberry.local:robocup2026-raspberrypi-kanto

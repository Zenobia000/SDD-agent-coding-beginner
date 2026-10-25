"""Package separate student and company handouts using only the standard library."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import argparse

ROOT = Path(__file__).resolve().parents[1]


def package(output, files):
    files = sorted(files)
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
        for source in files:
            archive.write(source, source.relative_to(ROOT).as_posix())
    print(f'{output.relative_to(ROOT)}: {len(files)} files, {output.stat().st_size:,} bytes')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    student = [ROOT / '開啟講義.html', ROOT / 'LICENSE']
    student += [p for p in (ROOT / 'handbook/site').rglob('*') if p.is_file()]
    gifts = [ROOT / 'starter-kit/index.html', ROOT / 'starter-kit/README.md']
    for folder in ('deck', 'skill-deck'):
        gifts += [p for p in (ROOT / 'starter-kit' / folder).rglob('*') if p.is_file()]
    package(args.output_dir / '學生講義.zip', student)
    package(args.output_dir / '企業贈禮.zip', gifts)


if __name__ == '__main__':
    main()

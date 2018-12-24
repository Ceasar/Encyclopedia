import sass


def main(sass_dir, css_dir):
    sass.compile(dirname=(sass_dir, css_dir), output_style='compressed')

if __name__ == '__main__':
    import sys
    main(sys.argv[1], sys.argv[2])

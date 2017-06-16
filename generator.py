def generate_html(lines, mode="110"):
    title = mode
    fo = open("index.html", "w")
    head = "<!DOCTYPE html>\n" \
          + "<html lang=\"en\">\n" \
          + "<head>\n" \
          + "<meta http-equiv=\"Content-Type\"content=\"text/html; charset=utf-8\">\n" \
          + "<title>Rule " + title + "</title>\n" \
          + "<link rel=\"stylesheet\"type=\"text/css\" href=\"css/styles.css\"></head><body>"
    print(head, file=fo)

    count = 0

    cp0 = "<input type=\"checkbox\" id=\"cp"
    cp1 = "\" class=\"hidden\" />\n"

    cpl0 = "<label for=\"cp"
    cpl1 = "\"></label>"

    c0 = "<input type=\"checkbox\" id=\"c"
    c1 = "\"/>\n<label for=\"c"
    c2 = "\"></label>"

    for i in range(lines):
        for i in range(10):
            if i % 10 == 0:
                print(cp0 + str(count) + cp1 + cpl0 + str(count) + cpl1, file=fo)
            print(c0 + str(count) + c1 + str(count) + c2, file=fo)
            count += 1

    tail = '<div id="infobox">\n' \
         + '<input type="checkbox" id="ready" />\n' \
         + '<ul id="messages">\n' \
         + '<li><label for="ready">Click me when ready.</label></li>\n' \
         + '<li>Tap tab.</li>\n' \
         + '<li>Press space.</li>\n' \
         + '</ul>\n' \
         + '</div>\n' \
         + '</body>\n' \
         + '</html>'

    print(tail, file=fo)
    fo.close()

if __name__ == "__main__":
    generate_html(100)

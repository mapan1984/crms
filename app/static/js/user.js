$(document).ready(function() {
    var st = $('td.spend_time'),
        h  = st.text()[0],
        m  = st.text().substring(2, 4),
        s  = st.text().substring(5, 7);
    h = parseInt(h, 10);
    s = parseInt(s, 10);
    m = parseInt(m, 10);
    setInterval(function() {
        st.text(h+':'+m+':'+s);
        s = s + 1;
        if (s == 60) {
            s = 0;
            m = m + 1;
        }
        if (m == 60) {
            m = 0;
            h = h +1;
        }
    }, 1000);
});

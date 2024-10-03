cryptoIS = require("crypto-js")
function Qt() {
            var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {}
              , e = {
                app_id: F,
                ts: +new Date,
                platform: "desktop",
                v: 210
            };
            Object.assign(t, e);
            var n = Wt(t);
            return n += "&key=" + U,
            t.sign = Xt(n),
            Object.assign(t, e)
        }

var DiffieHellman = /** @class */ (function () {
    function DiffieHellman(p, g) {
        this.p = p;
        this.g = g;
        this.b = 0;
    }
    DiffieHellman.prototype.bobInit = function () {
        this.b = Math.floor(Math.random() * ((500 - 200) + 1) + 5);
        var B = (Math.pow(this.g, this.b) % this.b);
    };
    DiffieHellman.prototype.bobKey = function (aliceKey) {
        return (Math.pow(aliceKey, this.b) % this.p);
    };
    return DiffieHellman;
}());

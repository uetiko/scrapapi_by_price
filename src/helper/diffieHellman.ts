class DiffieHellman {
  p: number;
  g: number;
  b: number;
  
  constructor(p: number, g: number){
    this.p = p;
    this.g = g;
    this.b = 0;
  }
  bobInit(){
    this.b = Math.floor(Math.random() * ((500 - 200) + 1) + 5);
    var B = (Math.pow(this.g, this.b) % this.b);
  }
  bobKey(aliceKey: number){
    return (Math.pow(aliceKey, this.b) % this.p);
  }
}

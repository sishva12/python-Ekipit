var s1=0;
var s2=1;
for(let x = 1; x<=100; x++)  { 
if(x%2 == 0){
   s1=s1+x;
}

else if(x%2 == 1) {
    s2=s2*x;
}
}
console.log("even numbers sum is:"+" "+s1);
console.log("odd numbers multiplication is:"+" "+s2);

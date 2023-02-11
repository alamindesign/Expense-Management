// Daily expenses calculating total price
let itemPrice = document.querySelectorAll(".itemPrice");
let priceArray = Array.from(itemPrice);
let itemQuantity = document.querySelectorAll(".itemQuantity");
let quantityArray = Array.from(itemQuantity);
let totalPrice = document.querySelectorAll(".totalPrice");
let totalPriceArray = Array.from(totalPrice);
for(i = 0; i < priceArray.length; i++){
    let total = (Number(priceArray[i].innerHTML) * Number(quantityArray[i].innerHTML));
    totalPriceArray[i].innerHTML = total;
}

// Balance  Calculating net balance
let previousBalance = document.querySelectorAll(".priviousBalance");
let priviousBalanceArray = Array.from(previousBalance);
console.log(priviousBalanceArray);
let withdrawAmount = document.querySelectorAll(".withdrawAmount");
let withdrawAmountArray= Array.from(withdrawAmount);
let totalCost = document.querySelectorAll(".totalCOst");
let totalCostArray = Array.from(totalCost);
let netBalance = document.querySelectorAll(".netBalance");
let netBalanceArray= Array.from(netBalance);
for(i = 0; i < priviousBalanceArray.length; i++){
    netBalanceArray[i].innerHTML = Number(priviousBalanceArray[i].innerHTML) + Number(withdrawAmountArray[i].innerHTML)- Number(totalCostArray[i].innerHTML);
}
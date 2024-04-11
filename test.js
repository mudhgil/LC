// function merge(a,b){
//     let result = ''
//     const minLength = Math.min(a.length, b.length)
//     for(let i = 0; i<minLength; i++){
//         result += a + b
//     }
//     return result + a.slice(minLength) + b.slice(minLength)
// }
// console.log(merge('cat','dog'))

// #GCD

// function gcd(a, b){
//     while(b !== 0){
//         let temp = b;
//         b = a%b;
//         a = temp;
//     }
//     return a;
// }
// function common(a, b){
//     const gcdValue = gcd(a.length, b.length);
//     return b.slice(b.length - gcdValue);
// }
// console.log(common(a = "ABCABC", b = "ABC"))


//Kids with Candies


// var kidsWithCandies = function(candies, extraCandies) {
//     const maxCandies = Math.max(...candies);
    
//     const result = [];
    
//     for (let i = 0; i < candies.length; i++) {
//       if (candies + extraCandies >= maxCandies) {
//         result.push(true);
//       } else {
//         result.push(false);
//       }
//     }
    
//     return result;
//   };
  
//   console.log(candy([2, 3, 5, 1, 3], 3));

//Flowerbed

// function flower(flowerbed, n){
//     if (n === 0){
//         return true;
//     }
//     for (let i = 0; i < flowerbed.length; i++){
//         if (flowerbed == 0 && (i == 0 || flowerbed[i-1]==0) && (i == flowerbed.length-1 || flowerbed[i+1]==0)){
//             flowerbed = 1
//             n -= 1
//             i++;
//             if (n == 0){
//                 return true
//             }
    
//         }
//     }
//     return false
// }
// console.log(flower([1,0,0,0,0,0,1], 2))

//reverseVowel

// const reverse = (s) =>{
//     const vowels = 'aeiouAEIOU'
//     const strArr = s.split('')
//     let l = 0
//     let r = strArr.length-1
//     while(l<r){
//         if(vowels.includes(strArr[l]) && vowels.includes(strArr[r])){
//             [strArr[l], strArr[r]] = [strArr[r], strArr[l]];
//             l++;
//             r--;
//         }else if (!vowels.includes(strArr[l])){
//             l++;
//         }else{
//             r--;
//         }
//     }
//     return strArr.join('')
// }
// console.log(reverse('hello'))

//STRING REVERSAL

// const reversal = (s) =>  {
// const x = s.split(' ');
// const reversedWords = x.reverse();
// return reversedWords.join(' ');
// }
// console.log(reversal('the sky is blue'))


//Product except self

// const product = (arr) =>{
//     const l = arr.length
//     const result = Array(l).fill(1)
//     let pre = 1
//     let post = 1
//     for (let i=0; i<l; i++){
//         result = result*pre
//         pre = pre*arr
//         result[l-1-i] = result*post
//         post = post*arr[l-1-i]
        
//     }
//     return result
// }
// console.log(product([1,2,3,4]))

//Increasing Triplet

// const triplet = (nums) =>{
//     let first_small = Infinity
//     let second_small = Infinity
//     for (let num of nums){
//         if (num< first_small){
//             second_small = first_small
//             first_small = num
//         }else if (num<second_small){
//             second_small = num
//         }else{
//             return true
//         }
//     }
//     return false
// }
// console.log(triplet([5,4,3,2,1]))

// Move Zeroes

// const moveZeroes = (nums) =>{
//     let i = 0
//     for (let j=0; j<nums.length; j++){
//         if (nums[j] != 0){
//             [nums[i], nums[j]] = [nums[j], nums[i]]
//             i++
//         }
//     }
//     return nums
// }
// console.log(moveZeroes([0,6,4,0,2,4]))

// const sequence = (s, t) =>{
//     let i = 0
//     let j = 0
//     while (i<s.length && j<t.length){
//         if (s[i] == t[j]){
//             i+=1
//         }
//         j+=1
    
//     }
//     return i == s.length
// }
// console.log(sequence("abc", "ahbgdc"))

//Container with most water

// const water = (h) =>{
//     let l = 0
//     let r = h.length-1
//     let result = 0
//     let currVal = 0
//     while (l<r){
//         currVal = Math.min(h[r], h[l]) * (r-l)
//         result = Math.max(currVal, result)
//         if (h[l]<h[r]){
//             l += 1
//         }else {
//             r -= 1
//         }
//     }
//     return result
// }
// console.log(water([1,1]))

//K-sum pair
// const ksum = (nums, k) =>{
//     let count = 0
//     l = 0
//     r = nums.length-1
//     while (l<r){
//         if (nums[l] + nums[r] == k){
//             l += 1
//             r -= 1
//             count += 1
//         }else if (nums[l] + nums[r] > k){
//             l += 1
//         }else{
//             r -= 1
//         }
//     }
//     return count
// }
// console.log(ksum([3,1,3,4,3], k = 6))

const avg = (nums, k) => {
    let maxSum = nums.slice(0, k).reduce((acc, curr) => acc + curr, 0);
    let currSum = maxSum;
    for (let i = k; i < nums.length; i++) {
      currSum += nums[i] - nums[i - k];
      maxSum = Math.max(currSum, maxSum);
    }
    return maxSum/k;
  };
  
  console.log(avg([1, 12, -5, -6, 50, 3], 4)); // Output: 52
// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let customer_name;
let balance;

function openAccount(name){
  balance = 0;
  // Set the value for customer_name equal to name below
  //First write the function
  customer_name = name;
  // if ('customer_name'= name)
  return `Hello ${customer_name}`//write the statment you need to return here
}

function deposit(value){
  balance = balance + value;
  return `${customer_name} has ${balance} in account.`
  // update the value of balance
  //return the correct statement
}

function withdraw(wdvalue){
  balance = balance - wdvalue
  return `${customer_name} has ${balance} in account`;
  //update the value of balance
  //return the correct statement
}

// Write your script below

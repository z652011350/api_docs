

============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SortedArray.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SortedArray

# Interface: SortedArray\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:31

## Extends

- `Array`\<`T`\>

## Type Parameters

### T

`T`

## Indexable

\[`n`: `number`\]: `T`

## Properties

###  \_\_sortedArrayBrand

> ** \_\_sortedArrayBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:32

***

### \[unscopables\]

> `readonly` **\[unscopables\]**: `object`

Defined in: node\_modules/typescript/lib/lib.es2015.symbol.wellknown.d.ts:97

Is an object whose properties have the value 'true'
when they will be absent when used in a 'with' statement.

#### Index Signature

\[`key`: `number`\]: `undefined` \| `boolean`

#### \[iterator\]?

> `optional` **\[iterator\]**: `boolean`

#### \[unscopables\]?

> `readonly` `optional` **\[unscopables\]**: `boolean`

Is an object whose properties have the value 'true'
when they will be absent when used in a 'with' statement.

#### at?

> `optional` **at**: `boolean`

#### concat?

> `optional` **concat**: `boolean`

#### copyWithin?

> `optional` **copyWithin**: `boolean`

#### entries?

> `optional` **entries**: `boolean`

#### every?

> `optional` **every**: `boolean`

#### fill?

> `optional` **fill**: `boolean`

#### filter?

> `optional` **filter**: `boolean`

#### find?

> `optional` **find**: `boolean`

#### findIndex?

> `optional` **findIndex**: `boolean`

#### flat?

> `optional` **flat**: `boolean`

#### flatMap?

> `optional` **flatMap**: `boolean`

#### forEach?

> `optional` **forEach**: `boolean`

#### includes?

> `optional` **includes**: `boolean`

#### indexOf?

> `optional` **indexOf**: `boolean`

#### join?

> `optional` **join**: `boolean`

#### keys?

> `optional` **keys**: `boolean`

#### lastIndexOf?

> `optional` **lastIndexOf**: `boolean`

#### length?

> `optional` **length**: `boolean`

Gets or sets the length of the array. This is a number one higher than the highest index in the array.

#### map?

> `optional` **map**: `boolean`

#### pop?

> `optional` **pop**: `boolean`

#### push?

> `optional` **push**: `boolean`

#### reduce?

> `optional` **reduce**: `boolean`

#### reduceRight?

> `optional` **reduceRight**: `boolean`

#### reverse?

> `optional` **reverse**: `boolean`

#### shift?

> `optional` **shift**: `boolean`

#### slice?

> `optional` **slice**: `boolean`

#### some?

> `optional` **some**: `boolean`

#### sort?

> `optional` **sort**: `boolean`

#### splice?

> `optional` **splice**: `boolean`

#### toLocaleString?

> `optional` **toLocaleString**: `boolean`

#### toString?

> `optional` **toString**: `boolean`

#### unshift?

> `optional` **unshift**: `boolean`

#### values?

> `optional` **values**: `boolean`

#### Inherited from

`Array.[unscopables]`

***

### length

> **length**: `number`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1326

Gets or sets the length of the array. This is a number one higher than the highest index in the array.

#### Inherited from

`Array.length`

## Methods

### \[iterator\]()

> **\[iterator\]**(): `IterableIterator`\<`T`\>

Defined in: node\_modules/typescript/lib/lib.es2015.iterable.d.ts:58

Iterator

#### Returns

`IterableIterator`\<`T`\>

#### Inherited from

`Array.[iterator]`

***

### at()

> **at**(`index`): `undefined` \| `T`

Defined in: node\_modules/@types/node/compatibility/indexable.d.ts:7

#### Parameters

##### index

`number`

#### Returns

`undefined` \| `T`

#### Inherited from

`Array.at`

***

### concat()

#### Call Signature

> **concat**(...`items`): `T`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1350

Combines two or more arrays.
This method returns a new array without modifying any existing arrays.

##### Parameters

###### items

...`ConcatArray`\<`T`\>[]

Additional arrays and/or items to add to the end of the array.

##### Returns

`T`[]

##### Inherited from

`Array.concat`

#### Call Signature

> **concat**(...`items`): `T`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1356

Combines two or more arrays.
This method returns a new array without modifying any existing arrays.

##### Parameters

###### items

...(`T` \| `ConcatArray`\<`T`\>)[]

Additional arrays and/or items to add to the end of the array.

##### Returns

`T`[]

##### Inherited from

`Array.concat`

***

### copyWithin()

> **copyWithin**(`target`, `start`, `end?`): `this`

Defined in: node\_modules/typescript/lib/lib.es2015.core.d.ts:62

Returns the this object after copying a section of the array identified by start and end
to the same array starting at position target

#### Parameters

##### target

`number`

If target is negative, it is treated as length+target where length is the
length of the array.

##### start

`number`

If start is negative, it is treated as length+start. If end is negative, it
is treated as length+end.

##### end?

`number`

If not specified, length of the this object is used as its default value.

#### Returns

`this`

#### Inherited from

`Array.copyWithin`

***

### entries()

> **entries**(): `IterableIterator`\<\[`number`, `T`\]\>

Defined in: node\_modules/typescript/lib/lib.es2015.iterable.d.ts:63

Returns an iterable of key, value pairs for every entry in the array

#### Returns

`IterableIterator`\<\[`number`, `T`\]\>

#### Inherited from

`Array.entries`

***

### every()

#### Call Signature

> **every**\<`S`\>(`predicate`, `thisArg?`): `this is S[]`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1433

Determines whether all the members of an array satisfy the specified test.

##### Type Parameters

###### S

`S`

##### Parameters

###### predicate

(`value`, `index`, `array`) => `value is S`

A function that accepts up to three arguments. The every method calls
the predicate function for each element in the array until the predicate returns a value
which is coercible to the Boolean value false, or until the end of the array.

###### thisArg?

`any`

An object to which the this keyword can refer in the predicate function.
If thisArg is omitted, undefined is used as the this value.

##### Returns

`this is S[]`

##### Inherited from

`Array.every`

#### Call Signature

> **every**(`predicate`, `thisArg?`): `boolean`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1442

Determines whether all the members of an array satisfy the specified test.

##### Parameters

###### predicate

(`value`, `index`, `array`) => `unknown`

A function that accepts up to three arguments. The every method calls
the predicate function for each element in the array until the predicate returns a value
which is coercible to the Boolean value false, or until the end of the array.

###### thisArg?

`any`

An object to which the this keyword can refer in the predicate function.
If thisArg is omitted, undefined is used as the this value.

##### Returns

`boolean`

##### Inherited from

`Array.every`

***

### fill()

> **fill**(`value`, `start?`, `end?`): `this`

Defined in: node\_modules/typescript/lib/lib.es2015.core.d.ts:51

Changes all array elements from `start` to `end` index to a static `value` and returns the modified array

#### Parameters

##### value

`T`

value to fill array section with

##### start?

`number`

index to start filling the array at. If start is negative, it is treated as
length+start where length is the length of the array.

##### end?

`number`

index to stop filling the array at. If end is negative, it is treated as
length+end.

#### Returns

`this`

#### Inherited from

`Array.fill`

***

### filter()

#### Call Signature

> **filter**\<`S`\>(`predicate`, `thisArg?`): `S`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1469

Returns the elements of an array that meet the condition specified in a callback function.

##### Type Parameters

###### S

`S`

##### Parameters

###### predicate

(`value`, `index`, `array`) => `value is S`

A function that accepts up to three arguments. The filter method calls the predicate function one time for each element in the array.

###### thisArg?

`any`

An object to which the this keyword can refer in the predicate function. If thisArg is omitted, undefined is used as the this value.

##### Returns

`S`[]

##### Inherited from

`Array.filter`

#### Call Signature

> **filter**(`predicate`, `thisArg?`): `T`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1475

Returns the elements of an array that meet the condition specified in a callback function.

##### Parameters

###### predicate

(`value`, `index`, `array`) => `unknown`

A function that accepts up to three arguments. The filter method calls the predicate function one time for each element in the array.

###### thisArg?

`any`

An object to which the this keyword can refer in the predicate function. If thisArg is omitted, undefined is used as the this value.

##### Returns

`T`[]

##### Inherited from

`Array.filter`

***

### find()

#### Call Signature

> **find**\<`S`\>(`predicate`, `thisArg?`): `undefined` \| `S`

Defined in: node\_modules/typescript/lib/lib.es2015.core.d.ts:29

Returns the value of the first element in the array where predicate is true, and undefined
otherwise.

##### Type Parameters

###### S

`S`

##### Parameters

###### predicate

(`value`, `index`, `obj`) => `value is S`

find calls predicate once for each element of the array, in ascending
order, until it finds one where predicate returns true. If such an element is found, find
immediately returns that element value. Otherwise, find returns undefined.

###### thisArg?

`any`

If provided, it will be used as the this value for each invocation of
predicate. If it is not provided, undefined is used instead.

##### Returns

`undefined` \| `S`

##### Inherited from

`Array.find`

#### Call Signature

> **find**(`predicate`, `thisArg?`): `undefined` \| `T`

Defined in: node\_modules/typescript/lib/lib.es2015.core.d.ts:30

##### Parameters

###### predicate

(`value`, `index`, `obj`) => `unknown`

###### thisArg?

`any`

##### Returns

`undefined` \| `T`

##### Inherited from

`Array.find`

***

### findIndex()

> **findIndex**(`predicate`, `thisArg?`): `number`

Defined in: node\_modules/typescript/lib/lib.es2015.core.d.ts:41

Returns the index of the first element in the array where predicate is true, and -1
otherwise.

#### Parameters

##### predicate

(`value`, `index`, `obj`) => `unknown`

find calls predicate once for each element of the array, in ascending
order, until it finds one where predicate returns true. If such an element is found,
findIndex immediately returns that element index. Otherwise, findIndex returns -1.

##### thisArg?

`any`

If provided, it will be used as the this value for each invocation of
predicate. If it is not provided, undefined is used instead.

#### Returns

`number`

#### Inherited from

`Array.findIndex`

***

### flat()

> **flat**\<`A`, `D`\>(`this`, `depth?`): `FlatArray`\<`A`, `D`\>[]

Defined in: node\_modules/typescript/lib/lib.es2019.array.d.ts:75

Returns a new array with all sub-array elements concatenated into it recursively up to the
specified depth.

#### Type Parameters

##### A

`A`

##### D

`D` *extends* `number` = `1`

#### Parameters

##### this

`A`

##### depth?

`D`

The maximum recursion depth

#### Returns

`FlatArray`\<`A`, `D`\>[]

#### Inherited from

`Array.flat`

***

### flatMap()

> **flatMap**\<`U`, `This`\>(`callback`, `thisArg?`): `U`[]

Defined in: node\_modules/typescript/lib/lib.es2019.array.d.ts:64

Calls a defined callback function on each element of an array. Then, flattens the result into
a new array.
This is identical to a map followed by flat with depth 1.

#### Type Parameters

##### U

`U`

##### This

`This` = `undefined`

#### Parameters

##### callback

(`this`, `value`, `index`, `array`) => `U` \| readonly `U`[]

A function that accepts up to three arguments. The flatMap method calls the
callback function one time for each element in the array.

##### thisArg?

`This`

An object to which the this keyword can refer in the callback function. If
thisArg is omitted, undefined is used as the this value.

#### Returns

`U`[]

#### Inherited from

`Array.flatMap`

***

### forEach()

> **forEach**(`callbackfn`, `thisArg?`): `void`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1457

Performs the specified action for each element in an array.

#### Parameters

##### callbackfn

(`value`, `index`, `array`) => `void`

A function that accepts up to three arguments. forEach calls the callbackfn function one time for each element in the array.

##### thisArg?

`any`

An object to which the this keyword can refer in the callbackfn function. If thisArg is omitted, undefined is used as the this value.

#### Returns

`void`

#### Inherited from

`Array.forEach`

***

### includes()

> **includes**(`searchElement`, `fromIndex?`): `boolean`

Defined in: node\_modules/typescript/lib/lib.es2016.array.include.d.ts:25

Determines whether an array includes a certain element, returning true or false as appropriate.

#### Parameters

##### searchElement

`T`

The element to search for.

##### fromIndex?

`number`

The position in this array at which to begin searching for searchElement.

#### Returns

`boolean`

#### Inherited from

`Array.includes`

***

### indexOf()

> **indexOf**(`searchElement`, `fromIndex?`): `number`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1418

Returns the index of the first occurrence of a value in an array, or -1 if it is not present.

#### Parameters

##### searchElement

`T`

The value to locate in the array.

##### fromIndex?

`number`

The array index at which to begin the search. If fromIndex is omitted, the search starts at index 0.

#### Returns

`number`

#### Inherited from

`Array.indexOf`

***

### join()

> **join**(`separator?`): `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1361

Adds all the elements of an array into a string, separated by the specified separator string.

#### Parameters

##### separator?

`string`

A string used to separate one element of the array from the next in the resulting string. If omitted, the array elements are separated with a comma.

#### Returns

`string`

#### Inherited from

`Array.join`

***

### keys()

> **keys**(): `IterableIterator`\<`number`\>

Defined in: node\_modules/typescript/lib/lib.es2015.iterable.d.ts:68

Returns an iterable of keys in the array

#### Returns

`IterableIterator`\<`number`\>

#### Inherited from

`Array.keys`

***

### lastIndexOf()

> **lastIndexOf**(`searchElement`, `fromIndex?`): `number`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1424

Returns the index of the last occurrence of a specified value in an array, or -1 if it is not present.

#### Parameters

##### searchElement

`T`

The value to locate in the array.

##### fromIndex?

`number`

The array index at which to begin searching backward. If fromIndex is omitted, the search starts at the last index in the array.

#### Returns

`number`

#### Inherited from

`Array.lastIndexOf`

***

### map()

> **map**\<`U`\>(`callbackfn`, `thisArg?`): `U`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1463

Calls a defined callback function on each element of an array, and returns an array that contains the results.

#### Type Parameters

##### U

`U`

#### Parameters

##### callbackfn

(`value`, `index`, `array`) => `U`

A function that accepts up to three arguments. The map method calls the callbackfn function one time for each element in the array.

##### thisArg?

`any`

An object to which the this keyword can refer in the callbackfn function. If thisArg is omitted, undefined is used as the this value.

#### Returns

`U`[]

#### Inherited from

`Array.map`

***

### pop()

> **pop**(): `undefined` \| `T`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1339

Removes the last element from an array and returns it.
If the array is empty, undefined is returned and the array is not modified.

#### Returns

`undefined` \| `T`

#### Inherited from

`Array.pop`

***

### push()

> **push**(...`items`): `number`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1344

Appends new elements to the end of an array, and returns the new length of the array.

#### Parameters

##### items

...`T`[]

New elements to add to the array.

#### Returns

`number`

#### Inherited from

`Array.push`

***

### reduce()

#### Call Signature

> **reduce**(`callbackfn`): `T`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1481

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

##### Parameters

###### callbackfn

(`previousValue`, `currentValue`, `currentIndex`, `array`) => `T`

A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array.

##### Returns

`T`

##### Inherited from

`Array.reduce`

#### Call Signature

> **reduce**(`callbackfn`, `initialValue`): `T`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1482

##### Parameters

###### callbackfn

(`previousValue`, `currentValue`, `currentIndex`, `array`) => `T`

###### initialValue

`T`

##### Returns

`T`

##### Inherited from

`Array.reduce`

#### Call Signature

> **reduce**\<`U`\>(`callbackfn`, `initialValue`): `U`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1488

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

##### Type Parameters

###### U

`U`

##### Parameters

###### callbackfn

(`previousValue`, `currentValue`, `currentIndex`, `array`) => `U`

A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array.

###### initialValue

`U`

If initialValue is specified, it is used as the initial value to start the accumulation. The first call to the callbackfn function provides this value as an argument instead of an array value.

##### Returns

`U`

##### Inherited from

`Array.reduce`

***

### reduceRight()

#### Call Signature

> **reduceRight**(`callbackfn`): `T`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1494

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

##### Parameters

###### callbackfn

(`previousValue`, `currentValue`, `currentIndex`, `array`) => `T`

A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array.

##### Returns

`T`

##### Inherited from

`Array.reduceRight`

#### Call Signature

> **reduceRight**(`callbackfn`, `initialValue`): `T`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1495

##### Parameters

###### callbackfn

(`previousValue`, `currentValue`, `currentIndex`, `array`) => `T`

###### initialValue

`T`

##### Returns

`T`

##### Inherited from

`Array.reduceRight`

#### Call Signature

> **reduceRight**\<`U`\>(`callbackfn`, `initialValue`): `U`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1501

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

##### Type Parameters

###### U

`U`

##### Parameters

###### callbackfn

(`previousValue`, `currentValue`, `currentIndex`, `array`) => `U`

A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array.

###### initialValue

`U`

If initialValue is specified, it is used as the initial value to start the accumulation. The first call to the callbackfn function provides this value as an argument instead of an array value.

##### Returns

`U`

##### Inherited from

`Array.reduceRight`

***

### reverse()

> **reverse**(): `T`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1366

Reverses the elements in an array in place.
This method mutates the array and returns a reference to the same array.

#### Returns

`T`[]

#### Inherited from

`Array.reverse`

***

### shift()

> **shift**(): `undefined` \| `T`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1371

Removes the first element from an array and returns it.
If the array is empty, undefined is returned and the array is not modified.

#### Returns

`undefined` \| `T`

#### Inherited from

`Array.shift`

***

### slice()

> **slice**(`start?`, `end?`): `T`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1381

Returns a copy of a section of an array.
For both start and end, a negative index can be used to indicate an offset from the end of the array.
For example, -2 refers to the second to last element of the array.

#### Parameters

##### start?

`number`

The beginning index of the specified portion of the array.
If start is undefined, then the slice begins at index 0.

##### end?

`number`

The end index of the specified portion of the array. This is exclusive of the element at the index 'end'.
If end is undefined, then the slice extends to the end of the array.

#### Returns

`T`[]

#### Inherited from

`Array.slice`

***

### some()

> **some**(`predicate`, `thisArg?`): `boolean`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1451

Determines whether the specified callback function returns true for any element of an array.

#### Parameters

##### predicate

(`value`, `index`, `array`) => `unknown`

A function that accepts up to three arguments. The some method calls
the predicate function for each element in the array until the predicate returns a value
which is coercible to the Boolean value true, or until the end of the array.

##### thisArg?

`any`

An object to which the this keyword can refer in the predicate function.
If thisArg is omitted, undefined is used as the this value.

#### Returns

`boolean`

#### Inherited from

`Array.some`

***

### sort()

> **sort**(`compareFn?`): `this`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1392

Sorts an array in place.
This method mutates the array and returns a reference to the same array.

#### Parameters

##### compareFn?

(`a`, `b`) => `number`

Function used to determine the order of the elements. It is expected to return
a negative value if the first argument is less than the second argument, zero if they're equal, and a positive
value otherwise. If omitted, the elements are sorted in ascending, ASCII character order.
```ts
[11,2,22,1].sort((a, b) => a - b)
```

#### Returns

`this`

#### Inherited from

`Array.sort`

***

### splice()

#### Call Signature

> **splice**(`start`, `deleteCount?`): `T`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1399

Removes elements from an array and, if necessary, inserts new elements in their place, returning the deleted elements.

##### Parameters

###### start

`number`

The zero-based location in the array from which to start removing elements.

###### deleteCount?

`number`

The number of elements to remove.

##### Returns

`T`[]

An array containing the elements that were deleted.

##### Inherited from

`Array.splice`

#### Call Signature

> **splice**(`start`, `deleteCount`, ...`items`): `T`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1407

Removes elements from an array and, if necessary, inserts new elements in their place, returning the deleted elements.

##### Parameters

###### start

`number`

The zero-based location in the array from which to start removing elements.

###### deleteCount

`number`

The number of elements to remove.

###### items

...`T`[]

Elements to insert into the array in place of the deleted elements.

##### Returns

`T`[]

An array containing the elements that were deleted.

##### Inherited from

`Array.splice`

***

### toLocaleString()

> **toLocaleString**(): `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1334

Returns a string representation of an array. The elements are converted to string using their toLocaleString methods.

#### Returns

`string`

#### Inherited from

`Array.toLocaleString`

***

### toString()

> **toString**(): `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1330

Returns a string representation of an array.

#### Returns

`string`

#### Inherited from

`Array.toString`

***

### unshift()

> **unshift**(...`items`): `number`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1412

Inserts new elements at the start of an array, and returns the new length of the array.

#### Parameters

##### items

...`T`[]

Elements to insert at the start of the array.

#### Returns

`number`

#### Inherited from

`Array.unshift`

***

### values()

> **values**(): `IterableIterator`\<`T`\>

Defined in: node\_modules/typescript/lib/lib.es2015.iterable.d.ts:73

Returns an iterable of values in the array

#### Returns

`IterableIterator`\<`T`\>

#### Inherited from

`Array.values`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SortedReadonlyArray.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SortedReadonlyArray

# Interface: SortedReadonlyArray\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:28

## Extends

- `ReadonlyArray`\<`T`\>

## Type Parameters

### T

`T`

## Indexable

\[`n`: `number`\]: `T`

## Properties

###  \_\_sortedArrayBrand

> ** \_\_sortedArrayBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:29

***

### \[unscopables\]

> `readonly` **\[unscopables\]**: `object`

Defined in: node\_modules/typescript/lib/lib.es2015.symbol.wellknown.d.ts:107

Is an object whose properties have the value 'true'
when they will be absent when used in a 'with' statement.

#### Index Signature

\[`key`: `number`\]: `undefined` \| `boolean`

#### \[iterator\]?

> `optional` **\[iterator\]**: `boolean`

#### \[unscopables\]?

> `readonly` `optional` **\[unscopables\]**: `boolean`

Is an object whose properties have the value 'true'
when they will be absent when used in a 'with' statement.

#### at?

> `optional` **at**: `boolean`

#### concat?

> `optional` **concat**: `boolean`

#### entries?

> `optional` **entries**: `boolean`

#### every?

> `optional` **every**: `boolean`

#### filter?

> `optional` **filter**: `boolean`

#### find?

> `optional` **find**: `boolean`

#### findIndex?

> `optional` **findIndex**: `boolean`

#### flat?

> `optional` **flat**: `boolean`

#### flatMap?

> `optional` **flatMap**: `boolean`

#### forEach?

> `optional` **forEach**: `boolean`

#### includes?

> `optional` **includes**: `boolean`

#### indexOf?

> `optional` **indexOf**: `boolean`

#### join?

> `optional` **join**: `boolean`

#### keys?

> `optional` **keys**: `boolean`

#### lastIndexOf?

> `optional` **lastIndexOf**: `boolean`

#### length?

> `readonly` `optional` **length**: `boolean`

Gets the length of the array. This is a number one higher than the highest element defined in an array.

#### map?

> `optional` **map**: `boolean`

#### reduce?

> `optional` **reduce**: `boolean`

#### reduceRight?

> `optional` **reduceRight**: `boolean`

#### slice?

> `optional` **slice**: `boolean`

#### some?

> `optional` **some**: `boolean`

#### toLocaleString?

> `optional` **toLocaleString**: `boolean`

#### toString?

> `optional` **toString**: `boolean`

#### values?

> `optional` **values**: `boolean`

#### Inherited from

`ReadonlyArray.[unscopables]`

***

### length

> `readonly` **length**: `number`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1192

Gets the length of the array. This is a number one higher than the highest element defined in an array.

#### Inherited from

`ReadonlyArray.length`

## Methods

### \[iterator\]()

> **\[iterator\]**(): `IterableIterator`\<`T`\>

Defined in: node\_modules/typescript/lib/lib.es2015.iterable.d.ts:94

Iterator of values in the array.

#### Returns

`IterableIterator`\<`T`\>

#### Inherited from

`ReadonlyArray.[iterator]`

***

### at()

> **at**(`index`): `undefined` \| `T`

Defined in: node\_modules/@types/node/compatibility/indexable.d.ts:7

#### Parameters

##### index

`number`

#### Returns

`undefined` \| `T`

#### Inherited from

`ReadonlyArray.at`

***

### concat()

#### Call Signature

> **concat**(...`items`): `T`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1205

Combines two or more arrays.

##### Parameters

###### items

...`ConcatArray`\<`T`\>[]

Additional items to add to the end of array1.

##### Returns

`T`[]

##### Inherited from

`ReadonlyArray.concat`

#### Call Signature

> **concat**(...`items`): `T`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1210

Combines two or more arrays.

##### Parameters

###### items

...(`T` \| `ConcatArray`\<`T`\>)[]

Additional items to add to the end of array1.

##### Returns

`T`[]

##### Inherited from

`ReadonlyArray.concat`

***

### entries()

> **entries**(): `IterableIterator`\<\[`number`, `T`\]\>

Defined in: node\_modules/typescript/lib/lib.es2015.iterable.d.ts:99

Returns an iterable of key, value pairs for every entry in the array

#### Returns

`IterableIterator`\<\[`number`, `T`\]\>

#### Inherited from

`ReadonlyArray.entries`

***

### every()

#### Call Signature

> **every**\<`S`\>(`predicate`, `thisArg?`): `this is readonly S[]`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1242

Determines whether all the members of an array satisfy the specified test.

##### Type Parameters

###### S

`S`

##### Parameters

###### predicate

(`value`, `index`, `array`) => `value is S`

A function that accepts up to three arguments. The every method calls
the predicate function for each element in the array until the predicate returns a value
which is coercible to the Boolean value false, or until the end of the array.

###### thisArg?

`any`

An object to which the this keyword can refer in the predicate function.
If thisArg is omitted, undefined is used as the this value.

##### Returns

`this is readonly S[]`

##### Inherited from

`ReadonlyArray.every`

#### Call Signature

> **every**(`predicate`, `thisArg?`): `boolean`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1251

Determines whether all the members of an array satisfy the specified test.

##### Parameters

###### predicate

(`value`, `index`, `array`) => `unknown`

A function that accepts up to three arguments. The every method calls
the predicate function for each element in the array until the predicate returns a value
which is coercible to the Boolean value false, or until the end of the array.

###### thisArg?

`any`

An object to which the this keyword can refer in the predicate function.
If thisArg is omitted, undefined is used as the this value.

##### Returns

`boolean`

##### Inherited from

`ReadonlyArray.every`

***

### filter()

#### Call Signature

> **filter**\<`S`\>(`predicate`, `thisArg?`): `S`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1278

Returns the elements of an array that meet the condition specified in a callback function.

##### Type Parameters

###### S

`S`

##### Parameters

###### predicate

(`value`, `index`, `array`) => `value is S`

A function that accepts up to three arguments. The filter method calls the predicate function one time for each element in the array.

###### thisArg?

`any`

An object to which the this keyword can refer in the predicate function. If thisArg is omitted, undefined is used as the this value.

##### Returns

`S`[]

##### Inherited from

`ReadonlyArray.filter`

#### Call Signature

> **filter**(`predicate`, `thisArg?`): `T`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1284

Returns the elements of an array that meet the condition specified in a callback function.

##### Parameters

###### predicate

(`value`, `index`, `array`) => `unknown`

A function that accepts up to three arguments. The filter method calls the predicate function one time for each element in the array.

###### thisArg?

`any`

An object to which the this keyword can refer in the predicate function. If thisArg is omitted, undefined is used as the this value.

##### Returns

`T`[]

##### Inherited from

`ReadonlyArray.filter`

***

### find()

#### Call Signature

> **find**\<`S`\>(`predicate`, `thisArg?`): `undefined` \| `S`

Defined in: node\_modules/typescript/lib/lib.es2015.core.d.ts:350

Returns the value of the first element in the array where predicate is true, and undefined
otherwise.

##### Type Parameters

###### S

`S`

##### Parameters

###### predicate

(`value`, `index`, `obj`) => `value is S`

find calls predicate once for each element of the array, in ascending
order, until it finds one where predicate returns true. If such an element is found, find
immediately returns that element value. Otherwise, find returns undefined.

###### thisArg?

`any`

If provided, it will be used as the this value for each invocation of
predicate. If it is not provided, undefined is used instead.

##### Returns

`undefined` \| `S`

##### Inherited from

`ReadonlyArray.find`

#### Call Signature

> **find**(`predicate`, `thisArg?`): `undefined` \| `T`

Defined in: node\_modules/typescript/lib/lib.es2015.core.d.ts:351

##### Parameters

###### predicate

(`value`, `index`, `obj`) => `unknown`

###### thisArg?

`any`

##### Returns

`undefined` \| `T`

##### Inherited from

`ReadonlyArray.find`

***

### findIndex()

> **findIndex**(`predicate`, `thisArg?`): `number`

Defined in: node\_modules/typescript/lib/lib.es2015.core.d.ts:362

Returns the index of the first element in the array where predicate is true, and -1
otherwise.

#### Parameters

##### predicate

(`value`, `index`, `obj`) => `unknown`

find calls predicate once for each element of the array, in ascending
order, until it finds one where predicate returns true. If such an element is found,
findIndex immediately returns that element index. Otherwise, findIndex returns -1.

##### thisArg?

`any`

If provided, it will be used as the this value for each invocation of
predicate. If it is not provided, undefined is used instead.

#### Returns

`number`

#### Inherited from

`ReadonlyArray.findIndex`

***

### flat()

> **flat**\<`A`, `D`\>(`this`, `depth?`): `FlatArray`\<`A`, `D`\>[]

Defined in: node\_modules/typescript/lib/lib.es2019.array.d.ts:47

Returns a new array with all sub-array elements concatenated into it recursively up to the
specified depth.

#### Type Parameters

##### A

`A`

##### D

`D` *extends* `number` = `1`

#### Parameters

##### this

`A`

##### depth?

`D`

The maximum recursion depth

#### Returns

`FlatArray`\<`A`, `D`\>[]

#### Inherited from

`ReadonlyArray.flat`

***

### flatMap()

> **flatMap**\<`U`, `This`\>(`callback`, `thisArg?`): `U`[]

Defined in: node\_modules/typescript/lib/lib.es2019.array.d.ts:36

Calls a defined callback function on each element of an array. Then, flattens the result into
a new array.
This is identical to a map followed by flat with depth 1.

#### Type Parameters

##### U

`U`

##### This

`This` = `undefined`

#### Parameters

##### callback

(`this`, `value`, `index`, `array`) => `U` \| readonly `U`[]

A function that accepts up to three arguments. The flatMap method calls the
callback function one time for each element in the array.

##### thisArg?

`This`

An object to which the this keyword can refer in the callback function. If
thisArg is omitted, undefined is used as the this value.

#### Returns

`U`[]

#### Inherited from

`ReadonlyArray.flatMap`

***

### forEach()

> **forEach**(`callbackfn`, `thisArg?`): `void`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1266

Performs the specified action for each element in an array.

#### Parameters

##### callbackfn

(`value`, `index`, `array`) => `void`

A function that accepts up to three arguments. forEach calls the callbackfn function one time for each element in the array.

##### thisArg?

`any`

An object to which the this keyword can refer in the callbackfn function. If thisArg is omitted, undefined is used as the this value.

#### Returns

`void`

#### Inherited from

`ReadonlyArray.forEach`

***

### includes()

> **includes**(`searchElement`, `fromIndex?`): `boolean`

Defined in: node\_modules/typescript/lib/lib.es2016.array.include.d.ts:34

Determines whether an array includes a certain element, returning true or false as appropriate.

#### Parameters

##### searchElement

`T`

The element to search for.

##### fromIndex?

`number`

The position in this array at which to begin searching for searchElement.

#### Returns

`boolean`

#### Inherited from

`ReadonlyArray.includes`

***

### indexOf()

> **indexOf**(`searchElement`, `fromIndex?`): `number`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1227

Returns the index of the first occurrence of a value in an array.

#### Parameters

##### searchElement

`T`

The value to locate in the array.

##### fromIndex?

`number`

The array index at which to begin the search. If fromIndex is omitted, the search starts at index 0.

#### Returns

`number`

#### Inherited from

`ReadonlyArray.indexOf`

***

### join()

> **join**(`separator?`): `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1215

Adds all the elements of an array separated by the specified separator string.

#### Parameters

##### separator?

`string`

A string used to separate one element of an array from the next in the resulting String. If omitted, the array elements are separated with a comma.

#### Returns

`string`

#### Inherited from

`ReadonlyArray.join`

***

### keys()

> **keys**(): `IterableIterator`\<`number`\>

Defined in: node\_modules/typescript/lib/lib.es2015.iterable.d.ts:104

Returns an iterable of keys in the array

#### Returns

`IterableIterator`\<`number`\>

#### Inherited from

`ReadonlyArray.keys`

***

### lastIndexOf()

> **lastIndexOf**(`searchElement`, `fromIndex?`): `number`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1233

Returns the index of the last occurrence of a specified value in an array.

#### Parameters

##### searchElement

`T`

The value to locate in the array.

##### fromIndex?

`number`

The array index at which to begin the search. If fromIndex is omitted, the search starts at the last index in the array.

#### Returns

`number`

#### Inherited from

`ReadonlyArray.lastIndexOf`

***

### map()

> **map**\<`U`\>(`callbackfn`, `thisArg?`): `U`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1272

Calls a defined callback function on each element of an array, and returns an array that contains the results.

#### Type Parameters

##### U

`U`

#### Parameters

##### callbackfn

(`value`, `index`, `array`) => `U`

A function that accepts up to three arguments. The map method calls the callbackfn function one time for each element in the array.

##### thisArg?

`any`

An object to which the this keyword can refer in the callbackfn function. If thisArg is omitted, undefined is used as the this value.

#### Returns

`U`[]

#### Inherited from

`ReadonlyArray.map`

***

### reduce()

#### Call Signature

> **reduce**(`callbackfn`): `T`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1290

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

##### Parameters

###### callbackfn

(`previousValue`, `currentValue`, `currentIndex`, `array`) => `T`

A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array.

##### Returns

`T`

##### Inherited from

`ReadonlyArray.reduce`

#### Call Signature

> **reduce**(`callbackfn`, `initialValue`): `T`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1291

##### Parameters

###### callbackfn

(`previousValue`, `currentValue`, `currentIndex`, `array`) => `T`

###### initialValue

`T`

##### Returns

`T`

##### Inherited from

`ReadonlyArray.reduce`

#### Call Signature

> **reduce**\<`U`\>(`callbackfn`, `initialValue`): `U`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1297

Calls the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

##### Type Parameters

###### U

`U`

##### Parameters

###### callbackfn

(`previousValue`, `currentValue`, `currentIndex`, `array`) => `U`

A function that accepts up to four arguments. The reduce method calls the callbackfn function one time for each element in the array.

###### initialValue

`U`

If initialValue is specified, it is used as the initial value to start the accumulation. The first call to the callbackfn function provides this value as an argument instead of an array value.

##### Returns

`U`

##### Inherited from

`ReadonlyArray.reduce`

***

### reduceRight()

#### Call Signature

> **reduceRight**(`callbackfn`): `T`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1303

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

##### Parameters

###### callbackfn

(`previousValue`, `currentValue`, `currentIndex`, `array`) => `T`

A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array.

##### Returns

`T`

##### Inherited from

`ReadonlyArray.reduceRight`

#### Call Signature

> **reduceRight**(`callbackfn`, `initialValue`): `T`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1304

##### Parameters

###### callbackfn

(`previousValue`, `currentValue`, `currentIndex`, `array`) => `T`

###### initialValue

`T`

##### Returns

`T`

##### Inherited from

`ReadonlyArray.reduceRight`

#### Call Signature

> **reduceRight**\<`U`\>(`callbackfn`, `initialValue`): `U`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1310

Calls the specified callback function for all the elements in an array, in descending order. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.

##### Type Parameters

###### U

`U`

##### Parameters

###### callbackfn

(`previousValue`, `currentValue`, `currentIndex`, `array`) => `U`

A function that accepts up to four arguments. The reduceRight method calls the callbackfn function one time for each element in the array.

###### initialValue

`U`

If initialValue is specified, it is used as the initial value to start the accumulation. The first call to the callbackfn function provides this value as an argument instead of an array value.

##### Returns

`U`

##### Inherited from

`ReadonlyArray.reduceRight`

***

### slice()

> **slice**(`start?`, `end?`): `T`[]

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1221

Returns a section of an array.

#### Parameters

##### start?

`number`

The beginning of the specified portion of the array.

##### end?

`number`

The end of the specified portion of the array. This is exclusive of the element at the index 'end'.

#### Returns

`T`[]

#### Inherited from

`ReadonlyArray.slice`

***

### some()

> **some**(`predicate`, `thisArg?`): `boolean`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1260

Determines whether the specified callback function returns true for any element of an array.

#### Parameters

##### predicate

(`value`, `index`, `array`) => `unknown`

A function that accepts up to three arguments. The some method calls
the predicate function for each element in the array until the predicate returns a value
which is coercible to the Boolean value true, or until the end of the array.

##### thisArg?

`any`

An object to which the this keyword can refer in the predicate function.
If thisArg is omitted, undefined is used as the this value.

#### Returns

`boolean`

#### Inherited from

`ReadonlyArray.some`

***

### toLocaleString()

> **toLocaleString**(): `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1200

Returns a string representation of an array. The elements are converted to string using their toLocaleString methods.

#### Returns

`string`

#### Inherited from

`ReadonlyArray.toLocaleString`

***

### toString()

> **toString**(): `string`

Defined in: node\_modules/typescript/lib/lib.es5.d.ts:1196

Returns a string representation of an array.

#### Returns

`string`

#### Inherited from

`ReadonlyArray.toString`

***

### values()

> **values**(): `IterableIterator`\<`T`\>

Defined in: node\_modules/typescript/lib/lib.es2015.iterable.d.ts:109

Returns an iterable of values in the array

#### Returns

`IterableIterator`\<`T`\>

#### Inherited from

`ReadonlyArray.values`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SourceFile.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SourceFile

# Interface: SourceFile

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2116

## Extends

- [`Declaration`](Declaration.md)

## Extended by

- [`JsonSourceFile`](JsonSourceFile.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`Declaration`](Declaration.md).[`_declarationBrand`](Declaration.md#_declarationbrand)

***

### amdDependencies

> **amdDependencies**: readonly [`AmdDependency`](AmdDependency.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2122

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`Declaration`](Declaration.md).[`decorators`](Declaration.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Declaration`](Declaration.md).[`end`](Declaration.md#end)

***

### endOfFileToken

> `readonly` **endOfFileToken**: [`Token`](Token.md)\<[`EndOfFileToken`](../enumerations/SyntaxKind.md#endoffiletoken)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2119

***

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2120

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Declaration`](Declaration.md).[`flags`](Declaration.md#flags)

***

### hasNoDefaultLib

> **hasNoDefaultLib**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2137

lib.d.ts should have a reference comment like

 /// <reference no-default-lib="true"/>

If any other file has this comment, it signals not to include lib.d.ts
because this containing file is intended to act as a default library.

***

### impliedNodeFormat?

> `optional` **impliedNodeFormat**: [`CommonJS`](../enumerations/ModuleKind.md#commonjs) \| [`ESNext`](../enumerations/ModuleKind.md#esnext)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2156

When `module` is `Node16` or `NodeNext`, this field controls whether the
source file in question is an ESNext-output-format file, or a CommonJS-output-format
module. This is derived by the module resolver as it looks up the file, since
it is derived from either the file extension of the module, or the containing
`package.json` context, and affects both checking and emit.

It is _public_ so that (pre)transformers can set this field,
since it switches the builtin `node` module transform. Generally speaking, if unset,
the field is treated as though it is `ModuleKind.CommonJS`.

Note that this field is only set by the module resolution process when
`moduleResolution` is `Node16` or `NodeNext`, which is implied by the `module` setting
of `Node16` or `NodeNext`, respectively, but may be overriden (eg, by a `moduleResolution`
of `node`). If so, this field will be unset and source files will be considered to be
CommonJS-output-format by the node module transformer and type checker, regardless of extension or context.

***

### isDeclarationFile

> **isDeclarationFile**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2128

***

### kind

> `readonly` **kind**: [`SourceFile`](../enumerations/SyntaxKind.md#sourcefile)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2117

#### Overrides

[`Declaration`](Declaration.md).[`kind`](Declaration.md#kind)

***

### languageVariant

> **languageVariant**: [`LanguageVariant`](../enumerations/LanguageVariant.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2127

***

### languageVersion

> **languageVersion**: [`ScriptTarget`](../enumerations/ScriptTarget.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2138

***

### libReferenceDirectives

> **libReferenceDirectives**: readonly [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2126

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Declaration`](Declaration.md).[`locals`](Declaration.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`Declaration`](Declaration.md).[`modifiers`](Declaration.md#modifiers)

***

### moduleName?

> `optional` **moduleName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2123

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`Declaration`](Declaration.md).[`parent`](Declaration.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`Declaration`](Declaration.md).[`pos`](Declaration.md#pos)

***

### referencedFiles

> **referencedFiles**: readonly [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2124

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Declaration`](Declaration.md).[`skipCheck`](Declaration.md#skipcheck)

***

### statements

> `readonly` **statements**: [`NodeArray`](NodeArray.md)\<[`Statement`](Statement.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2118

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Declaration`](Declaration.md).[`symbol`](Declaration.md#symbol)

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2121

***

### typeReferenceDirectives

> **typeReferenceDirectives**: readonly [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2125

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`Declaration`](Declaration.md).[`forEachChild`](Declaration.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

`SourceFile`

#### Returns

[`Node`](Node.md)

#### Inherited from

[`Declaration`](Declaration.md).[`getChildAt`](Declaration.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

`SourceFile`

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getChildCount`](Declaration.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

`SourceFile`

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`Declaration`](Declaration.md).[`getChildren`](Declaration.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getEnd`](Declaration.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

`SourceFile`

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Declaration`](Declaration.md).[`getFirstToken`](Declaration.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getFullStart`](Declaration.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

`SourceFile`

#### Returns

`string`

#### Inherited from

[`Declaration`](Declaration.md).[`getFullText`](Declaration.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getFullWidth`](Declaration.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

`SourceFile`

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Declaration`](Declaration.md).[`getLastToken`](Declaration.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

`SourceFile`

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getLeadingTriviaWidth`](Declaration.md#getleadingtriviawidth)

***

### getLineAndCharacterOfPosition()

> **getLineAndCharacterOfPosition**(`pos`): [`LineAndCharacter`](LineAndCharacter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6157

#### Parameters

##### pos

`number`

#### Returns

[`LineAndCharacter`](LineAndCharacter.md)

***

### getLineEndOfPosition()

> **getLineEndOfPosition**(`pos`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6158

#### Parameters

##### pos

`number`

#### Returns

`number`

***

### getLineStarts()

> **getLineStarts**(): readonly `number`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6159

#### Returns

readonly `number`[]

***

### getPositionOfLineAndCharacter()

> **getPositionOfLineAndCharacter**(`line`, `character`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6160

#### Parameters

##### line

`number`

##### character

`number`

#### Returns

`number`

***

### getSourceFile()

> **getSourceFile**(): `SourceFile`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

`SourceFile`

#### Inherited from

[`Declaration`](Declaration.md).[`getSourceFile`](Declaration.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

`SourceFile`

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getStart`](Declaration.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

`SourceFile`

#### Returns

`string`

#### Inherited from

[`Declaration`](Declaration.md).[`getText`](Declaration.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getWidth`](Declaration.md#getwidth)

***

### update()

> **update**(`newText`, `textChangeRange`): `SourceFile`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6161

#### Parameters

##### newText

`string`

##### textChangeRange

[`TextChangeRange`](TextChangeRange.md)

#### Returns

`SourceFile`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SourceFileLike.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SourceFileLike

# Interface: SourceFileLike

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2112

Subset of properties from SourceFile that are used in multiple utility functions

## Properties

### fileName?

> `readonly` `optional` **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2114

***

### text

> `readonly` **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2113

## Methods

### getLineAndCharacterOfPosition()

> **getLineAndCharacterOfPosition**(`pos`): [`LineAndCharacter`](LineAndCharacter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6164

#### Parameters

##### pos

`number`

#### Returns

[`LineAndCharacter`](LineAndCharacter.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SourceFileMayBeEmittedHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SourceFileMayBeEmittedHost

# Interface: SourceFileMayBeEmittedHost

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3578

## Extended by

- [`EmitHost`](EmitHost.md)

## Methods

### getCompilerOptions()

> **getCompilerOptions**(): [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3579

#### Returns

[`CompilerOptions`](CompilerOptions.md)

***

### getResolvedProjectReferenceToRedirect()

> **getResolvedProjectReferenceToRedirect**(`fileName`): `undefined` \| [`ResolvedProjectReference`](ResolvedProjectReference.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3581

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| [`ResolvedProjectReference`](ResolvedProjectReference.md)

***

### isSourceFileFromExternalLibrary()

> **isSourceFileFromExternalLibrary**(`file`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3580

#### Parameters

##### file

[`SourceFile`](SourceFile.md)

#### Returns

`boolean`

***

### isSourceOfProjectReferenceRedirect()

> **isSourceOfProjectReferenceRedirect**(`fileName`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3582

#### Parameters

##### fileName

`string`

#### Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SourceMapGenerator.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SourceMapGenerator

# Interface: SourceMapGenerator

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4284

Generates a source map.

## Methods

### addMapping()

#### Call Signature

> **addMapping**(`generatedLine`, `generatedCharacter`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4301

Adds a mapping without source information.

##### Parameters

###### generatedLine

`number`

###### generatedCharacter

`number`

##### Returns

`void`

#### Call Signature

> **addMapping**(`generatedLine`, `generatedCharacter`, `sourceIndex`, `sourceLine`, `sourceCharacter`, `nameIndex?`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4305

Adds a mapping with source information.

##### Parameters

###### generatedLine

`number`

###### generatedCharacter

`number`

###### sourceIndex

`number`

###### sourceLine

`number`

###### sourceCharacter

`number`

###### nameIndex?

`number`

##### Returns

`void`

***

### addName()

> **addName**(`name`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4297

Adds a name.

#### Parameters

##### name

`string`

#### Returns

`number`

***

### addSource()

> **addSource**(`fileName`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4289

Adds a source to the source map.

#### Parameters

##### fileName

`string`

#### Returns

`number`

***

### appendSourceMap()

> **appendSourceMap**(`generatedLine`, `generatedCharacter`, `sourceMap`, `sourceMapPath`, `start?`, `end?`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4309

Appends a source map.

#### Parameters

##### generatedLine

`number`

##### generatedCharacter

`number`

##### sourceMap

[`RawSourceMap`](RawSourceMap.md)

##### sourceMapPath

`string`

##### start?

[`LineAndCharacter`](LineAndCharacter.md)

##### end?

[`LineAndCharacter`](LineAndCharacter.md)

#### Returns

`void`

***

### getSources()

> **getSources**(): readonly `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4285

#### Returns

readonly `string`[]

***

### setSourceContent()

> **setSourceContent**(`sourceIndex`, `content`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4293

Set the content for a source.

#### Parameters

##### sourceIndex

`number`

##### content

`null` | `string`

#### Returns

`void`

***

### toJSON()

> **toJSON**(): [`RawSourceMap`](RawSourceMap.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4313

Gets the source map as a `RawSourceMap` object.

#### Returns

[`RawSourceMap`](RawSourceMap.md)

***

### toString()

> **toString**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4317

Gets the string representation of the source map.

#### Returns

`string`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SourceMapGeneratorOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SourceMapGeneratorOptions

# Interface: SourceMapGeneratorOptions

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5531

## Properties

### extendedDiagnostics?

> `optional` **extendedDiagnostics**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5532




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SourceMapRange.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SourceMapRange

# Interface: SourceMapRange

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3514

## Extends

- [`TextRange`](TextRange.md)

## Properties

### end

> **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:99

#### Inherited from

[`TextRange`](TextRange.md).[`end`](TextRange.md#end)

***

### pos

> **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:98

#### Inherited from

[`TextRange`](TextRange.md).[`pos`](TextRange.md#pos)

***

### source?

> `optional` **source**: [`SourceMapSource`](SourceMapSource.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3515




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SourceMapSource.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SourceMapSource

# Interface: SourceMapSource

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3517

## Properties

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3518

***

### skipTrivia()?

> `optional` **skipTrivia**: (`pos`) => `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3520

#### Parameters

##### pos

`number`

#### Returns

`number`

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3519

## Methods

### getLineAndCharacterOfPosition()

> **getLineAndCharacterOfPosition**(`pos`): [`LineAndCharacter`](LineAndCharacter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6167

#### Parameters

##### pos

`number`

#### Returns

[`LineAndCharacter`](LineAndCharacter.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SourceMapSpan.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SourceMapSpan

# Interface: SourceMapSpan

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2354

## Properties

### emittedColumn

> **emittedColumn**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2358

Column number in the .js file.

***

### emittedLine

> **emittedLine**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2356

Line number in the .js file.

***

### nameIndex?

> `optional` **nameIndex**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2364

Optional name (index into names array) associated with this span.

***

### sourceColumn

> **sourceColumn**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2362

Column number in the .ts file.

***

### sourceIndex

> **sourceIndex**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2366

.ts file (index into sources array) associated with this span

***

### sourceLine

> **sourceLine**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2360

Line number in the .ts file.




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SpreadAssignment.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SpreadAssignment

# Interface: SpreadAssignment

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:816

## Extends

- [`ObjectLiteralElement`](ObjectLiteralElement.md).[`JSDocContainer`](JSDocContainer.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`_declarationBrand`](ObjectLiteralElement.md#_declarationbrand)

***

### \_objectLiteralBrand

> **\_objectLiteralBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:798

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`_objectLiteralBrand`](ObjectLiteralElement.md#_objectliteralbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`decorators`](ObjectLiteralElement.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`end`](ObjectLiteralElement.md#end)

***

### expression

> `readonly` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:819

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`flags`](ObjectLiteralElement.md#flags)

***

### kind

> `readonly` **kind**: [`SpreadAssignment`](../enumerations/SyntaxKind.md#spreadassignment)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:817

#### Overrides

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`kind`](ObjectLiteralElement.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`locals`](ObjectLiteralElement.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`modifiers`](ObjectLiteralElement.md#modifiers)

***

### name?

> `readonly` `optional` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:799

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`name`](ObjectLiteralElement.md#name)

***

### parent

> `readonly` **parent**: [`ObjectLiteralExpression`](ObjectLiteralExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:818

#### Overrides

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`parent`](ObjectLiteralElement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`pos`](ObjectLiteralElement.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`skipCheck`](ObjectLiteralElement.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`symbol`](ObjectLiteralElement.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`forEachChild`](ObjectLiteralElement.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getChildAt`](ObjectLiteralElement.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getChildCount`](ObjectLiteralElement.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getChildren`](ObjectLiteralElement.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getEnd`](ObjectLiteralElement.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getFirstToken`](ObjectLiteralElement.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getFullStart`](ObjectLiteralElement.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getFullText`](ObjectLiteralElement.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getFullWidth`](ObjectLiteralElement.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getLastToken`](ObjectLiteralElement.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getLeadingTriviaWidth`](ObjectLiteralElement.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getSourceFile`](ObjectLiteralElement.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getStart`](ObjectLiteralElement.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getText`](ObjectLiteralElement.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`getWidth`](ObjectLiteralElement.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SpreadElement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SpreadElement

# Interface: SpreadElement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1284

## Extends

- [`Expression`](Expression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`Expression`](Expression.md).[`_expressionBrand`](Expression.md#_expressionbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`Expression`](Expression.md).[`decorators`](Expression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Expression`](Expression.md).[`end`](Expression.md#end)

***

### expression

> `readonly` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1287

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Expression`](Expression.md).[`flags`](Expression.md#flags)

***

### kind

> `readonly` **kind**: [`SpreadElement`](../enumerations/SyntaxKind.md#spreadelement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1285

#### Overrides

[`Expression`](Expression.md).[`kind`](Expression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Expression`](Expression.md).[`locals`](Expression.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`Expression`](Expression.md).[`modifiers`](Expression.md#modifiers)

***

### parent

> `readonly` **parent**: [`CallExpression`](CallExpression.md) \| [`NewExpression`](NewExpression.md) \| [`ArrayLiteralExpression`](ArrayLiteralExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1286

#### Overrides

[`Expression`](Expression.md).[`parent`](Expression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`Expression`](Expression.md).[`pos`](Expression.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Expression`](Expression.md).[`skipCheck`](Expression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Expression`](Expression.md).[`symbol`](Expression.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`Expression`](Expression.md).[`forEachChild`](Expression.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`Expression`](Expression.md).[`getChildAt`](Expression.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getChildCount`](Expression.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`Expression`](Expression.md).[`getChildren`](Expression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getEnd`](Expression.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Expression`](Expression.md).[`getFirstToken`](Expression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getFullStart`](Expression.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Expression`](Expression.md).[`getFullText`](Expression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getFullWidth`](Expression.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Expression`](Expression.md).[`getLastToken`](Expression.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getLeadingTriviaWidth`](Expression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`Expression`](Expression.md).[`getSourceFile`](Expression.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getStart`](Expression.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Expression`](Expression.md).[`getText`](Expression.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getWidth`](Expression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Statement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Statement

# Interface: Statement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1470

## Extends

- [`Node`](Node.md).[`JSDocContainer`](JSDocContainer.md)

## Extended by

- [`DeclarationStatement`](DeclarationStatement.md)
- [`NotEmittedStatement`](NotEmittedStatement.md)
- [`EmptyStatement`](EmptyStatement.md)
- [`DebuggerStatement`](DebuggerStatement.md)
- [`Block`](Block.md)
- [`VariableStatement`](VariableStatement.md)
- [`ExpressionStatement`](ExpressionStatement.md)
- [`IfStatement`](IfStatement.md)
- [`IterationStatement`](IterationStatement.md)
- [`BreakStatement`](BreakStatement.md)
- [`ContinueStatement`](ContinueStatement.md)
- [`ReturnStatement`](ReturnStatement.md)
- [`WithStatement`](WithStatement.md)
- [`SwitchStatement`](SwitchStatement.md)
- [`LabeledStatement`](LabeledStatement.md)
- [`ThrowStatement`](ThrowStatement.md)
- [`TryStatement`](TryStatement.md)
- [`ModuleBlock`](ModuleBlock.md)
- [`ImportDeclaration`](ImportDeclaration.md)

## Properties

### \_statementBrand

> **\_statementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1471

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`Node`](Node.md).[`decorators`](Node.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Node`](Node.md).[`end`](Node.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Node`](Node.md).[`flags`](Node.md#flags)

***

### kind

> `readonly` **kind**: [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:598

#### Inherited from

[`Node`](Node.md).[`kind`](Node.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Node`](Node.md).[`locals`](Node.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`Node`](Node.md).[`modifiers`](Node.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`Node`](Node.md).[`parent`](Node.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`Node`](Node.md).[`pos`](Node.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Node`](Node.md).[`skipCheck`](Node.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Node`](Node.md).[`symbol`](Node.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`Node`](Node.md).[`forEachChild`](Node.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`Node`](Node.md).[`getChildAt`](Node.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getChildCount`](Node.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`Node`](Node.md).[`getChildren`](Node.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getEnd`](Node.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Node`](Node.md).[`getFirstToken`](Node.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getFullStart`](Node.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Node`](Node.md).[`getFullText`](Node.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getFullWidth`](Node.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Node`](Node.md).[`getLastToken`](Node.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getLeadingTriviaWidth`](Node.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`Node`](Node.md).[`getSourceFile`](Node.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getStart`](Node.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Node`](Node.md).[`getText`](Node.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getWidth`](Node.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/StringLiteral.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / StringLiteral

# Interface: StringLiteral

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1039

## Extends

- [`LiteralExpression`](LiteralExpression.md).[`Declaration`](Declaration.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`Declaration`](Declaration.md).[`_declarationBrand`](Declaration.md#_declarationbrand)

***

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`_expressionBrand`](LiteralExpression.md#_expressionbrand)

***

### \_leftHandSideExpressionBrand

> **\_leftHandSideExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1086

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`_leftHandSideExpressionBrand`](LiteralExpression.md#_lefthandsideexpressionbrand)

***

### \_literalExpressionBrand

> **\_literalExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1227

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`_literalExpressionBrand`](LiteralExpression.md#_literalexpressionbrand)

***

### \_memberExpressionBrand

> **\_memberExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1089

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`_memberExpressionBrand`](LiteralExpression.md#_memberexpressionbrand)

***

### \_primaryExpressionBrand

> **\_primaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1092

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`_primaryExpressionBrand`](LiteralExpression.md#_primaryexpressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`_unaryExpressionBrand`](LiteralExpression.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`_updateExpressionBrand`](LiteralExpression.md#_updateexpressionbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`Declaration`](Declaration.md).[`decorators`](Declaration.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Declaration`](Declaration.md).[`end`](Declaration.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Declaration`](Declaration.md).[`flags`](Declaration.md#flags)

***

### hasExtendedUnicodeEscape?

> `optional` **hasExtendedUnicodeEscape**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1221

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`hasExtendedUnicodeEscape`](LiteralExpression.md#hasextendedunicodeescape)

***

### isUnterminated?

> `optional` **isUnterminated**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1220

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`isUnterminated`](LiteralExpression.md#isunterminated)

***

### kind

> `readonly` **kind**: [`StringLiteral`](../enumerations/SyntaxKind.md#stringliteral)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1040

#### Overrides

[`Declaration`](Declaration.md).[`kind`](Declaration.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Declaration`](Declaration.md).[`locals`](Declaration.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`Declaration`](Declaration.md).[`modifiers`](Declaration.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`Declaration`](Declaration.md).[`parent`](Declaration.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`Declaration`](Declaration.md).[`pos`](Declaration.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Declaration`](Declaration.md).[`skipCheck`](Declaration.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Declaration`](Declaration.md).[`symbol`](Declaration.md#symbol)

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1219

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`text`](LiteralExpression.md#text)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`Declaration`](Declaration.md).[`forEachChild`](Declaration.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`Declaration`](Declaration.md).[`getChildAt`](Declaration.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getChildCount`](Declaration.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`Declaration`](Declaration.md).[`getChildren`](Declaration.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getEnd`](Declaration.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Declaration`](Declaration.md).[`getFirstToken`](Declaration.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getFullStart`](Declaration.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Declaration`](Declaration.md).[`getFullText`](Declaration.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getFullWidth`](Declaration.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Declaration`](Declaration.md).[`getLastToken`](Declaration.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getLeadingTriviaWidth`](Declaration.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`Declaration`](Declaration.md).[`getSourceFile`](Declaration.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getStart`](Declaration.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Declaration`](Declaration.md).[`getText`](Declaration.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`Declaration`](Declaration.md).[`getWidth`](Declaration.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/StringLiteralType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / StringLiteralType

# Interface: StringLiteralType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2785

## Extends

- [`LiteralType`](LiteralType.md)

## Properties

### aliasSymbol?

> `optional` **aliasSymbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2773

#### Inherited from

[`LiteralType`](LiteralType.md).[`aliasSymbol`](LiteralType.md#aliassymbol)

***

### aliasTypeArguments?

> `optional` **aliasTypeArguments**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2774

#### Inherited from

[`LiteralType`](LiteralType.md).[`aliasTypeArguments`](LiteralType.md#aliastypearguments)

***

### flags

> **flags**: [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2770

#### Inherited from

[`LiteralType`](LiteralType.md).[`flags`](LiteralType.md#flags)

***

### freshType

> **freshType**: [`LiteralType`](LiteralType.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2778

#### Inherited from

[`LiteralType`](LiteralType.md).[`freshType`](LiteralType.md#freshtype)

***

### pattern?

> `optional` **pattern**: [`DestructuringPattern`](../type-aliases/DestructuringPattern.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2772

#### Inherited from

[`LiteralType`](LiteralType.md).[`pattern`](LiteralType.md#pattern)

***

### regularType

> **regularType**: [`LiteralType`](LiteralType.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2779

#### Inherited from

[`LiteralType`](LiteralType.md).[`regularType`](LiteralType.md#regulartype)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2771

#### Inherited from

[`LiteralType`](LiteralType.md).[`symbol`](LiteralType.md#symbol)

***

### value

> **value**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2786

#### Overrides

[`LiteralType`](LiteralType.md).[`value`](LiteralType.md#value)

## Methods

### getApparentProperties()

> **getApparentProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6124

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`LiteralType`](LiteralType.md).[`getApparentProperties`](LiteralType.md#getapparentproperties)

***

### getBaseTypes()

> **getBaseTypes**(): `undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6129

#### Returns

`undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

#### Inherited from

[`LiteralType`](LiteralType.md).[`getBaseTypes`](LiteralType.md#getbasetypes)

***

### getCallSignatures()

> **getCallSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6125

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`LiteralType`](LiteralType.md).[`getCallSignatures`](LiteralType.md#getcallsignatures)

***

### getConstraint()

> **getConstraint**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6131

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`LiteralType`](LiteralType.md).[`getConstraint`](LiteralType.md#getconstraint)

***

### getConstructSignatures()

> **getConstructSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6126

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`LiteralType`](LiteralType.md).[`getConstructSignatures`](LiteralType.md#getconstructsignatures)

***

### getDefault()

> **getDefault**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6132

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`LiteralType`](LiteralType.md).[`getDefault`](LiteralType.md#getdefault)

***

### getFlags()

> **getFlags**(): [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6120

#### Returns

[`TypeFlags`](../enumerations/TypeFlags.md)

#### Inherited from

[`LiteralType`](LiteralType.md).[`getFlags`](LiteralType.md#getflags)

***

### getNonNullableType()

> **getNonNullableType**(): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6130

#### Returns

[`Type`](Type.md)

#### Inherited from

[`LiteralType`](LiteralType.md).[`getNonNullableType`](LiteralType.md#getnonnullabletype)

***

### getNumberIndexType()

> **getNumberIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6128

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`LiteralType`](LiteralType.md).[`getNumberIndexType`](LiteralType.md#getnumberindextype)

***

### getProperties()

> **getProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6122

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`LiteralType`](LiteralType.md).[`getProperties`](LiteralType.md#getproperties)

***

### getProperty()

> **getProperty**(`propertyName`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6123

#### Parameters

##### propertyName

`string`

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`LiteralType`](LiteralType.md).[`getProperty`](LiteralType.md#getproperty)

***

### getStringIndexType()

> **getStringIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6127

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`LiteralType`](LiteralType.md).[`getStringIndexType`](LiteralType.md#getstringindextype)

***

### getSymbol()

> **getSymbol**(): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6121

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`LiteralType`](LiteralType.md).[`getSymbol`](LiteralType.md#getsymbol)

***

### isClass()

> **isClass**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6141

#### Returns

`this is InterfaceType`

#### Inherited from

[`LiteralType`](LiteralType.md).[`isClass`](LiteralType.md#isclass)

***

### isClassOrInterface()

> **isClassOrInterface**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6140

#### Returns

`this is InterfaceType`

#### Inherited from

[`LiteralType`](LiteralType.md).[`isClassOrInterface`](LiteralType.md#isclassorinterface)

***

### isIndexType()

> **isIndexType**(): `this is IndexType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6142

#### Returns

`this is IndexType`

#### Inherited from

[`LiteralType`](LiteralType.md).[`isIndexType`](LiteralType.md#isindextype)

***

### isIntersection()

> **isIntersection**(): `this is IntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6134

#### Returns

`this is IntersectionType`

#### Inherited from

[`LiteralType`](LiteralType.md).[`isIntersection`](LiteralType.md#isintersection)

***

### isLiteral()

> **isLiteral**(): `this is LiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6136

#### Returns

`this is LiteralType`

#### Inherited from

[`LiteralType`](LiteralType.md).[`isLiteral`](LiteralType.md#isliteral)

***

### isNumberLiteral()

> **isNumberLiteral**(): `this is NumberLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6138

#### Returns

`this is NumberLiteralType`

#### Inherited from

[`LiteralType`](LiteralType.md).[`isNumberLiteral`](LiteralType.md#isnumberliteral)

***

### isStringLiteral()

> **isStringLiteral**(): `this is StringLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6137

#### Returns

`this is StringLiteralType`

#### Inherited from

[`LiteralType`](LiteralType.md).[`isStringLiteral`](LiteralType.md#isstringliteral)

***

### isTypeParameter()

> **isTypeParameter**(): `this is TypeParameter`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6139

#### Returns

`this is TypeParameter`

#### Inherited from

[`LiteralType`](LiteralType.md).[`isTypeParameter`](LiteralType.md#istypeparameter)

***

### isUnion()

> **isUnion**(): `this is UnionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6133

#### Returns

`this is UnionType`

#### Inherited from

[`LiteralType`](LiteralType.md).[`isUnion`](LiteralType.md#isunion)

***

### isUnionOrIntersection()

> **isUnionOrIntersection**(): `this is UnionOrIntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6135

#### Returns

`this is UnionOrIntersectionType`

#### Inherited from

[`LiteralType`](LiteralType.md).[`isUnionOrIntersection`](LiteralType.md#isunionorintersection)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/StringMappingType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / StringMappingType

# Interface: StringMappingType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2923

## Extends

- [`InstantiableType`](InstantiableType.md)

## Properties

### aliasSymbol?

> `optional` **aliasSymbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2773

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`aliasSymbol`](InstantiableType.md#aliassymbol)

***

### aliasTypeArguments?

> `optional` **aliasTypeArguments**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2774

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`aliasTypeArguments`](InstantiableType.md#aliastypearguments)

***

### flags

> **flags**: [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2770

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`flags`](InstantiableType.md#flags)

***

### pattern?

> `optional` **pattern**: [`DestructuringPattern`](../type-aliases/DestructuringPattern.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2772

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`pattern`](InstantiableType.md#pattern)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2924

#### Overrides

[`InstantiableType`](InstantiableType.md).[`symbol`](InstantiableType.md#symbol)

***

### type

> **type**: [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2925

## Methods

### getApparentProperties()

> **getApparentProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6124

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getApparentProperties`](InstantiableType.md#getapparentproperties)

***

### getBaseTypes()

> **getBaseTypes**(): `undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6129

#### Returns

`undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getBaseTypes`](InstantiableType.md#getbasetypes)

***

### getCallSignatures()

> **getCallSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6125

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getCallSignatures`](InstantiableType.md#getcallsignatures)

***

### getConstraint()

> **getConstraint**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6131

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getConstraint`](InstantiableType.md#getconstraint)

***

### getConstructSignatures()

> **getConstructSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6126

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getConstructSignatures`](InstantiableType.md#getconstructsignatures)

***

### getDefault()

> **getDefault**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6132

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getDefault`](InstantiableType.md#getdefault)

***

### getFlags()

> **getFlags**(): [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6120

#### Returns

[`TypeFlags`](../enumerations/TypeFlags.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getFlags`](InstantiableType.md#getflags)

***

### getNonNullableType()

> **getNonNullableType**(): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6130

#### Returns

[`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getNonNullableType`](InstantiableType.md#getnonnullabletype)

***

### getNumberIndexType()

> **getNumberIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6128

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getNumberIndexType`](InstantiableType.md#getnumberindextype)

***

### getProperties()

> **getProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6122

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getProperties`](InstantiableType.md#getproperties)

***

### getProperty()

> **getProperty**(`propertyName`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6123

#### Parameters

##### propertyName

`string`

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getProperty`](InstantiableType.md#getproperty)

***

### getStringIndexType()

> **getStringIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6127

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getStringIndexType`](InstantiableType.md#getstringindextype)

***

### getSymbol()

> **getSymbol**(): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6121

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getSymbol`](InstantiableType.md#getsymbol)

***

### isClass()

> **isClass**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6141

#### Returns

`this is InterfaceType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isClass`](InstantiableType.md#isclass)

***

### isClassOrInterface()

> **isClassOrInterface**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6140

#### Returns

`this is InterfaceType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isClassOrInterface`](InstantiableType.md#isclassorinterface)

***

### isIndexType()

> **isIndexType**(): `this is IndexType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6142

#### Returns

`this is IndexType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isIndexType`](InstantiableType.md#isindextype)

***

### isIntersection()

> **isIntersection**(): `this is IntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6134

#### Returns

`this is IntersectionType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isIntersection`](InstantiableType.md#isintersection)

***

### isLiteral()

> **isLiteral**(): `this is LiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6136

#### Returns

`this is LiteralType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isLiteral`](InstantiableType.md#isliteral)

***

### isNumberLiteral()

> **isNumberLiteral**(): `this is NumberLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6138

#### Returns

`this is NumberLiteralType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isNumberLiteral`](InstantiableType.md#isnumberliteral)

***

### isStringLiteral()

> **isStringLiteral**(): `this is StringLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6137

#### Returns

`this is StringLiteralType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isStringLiteral`](InstantiableType.md#isstringliteral)

***

### isTypeParameter()

> **isTypeParameter**(): `this is TypeParameter`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6139

#### Returns

`this is TypeParameter`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isTypeParameter`](InstantiableType.md#istypeparameter)

***

### isUnion()

> **isUnion**(): `this is UnionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6133

#### Returns

`this is UnionType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isUnion`](InstantiableType.md#isunion)

***

### isUnionOrIntersection()

> **isUnionOrIntersection**(): `this is UnionOrIntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6135

#### Returns

`this is UnionOrIntersectionType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isUnionOrIntersection`](InstantiableType.md#isunionorintersection)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/StructDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / StructDeclaration

# Interface: StructDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1621

## Extends

- [`ClassLikeDeclarationBase`](ClassLikeDeclarationBase.md).[`DeclarationStatement`](DeclarationStatement.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`_declarationBrand`](DeclarationStatement.md#_declarationbrand)

***

### \_statementBrand

> **\_statementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1471

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`_statementBrand`](DeclarationStatement.md#_statementbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`decorators`](DeclarationStatement.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`end`](DeclarationStatement.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`flags`](DeclarationStatement.md#flags)

***

### heritageClauses?

> `readonly` `optional` **heritageClauses**: [`NodeArray`](NodeArray.md)\<[`HeritageClause`](HeritageClause.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1612

#### Inherited from

[`ClassLikeDeclarationBase`](ClassLikeDeclarationBase.md).[`heritageClauses`](ClassLikeDeclarationBase.md#heritageclauses)

***

### kind

> `readonly` **kind**: [`StructDeclaration`](../enumerations/SyntaxKind.md#structdeclaration)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1622

#### Overrides

[`DeclarationStatement`](DeclarationStatement.md).[`kind`](DeclarationStatement.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`locals`](DeclarationStatement.md#locals)

***

### members

> `readonly` **members**: [`NodeArray`](NodeArray.md)\<[`ClassElement`](ClassElement.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1613

#### Inherited from

[`ClassLikeDeclarationBase`](ClassLikeDeclarationBase.md).[`members`](ClassLikeDeclarationBase.md#members)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1623

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Overrides

[`DeclarationStatement`](DeclarationStatement.md).[`modifiers`](DeclarationStatement.md#modifiers)

***

### name?

> `readonly` `optional` **name**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1625

May be undefined in `export default class { ... }`.

#### Overrides

[`DeclarationStatement`](DeclarationStatement.md).[`name`](DeclarationStatement.md#name)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`parent`](DeclarationStatement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`pos`](DeclarationStatement.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`skipCheck`](DeclarationStatement.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`symbol`](DeclarationStatement.md#symbol)

***

### typeParameters?

> `readonly` `optional` **typeParameters**: [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1611

#### Inherited from

[`ClassLikeDeclarationBase`](ClassLikeDeclarationBase.md).[`typeParameters`](ClassLikeDeclarationBase.md#typeparameters)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`forEachChild`](DeclarationStatement.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getChildAt`](DeclarationStatement.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getChildCount`](DeclarationStatement.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getChildren`](DeclarationStatement.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getEnd`](DeclarationStatement.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getFirstToken`](DeclarationStatement.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getFullStart`](DeclarationStatement.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getFullText`](DeclarationStatement.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getFullWidth`](DeclarationStatement.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getLastToken`](DeclarationStatement.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getLeadingTriviaWidth`](DeclarationStatement.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getSourceFile`](DeclarationStatement.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getStart`](DeclarationStatement.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getText`](DeclarationStatement.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getWidth`](DeclarationStatement.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SubstitutionType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SubstitutionType

# Interface: SubstitutionType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2927

## Extends

- [`InstantiableType`](InstantiableType.md)

## Properties

### aliasSymbol?

> `optional` **aliasSymbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2773

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`aliasSymbol`](InstantiableType.md#aliassymbol)

***

### aliasTypeArguments?

> `optional` **aliasTypeArguments**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2774

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`aliasTypeArguments`](InstantiableType.md#aliastypearguments)

***

### baseType

> **baseType**: [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2929

***

### constraint

> **constraint**: [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2930

***

### flags

> **flags**: [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2770

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`flags`](InstantiableType.md#flags)

***

### objectFlags

> **objectFlags**: [`ObjectFlags`](../enumerations/ObjectFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2928

***

### pattern?

> `optional` **pattern**: [`DestructuringPattern`](../type-aliases/DestructuringPattern.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2772

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`pattern`](InstantiableType.md#pattern)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2771

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`symbol`](InstantiableType.md#symbol)

## Methods

### getApparentProperties()

> **getApparentProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6124

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getApparentProperties`](InstantiableType.md#getapparentproperties)

***

### getBaseTypes()

> **getBaseTypes**(): `undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6129

#### Returns

`undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getBaseTypes`](InstantiableType.md#getbasetypes)

***

### getCallSignatures()

> **getCallSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6125

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getCallSignatures`](InstantiableType.md#getcallsignatures)

***

### getConstraint()

> **getConstraint**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6131

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getConstraint`](InstantiableType.md#getconstraint)

***

### getConstructSignatures()

> **getConstructSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6126

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getConstructSignatures`](InstantiableType.md#getconstructsignatures)

***

### getDefault()

> **getDefault**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6132

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getDefault`](InstantiableType.md#getdefault)

***

### getFlags()

> **getFlags**(): [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6120

#### Returns

[`TypeFlags`](../enumerations/TypeFlags.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getFlags`](InstantiableType.md#getflags)

***

### getNonNullableType()

> **getNonNullableType**(): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6130

#### Returns

[`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getNonNullableType`](InstantiableType.md#getnonnullabletype)

***

### getNumberIndexType()

> **getNumberIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6128

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getNumberIndexType`](InstantiableType.md#getnumberindextype)

***

### getProperties()

> **getProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6122

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getProperties`](InstantiableType.md#getproperties)

***

### getProperty()

> **getProperty**(`propertyName`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6123

#### Parameters

##### propertyName

`string`

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getProperty`](InstantiableType.md#getproperty)

***

### getStringIndexType()

> **getStringIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6127

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getStringIndexType`](InstantiableType.md#getstringindextype)

***

### getSymbol()

> **getSymbol**(): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6121

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getSymbol`](InstantiableType.md#getsymbol)

***

### isClass()

> **isClass**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6141

#### Returns

`this is InterfaceType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isClass`](InstantiableType.md#isclass)

***

### isClassOrInterface()

> **isClassOrInterface**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6140

#### Returns

`this is InterfaceType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isClassOrInterface`](InstantiableType.md#isclassorinterface)

***

### isIndexType()

> **isIndexType**(): `this is IndexType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6142

#### Returns

`this is IndexType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isIndexType`](InstantiableType.md#isindextype)

***

### isIntersection()

> **isIntersection**(): `this is IntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6134

#### Returns

`this is IntersectionType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isIntersection`](InstantiableType.md#isintersection)

***

### isLiteral()

> **isLiteral**(): `this is LiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6136

#### Returns

`this is LiteralType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isLiteral`](InstantiableType.md#isliteral)

***

### isNumberLiteral()

> **isNumberLiteral**(): `this is NumberLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6138

#### Returns

`this is NumberLiteralType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isNumberLiteral`](InstantiableType.md#isnumberliteral)

***

### isStringLiteral()

> **isStringLiteral**(): `this is StringLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6137

#### Returns

`this is StringLiteralType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isStringLiteral`](InstantiableType.md#isstringliteral)

***

### isTypeParameter()

> **isTypeParameter**(): `this is TypeParameter`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6139

#### Returns

`this is TypeParameter`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isTypeParameter`](InstantiableType.md#istypeparameter)

***

### isUnion()

> **isUnion**(): `this is UnionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6133

#### Returns

`this is UnionType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isUnion`](InstantiableType.md#isunion)

***

### isUnionOrIntersection()

> **isUnionOrIntersection**(): `this is UnionOrIntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6135

#### Returns

`this is UnionOrIntersectionType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isUnionOrIntersection`](InstantiableType.md#isunionorintersection)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SuperCall.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SuperCall

# Interface: SuperCall

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1347

## Extends

- [`CallExpression`](CallExpression.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`CallExpression`](CallExpression.md).[`_declarationBrand`](CallExpression.md#_declarationbrand)

***

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`CallExpression`](CallExpression.md).[`_expressionBrand`](CallExpression.md#_expressionbrand)

***

### \_leftHandSideExpressionBrand

> **\_leftHandSideExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1086

#### Inherited from

[`CallExpression`](CallExpression.md).[`_leftHandSideExpressionBrand`](CallExpression.md#_lefthandsideexpressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`CallExpression`](CallExpression.md).[`_unaryExpressionBrand`](CallExpression.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`CallExpression`](CallExpression.md).[`_updateExpressionBrand`](CallExpression.md#_updateexpressionbrand)

***

### arguments

> `readonly` **arguments**: [`NodeArray`](NodeArray.md)\<[`Expression`](Expression.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1341

#### Inherited from

[`CallExpression`](CallExpression.md).[`arguments`](CallExpression.md#arguments)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`CallExpression`](CallExpression.md).[`decorators`](CallExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`CallExpression`](CallExpression.md).[`end`](CallExpression.md#end)

***

### expression

> `readonly` **expression**: [`SuperExpression`](SuperExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1348

#### Overrides

[`CallExpression`](CallExpression.md).[`expression`](CallExpression.md#expression)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`CallExpression`](CallExpression.md).[`flags`](CallExpression.md#flags)

***

### kind

> `readonly` **kind**: [`CallExpression`](../enumerations/SyntaxKind.md#callexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1337

#### Inherited from

[`CallExpression`](CallExpression.md).[`kind`](CallExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`CallExpression`](CallExpression.md).[`locals`](CallExpression.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`CallExpression`](CallExpression.md).[`modifiers`](CallExpression.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`CallExpression`](CallExpression.md).[`parent`](CallExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`CallExpression`](CallExpression.md).[`pos`](CallExpression.md#pos)

***

### questionDotToken?

> `readonly` `optional` **questionDotToken**: [`QuestionDotToken`](../type-aliases/QuestionDotToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1339

#### Inherited from

[`CallExpression`](CallExpression.md).[`questionDotToken`](CallExpression.md#questiondottoken)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`CallExpression`](CallExpression.md).[`skipCheck`](CallExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`CallExpression`](CallExpression.md).[`symbol`](CallExpression.md#symbol)

***

### typeArguments?

> `readonly` `optional` **typeArguments**: [`NodeArray`](NodeArray.md)\<[`TypeNode`](TypeNode.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1340

#### Inherited from

[`CallExpression`](CallExpression.md).[`typeArguments`](CallExpression.md#typearguments)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`CallExpression`](CallExpression.md).[`forEachChild`](CallExpression.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`CallExpression`](CallExpression.md).[`getChildAt`](CallExpression.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`CallExpression`](CallExpression.md).[`getChildCount`](CallExpression.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`CallExpression`](CallExpression.md).[`getChildren`](CallExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`CallExpression`](CallExpression.md).[`getEnd`](CallExpression.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`CallExpression`](CallExpression.md).[`getFirstToken`](CallExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`CallExpression`](CallExpression.md).[`getFullStart`](CallExpression.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`CallExpression`](CallExpression.md).[`getFullText`](CallExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`CallExpression`](CallExpression.md).[`getFullWidth`](CallExpression.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`CallExpression`](CallExpression.md).[`getLastToken`](CallExpression.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`CallExpression`](CallExpression.md).[`getLeadingTriviaWidth`](CallExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`CallExpression`](CallExpression.md).[`getSourceFile`](CallExpression.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`CallExpression`](CallExpression.md).[`getStart`](CallExpression.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`CallExpression`](CallExpression.md).[`getText`](CallExpression.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`CallExpression`](CallExpression.md).[`getWidth`](CallExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SuperElementAccessExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SuperElementAccessExpression

# Interface: SuperElementAccessExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1332

## Extends

- [`ElementAccessExpression`](ElementAccessExpression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`_expressionBrand`](ElementAccessExpression.md#_expressionbrand)

***

### \_leftHandSideExpressionBrand

> **\_leftHandSideExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1086

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`_leftHandSideExpressionBrand`](ElementAccessExpression.md#_lefthandsideexpressionbrand)

***

### \_memberExpressionBrand

> **\_memberExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1089

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`_memberExpressionBrand`](ElementAccessExpression.md#_memberexpressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`_unaryExpressionBrand`](ElementAccessExpression.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`_updateExpressionBrand`](ElementAccessExpression.md#_updateexpressionbrand)

***

### argumentExpression

> `readonly` **argumentExpression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1327

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`argumentExpression`](ElementAccessExpression.md#argumentexpression)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`decorators`](ElementAccessExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`end`](ElementAccessExpression.md#end)

***

### expression

> `readonly` **expression**: [`SuperExpression`](SuperExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1333

#### Overrides

[`ElementAccessExpression`](ElementAccessExpression.md).[`expression`](ElementAccessExpression.md#expression)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`flags`](ElementAccessExpression.md#flags)

***

### kind

> `readonly` **kind**: [`ElementAccessExpression`](../enumerations/SyntaxKind.md#elementaccessexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1324

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`kind`](ElementAccessExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`locals`](ElementAccessExpression.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`modifiers`](ElementAccessExpression.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`parent`](ElementAccessExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`pos`](ElementAccessExpression.md#pos)

***

### questionDotToken?

> `readonly` `optional` **questionDotToken**: [`QuestionDotToken`](../type-aliases/QuestionDotToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1326

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`questionDotToken`](ElementAccessExpression.md#questiondottoken)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`skipCheck`](ElementAccessExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`symbol`](ElementAccessExpression.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`forEachChild`](ElementAccessExpression.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getChildAt`](ElementAccessExpression.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getChildCount`](ElementAccessExpression.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getChildren`](ElementAccessExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getEnd`](ElementAccessExpression.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getFirstToken`](ElementAccessExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getFullStart`](ElementAccessExpression.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getFullText`](ElementAccessExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getFullWidth`](ElementAccessExpression.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getLastToken`](ElementAccessExpression.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getLeadingTriviaWidth`](ElementAccessExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getSourceFile`](ElementAccessExpression.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getStart`](ElementAccessExpression.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getText`](ElementAccessExpression.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`ElementAccessExpression`](ElementAccessExpression.md).[`getWidth`](ElementAccessExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SuperExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SuperExpression

# Interface: SuperExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1107

## Extends

- [`PrimaryExpression`](PrimaryExpression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_expressionBrand`](PrimaryExpression.md#_expressionbrand)

***

### \_leftHandSideExpressionBrand

> **\_leftHandSideExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1086

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_leftHandSideExpressionBrand`](PrimaryExpression.md#_lefthandsideexpressionbrand)

***

### \_memberExpressionBrand

> **\_memberExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1089

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_memberExpressionBrand`](PrimaryExpression.md#_memberexpressionbrand)

***

### \_primaryExpressionBrand

> **\_primaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1092

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_primaryExpressionBrand`](PrimaryExpression.md#_primaryexpressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_unaryExpressionBrand`](PrimaryExpression.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_updateExpressionBrand`](PrimaryExpression.md#_updateexpressionbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`decorators`](PrimaryExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`end`](PrimaryExpression.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`flags`](PrimaryExpression.md#flags)

***

### kind

> `readonly` **kind**: [`SuperKeyword`](../enumerations/SyntaxKind.md#superkeyword)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1108

#### Overrides

[`PrimaryExpression`](PrimaryExpression.md).[`kind`](PrimaryExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`locals`](PrimaryExpression.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`modifiers`](PrimaryExpression.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`parent`](PrimaryExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`pos`](PrimaryExpression.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`skipCheck`](PrimaryExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`symbol`](PrimaryExpression.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`forEachChild`](PrimaryExpression.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getChildAt`](PrimaryExpression.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getChildCount`](PrimaryExpression.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getChildren`](PrimaryExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getEnd`](PrimaryExpression.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFirstToken`](PrimaryExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFullStart`](PrimaryExpression.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFullText`](PrimaryExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFullWidth`](PrimaryExpression.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getLastToken`](PrimaryExpression.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getLeadingTriviaWidth`](PrimaryExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getSourceFile`](PrimaryExpression.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getStart`](PrimaryExpression.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getText`](PrimaryExpression.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getWidth`](PrimaryExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SuperPropertyAccessExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SuperPropertyAccessExpression

# Interface: SuperPropertyAccessExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1314

## Extends

- [`PropertyAccessExpression`](PropertyAccessExpression.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`_declarationBrand`](PropertyAccessExpression.md#_declarationbrand)

***

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`_expressionBrand`](PropertyAccessExpression.md#_expressionbrand)

***

### \_leftHandSideExpressionBrand

> **\_leftHandSideExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1086

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`_leftHandSideExpressionBrand`](PropertyAccessExpression.md#_lefthandsideexpressionbrand)

***

### \_memberExpressionBrand

> **\_memberExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1089

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`_memberExpressionBrand`](PropertyAccessExpression.md#_memberexpressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`_unaryExpressionBrand`](PropertyAccessExpression.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`_updateExpressionBrand`](PropertyAccessExpression.md#_updateexpressionbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`decorators`](PropertyAccessExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`end`](PropertyAccessExpression.md#end)

***

### expression

> `readonly` **expression**: [`SuperExpression`](SuperExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1315

#### Overrides

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`expression`](PropertyAccessExpression.md#expression)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`flags`](PropertyAccessExpression.md#flags)

***

### kind

> `readonly` **kind**: [`PropertyAccessExpression`](../enumerations/SyntaxKind.md#propertyaccessexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1305

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`kind`](PropertyAccessExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`locals`](PropertyAccessExpression.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`modifiers`](PropertyAccessExpression.md#modifiers)

***

### name

> `readonly` **name**: [`MemberName`](../type-aliases/MemberName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1308

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`name`](PropertyAccessExpression.md#name)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`parent`](PropertyAccessExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`pos`](PropertyAccessExpression.md#pos)

***

### questionDotToken?

> `readonly` `optional` **questionDotToken**: [`QuestionDotToken`](../type-aliases/QuestionDotToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1307

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`questionDotToken`](PropertyAccessExpression.md#questiondottoken)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`skipCheck`](PropertyAccessExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`symbol`](PropertyAccessExpression.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`forEachChild`](PropertyAccessExpression.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getChildAt`](PropertyAccessExpression.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getChildCount`](PropertyAccessExpression.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getChildren`](PropertyAccessExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getEnd`](PropertyAccessExpression.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getFirstToken`](PropertyAccessExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getFullStart`](PropertyAccessExpression.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getFullText`](PropertyAccessExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getFullWidth`](PropertyAccessExpression.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getLastToken`](PropertyAccessExpression.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getLeadingTriviaWidth`](PropertyAccessExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getSourceFile`](PropertyAccessExpression.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getStart`](PropertyAccessExpression.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getText`](PropertyAccessExpression.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`PropertyAccessExpression`](PropertyAccessExpression.md).[`getWidth`](PropertyAccessExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SwitchStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SwitchStatement

# Interface: SwitchStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1561

## Extends

- [`Statement`](Statement.md)

## Properties

### \_statementBrand

> **\_statementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1471

#### Inherited from

[`Statement`](Statement.md).[`_statementBrand`](Statement.md#_statementbrand)

***

### caseBlock

> `readonly` **caseBlock**: [`CaseBlock`](CaseBlock.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1564

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`Statement`](Statement.md).[`decorators`](Statement.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Statement`](Statement.md).[`end`](Statement.md#end)

***

### expression

> `readonly` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1563

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Statement`](Statement.md).[`flags`](Statement.md#flags)

***

### kind

> `readonly` **kind**: [`SwitchStatement`](../enumerations/SyntaxKind.md#switchstatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1562

#### Overrides

[`Statement`](Statement.md).[`kind`](Statement.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Statement`](Statement.md).[`locals`](Statement.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`Statement`](Statement.md).[`modifiers`](Statement.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`Statement`](Statement.md).[`parent`](Statement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`Statement`](Statement.md).[`pos`](Statement.md#pos)

***

### possiblyExhaustive?

> `optional` **possiblyExhaustive**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1565

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Statement`](Statement.md).[`skipCheck`](Statement.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Statement`](Statement.md).[`symbol`](Statement.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`Statement`](Statement.md).[`forEachChild`](Statement.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`Statement`](Statement.md).[`getChildAt`](Statement.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getChildCount`](Statement.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`Statement`](Statement.md).[`getChildren`](Statement.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getEnd`](Statement.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Statement`](Statement.md).[`getFirstToken`](Statement.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getFullStart`](Statement.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Statement`](Statement.md).[`getFullText`](Statement.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getFullWidth`](Statement.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Statement`](Statement.md).[`getLastToken`](Statement.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getLeadingTriviaWidth`](Statement.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`Statement`](Statement.md).[`getSourceFile`](Statement.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getStart`](Statement.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Statement`](Statement.md).[`getText`](Statement.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getWidth`](Statement.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Symbol.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Symbol

# Interface: Symbol

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2668

## Properties

### declarations?

> `optional` **declarations**: [`Declaration`](Declaration.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2671

***

### escapedName

> **escapedName**: [`__String`](../type-aliases/String.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2670

***

### exports?

> `optional` **exports**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2674

***

### exportSymbol?

> `optional` **exportSymbol**: `Symbol`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2676

***

### flags

> **flags**: [`SymbolFlags`](../enumerations/SymbolFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2669

***

### globalExports?

> `optional` **globalExports**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2675

***

### members?

> `optional` **members**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2673

***

### name

> `readonly` **name**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6111

***

### valueDeclaration?

> `optional` **valueDeclaration**: [`Declaration`](Declaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2672

## Methods

### getDeclarations()

> **getDeclarations**(): `undefined` \| [`Declaration`](Declaration.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6115

#### Returns

`undefined` \| [`Declaration`](Declaration.md)[]

***

### getDocumentationComment()

> **getDocumentationComment**(`typeChecker`): [`SymbolDisplayPart`](SymbolDisplayPart.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6116

#### Parameters

##### typeChecker

`undefined` | [`TypeChecker`](TypeChecker.md)

#### Returns

[`SymbolDisplayPart`](SymbolDisplayPart.md)[]

***

### getEscapedName()

> **getEscapedName**(): [`__String`](../type-aliases/String.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6113

#### Returns

[`__String`](../type-aliases/String.md)

***

### getFlags()

> **getFlags**(): [`SymbolFlags`](../enumerations/SymbolFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6112

#### Returns

[`SymbolFlags`](../enumerations/SymbolFlags.md)

***

### getJsDocTags()

> **getJsDocTags**(`checker?`): [`JSDocTagInfo`](JSDocTagInfo-1.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6117

#### Parameters

##### checker?

[`TypeChecker`](TypeChecker.md)

#### Returns

[`JSDocTagInfo`](JSDocTagInfo-1.md)[]

***

### getName()

> **getName**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6114

#### Returns

`string`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SymbolDisplayPart.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SymbolDisplayPart

# Interface: SymbolDisplayPart

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2265

## Extended by

- [`JSDocLinkDisplayPart`](JSDocLinkDisplayPart.md)

## Properties

### kind

> **kind**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2267

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2266




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SymbolTracker.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SymbolTracker

# Interface: SymbolTracker

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4376

## Properties

### moduleResolverHost?

> `optional` **moduleResolverHost**: [`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md) & `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4384

#### Type declaration

##### getCommonSourceDirectory()

> **getCommonSourceDirectory**(): `string`

###### Returns

`string`

## Methods

### reportCyclicStructureError()?

> `optional` **reportCyclicStructureError**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4381

#### Returns

`void`

***

### reportImportTypeNodeResolutionModeOverride()?

> `optional` **reportImportTypeNodeResolutionModeOverride**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4391

#### Returns

`void`

***

### reportInaccessibleThisError()?

> `optional` **reportInaccessibleThisError**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4378

#### Returns

`void`

***

### reportInaccessibleUniqueSymbolError()?

> `optional` **reportInaccessibleUniqueSymbolError**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4380

#### Returns

`void`

***

### reportLikelyUnsafeImportRequiredError()?

> `optional` **reportLikelyUnsafeImportRequiredError**(`specifier`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4382

#### Parameters

##### specifier

`string`

#### Returns

`void`

***

### reportNonlocalAugmentation()?

> `optional` **reportNonlocalAugmentation**(`containingFile`, `parentSymbol`, `augmentingSymbol`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4389

#### Parameters

##### containingFile

[`SourceFile`](SourceFile.md)

##### parentSymbol

[`Symbol`](Symbol.md)

##### augmentingSymbol

[`Symbol`](Symbol.md)

#### Returns

`void`

***

### reportNonSerializableProperty()?

> `optional` **reportNonSerializableProperty**(`propertyName`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4390

#### Parameters

##### propertyName

`string`

#### Returns

`void`

***

### reportPrivateInBaseOfClassExpression()?

> `optional` **reportPrivateInBaseOfClassExpression**(`propertyName`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4379

#### Parameters

##### propertyName

`string`

#### Returns

`void`

***

### reportTruncationError()?

> `optional` **reportTruncationError**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4383

#### Returns

`void`

***

### trackExternalModuleSymbolOfImportTypeNode()?

> `optional` **trackExternalModuleSymbolOfImportTypeNode**(`symbol`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4388

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

#### Returns

`void`

***

### trackReferencedAmbientModule()?

> `optional` **trackReferencedAmbientModule**(`decl`, `symbol`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4387

#### Parameters

##### decl

[`ModuleDeclaration`](ModuleDeclaration.md)

##### symbol

[`Symbol`](Symbol.md)

#### Returns

`void`

***

### trackSymbol()?

> `optional` **trackSymbol**(`symbol`, `enclosingDeclaration`, `meaning`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4377

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

##### enclosingDeclaration

`undefined` | [`Node`](Node.md)

##### meaning

[`SymbolFlags`](../enumerations/SymbolFlags.md)

#### Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SyntaxList.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SyntaxList

# Interface: SyntaxList

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4401

## Extends

- [`Node`](Node.md)

## Properties

### \_children

> **\_children**: [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4403

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`Node`](Node.md).[`decorators`](Node.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Node`](Node.md).[`end`](Node.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Node`](Node.md).[`flags`](Node.md#flags)

***

### kind

> **kind**: [`SyntaxList`](../enumerations/SyntaxKind.md#syntaxlist)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4402

#### Overrides

[`Node`](Node.md).[`kind`](Node.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Node`](Node.md).[`locals`](Node.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`Node`](Node.md).[`modifiers`](Node.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`Node`](Node.md).[`parent`](Node.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`Node`](Node.md).[`pos`](Node.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Node`](Node.md).[`skipCheck`](Node.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Node`](Node.md).[`symbol`](Node.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`Node`](Node.md).[`forEachChild`](Node.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`Node`](Node.md).[`getChildAt`](Node.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getChildCount`](Node.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`Node`](Node.md).[`getChildren`](Node.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getEnd`](Node.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Node`](Node.md).[`getFirstToken`](Node.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getFullStart`](Node.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Node`](Node.md).[`getFullText`](Node.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getFullWidth`](Node.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Node`](Node.md).[`getLastToken`](Node.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getLeadingTriviaWidth`](Node.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`Node`](Node.md).[`getSourceFile`](Node.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getStart`](Node.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Node`](Node.md).[`getText`](Node.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getWidth`](Node.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SynthesizedComment.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SynthesizedComment

# Interface: SynthesizedComment

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1850

## Extends

- [`CommentRange`](CommentRange.md)

## Properties

### end

> **end**: `-1`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1853

#### Overrides

[`CommentRange`](CommentRange.md).[`end`](CommentRange.md#end)

***

### hasLeadingNewline?

> `optional` **hasLeadingNewline**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1854

***

### hasTrailingNewLine?

> `optional` **hasTrailingNewLine**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1847

#### Inherited from

[`CommentRange`](CommentRange.md).[`hasTrailingNewLine`](CommentRange.md#hastrailingnewline)

***

### kind

> **kind**: [`CommentKind`](../type-aliases/CommentKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1848

#### Inherited from

[`CommentRange`](CommentRange.md).[`kind`](CommentRange.md#kind)

***

### pos

> **pos**: `-1`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1852

#### Overrides

[`CommentRange`](CommentRange.md).[`pos`](CommentRange.md#pos)

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1851




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SyntheticExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SyntheticExpression

# Interface: SyntheticExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1134

## Extends

- [`Expression`](Expression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`Expression`](Expression.md).[`_expressionBrand`](Expression.md#_expressionbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`Expression`](Expression.md).[`decorators`](Expression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Expression`](Expression.md).[`end`](Expression.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Expression`](Expression.md).[`flags`](Expression.md#flags)

***

### isSpread

> `readonly` **isSpread**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1136

***

### kind

> `readonly` **kind**: [`SyntheticExpression`](../enumerations/SyntaxKind.md#syntheticexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1135

#### Overrides

[`Expression`](Expression.md).[`kind`](Expression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Expression`](Expression.md).[`locals`](Expression.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`Expression`](Expression.md).[`modifiers`](Expression.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`Expression`](Expression.md).[`parent`](Expression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`Expression`](Expression.md).[`pos`](Expression.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Expression`](Expression.md).[`skipCheck`](Expression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Expression`](Expression.md).[`symbol`](Expression.md#symbol)

***

### tupleNameSource?

> `readonly` `optional` **tupleNameSource**: [`ParameterDeclaration`](ParameterDeclaration.md) \| [`NamedTupleMember`](NamedTupleMember.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1138

***

### type

> `readonly` **type**: [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1137

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`Expression`](Expression.md).[`forEachChild`](Expression.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`Expression`](Expression.md).[`getChildAt`](Expression.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getChildCount`](Expression.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`Expression`](Expression.md).[`getChildren`](Expression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getEnd`](Expression.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Expression`](Expression.md).[`getFirstToken`](Expression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getFullStart`](Expression.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Expression`](Expression.md).[`getFullText`](Expression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getFullWidth`](Expression.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Expression`](Expression.md).[`getLastToken`](Expression.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getLeadingTriviaWidth`](Expression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`Expression`](Expression.md).[`getSourceFile`](Expression.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getStart`](Expression.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Expression`](Expression.md).[`getText`](Expression.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`Expression`](Expression.md).[`getWidth`](Expression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/System.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / System

# Interface: System

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4523

## Properties

### args

> **args**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4524

***

### newLine

> **newLine**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4525

***

### useCaseSensitiveFileNames

> **useCaseSensitiveFileNames**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4526

## Methods

### base64decode()?

> `optional` **base64decode**(`input`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4562

#### Parameters

##### input

`string`

#### Returns

`string`

***

### base64encode()?

> `optional` **base64encode**(`input`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4563

#### Parameters

##### input

`string`

#### Returns

`string`

***

### clearScreen()?

> `optional` **clearScreen**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4561

#### Returns

`void`

***

### clearTimeout()?

> `optional` **clearTimeout**(`timeoutId`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4560

#### Parameters

##### timeoutId

`any`

#### Returns

`void`

***

### createDirectory()

> **createDirectory**(`path`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4542

#### Parameters

##### path

`string`

#### Returns

`void`

***

### createHash()?

> `optional` **createHash**(`data`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4553

A good implementation is node.js' `crypto.createHash`. (https://nodejs.org/api/crypto.html#crypto_crypto_createhash_algorithm)

#### Parameters

##### data

`string`

#### Returns

`string`

***

### createSHA256Hash()?

> `optional` **createSHA256Hash**(`data`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4555

This must be cryptographically secure. Only implement this method using `crypto.createHash("sha256")`.

#### Parameters

##### data

`string`

#### Returns

`string`

***

### deleteFile()?

> `optional` **deleteFile**(`path`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4549

#### Parameters

##### path

`string`

#### Returns

`void`

***

### directoryExists()

> **directoryExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4541

#### Parameters

##### path

`string`

#### Returns

`boolean`

***

### exit()

> **exit**(`exitCode?`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4557

#### Parameters

##### exitCode?

`number`

#### Returns

`void`

***

### fileExists()

> **fileExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4540

#### Parameters

##### path

`string`

#### Returns

`boolean`

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4544

#### Returns

`string`

***

### getDirectories()

> **getDirectories**(`path`): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4545

#### Parameters

##### path

`string`

#### Returns

`string`[]

***

### getExecutingFilePath()

> **getExecutingFilePath**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4543

#### Returns

`string`

***

### getFileSize()?

> `optional` **getFileSize**(`path`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4531

#### Parameters

##### path

`string`

#### Returns

`number`

***

### getMemoryUsage()?

> `optional` **getMemoryUsage**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4556

#### Returns

`number`

***

### getModifiedTime()?

> `optional` **getModifiedTime**(`path`): `undefined` \| `Date`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4547

#### Parameters

##### path

`string`

#### Returns

`undefined` \| `Date`

***

### getWidthOfTerminal()?

> `optional` **getWidthOfTerminal**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4529

#### Returns

`number`

***

### readDirectory()

> **readDirectory**(`path`, `extensions?`, `exclude?`, `include?`, `depth?`): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4546

#### Parameters

##### path

`string`

##### extensions?

readonly `string`[]

##### exclude?

readonly `string`[]

##### include?

readonly `string`[]

##### depth?

`number`

#### Returns

`string`[]

***

### readFile()

> **readFile**(`path`, `encoding?`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4530

#### Parameters

##### path

`string`

##### encoding?

`string`

#### Returns

`undefined` \| `string`

***

### realpath()?

> `optional` **realpath**(`path`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4558

#### Parameters

##### path

`string`

#### Returns

`string`

***

### resolvePath()

> **resolvePath**(`path`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4539

#### Parameters

##### path

`string`

#### Returns

`string`

***

### setModifiedTime()?

> `optional` **setModifiedTime**(`path`, `time`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4548

#### Parameters

##### path

`string`

##### time

`Date`

#### Returns

`void`

***

### setTimeout()?

> `optional` **setTimeout**(`callback`, `ms`, ...`args`): `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4559

#### Parameters

##### callback

(...`args`) => `void`

##### ms

`number`

##### args

...`any`[]

#### Returns

`any`

***

### watchDirectory()?

> `optional` **watchDirectory**(`path`, `callback`, `recursive?`, `options?`): [`FileWatcher`](FileWatcher.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4538

#### Parameters

##### path

`string`

##### callback

[`DirectoryWatcherCallback`](../type-aliases/DirectoryWatcherCallback.md)

##### recursive?

`boolean`

##### options?

[`WatchOptions`](WatchOptions.md)

#### Returns

[`FileWatcher`](FileWatcher.md)

***

### watchFile()?

> `optional` **watchFile**(`path`, `callback`, `pollingInterval?`, `options?`): [`FileWatcher`](FileWatcher.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4537

#### Parameters

##### path

`string`

##### callback

[`FileWatcherCallback`](../type-aliases/FileWatcherCallback.md)

##### pollingInterval?

`number`

##### options?

[`WatchOptions`](WatchOptions.md)

#### Returns

[`FileWatcher`](FileWatcher.md)

#### Polling Interval

- this parameter is used in polling-based watchers and ignored in watchers that
use native OS file watching

***

### write()

> **write**(`s`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4527

#### Parameters

##### s

`string`

#### Returns

`void`

***

### writeFile()

> **writeFile**(`path`, `data`, `writeByteOrderMark?`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4532

#### Parameters

##### path

`string`

##### data

`string`

##### writeByteOrderMark?

`boolean`

#### Returns

`void`

***

### writeOutputIsTTY()?

> `optional` **writeOutputIsTTY**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4528

#### Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TagCheckConfig.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TagCheckConfig

# Interface: TagCheckConfig

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3462

## Properties

### message

> **message**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3464

***

### needConditionCheck

> **needConditionCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3465

***

### specifyCheckConditionFuncName

> **specifyCheckConditionFuncName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3466

***

### tagName

> **tagName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3463




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TagCheckParam.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TagCheckParam

# Interface: TagCheckParam

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3458

## Properties

### checkConfig

> **checkConfig**: [`TagCheckConfig`](TagCheckConfig.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3460

***

### needCheck

> **needCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3459




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TaggedTemplateExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TaggedTemplateExpression

# Interface: TaggedTemplateExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1363

## Extends

- [`MemberExpression`](MemberExpression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`_expressionBrand`](MemberExpression.md#_expressionbrand)

***

### \_leftHandSideExpressionBrand

> **\_leftHandSideExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1086

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`_leftHandSideExpressionBrand`](MemberExpression.md#_lefthandsideexpressionbrand)

***

### \_memberExpressionBrand

> **\_memberExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1089

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`_memberExpressionBrand`](MemberExpression.md#_memberexpressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`_unaryExpressionBrand`](MemberExpression.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`_updateExpressionBrand`](MemberExpression.md#_updateexpressionbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`decorators`](MemberExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`end`](MemberExpression.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`flags`](MemberExpression.md#flags)

***

### kind

> `readonly` **kind**: [`TaggedTemplateExpression`](../enumerations/SyntaxKind.md#taggedtemplateexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1364

#### Overrides

[`MemberExpression`](MemberExpression.md).[`kind`](MemberExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`locals`](MemberExpression.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`modifiers`](MemberExpression.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`parent`](MemberExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`pos`](MemberExpression.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`skipCheck`](MemberExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`symbol`](MemberExpression.md#symbol)

***

### tag

> `readonly` **tag**: [`LeftHandSideExpression`](LeftHandSideExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1365

***

### template

> `readonly` **template**: [`TemplateLiteral`](../type-aliases/TemplateLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1367

***

### typeArguments?

> `readonly` `optional` **typeArguments**: [`NodeArray`](NodeArray.md)\<[`TypeNode`](TypeNode.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1366

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`forEachChild`](MemberExpression.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getChildAt`](MemberExpression.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getChildCount`](MemberExpression.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getChildren`](MemberExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getEnd`](MemberExpression.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getFirstToken`](MemberExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getFullStart`](MemberExpression.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getFullText`](MemberExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getFullWidth`](MemberExpression.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getLastToken`](MemberExpression.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getLeadingTriviaWidth`](MemberExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getSourceFile`](MemberExpression.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getStart`](MemberExpression.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getText`](MemberExpression.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`getWidth`](MemberExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TemplateExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TemplateExpression

# Interface: TemplateExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1264

## Extends

- [`PrimaryExpression`](PrimaryExpression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_expressionBrand`](PrimaryExpression.md#_expressionbrand)

***

### \_leftHandSideExpressionBrand

> **\_leftHandSideExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1086

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_leftHandSideExpressionBrand`](PrimaryExpression.md#_lefthandsideexpressionbrand)

***

### \_memberExpressionBrand

> **\_memberExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1089

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_memberExpressionBrand`](PrimaryExpression.md#_memberexpressionbrand)

***

### \_primaryExpressionBrand

> **\_primaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1092

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_primaryExpressionBrand`](PrimaryExpression.md#_primaryexpressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_unaryExpressionBrand`](PrimaryExpression.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_updateExpressionBrand`](PrimaryExpression.md#_updateexpressionbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`decorators`](PrimaryExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`end`](PrimaryExpression.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`flags`](PrimaryExpression.md#flags)

***

### head

> `readonly` **head**: [`TemplateHead`](TemplateHead.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1266

***

### kind

> `readonly` **kind**: [`TemplateExpression`](../enumerations/SyntaxKind.md#templateexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1265

#### Overrides

[`PrimaryExpression`](PrimaryExpression.md).[`kind`](PrimaryExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`locals`](PrimaryExpression.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`modifiers`](PrimaryExpression.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`parent`](PrimaryExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`pos`](PrimaryExpression.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`skipCheck`](PrimaryExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`symbol`](PrimaryExpression.md#symbol)

***

### templateSpans

> `readonly` **templateSpans**: [`NodeArray`](NodeArray.md)\<[`TemplateSpan`](TemplateSpan.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1267

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`forEachChild`](PrimaryExpression.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getChildAt`](PrimaryExpression.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getChildCount`](PrimaryExpression.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getChildren`](PrimaryExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getEnd`](PrimaryExpression.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFirstToken`](PrimaryExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFullStart`](PrimaryExpression.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFullText`](PrimaryExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFullWidth`](PrimaryExpression.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getLastToken`](PrimaryExpression.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getLeadingTriviaWidth`](PrimaryExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getSourceFile`](PrimaryExpression.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getStart`](PrimaryExpression.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getText`](PrimaryExpression.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getWidth`](PrimaryExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TemplateHead.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TemplateHead

# Interface: TemplateHead

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1250

## Extends

- [`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md)

## Properties

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`decorators`](TemplateLiteralLikeNode.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`end`](TemplateLiteralLikeNode.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`flags`](TemplateLiteralLikeNode.md#flags)

***

### hasExtendedUnicodeEscape?

> `optional` **hasExtendedUnicodeEscape**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1221

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`hasExtendedUnicodeEscape`](TemplateLiteralLikeNode.md#hasextendedunicodeescape)

***

### isUnterminated?

> `optional` **isUnterminated**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1220

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`isUnterminated`](TemplateLiteralLikeNode.md#isunterminated)

***

### kind

> `readonly` **kind**: [`TemplateHead`](../enumerations/SyntaxKind.md#templatehead)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1251

#### Overrides

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`kind`](TemplateLiteralLikeNode.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`locals`](TemplateLiteralLikeNode.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`modifiers`](TemplateLiteralLikeNode.md#modifiers)

***

### parent

> `readonly` **parent**: [`TemplateExpression`](TemplateExpression.md) \| [`TemplateLiteralTypeNode`](TemplateLiteralTypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1252

#### Overrides

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`parent`](TemplateLiteralLikeNode.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`pos`](TemplateLiteralLikeNode.md#pos)

***

### rawText?

> `optional` **rawText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1224

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`rawText`](TemplateLiteralLikeNode.md#rawtext)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`skipCheck`](TemplateLiteralLikeNode.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`symbol`](TemplateLiteralLikeNode.md#symbol)

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1219

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`text`](TemplateLiteralLikeNode.md#text)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`forEachChild`](TemplateLiteralLikeNode.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getChildAt`](TemplateLiteralLikeNode.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getChildCount`](TemplateLiteralLikeNode.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getChildren`](TemplateLiteralLikeNode.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getEnd`](TemplateLiteralLikeNode.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getFirstToken`](TemplateLiteralLikeNode.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getFullStart`](TemplateLiteralLikeNode.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getFullText`](TemplateLiteralLikeNode.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getFullWidth`](TemplateLiteralLikeNode.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getLastToken`](TemplateLiteralLikeNode.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getLeadingTriviaWidth`](TemplateLiteralLikeNode.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getSourceFile`](TemplateLiteralLikeNode.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getStart`](TemplateLiteralLikeNode.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getText`](TemplateLiteralLikeNode.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getWidth`](TemplateLiteralLikeNode.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TemplateLiteralLikeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TemplateLiteralLikeNode

# Interface: TemplateLiteralLikeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1223

## Extends

- [`LiteralLikeNode`](LiteralLikeNode.md)

## Extended by

- [`NoSubstitutionTemplateLiteral`](NoSubstitutionTemplateLiteral.md)
- [`TemplateHead`](TemplateHead.md)
- [`TemplateMiddle`](TemplateMiddle.md)
- [`TemplateTail`](TemplateTail.md)

## Properties

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`decorators`](LiteralLikeNode.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`end`](LiteralLikeNode.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`flags`](LiteralLikeNode.md#flags)

***

### hasExtendedUnicodeEscape?

> `optional` **hasExtendedUnicodeEscape**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1221

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`hasExtendedUnicodeEscape`](LiteralLikeNode.md#hasextendedunicodeescape)

***

### isUnterminated?

> `optional` **isUnterminated**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1220

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`isUnterminated`](LiteralLikeNode.md#isunterminated)

***

### kind

> `readonly` **kind**: [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:598

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`kind`](LiteralLikeNode.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`locals`](LiteralLikeNode.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`modifiers`](LiteralLikeNode.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`parent`](LiteralLikeNode.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`pos`](LiteralLikeNode.md#pos)

***

### rawText?

> `optional` **rawText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1224

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`skipCheck`](LiteralLikeNode.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`symbol`](LiteralLikeNode.md#symbol)

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1219

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`text`](LiteralLikeNode.md#text)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`forEachChild`](LiteralLikeNode.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getChildAt`](LiteralLikeNode.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getChildCount`](LiteralLikeNode.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getChildren`](LiteralLikeNode.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getEnd`](LiteralLikeNode.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getFirstToken`](LiteralLikeNode.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getFullStart`](LiteralLikeNode.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getFullText`](LiteralLikeNode.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getFullWidth`](LiteralLikeNode.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getLastToken`](LiteralLikeNode.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getLeadingTriviaWidth`](LiteralLikeNode.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getSourceFile`](LiteralLikeNode.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getStart`](LiteralLikeNode.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getText`](LiteralLikeNode.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`getWidth`](LiteralLikeNode.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TemplateLiteralType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TemplateLiteralType

# Interface: TemplateLiteralType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2919

## Extends

- [`InstantiableType`](InstantiableType.md)

## Properties

### aliasSymbol?

> `optional` **aliasSymbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2773

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`aliasSymbol`](InstantiableType.md#aliassymbol)

***

### aliasTypeArguments?

> `optional` **aliasTypeArguments**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2774

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`aliasTypeArguments`](InstantiableType.md#aliastypearguments)

***

### flags

> **flags**: [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2770

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`flags`](InstantiableType.md#flags)

***

### pattern?

> `optional` **pattern**: [`DestructuringPattern`](../type-aliases/DestructuringPattern.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2772

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`pattern`](InstantiableType.md#pattern)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2771

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`symbol`](InstantiableType.md#symbol)

***

### texts

> **texts**: readonly `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2920

***

### types

> **types**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2921

## Methods

### getApparentProperties()

> **getApparentProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6124

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getApparentProperties`](InstantiableType.md#getapparentproperties)

***

### getBaseTypes()

> **getBaseTypes**(): `undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6129

#### Returns

`undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getBaseTypes`](InstantiableType.md#getbasetypes)

***

### getCallSignatures()

> **getCallSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6125

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getCallSignatures`](InstantiableType.md#getcallsignatures)

***

### getConstraint()

> **getConstraint**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6131

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getConstraint`](InstantiableType.md#getconstraint)

***

### getConstructSignatures()

> **getConstructSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6126

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getConstructSignatures`](InstantiableType.md#getconstructsignatures)

***

### getDefault()

> **getDefault**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6132

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getDefault`](InstantiableType.md#getdefault)

***

### getFlags()

> **getFlags**(): [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6120

#### Returns

[`TypeFlags`](../enumerations/TypeFlags.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getFlags`](InstantiableType.md#getflags)

***

### getNonNullableType()

> **getNonNullableType**(): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6130

#### Returns

[`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getNonNullableType`](InstantiableType.md#getnonnullabletype)

***

### getNumberIndexType()

> **getNumberIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6128

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getNumberIndexType`](InstantiableType.md#getnumberindextype)

***

### getProperties()

> **getProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6122

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getProperties`](InstantiableType.md#getproperties)

***

### getProperty()

> **getProperty**(`propertyName`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6123

#### Parameters

##### propertyName

`string`

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getProperty`](InstantiableType.md#getproperty)

***

### getStringIndexType()

> **getStringIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6127

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getStringIndexType`](InstantiableType.md#getstringindextype)

***

### getSymbol()

> **getSymbol**(): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6121

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`getSymbol`](InstantiableType.md#getsymbol)

***

### isClass()

> **isClass**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6141

#### Returns

`this is InterfaceType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isClass`](InstantiableType.md#isclass)

***

### isClassOrInterface()

> **isClassOrInterface**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6140

#### Returns

`this is InterfaceType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isClassOrInterface`](InstantiableType.md#isclassorinterface)

***

### isIndexType()

> **isIndexType**(): `this is IndexType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6142

#### Returns

`this is IndexType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isIndexType`](InstantiableType.md#isindextype)

***

### isIntersection()

> **isIntersection**(): `this is IntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6134

#### Returns

`this is IntersectionType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isIntersection`](InstantiableType.md#isintersection)

***

### isLiteral()

> **isLiteral**(): `this is LiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6136

#### Returns

`this is LiteralType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isLiteral`](InstantiableType.md#isliteral)

***

### isNumberLiteral()

> **isNumberLiteral**(): `this is NumberLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6138

#### Returns

`this is NumberLiteralType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isNumberLiteral`](InstantiableType.md#isnumberliteral)

***

### isStringLiteral()

> **isStringLiteral**(): `this is StringLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6137

#### Returns

`this is StringLiteralType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isStringLiteral`](InstantiableType.md#isstringliteral)

***

### isTypeParameter()

> **isTypeParameter**(): `this is TypeParameter`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6139

#### Returns

`this is TypeParameter`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isTypeParameter`](InstantiableType.md#istypeparameter)

***

### isUnion()

> **isUnion**(): `this is UnionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6133

#### Returns

`this is UnionType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isUnion`](InstantiableType.md#isunion)

***

### isUnionOrIntersection()

> **isUnionOrIntersection**(): `this is UnionOrIntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6135

#### Returns

`this is UnionOrIntersectionType`

#### Inherited from

[`InstantiableType`](InstantiableType.md).[`isUnionOrIntersection`](InstantiableType.md#isunionorintersection)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TemplateLiteralTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TemplateLiteralTypeNode

# Interface: TemplateLiteralTypeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1044

## Extends

- [`TypeNode`](TypeNode.md)

## Properties

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`TypeNode`](TypeNode.md).[`_typeNodeBrand`](TypeNode.md#_typenodebrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`TypeNode`](TypeNode.md).[`decorators`](TypeNode.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`TypeNode`](TypeNode.md).[`end`](TypeNode.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`TypeNode`](TypeNode.md).[`flags`](TypeNode.md#flags)

***

### head

> `readonly` **head**: [`TemplateHead`](TemplateHead.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1046

***

### kind

> **kind**: [`TemplateLiteralType`](../enumerations/SyntaxKind.md#templateliteraltype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1045

#### Overrides

[`TypeNode`](TypeNode.md).[`kind`](TypeNode.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`TypeNode`](TypeNode.md).[`locals`](TypeNode.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`TypeNode`](TypeNode.md).[`modifiers`](TypeNode.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`TypeNode`](TypeNode.md).[`parent`](TypeNode.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`TypeNode`](TypeNode.md).[`pos`](TypeNode.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`TypeNode`](TypeNode.md).[`skipCheck`](TypeNode.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`TypeNode`](TypeNode.md).[`symbol`](TypeNode.md#symbol)

***

### templateSpans

> `readonly` **templateSpans**: [`NodeArray`](NodeArray.md)\<[`TemplateLiteralTypeSpan`](TemplateLiteralTypeSpan.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1047

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`TypeNode`](TypeNode.md).[`forEachChild`](TypeNode.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getChildAt`](TypeNode.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getChildCount`](TypeNode.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`TypeNode`](TypeNode.md).[`getChildren`](TypeNode.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getEnd`](TypeNode.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFirstToken`](TypeNode.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFullStart`](TypeNode.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFullText`](TypeNode.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFullWidth`](TypeNode.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getLastToken`](TypeNode.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getLeadingTriviaWidth`](TypeNode.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getSourceFile`](TypeNode.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getStart`](TypeNode.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getText`](TypeNode.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getWidth`](TypeNode.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TemplateLiteralTypeSpan.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TemplateLiteralTypeSpan

# Interface: TemplateLiteralTypeSpan

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1049

## Extends

- [`TypeNode`](TypeNode.md)

## Properties

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`TypeNode`](TypeNode.md).[`_typeNodeBrand`](TypeNode.md#_typenodebrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`TypeNode`](TypeNode.md).[`decorators`](TypeNode.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`TypeNode`](TypeNode.md).[`end`](TypeNode.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`TypeNode`](TypeNode.md).[`flags`](TypeNode.md#flags)

***

### kind

> `readonly` **kind**: [`TemplateLiteralTypeSpan`](../enumerations/SyntaxKind.md#templateliteraltypespan)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1050

#### Overrides

[`TypeNode`](TypeNode.md).[`kind`](TypeNode.md#kind)

***

### literal

> `readonly` **literal**: [`TemplateMiddle`](TemplateMiddle.md) \| [`TemplateTail`](TemplateTail.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1053

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`TypeNode`](TypeNode.md).[`locals`](TypeNode.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`TypeNode`](TypeNode.md).[`modifiers`](TypeNode.md#modifiers)

***

### parent

> `readonly` **parent**: [`TemplateLiteralTypeNode`](TemplateLiteralTypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1051

#### Overrides

[`TypeNode`](TypeNode.md).[`parent`](TypeNode.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`TypeNode`](TypeNode.md).[`pos`](TypeNode.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`TypeNode`](TypeNode.md).[`skipCheck`](TypeNode.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`TypeNode`](TypeNode.md).[`symbol`](TypeNode.md#symbol)

***

### type

> `readonly` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1052

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`TypeNode`](TypeNode.md).[`forEachChild`](TypeNode.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getChildAt`](TypeNode.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getChildCount`](TypeNode.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`TypeNode`](TypeNode.md).[`getChildren`](TypeNode.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getEnd`](TypeNode.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFirstToken`](TypeNode.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFullStart`](TypeNode.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFullText`](TypeNode.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFullWidth`](TypeNode.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getLastToken`](TypeNode.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getLeadingTriviaWidth`](TypeNode.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getSourceFile`](TypeNode.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getStart`](TypeNode.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getText`](TypeNode.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getWidth`](TypeNode.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TemplateMiddle.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TemplateMiddle

# Interface: TemplateMiddle

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1254

## Extends

- [`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md)

## Properties

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`decorators`](TemplateLiteralLikeNode.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`end`](TemplateLiteralLikeNode.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`flags`](TemplateLiteralLikeNode.md#flags)

***

### hasExtendedUnicodeEscape?

> `optional` **hasExtendedUnicodeEscape**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1221

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`hasExtendedUnicodeEscape`](TemplateLiteralLikeNode.md#hasextendedunicodeescape)

***

### isUnterminated?

> `optional` **isUnterminated**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1220

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`isUnterminated`](TemplateLiteralLikeNode.md#isunterminated)

***

### kind

> `readonly` **kind**: [`TemplateMiddle`](../enumerations/SyntaxKind.md#templatemiddle)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1255

#### Overrides

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`kind`](TemplateLiteralLikeNode.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`locals`](TemplateLiteralLikeNode.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`modifiers`](TemplateLiteralLikeNode.md#modifiers)

***

### parent

> `readonly` **parent**: [`TemplateSpan`](TemplateSpan.md) \| [`TemplateLiteralTypeSpan`](TemplateLiteralTypeSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1256

#### Overrides

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`parent`](TemplateLiteralLikeNode.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`pos`](TemplateLiteralLikeNode.md#pos)

***

### rawText?

> `optional` **rawText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1224

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`rawText`](TemplateLiteralLikeNode.md#rawtext)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`skipCheck`](TemplateLiteralLikeNode.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`symbol`](TemplateLiteralLikeNode.md#symbol)

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1219

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`text`](TemplateLiteralLikeNode.md#text)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`forEachChild`](TemplateLiteralLikeNode.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getChildAt`](TemplateLiteralLikeNode.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getChildCount`](TemplateLiteralLikeNode.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getChildren`](TemplateLiteralLikeNode.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getEnd`](TemplateLiteralLikeNode.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getFirstToken`](TemplateLiteralLikeNode.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getFullStart`](TemplateLiteralLikeNode.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getFullText`](TemplateLiteralLikeNode.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getFullWidth`](TemplateLiteralLikeNode.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getLastToken`](TemplateLiteralLikeNode.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getLeadingTriviaWidth`](TemplateLiteralLikeNode.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getSourceFile`](TemplateLiteralLikeNode.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getStart`](TemplateLiteralLikeNode.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getText`](TemplateLiteralLikeNode.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getWidth`](TemplateLiteralLikeNode.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TemplateSpan.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TemplateSpan

# Interface: TemplateSpan

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1270

## Extends

- [`Node`](Node.md)

## Properties

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`Node`](Node.md).[`decorators`](Node.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Node`](Node.md).[`end`](Node.md#end)

***

### expression

> `readonly` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1273

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Node`](Node.md).[`flags`](Node.md#flags)

***

### kind

> `readonly` **kind**: [`TemplateSpan`](../enumerations/SyntaxKind.md#templatespan)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1271

#### Overrides

[`Node`](Node.md).[`kind`](Node.md#kind)

***

### literal

> `readonly` **literal**: [`TemplateMiddle`](TemplateMiddle.md) \| [`TemplateTail`](TemplateTail.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1274

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Node`](Node.md).[`locals`](Node.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`Node`](Node.md).[`modifiers`](Node.md#modifiers)

***

### parent

> `readonly` **parent**: [`TemplateExpression`](TemplateExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1272

#### Overrides

[`Node`](Node.md).[`parent`](Node.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`Node`](Node.md).[`pos`](Node.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Node`](Node.md).[`skipCheck`](Node.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Node`](Node.md).[`symbol`](Node.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`Node`](Node.md).[`forEachChild`](Node.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`Node`](Node.md).[`getChildAt`](Node.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getChildCount`](Node.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`Node`](Node.md).[`getChildren`](Node.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getEnd`](Node.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Node`](Node.md).[`getFirstToken`](Node.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getFullStart`](Node.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Node`](Node.md).[`getFullText`](Node.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getFullWidth`](Node.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Node`](Node.md).[`getLastToken`](Node.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getLeadingTriviaWidth`](Node.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`Node`](Node.md).[`getSourceFile`](Node.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getStart`](Node.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Node`](Node.md).[`getText`](Node.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getWidth`](Node.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TemplateTail.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TemplateTail

# Interface: TemplateTail

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1258

## Extends

- [`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md)

## Properties

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`decorators`](TemplateLiteralLikeNode.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`end`](TemplateLiteralLikeNode.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`flags`](TemplateLiteralLikeNode.md#flags)

***

### hasExtendedUnicodeEscape?

> `optional` **hasExtendedUnicodeEscape**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1221

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`hasExtendedUnicodeEscape`](TemplateLiteralLikeNode.md#hasextendedunicodeescape)

***

### isUnterminated?

> `optional` **isUnterminated**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1220

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`isUnterminated`](TemplateLiteralLikeNode.md#isunterminated)

***

### kind

> `readonly` **kind**: [`TemplateTail`](../enumerations/SyntaxKind.md#templatetail)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1259

#### Overrides

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`kind`](TemplateLiteralLikeNode.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`locals`](TemplateLiteralLikeNode.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`modifiers`](TemplateLiteralLikeNode.md#modifiers)

***

### parent

> `readonly` **parent**: [`TemplateSpan`](TemplateSpan.md) \| [`TemplateLiteralTypeSpan`](TemplateLiteralTypeSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1260

#### Overrides

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`parent`](TemplateLiteralLikeNode.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`pos`](TemplateLiteralLikeNode.md#pos)

***

### rawText?

> `optional` **rawText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1224

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`rawText`](TemplateLiteralLikeNode.md#rawtext)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`skipCheck`](TemplateLiteralLikeNode.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`symbol`](TemplateLiteralLikeNode.md#symbol)

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1219

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`text`](TemplateLiteralLikeNode.md#text)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`forEachChild`](TemplateLiteralLikeNode.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getChildAt`](TemplateLiteralLikeNode.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getChildCount`](TemplateLiteralLikeNode.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getChildren`](TemplateLiteralLikeNode.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getEnd`](TemplateLiteralLikeNode.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getFirstToken`](TemplateLiteralLikeNode.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getFullStart`](TemplateLiteralLikeNode.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getFullText`](TemplateLiteralLikeNode.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getFullWidth`](TemplateLiteralLikeNode.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getLastToken`](TemplateLiteralLikeNode.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getLeadingTriviaWidth`](TemplateLiteralLikeNode.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getSourceFile`](TemplateLiteralLikeNode.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getStart`](TemplateLiteralLikeNode.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getText`](TemplateLiteralLikeNode.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md).[`getWidth`](TemplateLiteralLikeNode.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TextChange.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TextChange

# Interface: TextChange

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6599

## Properties

### newText

> **newText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6601

***

### span

> **span**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6600




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TextChangeRange.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TextChangeRange

# Interface: TextChangeRange

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4397

## Properties

### newLength

> **newLength**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4399

***

### span

> **span**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4398




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TextInsertion.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TextInsertion

# Interface: TextInsertion

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6695

## Properties

### caretOffset

> **caretOffset**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6698

The position in newText the caret should point to after the insertion.

***

### newText

> **newText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6696




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TextRange.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TextRange

# Interface: TextRange

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:97

## Extended by

- [`FileReference`](FileReference.md)
- [`CheckJsDirective`](CheckJsDirective.md)
- [`CommentRange`](CommentRange.md)
- [`SourceMapRange`](SourceMapRange.md)

## Properties

### end

> **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:99

***

### pos

> **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:98




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TextSpan.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TextSpan

# Interface: TextSpan

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4393

## Properties

### length

> **length**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4395

***

### start

> **start**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4394




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ThisExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ThisExpression

# Interface: ThisExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1104

## Extends

- [`PrimaryExpression`](PrimaryExpression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_expressionBrand`](PrimaryExpression.md#_expressionbrand)

***

### \_leftHandSideExpressionBrand

> **\_leftHandSideExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1086

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_leftHandSideExpressionBrand`](PrimaryExpression.md#_lefthandsideexpressionbrand)

***

### \_memberExpressionBrand

> **\_memberExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1089

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_memberExpressionBrand`](PrimaryExpression.md#_memberexpressionbrand)

***

### \_primaryExpressionBrand

> **\_primaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1092

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_primaryExpressionBrand`](PrimaryExpression.md#_primaryexpressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_unaryExpressionBrand`](PrimaryExpression.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_updateExpressionBrand`](PrimaryExpression.md#_updateexpressionbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`decorators`](PrimaryExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`end`](PrimaryExpression.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`flags`](PrimaryExpression.md#flags)

***

### kind

> `readonly` **kind**: [`ThisKeyword`](../enumerations/SyntaxKind.md#thiskeyword)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1105

#### Overrides

[`PrimaryExpression`](PrimaryExpression.md).[`kind`](PrimaryExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`locals`](PrimaryExpression.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`modifiers`](PrimaryExpression.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`parent`](PrimaryExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`pos`](PrimaryExpression.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`skipCheck`](PrimaryExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`symbol`](PrimaryExpression.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`forEachChild`](PrimaryExpression.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getChildAt`](PrimaryExpression.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getChildCount`](PrimaryExpression.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getChildren`](PrimaryExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getEnd`](PrimaryExpression.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFirstToken`](PrimaryExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFullStart`](PrimaryExpression.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFullText`](PrimaryExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFullWidth`](PrimaryExpression.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getLastToken`](PrimaryExpression.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getLeadingTriviaWidth`](PrimaryExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getSourceFile`](PrimaryExpression.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getStart`](PrimaryExpression.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getText`](PrimaryExpression.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getWidth`](PrimaryExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ThisTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ThisTypeNode

# Interface: ThisTypeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:930

## Extends

- [`TypeNode`](TypeNode.md)

## Properties

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`TypeNode`](TypeNode.md).[`_typeNodeBrand`](TypeNode.md#_typenodebrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`TypeNode`](TypeNode.md).[`decorators`](TypeNode.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`TypeNode`](TypeNode.md).[`end`](TypeNode.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`TypeNode`](TypeNode.md).[`flags`](TypeNode.md#flags)

***

### kind

> `readonly` **kind**: [`ThisType`](../enumerations/SyntaxKind.md#thistype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:931

#### Overrides

[`TypeNode`](TypeNode.md).[`kind`](TypeNode.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`TypeNode`](TypeNode.md).[`locals`](TypeNode.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`TypeNode`](TypeNode.md).[`modifiers`](TypeNode.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`TypeNode`](TypeNode.md).[`parent`](TypeNode.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`TypeNode`](TypeNode.md).[`pos`](TypeNode.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`TypeNode`](TypeNode.md).[`skipCheck`](TypeNode.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`TypeNode`](TypeNode.md).[`symbol`](TypeNode.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`TypeNode`](TypeNode.md).[`forEachChild`](TypeNode.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getChildAt`](TypeNode.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getChildCount`](TypeNode.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`TypeNode`](TypeNode.md).[`getChildren`](TypeNode.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getEnd`](TypeNode.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFirstToken`](TypeNode.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFullStart`](TypeNode.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFullText`](TypeNode.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFullWidth`](TypeNode.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getLastToken`](TypeNode.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getLeadingTriviaWidth`](TypeNode.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getSourceFile`](TypeNode.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getStart`](TypeNode.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getText`](TypeNode.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getWidth`](TypeNode.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ThisTypePredicate.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ThisTypePredicate

# Interface: ThisTypePredicate

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2581

## Extends

- [`TypePredicateBase`](TypePredicateBase.md)

## Properties

### kind

> **kind**: [`This`](../enumerations/TypePredicateKind.md#this)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2582

#### Overrides

[`TypePredicateBase`](TypePredicateBase.md).[`kind`](TypePredicateBase.md#kind)

***

### parameterIndex

> **parameterIndex**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2584

***

### parameterName

> **parameterName**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2583

***

### type

> **type**: [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2585

#### Overrides

[`TypePredicateBase`](TypePredicateBase.md).[`type`](TypePredicateBase.md#type)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ThrowStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ThrowStatement

# Interface: ThrowStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1589

## Extends

- [`Statement`](Statement.md)

## Properties

### \_statementBrand

> **\_statementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1471

#### Inherited from

[`Statement`](Statement.md).[`_statementBrand`](Statement.md#_statementbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`Statement`](Statement.md).[`decorators`](Statement.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Statement`](Statement.md).[`end`](Statement.md#end)

***

### expression

> `readonly` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1591

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Statement`](Statement.md).[`flags`](Statement.md#flags)

***

### kind

> `readonly` **kind**: [`ThrowStatement`](../enumerations/SyntaxKind.md#throwstatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1590

#### Overrides

[`Statement`](Statement.md).[`kind`](Statement.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Statement`](Statement.md).[`locals`](Statement.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`Statement`](Statement.md).[`modifiers`](Statement.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`Statement`](Statement.md).[`parent`](Statement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`Statement`](Statement.md).[`pos`](Statement.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Statement`](Statement.md).[`skipCheck`](Statement.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Statement`](Statement.md).[`symbol`](Statement.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`Statement`](Statement.md).[`forEachChild`](Statement.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`Statement`](Statement.md).[`getChildAt`](Statement.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getChildCount`](Statement.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`Statement`](Statement.md).[`getChildren`](Statement.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getEnd`](Statement.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Statement`](Statement.md).[`getFirstToken`](Statement.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getFullStart`](Statement.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Statement`](Statement.md).[`getFullText`](Statement.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getFullWidth`](Statement.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Statement`](Statement.md).[`getLastToken`](Statement.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getLeadingTriviaWidth`](Statement.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`Statement`](Statement.md).[`getSourceFile`](Statement.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getStart`](Statement.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Statement`](Statement.md).[`getText`](Statement.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getWidth`](Statement.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TodoComment.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TodoComment

# Interface: TodoComment

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6594

## Properties

### descriptor

> **descriptor**: [`TodoCommentDescriptor`](TodoCommentDescriptor.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6595

***

### message

> **message**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6596

***

### position

> **position**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6597




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TodoCommentDescriptor.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TodoCommentDescriptor

# Interface: TodoCommentDescriptor

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6590

## Properties

### priority

> **priority**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6592

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6591




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Token.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Token

# Interface: Token\<TKind\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:618

## Extends

- [`Node`](Node.md)

## Extended by

- [`PunctuationToken`](PunctuationToken.md)
- [`KeywordToken`](KeywordToken.md)

## Type Parameters

### TKind

`TKind` *extends* [`SyntaxKind`](../enumerations/SyntaxKind.md)

## Properties

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`Node`](Node.md).[`decorators`](Node.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Node`](Node.md).[`end`](Node.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Node`](Node.md).[`flags`](Node.md#flags)

***

### kind

> `readonly` **kind**: `TKind`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:619

#### Overrides

[`Node`](Node.md).[`kind`](Node.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Node`](Node.md).[`locals`](Node.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`Node`](Node.md).[`modifiers`](Node.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`Node`](Node.md).[`parent`](Node.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`Node`](Node.md).[`pos`](Node.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Node`](Node.md).[`skipCheck`](Node.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Node`](Node.md).[`symbol`](Node.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`Node`](Node.md).[`forEachChild`](Node.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`Node`](Node.md).[`getChildAt`](Node.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getChildCount`](Node.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`Node`](Node.md).[`getChildren`](Node.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getEnd`](Node.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Node`](Node.md).[`getFirstToken`](Node.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getFullStart`](Node.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Node`](Node.md).[`getFullText`](Node.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getFullWidth`](Node.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Node`](Node.md).[`getLastToken`](Node.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getLeadingTriviaWidth`](Node.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`Node`](Node.md).[`getSourceFile`](Node.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getStart`](Node.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Node`](Node.md).[`getText`](Node.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`Node`](Node.md).[`getWidth`](Node.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TransformationContext.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TransformationContext

# Interface: TransformationContext

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4095

## Extends

- [`CoreTransformationContext`](CoreTransformationContext.md)

## Properties

### factory

> `readonly` **factory**: [`NodeFactory`](NodeFactory.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4079

#### Inherited from

[`CoreTransformationContext`](CoreTransformationContext.md).[`factory`](CoreTransformationContext.md#factory)

***

### onEmitNode()

> **onEmitNode**: (`hint`, `node`, `emitCallback`) => `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4129

Hook used to allow transformers to capture state before or after
the printer emits a node.

NOTE: Transformation hooks should only be modified during `Transformer` initialization,
before returning the `NodeTransformer` callback.

#### Parameters

##### hint

[`EmitHint`](../enumerations/EmitHint.md)

##### node

[`Node`](Node.md)

##### emitCallback

(`hint`, `node`) => `void`

#### Returns

`void`

***

### onSubstituteNode()

> **onSubstituteNode**: (`hint`, `node`) => [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4111

Hook used by transformers to substitute expressions just before they
are emitted by the pretty printer.

NOTE: Transformation hooks should only be modified during `Transformer` initialization,
before returning the `NodeTransformer` callback.

#### Parameters

##### hint

[`EmitHint`](../enumerations/EmitHint.md)

##### node

[`Node`](Node.md)

#### Returns

[`Node`](Node.md)

## Methods

### enableEmitNotification()

> **enableEmitNotification**(`kind`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4116

Enables before/after emit notifications in the pretty printer for the provided
SyntaxKind.

#### Parameters

##### kind

[`SyntaxKind`](../enumerations/SyntaxKind.md)

#### Returns

`void`

***

### enableSubstitution()

> **enableSubstitution**(`kind`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4101

Enables expression substitutions in the pretty printer for the provided SyntaxKind.

#### Parameters

##### kind

[`SyntaxKind`](../enumerations/SyntaxKind.md)

#### Returns

`void`

***

### endLexicalEnvironment()

> **endLexicalEnvironment**(): `undefined` \| [`Statement`](Statement.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4089

Ends a lexical environment, returning any declarations.

#### Returns

`undefined` \| [`Statement`](Statement.md)[]

#### Inherited from

[`CoreTransformationContext`](CoreTransformationContext.md).[`endLexicalEnvironment`](CoreTransformationContext.md#endlexicalenvironment)

***

### getCompilerOptions()

> **getCompilerOptions**(): [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4081

Gets the compiler options supplied to the transformer.

#### Returns

[`CompilerOptions`](CompilerOptions.md)

#### Inherited from

[`CoreTransformationContext`](CoreTransformationContext.md).[`getCompilerOptions`](CoreTransformationContext.md#getcompileroptions)

***

### hoistFunctionDeclaration()

> **hoistFunctionDeclaration**(`node`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4091

Hoists a function declaration to the containing scope.

#### Parameters

##### node

[`FunctionDeclaration`](FunctionDeclaration.md)

#### Returns

`void`

#### Inherited from

[`CoreTransformationContext`](CoreTransformationContext.md).[`hoistFunctionDeclaration`](CoreTransformationContext.md#hoistfunctiondeclaration)

***

### hoistVariableDeclaration()

> **hoistVariableDeclaration**(`node`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4093

Hoists a variable declaration to the containing scope.

#### Parameters

##### node

[`Identifier`](Identifier.md)

#### Returns

`void`

#### Inherited from

[`CoreTransformationContext`](CoreTransformationContext.md).[`hoistVariableDeclaration`](CoreTransformationContext.md#hoistvariabledeclaration)

***

### isEmitNotificationEnabled()

> **isEmitNotificationEnabled**(`node`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4121

Determines whether before/after emit notifications should be raised in the pretty
printer when it emits a node.

#### Parameters

##### node

[`Node`](Node.md)

#### Returns

`boolean`

***

### isLexicalEnvironmentSuspended()?

> `optional` **isLexicalEnvironmentSuspended**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4131

Determines whether the lexical environment is suspended

#### Returns

`boolean`

***

### isSubstitutionEnabled()

> **isSubstitutionEnabled**(`node`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4103

Determines whether expression substitutions are enabled for the provided node.

#### Parameters

##### node

[`Node`](Node.md)

#### Returns

`boolean`

***

### readEmitHelpers()

> **readEmitHelpers**(): `undefined` \| [`EmitHelper`](../type-aliases/EmitHelper.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4099

Gets and resets the requested non-scoped emit helpers.

#### Returns

`undefined` \| [`EmitHelper`](../type-aliases/EmitHelper.md)[]

***

### requestEmitHelper()

> **requestEmitHelper**(`helper`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4097

Records a request for a non-scoped emit helper in the current context.

#### Parameters

##### helper

[`EmitHelper`](../type-aliases/EmitHelper.md)

#### Returns

`void`

***

### resumeLexicalEnvironment()

> **resumeLexicalEnvironment**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4087

Resumes a suspended lexical environment, usually before visiting a function body.

#### Returns

`void`

#### Inherited from

[`CoreTransformationContext`](CoreTransformationContext.md).[`resumeLexicalEnvironment`](CoreTransformationContext.md#resumelexicalenvironment)

***

### startLexicalEnvironment()

> **startLexicalEnvironment**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4083

Starts a new lexical environment.

#### Returns

`void`

#### Inherited from

[`CoreTransformationContext`](CoreTransformationContext.md).[`startLexicalEnvironment`](CoreTransformationContext.md#startlexicalenvironment)

***

### suspendLexicalEnvironment()

> **suspendLexicalEnvironment**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4085

Suspends the current lexical environment, usually after visiting a parameter list.

#### Returns

`void`

#### Inherited from

[`CoreTransformationContext`](CoreTransformationContext.md).[`suspendLexicalEnvironment`](CoreTransformationContext.md#suspendlexicalenvironment)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TransformationResult.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TransformationResult

# Interface: TransformationResult\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4133

## Type Parameters

### T

`T` *extends* [`Node`](Node.md)

## Properties

### diagnostics?

> `optional` **diagnostics**: [`DiagnosticWithLocation`](DiagnosticWithLocation.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4137

Gets diagnostics for the transformation.

***

### transformed

> **transformed**: `T`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4135

Gets the transformed source files.

## Methods

### dispose()

> **dispose**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4162

Clean up EmitNode entries on any parse-tree nodes.

#### Returns

`void`

***

### emitNodeWithNotification()

> **emitNodeWithNotification**(`hint`, `node`, `emitCallback`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4152

Emits a node with possible notification.

#### Parameters

##### hint

[`EmitHint`](../enumerations/EmitHint.md)

A hint as to the intended usage of the node.

##### node

[`Node`](Node.md)

The node to emit.

##### emitCallback

(`hint`, `node`) => `void`

A callback used to emit the node.

#### Returns

`void`

***

### isEmitNotificationEnabled()?

> `optional` **isEmitNotificationEnabled**(`node`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4158

Indicates if a given node needs an emit notification

#### Parameters

##### node

[`Node`](Node.md)

The node to emit.

#### Returns

`boolean`

***

### substituteNode()

> **substituteNode**(`hint`, `node`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4144

Gets a substitute for a node, if one is available; otherwise, returns the original node.

#### Parameters

##### hint

[`EmitHint`](../enumerations/EmitHint.md)

A hint as to the intended usage of the node.

##### node

[`Node`](Node.md)

The node to substitute.

#### Returns

[`Node`](Node.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TransientIdentifier.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TransientIdentifier

# Interface: TransientIdentifier

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:686

## Extends

- [`Identifier`](Identifier.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`Identifier`](Identifier.md).[`_declarationBrand`](Identifier.md#_declarationbrand)

***

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`Identifier`](Identifier.md).[`_expressionBrand`](Identifier.md#_expressionbrand)

***

### \_leftHandSideExpressionBrand

> **\_leftHandSideExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1086

#### Inherited from

[`Identifier`](Identifier.md).[`_leftHandSideExpressionBrand`](Identifier.md#_lefthandsideexpressionbrand)

***

### \_memberExpressionBrand

> **\_memberExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1089

#### Inherited from

[`Identifier`](Identifier.md).[`_memberExpressionBrand`](Identifier.md#_memberexpressionbrand)

***

### \_primaryExpressionBrand

> **\_primaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1092

#### Inherited from

[`Identifier`](Identifier.md).[`_primaryExpressionBrand`](Identifier.md#_primaryexpressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`Identifier`](Identifier.md).[`_unaryExpressionBrand`](Identifier.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`Identifier`](Identifier.md).[`_updateExpressionBrand`](Identifier.md#_updateexpressionbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`Identifier`](Identifier.md).[`decorators`](Identifier.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Identifier`](Identifier.md).[`end`](Identifier.md#end)

***

### escapedText

> `readonly` **escapedText**: [`__String`](../type-aliases/String.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:682

Prefer to use `id.unescapedText`. (Note: This is available only in services, not internally to the TypeScript compiler.)
Text of identifier, but if the identifier begins with two underscores, this will begin with three.

#### Inherited from

[`Identifier`](Identifier.md).[`escapedText`](Identifier.md#escapedtext)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Identifier`](Identifier.md).[`flags`](Identifier.md#flags)

***

### isInJSDocNamespace?

> `optional` **isInJSDocNamespace**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:684

#### Inherited from

[`Identifier`](Identifier.md).[`isInJSDocNamespace`](Identifier.md#isinjsdocnamespace)

***

### kind

> `readonly` **kind**: [`Identifier`](../enumerations/SyntaxKind.md#identifier)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:677

#### Inherited from

[`Identifier`](Identifier.md).[`kind`](Identifier.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Identifier`](Identifier.md).[`locals`](Identifier.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`Identifier`](Identifier.md).[`modifiers`](Identifier.md#modifiers)

***

### originalKeywordKind?

> `readonly` `optional` **originalKeywordKind**: [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:683

#### Inherited from

[`Identifier`](Identifier.md).[`originalKeywordKind`](Identifier.md#originalkeywordkind)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`Identifier`](Identifier.md).[`parent`](Identifier.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`Identifier`](Identifier.md).[`pos`](Identifier.md#pos)

***

### resolvedSymbol

> **resolvedSymbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:687

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Identifier`](Identifier.md).[`skipCheck`](Identifier.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Identifier`](Identifier.md).[`symbol`](Identifier.md#symbol)

***

### text

> `readonly` **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6105

#### Inherited from

[`Identifier`](Identifier.md).[`text`](Identifier.md#text)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`Identifier`](Identifier.md).[`forEachChild`](Identifier.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`Identifier`](Identifier.md).[`getChildAt`](Identifier.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Identifier`](Identifier.md).[`getChildCount`](Identifier.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`Identifier`](Identifier.md).[`getChildren`](Identifier.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`Identifier`](Identifier.md).[`getEnd`](Identifier.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Identifier`](Identifier.md).[`getFirstToken`](Identifier.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`Identifier`](Identifier.md).[`getFullStart`](Identifier.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Identifier`](Identifier.md).[`getFullText`](Identifier.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`Identifier`](Identifier.md).[`getFullWidth`](Identifier.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Identifier`](Identifier.md).[`getLastToken`](Identifier.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Identifier`](Identifier.md).[`getLeadingTriviaWidth`](Identifier.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`Identifier`](Identifier.md).[`getSourceFile`](Identifier.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`Identifier`](Identifier.md).[`getStart`](Identifier.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Identifier`](Identifier.md).[`getText`](Identifier.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`Identifier`](Identifier.md).[`getWidth`](Identifier.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TranspileOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TranspileOptions

# Interface: TranspileOptions

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7414

## Properties

### compilerOptions?

> `optional` **compilerOptions**: [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7415

***

### fileName?

> `optional` **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7416

***

### moduleName?

> `optional` **moduleName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7418

***

### renamedDependencies?

> `optional` **renamedDependencies**: [`MapLike`](MapLike.md)\<`string`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7419

***

### reportDiagnostics?

> `optional` **reportDiagnostics**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7417

***

### transformers?

> `optional` **transformers**: [`CustomTransformers`](CustomTransformers.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7420




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TranspileOutput.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TranspileOutput

# Interface: TranspileOutput

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7422

## Properties

### diagnostics?

> `optional` **diagnostics**: [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7424

***

### outputText

> **outputText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7423

***

### sourceMapText?

> `optional` **sourceMapText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7425




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TrueLiteral.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TrueLiteral

# Interface: TrueLiteral

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1097

## Extends

- [`PrimaryExpression`](PrimaryExpression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_expressionBrand`](PrimaryExpression.md#_expressionbrand)

***

### \_leftHandSideExpressionBrand

> **\_leftHandSideExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1086

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_leftHandSideExpressionBrand`](PrimaryExpression.md#_lefthandsideexpressionbrand)

***

### \_memberExpressionBrand

> **\_memberExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1089

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_memberExpressionBrand`](PrimaryExpression.md#_memberexpressionbrand)

***

### \_primaryExpressionBrand

> **\_primaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1092

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_primaryExpressionBrand`](PrimaryExpression.md#_primaryexpressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_unaryExpressionBrand`](PrimaryExpression.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_updateExpressionBrand`](PrimaryExpression.md#_updateexpressionbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`decorators`](PrimaryExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`end`](PrimaryExpression.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`flags`](PrimaryExpression.md#flags)

***

### kind

> `readonly` **kind**: [`TrueKeyword`](../enumerations/SyntaxKind.md#truekeyword)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1098

#### Overrides

[`PrimaryExpression`](PrimaryExpression.md).[`kind`](PrimaryExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`locals`](PrimaryExpression.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`modifiers`](PrimaryExpression.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`parent`](PrimaryExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`pos`](PrimaryExpression.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`skipCheck`](PrimaryExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`symbol`](PrimaryExpression.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`forEachChild`](PrimaryExpression.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getChildAt`](PrimaryExpression.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getChildCount`](PrimaryExpression.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getChildren`](PrimaryExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getEnd`](PrimaryExpression.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFirstToken`](PrimaryExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFullStart`](PrimaryExpression.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFullText`](PrimaryExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getFullWidth`](PrimaryExpression.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getLastToken`](PrimaryExpression.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getLeadingTriviaWidth`](PrimaryExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getSourceFile`](PrimaryExpression.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getStart`](PrimaryExpression.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getText`](PrimaryExpression.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`getWidth`](PrimaryExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TryStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TryStatement

# Interface: TryStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1593

## Extends

- [`Statement`](Statement.md)

## Properties

### \_statementBrand

> **\_statementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1471

#### Inherited from

[`Statement`](Statement.md).[`_statementBrand`](Statement.md#_statementbrand)

***

### catchClause?

> `readonly` `optional` **catchClause**: [`CatchClause`](CatchClause.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1596

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`Statement`](Statement.md).[`decorators`](Statement.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Statement`](Statement.md).[`end`](Statement.md#end)

***

### finallyBlock?

> `readonly` `optional` **finallyBlock**: [`Block`](Block.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1597

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Statement`](Statement.md).[`flags`](Statement.md#flags)

***

### kind

> `readonly` **kind**: [`TryStatement`](../enumerations/SyntaxKind.md#trystatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1594

#### Overrides

[`Statement`](Statement.md).[`kind`](Statement.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Statement`](Statement.md).[`locals`](Statement.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`Statement`](Statement.md).[`modifiers`](Statement.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`Statement`](Statement.md).[`parent`](Statement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`Statement`](Statement.md).[`pos`](Statement.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Statement`](Statement.md).[`skipCheck`](Statement.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Statement`](Statement.md).[`symbol`](Statement.md#symbol)

***

### tryBlock

> `readonly` **tryBlock**: [`Block`](Block.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1595

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`Statement`](Statement.md).[`forEachChild`](Statement.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`Statement`](Statement.md).[`getChildAt`](Statement.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getChildCount`](Statement.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`Statement`](Statement.md).[`getChildren`](Statement.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getEnd`](Statement.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Statement`](Statement.md).[`getFirstToken`](Statement.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getFullStart`](Statement.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Statement`](Statement.md).[`getFullText`](Statement.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getFullWidth`](Statement.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`Statement`](Statement.md).[`getLastToken`](Statement.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getLeadingTriviaWidth`](Statement.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`Statement`](Statement.md).[`getSourceFile`](Statement.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getStart`](Statement.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`Statement`](Statement.md).[`getText`](Statement.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`Statement`](Statement.md).[`getWidth`](Statement.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TsConfigSourceFile.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TsConfigSourceFile

# Interface: TsConfigSourceFile

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2218

## Extends

- [`JsonSourceFile`](JsonSourceFile.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`_declarationBrand`](JsonSourceFile.md#_declarationbrand)

***

### amdDependencies

> **amdDependencies**: readonly [`AmdDependency`](AmdDependency.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2122

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`amdDependencies`](JsonSourceFile.md#amddependencies)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`decorators`](JsonSourceFile.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`end`](JsonSourceFile.md#end)

***

### endOfFileToken

> `readonly` **endOfFileToken**: [`Token`](Token.md)\<[`EndOfFileToken`](../enumerations/SyntaxKind.md#endoffiletoken)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2119

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`endOfFileToken`](JsonSourceFile.md#endoffiletoken)

***

### extendedSourceFiles?

> `optional` **extendedSourceFiles**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2219

***

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2120

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`fileName`](JsonSourceFile.md#filename)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`flags`](JsonSourceFile.md#flags)

***

### hasNoDefaultLib

> **hasNoDefaultLib**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2137

lib.d.ts should have a reference comment like

 /// <reference no-default-lib="true"/>

If any other file has this comment, it signals not to include lib.d.ts
because this containing file is intended to act as a default library.

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`hasNoDefaultLib`](JsonSourceFile.md#hasnodefaultlib)

***

### impliedNodeFormat?

> `optional` **impliedNodeFormat**: [`CommonJS`](../enumerations/ModuleKind.md#commonjs) \| [`ESNext`](../enumerations/ModuleKind.md#esnext)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2156

When `module` is `Node16` or `NodeNext`, this field controls whether the
source file in question is an ESNext-output-format file, or a CommonJS-output-format
module. This is derived by the module resolver as it looks up the file, since
it is derived from either the file extension of the module, or the containing
`package.json` context, and affects both checking and emit.

It is _public_ so that (pre)transformers can set this field,
since it switches the builtin `node` module transform. Generally speaking, if unset,
the field is treated as though it is `ModuleKind.CommonJS`.

Note that this field is only set by the module resolution process when
`moduleResolution` is `Node16` or `NodeNext`, which is implied by the `module` setting
of `Node16` or `NodeNext`, respectively, but may be overriden (eg, by a `moduleResolution`
of `node`). If so, this field will be unset and source files will be considered to be
CommonJS-output-format by the node module transformer and type checker, regardless of extension or context.

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`impliedNodeFormat`](JsonSourceFile.md#impliednodeformat)

***

### isDeclarationFile

> **isDeclarationFile**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2128

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`isDeclarationFile`](JsonSourceFile.md#isdeclarationfile)

***

### kind

> `readonly` **kind**: [`SourceFile`](../enumerations/SyntaxKind.md#sourcefile)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2117

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`kind`](JsonSourceFile.md#kind)

***

### languageVariant

> **languageVariant**: [`LanguageVariant`](../enumerations/LanguageVariant.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2127

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`languageVariant`](JsonSourceFile.md#languagevariant)

***

### languageVersion

> **languageVersion**: [`ScriptTarget`](../enumerations/ScriptTarget.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2138

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`languageVersion`](JsonSourceFile.md#languageversion)

***

### libReferenceDirectives

> **libReferenceDirectives**: readonly [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2126

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`libReferenceDirectives`](JsonSourceFile.md#libreferencedirectives)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`locals`](JsonSourceFile.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`modifiers`](JsonSourceFile.md#modifiers)

***

### moduleName?

> `optional` **moduleName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2123

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`moduleName`](JsonSourceFile.md#modulename)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`parent`](JsonSourceFile.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`pos`](JsonSourceFile.md#pos)

***

### referencedFiles

> **referencedFiles**: readonly [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2124

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`referencedFiles`](JsonSourceFile.md#referencedfiles)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`skipCheck`](JsonSourceFile.md#skipcheck)

***

### statements

> `readonly` **statements**: [`NodeArray`](NodeArray.md)\<[`JsonObjectExpressionStatement`](JsonObjectExpressionStatement.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2216

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`statements`](JsonSourceFile.md#statements)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`symbol`](JsonSourceFile.md#symbol)

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2121

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`text`](JsonSourceFile.md#text)

***

### typeReferenceDirectives

> **typeReferenceDirectives**: readonly [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2125

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`typeReferenceDirectives`](JsonSourceFile.md#typereferencedirectives)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`forEachChild`](JsonSourceFile.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getChildAt`](JsonSourceFile.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getChildCount`](JsonSourceFile.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getChildren`](JsonSourceFile.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getEnd`](JsonSourceFile.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getFirstToken`](JsonSourceFile.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getFullStart`](JsonSourceFile.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getFullText`](JsonSourceFile.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getFullWidth`](JsonSourceFile.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getLastToken`](JsonSourceFile.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getLeadingTriviaWidth`](JsonSourceFile.md#getleadingtriviawidth)

***

### getLineAndCharacterOfPosition()

> **getLineAndCharacterOfPosition**(`pos`): [`LineAndCharacter`](LineAndCharacter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6157

#### Parameters

##### pos

`number`

#### Returns

[`LineAndCharacter`](LineAndCharacter.md)

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getLineAndCharacterOfPosition`](JsonSourceFile.md#getlineandcharacterofposition)

***

### getLineEndOfPosition()

> **getLineEndOfPosition**(`pos`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6158

#### Parameters

##### pos

`number`

#### Returns

`number`

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getLineEndOfPosition`](JsonSourceFile.md#getlineendofposition)

***

### getLineStarts()

> **getLineStarts**(): readonly `number`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6159

#### Returns

readonly `number`[]

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getLineStarts`](JsonSourceFile.md#getlinestarts)

***

### getPositionOfLineAndCharacter()

> **getPositionOfLineAndCharacter**(`line`, `character`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6160

#### Parameters

##### line

`number`

##### character

`number`

#### Returns

`number`

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getPositionOfLineAndCharacter`](JsonSourceFile.md#getpositionoflineandcharacter)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getSourceFile`](JsonSourceFile.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getStart`](JsonSourceFile.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getText`](JsonSourceFile.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`getWidth`](JsonSourceFile.md#getwidth)

***

### update()

> **update**(`newText`, `textChangeRange`): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6161

#### Parameters

##### newText

`string`

##### textChangeRange

[`TextChangeRange`](TextChangeRange.md)

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`JsonSourceFile`](JsonSourceFile.md).[`update`](JsonSourceFile.md#update)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TupleType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TupleType

# Interface: TupleType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2862

Class and interface types (ObjectFlags.Class and ObjectFlags.Interface).

## Extends

- [`GenericType`](GenericType.md)

## Properties

### aliasSymbol?

> `optional` **aliasSymbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2773

#### Inherited from

[`GenericType`](GenericType.md).[`aliasSymbol`](GenericType.md#aliassymbol)

***

### aliasTypeArguments?

> `optional` **aliasTypeArguments**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2774

#### Inherited from

[`GenericType`](GenericType.md).[`aliasTypeArguments`](GenericType.md#aliastypearguments)

***

### combinedFlags

> **combinedFlags**: [`ElementFlags`](../enumerations/ElementFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2867

***

### elementFlags

> **elementFlags**: readonly [`ElementFlags`](../enumerations/ElementFlags.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2863

***

### fixedLength

> **fixedLength**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2865

***

### flags

> **flags**: [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2770

#### Inherited from

[`GenericType`](GenericType.md).[`flags`](GenericType.md#flags)

***

### hasRestElement

> **hasRestElement**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2866

***

### labeledElementDeclarations?

> `optional` **labeledElementDeclarations**: readonly ([`ParameterDeclaration`](ParameterDeclaration.md) \| [`NamedTupleMember`](NamedTupleMember.md))[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2869

***

### localTypeParameters

> **localTypeParameters**: `undefined` \| [`TypeParameter`](TypeParameter.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2824

#### Inherited from

[`GenericType`](GenericType.md).[`localTypeParameters`](GenericType.md#localtypeparameters)

***

### minLength

> **minLength**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2864

***

### node?

> `optional` **node**: [`TypeReferenceNode`](TypeReferenceNode.md) \| [`ArrayTypeNode`](ArrayTypeNode.md) \| [`TupleTypeNode`](TupleTypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2846

#### Inherited from

[`GenericType`](GenericType.md).[`node`](GenericType.md#node)

***

### objectFlags

> **objectFlags**: [`ObjectFlags`](../enumerations/ObjectFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2818

#### Inherited from

[`GenericType`](GenericType.md).[`objectFlags`](GenericType.md#objectflags)

***

### outerTypeParameters

> **outerTypeParameters**: `undefined` \| [`TypeParameter`](TypeParameter.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2823

#### Inherited from

[`GenericType`](GenericType.md).[`outerTypeParameters`](GenericType.md#outertypeparameters)

***

### pattern?

> `optional` **pattern**: [`DestructuringPattern`](../type-aliases/DestructuringPattern.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2772

#### Inherited from

[`GenericType`](GenericType.md).[`pattern`](GenericType.md#pattern)

***

### readonly

> **readonly**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2868

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2771

#### Inherited from

[`GenericType`](GenericType.md).[`symbol`](GenericType.md#symbol)

***

### target

> **target**: [`GenericType`](GenericType.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2845

#### Inherited from

[`GenericType`](GenericType.md).[`target`](GenericType.md#target)

***

### thisType

> **thisType**: `undefined` \| [`TypeParameter`](TypeParameter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2825

#### Inherited from

[`GenericType`](GenericType.md).[`thisType`](GenericType.md#thistype)

***

### typeArguments?

> `optional` **typeArguments**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6145

#### Inherited from

[`GenericType`](GenericType.md).[`typeArguments`](GenericType.md#typearguments)

***

### typeParameters

> **typeParameters**: `undefined` \| [`TypeParameter`](TypeParameter.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2822

#### Inherited from

[`GenericType`](GenericType.md).[`typeParameters`](GenericType.md#typeparameters)

## Methods

### getApparentProperties()

> **getApparentProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6124

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`GenericType`](GenericType.md).[`getApparentProperties`](GenericType.md#getapparentproperties)

***

### getBaseTypes()

> **getBaseTypes**(): `undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6129

#### Returns

`undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

#### Inherited from

[`GenericType`](GenericType.md).[`getBaseTypes`](GenericType.md#getbasetypes)

***

### getCallSignatures()

> **getCallSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6125

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`GenericType`](GenericType.md).[`getCallSignatures`](GenericType.md#getcallsignatures)

***

### getConstraint()

> **getConstraint**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6131

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`GenericType`](GenericType.md).[`getConstraint`](GenericType.md#getconstraint)

***

### getConstructSignatures()

> **getConstructSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6126

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`GenericType`](GenericType.md).[`getConstructSignatures`](GenericType.md#getconstructsignatures)

***

### getDefault()

> **getDefault**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6132

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`GenericType`](GenericType.md).[`getDefault`](GenericType.md#getdefault)

***

### getFlags()

> **getFlags**(): [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6120

#### Returns

[`TypeFlags`](../enumerations/TypeFlags.md)

#### Inherited from

[`GenericType`](GenericType.md).[`getFlags`](GenericType.md#getflags)

***

### getNonNullableType()

> **getNonNullableType**(): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6130

#### Returns

[`Type`](Type.md)

#### Inherited from

[`GenericType`](GenericType.md).[`getNonNullableType`](GenericType.md#getnonnullabletype)

***

### getNumberIndexType()

> **getNumberIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6128

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`GenericType`](GenericType.md).[`getNumberIndexType`](GenericType.md#getnumberindextype)

***

### getProperties()

> **getProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6122

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`GenericType`](GenericType.md).[`getProperties`](GenericType.md#getproperties)

***

### getProperty()

> **getProperty**(`propertyName`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6123

#### Parameters

##### propertyName

`string`

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`GenericType`](GenericType.md).[`getProperty`](GenericType.md#getproperty)

***

### getStringIndexType()

> **getStringIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6127

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`GenericType`](GenericType.md).[`getStringIndexType`](GenericType.md#getstringindextype)

***

### getSymbol()

> **getSymbol**(): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6121

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`GenericType`](GenericType.md).[`getSymbol`](GenericType.md#getsymbol)

***

### isClass()

> **isClass**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6141

#### Returns

`this is InterfaceType`

#### Inherited from

[`GenericType`](GenericType.md).[`isClass`](GenericType.md#isclass)

***

### isClassOrInterface()

> **isClassOrInterface**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6140

#### Returns

`this is InterfaceType`

#### Inherited from

[`GenericType`](GenericType.md).[`isClassOrInterface`](GenericType.md#isclassorinterface)

***

### isIndexType()

> **isIndexType**(): `this is IndexType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6142

#### Returns

`this is IndexType`

#### Inherited from

[`GenericType`](GenericType.md).[`isIndexType`](GenericType.md#isindextype)

***

### isIntersection()

> **isIntersection**(): `this is IntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6134

#### Returns

`this is IntersectionType`

#### Inherited from

[`GenericType`](GenericType.md).[`isIntersection`](GenericType.md#isintersection)

***

### isLiteral()

> **isLiteral**(): `this is LiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6136

#### Returns

`this is LiteralType`

#### Inherited from

[`GenericType`](GenericType.md).[`isLiteral`](GenericType.md#isliteral)

***

### isNumberLiteral()

> **isNumberLiteral**(): `this is NumberLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6138

#### Returns

`this is NumberLiteralType`

#### Inherited from

[`GenericType`](GenericType.md).[`isNumberLiteral`](GenericType.md#isnumberliteral)

***

### isStringLiteral()

> **isStringLiteral**(): `this is StringLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6137

#### Returns

`this is StringLiteralType`

#### Inherited from

[`GenericType`](GenericType.md).[`isStringLiteral`](GenericType.md#isstringliteral)

***

### isTypeParameter()

> **isTypeParameter**(): `this is TypeParameter`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6139

#### Returns

`this is TypeParameter`

#### Inherited from

[`GenericType`](GenericType.md).[`isTypeParameter`](GenericType.md#istypeparameter)

***

### isUnion()

> **isUnion**(): `this is UnionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6133

#### Returns

`this is UnionType`

#### Inherited from

[`GenericType`](GenericType.md).[`isUnion`](GenericType.md#isunion)

***

### isUnionOrIntersection()

> **isUnionOrIntersection**(): `this is UnionOrIntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6135

#### Returns

`this is UnionOrIntersectionType`

#### Inherited from

[`GenericType`](GenericType.md).[`isUnionOrIntersection`](GenericType.md#isunionorintersection)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TupleTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TupleTypeNode

# Interface: TupleTypeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:972

## Extends

- [`TypeNode`](TypeNode.md)

## Properties

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`TypeNode`](TypeNode.md).[`_typeNodeBrand`](TypeNode.md#_typenodebrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`TypeNode`](TypeNode.md).[`decorators`](TypeNode.md#decorators)

***

### elements

> `readonly` **elements**: [`NodeArray`](NodeArray.md)\<[`TypeNode`](TypeNode.md) \| [`NamedTupleMember`](NamedTupleMember.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:974

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`TypeNode`](TypeNode.md).[`end`](TypeNode.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`TypeNode`](TypeNode.md).[`flags`](TypeNode.md#flags)

***

### kind

> `readonly` **kind**: [`TupleType`](../enumerations/SyntaxKind.md#tupletype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:973

#### Overrides

[`TypeNode`](TypeNode.md).[`kind`](TypeNode.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`TypeNode`](TypeNode.md).[`locals`](TypeNode.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`TypeNode`](TypeNode.md).[`modifiers`](TypeNode.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`TypeNode`](TypeNode.md).[`parent`](TypeNode.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`TypeNode`](TypeNode.md).[`pos`](TypeNode.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`TypeNode`](TypeNode.md).[`skipCheck`](TypeNode.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`TypeNode`](TypeNode.md).[`symbol`](TypeNode.md#symbol)

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`TypeNode`](TypeNode.md).[`forEachChild`](TypeNode.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getChildAt`](TypeNode.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getChildCount`](TypeNode.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`TypeNode`](TypeNode.md).[`getChildren`](TypeNode.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getEnd`](TypeNode.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFirstToken`](TypeNode.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFullStart`](TypeNode.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFullText`](TypeNode.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getFullWidth`](TypeNode.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getLastToken`](TypeNode.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getLeadingTriviaWidth`](TypeNode.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`TypeNode`](TypeNode.md).[`getSourceFile`](TypeNode.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getStart`](TypeNode.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getText`](TypeNode.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`TypeNode`](TypeNode.md).[`getWidth`](TypeNode.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TupleTypeReference.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TupleTypeReference

# Interface: TupleTypeReference

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2871

Type references (ObjectFlags.Reference). When a class or interface has type parameters or
a "this" type, references to the class or interface are made using type references. The
typeArguments property specifies the types to substitute for the type parameters of the
class or interface and optionally includes an extra element that specifies the type to
substitute for "this" in the resulting instantiation. When no extra argument is present,
the type reference itself is substituted for "this". The typeArguments property is undefined
if the class or interface has no type parameters and the reference isn't specifying an
explicit "this" argument.

## Extends

- [`TypeReference`](TypeReference.md)

## Properties

### aliasSymbol?

> `optional` **aliasSymbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2773

#### Inherited from

[`TypeReference`](TypeReference.md).[`aliasSymbol`](TypeReference.md#aliassymbol)

***

### aliasTypeArguments?

> `optional` **aliasTypeArguments**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2774

#### Inherited from

[`TypeReference`](TypeReference.md).[`aliasTypeArguments`](TypeReference.md#aliastypearguments)

***

### flags

> **flags**: [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2770

#### Inherited from

[`TypeReference`](TypeReference.md).[`flags`](TypeReference.md#flags)

***

### node?

> `optional` **node**: [`TypeReferenceNode`](TypeReferenceNode.md) \| [`ArrayTypeNode`](ArrayTypeNode.md) \| [`TupleTypeNode`](TupleTypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2846

#### Inherited from

[`TypeReference`](TypeReference.md).[`node`](TypeReference.md#node)

***

### objectFlags

> **objectFlags**: [`ObjectFlags`](../enumerations/ObjectFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2818

#### Inherited from

[`TypeReference`](TypeReference.md).[`objectFlags`](TypeReference.md#objectflags)

***

### pattern?

> `optional` **pattern**: [`DestructuringPattern`](../type-aliases/DestructuringPattern.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2772

#### Inherited from

[`TypeReference`](TypeReference.md).[`pattern`](TypeReference.md#pattern)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2771

#### Inherited from

[`TypeReference`](TypeReference.md).[`symbol`](TypeReference.md#symbol)

***

### target

> **target**: [`TupleType`](TupleType.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2872

#### Overrides

[`TypeReference`](TypeReference.md).[`target`](TypeReference.md#target)

***

### typeArguments?

> `optional` **typeArguments**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6145

#### Inherited from

[`TypeReference`](TypeReference.md).[`typeArguments`](TypeReference.md#typearguments)

## Methods

### getApparentProperties()

> **getApparentProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6124

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`TypeReference`](TypeReference.md).[`getApparentProperties`](TypeReference.md#getapparentproperties)

***

### getBaseTypes()

> **getBaseTypes**(): `undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6129

#### Returns

`undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

#### Inherited from

[`TypeReference`](TypeReference.md).[`getBaseTypes`](TypeReference.md#getbasetypes)

***

### getCallSignatures()

> **getCallSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6125

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`TypeReference`](TypeReference.md).[`getCallSignatures`](TypeReference.md#getcallsignatures)

***

### getConstraint()

> **getConstraint**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6131

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`TypeReference`](TypeReference.md).[`getConstraint`](TypeReference.md#getconstraint)

***

### getConstructSignatures()

> **getConstructSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6126

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`TypeReference`](TypeReference.md).[`getConstructSignatures`](TypeReference.md#getconstructsignatures)

***

### getDefault()

> **getDefault**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6132

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`TypeReference`](TypeReference.md).[`getDefault`](TypeReference.md#getdefault)

***

### getFlags()

> **getFlags**(): [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6120

#### Returns

[`TypeFlags`](../enumerations/TypeFlags.md)

#### Inherited from

[`TypeReference`](TypeReference.md).[`getFlags`](TypeReference.md#getflags)

***

### getNonNullableType()

> **getNonNullableType**(): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6130

#### Returns

[`Type`](Type.md)

#### Inherited from

[`TypeReference`](TypeReference.md).[`getNonNullableType`](TypeReference.md#getnonnullabletype)

***

### getNumberIndexType()

> **getNumberIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6128

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`TypeReference`](TypeReference.md).[`getNumberIndexType`](TypeReference.md#getnumberindextype)

***

### getProperties()

> **getProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6122

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`TypeReference`](TypeReference.md).[`getProperties`](TypeReference.md#getproperties)

***

### getProperty()

> **getProperty**(`propertyName`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6123

#### Parameters

##### propertyName

`string`

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`TypeReference`](TypeReference.md).[`getProperty`](TypeReference.md#getproperty)

***

### getStringIndexType()

> **getStringIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6127

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`TypeReference`](TypeReference.md).[`getStringIndexType`](TypeReference.md#getstringindextype)

***

### getSymbol()

> **getSymbol**(): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6121

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`TypeReference`](TypeReference.md).[`getSymbol`](TypeReference.md#getsymbol)

***

### isClass()

> **isClass**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6141

#### Returns

`this is InterfaceType`

#### Inherited from

[`TypeReference`](TypeReference.md).[`isClass`](TypeReference.md#isclass)

***

### isClassOrInterface()

> **isClassOrInterface**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6140

#### Returns

`this is InterfaceType`

#### Inherited from

[`TypeReference`](TypeReference.md).[`isClassOrInterface`](TypeReference.md#isclassorinterface)

***

### isIndexType()

> **isIndexType**(): `this is IndexType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6142

#### Returns

`this is IndexType`

#### Inherited from

[`TypeReference`](TypeReference.md).[`isIndexType`](TypeReference.md#isindextype)

***

### isIntersection()

> **isIntersection**(): `this is IntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6134

#### Returns

`this is IntersectionType`

#### Inherited from

[`TypeReference`](TypeReference.md).[`isIntersection`](TypeReference.md#isintersection)

***

### isLiteral()

> **isLiteral**(): `this is LiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6136

#### Returns

`this is LiteralType`

#### Inherited from

[`TypeReference`](TypeReference.md).[`isLiteral`](TypeReference.md#isliteral)

***

### isNumberLiteral()

> **isNumberLiteral**(): `this is NumberLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6138

#### Returns

`this is NumberLiteralType`

#### Inherited from

[`TypeReference`](TypeReference.md).[`isNumberLiteral`](TypeReference.md#isnumberliteral)

***

### isStringLiteral()

> **isStringLiteral**(): `this is StringLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6137

#### Returns

`this is StringLiteralType`

#### Inherited from

[`TypeReference`](TypeReference.md).[`isStringLiteral`](TypeReference.md#isstringliteral)

***

### isTypeParameter()

> **isTypeParameter**(): `this is TypeParameter`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6139

#### Returns

`this is TypeParameter`

#### Inherited from

[`TypeReference`](TypeReference.md).[`isTypeParameter`](TypeReference.md#istypeparameter)

***

### isUnion()

> **isUnion**(): `this is UnionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6133

#### Returns

`this is UnionType`

#### Inherited from

[`TypeReference`](TypeReference.md).[`isUnion`](TypeReference.md#isunion)

***

### isUnionOrIntersection()

> **isUnionOrIntersection**(): `this is UnionOrIntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6135

#### Returns

`this is UnionOrIntersectionType`

#### Inherited from

[`TypeReference`](TypeReference.md).[`isUnionOrIntersection`](TypeReference.md#isunionorintersection)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Type.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Type

# Interface: Type

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2769

## Extended by

- [`LiteralType`](LiteralType.md)
- [`UniqueESSymbolType`](UniqueESSymbolType.md)
- [`EnumType`](EnumType.md)
- [`ObjectType`](ObjectType.md)
- [`UnionOrIntersectionType`](UnionOrIntersectionType.md)
- [`InstantiableType`](InstantiableType.md)

## Properties

### aliasSymbol?

> `optional` **aliasSymbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2773

***

### aliasTypeArguments?

> `optional` **aliasTypeArguments**: readonly `Type`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2774

***

### flags

> **flags**: [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2770

***

### pattern?

> `optional` **pattern**: [`DestructuringPattern`](../type-aliases/DestructuringPattern.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2772

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2771

## Methods

### getApparentProperties()

> **getApparentProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6124

#### Returns

[`Symbol`](Symbol.md)[]

***

### getBaseTypes()

> **getBaseTypes**(): `undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6129

#### Returns

`undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

***

### getCallSignatures()

> **getCallSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6125

#### Returns

readonly [`Signature`](Signature.md)[]

***

### getConstraint()

> **getConstraint**(): `undefined` \| `Type`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6131

#### Returns

`undefined` \| `Type`

***

### getConstructSignatures()

> **getConstructSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6126

#### Returns

readonly [`Signature`](Signature.md)[]

***

### getDefault()

> **getDefault**(): `undefined` \| `Type`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6132

#### Returns

`undefined` \| `Type`

***

### getFlags()

> **getFlags**(): [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6120

#### Returns

[`TypeFlags`](../enumerations/TypeFlags.md)

***

### getNonNullableType()

> **getNonNullableType**(): `Type`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6130

#### Returns

`Type`

***

### getNumberIndexType()

> **getNumberIndexType**(): `undefined` \| `Type`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6128

#### Returns

`undefined` \| `Type`

***

### getProperties()

> **getProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6122

#### Returns

[`Symbol`](Symbol.md)[]

***

### getProperty()

> **getProperty**(`propertyName`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6123

#### Parameters

##### propertyName

`string`

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

***

### getStringIndexType()

> **getStringIndexType**(): `undefined` \| `Type`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6127

#### Returns

`undefined` \| `Type`

***

### getSymbol()

> **getSymbol**(): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6121

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

***

### isClass()

> **isClass**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6141

#### Returns

`this is InterfaceType`

***

### isClassOrInterface()

> **isClassOrInterface**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6140

#### Returns

`this is InterfaceType`

***

### isIndexType()

> **isIndexType**(): `this is IndexType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6142

#### Returns

`this is IndexType`

***

### isIntersection()

> **isIntersection**(): `this is IntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6134

#### Returns

`this is IntersectionType`

***

### isLiteral()

> **isLiteral**(): `this is LiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6136

#### Returns

`this is LiteralType`

***

### isNumberLiteral()

> **isNumberLiteral**(): `this is NumberLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6138

#### Returns

`this is NumberLiteralType`

***

### isStringLiteral()

> **isStringLiteral**(): `this is StringLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6137

#### Returns

`this is StringLiteralType`

***

### isTypeParameter()

> **isTypeParameter**(): `this is TypeParameter`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6139

#### Returns

`this is TypeParameter`

***

### isUnion()

> **isUnion**(): `this is UnionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6133

#### Returns

`this is UnionType`

***

### isUnionOrIntersection()

> **isUnionOrIntersection**(): `this is UnionOrIntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6135

#### Returns

`this is UnionOrIntersectionType`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeAcquisition.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeAcquisition

# Interface: TypeAcquisition

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3234

## Indexable

\[`option`: `string`\]: [`CompilerOptionsValue`](../type-aliases/CompilerOptionsValue.md)

## Properties

### disableFilenameBasedTypeAcquisition?

> `optional` **disableFilenameBasedTypeAcquisition**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3243

***

### enable?

> `optional` **enable**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3240

***

### ~~enableAutoDiscovery?~~

> `optional` **enableAutoDiscovery**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3239

#### Deprecated

typingOptions.enableAutoDiscovery
Use typeAcquisition.enable instead.

***

### exclude?

> `optional` **exclude**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3242

***

### include?

> `optional` **include**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3241




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeAliasDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeAliasDeclaration

# Interface: TypeAliasDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1655

## Extends

- [`DeclarationStatement`](DeclarationStatement.md).[`JSDocContainer`](JSDocContainer.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`_declarationBrand`](DeclarationStatement.md#_declarationbrand)

***

### \_statementBrand

> **\_statementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1471

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`_statementBrand`](DeclarationStatement.md#_statementbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`decorators`](DeclarationStatement.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`end`](DeclarationStatement.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`flags`](DeclarationStatement.md#flags)

***

### kind

> `readonly` **kind**: [`TypeAliasDeclaration`](../enumerations/SyntaxKind.md#typealiasdeclaration)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1656

#### Overrides

[`DeclarationStatement`](DeclarationStatement.md).[`kind`](DeclarationStatement.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`locals`](DeclarationStatement.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`Modifier`](../type-aliases/Modifier.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1657

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Overrides

[`DeclarationStatement`](DeclarationStatement.md).[`modifiers`](DeclarationStatement.md#modifiers)

***

### name

> `readonly` **name**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1658

#### Overrides

[`DeclarationStatement`](DeclarationStatement.md).[`name`](DeclarationStatement.md#name)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`parent`](DeclarationStatement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`pos`](DeclarationStatement.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`skipCheck`](DeclarationStatement.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`symbol`](DeclarationStatement.md#symbol)

***

### type

> `readonly` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1660

***

### typeParameters?

> `readonly` `optional` **typeParameters**: [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1659

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`forEachChild`](DeclarationStatement.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getChildAt`](DeclarationStatement.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getChildCount`](DeclarationStatement.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getChildren`](DeclarationStatement.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getEnd`](DeclarationStatement.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getFirstToken`](DeclarationStatement.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getFullStart`](DeclarationStatement.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getFullText`](DeclarationStatement.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getFullWidth`](DeclarationStatement.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getLastToken`](DeclarationStatement.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getLeadingTriviaWidth`](DeclarationStatement.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getSourceFile`](DeclarationStatement.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getStart`](DeclarationStatement.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getText`](DeclarationStatement.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`getWidth`](DeclarationStatement.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeAssertion.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeAssertion

# Interface: TypeAssertion

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1375

## Extends

- [`UnaryExpression`](UnaryExpression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`_expressionBrand`](UnaryExpression.md#_expressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`_unaryExpressionBrand`](UnaryExpression.md#_unaryexpressionbrand)

***

### ~~decorators?~~

> `readonly` `optional` **decorators**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8375

#### Deprecated

`decorators` has been removed from `Node` and merged with `modifiers` on the `Node` subtypes that support them.
Use `ts.canHaveDecorators()` to test whether a `Node` can have decorators.
Use `ts.getDecorators()` to get the decorators of a `Node`.

For example:
```ts
const decorators = ts.canHaveDecorators(node) ? ts.getDecorators(node) : undefined;
```

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`decorators`](UnaryExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`end`](UnaryExpression.md#end)

***

### expression

> `readonly` **expression**: [`UnaryExpression`](UnaryExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1378

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`flags`](UnaryExpression.md#flags)

***

### kind

> `readonly` **kind**: [`TypeAssertionExpression`](../enumerations/SyntaxKind.md#typeassertionexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1376

#### Overrides

[`UnaryExpression`](UnaryExpression.md).[`kind`](UnaryExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`locals`](UnaryExpression.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8386

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`modifiers`](UnaryExpression.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`parent`](UnaryExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`pos`](UnaryExpression.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`skipCheck`](UnaryExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`symbol`](UnaryExpression.md#symbol)

***

### type

> `readonly` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1377

## Methods

### forEachChild()

> **forEachChild**\<`T`\>(`cbNode`, `cbNodeArray?`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6102

#### Type Parameters

##### T

`T`

#### Parameters

##### cbNode

(`node`) => `undefined` \| `T`

##### cbNodeArray?

(`nodes`) => `undefined` \| `T`

#### Returns

`undefined` \| `T`

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`forEachChild`](UnaryExpression.md#foreachchild)

***

### getChildAt()

> **getChildAt**(`index`, `sourceFile?`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6090

#### Parameters

##### index

`number`

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getChildAt`](UnaryExpression.md#getchildat)

***

### getChildCount()

> **getChildCount**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6089

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getChildCount`](UnaryExpression.md#getchildcount)

***

### getChildren()

> **getChildren**(`sourceFile?`): [`Node`](Node.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6091

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

[`Node`](Node.md)[]

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getChildren`](UnaryExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getEnd`](UnaryExpression.md#getend)

***

### getFirstToken()

> **getFirstToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6100

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getFirstToken`](UnaryExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getFullStart`](UnaryExpression.md#getfullstart)

***

### getFullText()

> **getFullText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6098

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getFullText`](UnaryExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getFullWidth`](UnaryExpression.md#getfullwidth)

***

### getLastToken()

> **getLastToken**(`sourceFile?`): `undefined` \| [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6101

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`undefined` \| [`Node`](Node.md)

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getLastToken`](UnaryExpression.md#getlasttoken)

***

### getLeadingTriviaWidth()

> **getLeadingTriviaWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6097

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`number`

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getLeadingTriviaWidth`](UnaryExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getSourceFile`](UnaryExpression.md#getsourcefile)

***

### getStart()

> **getStart**(`sourceFile?`, `includeJsDocComment?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6092

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### includeJsDocComment?

`boolean`

#### Returns

`number`

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getStart`](UnaryExpression.md#getstart)

***

### getText()

> **getText**(`sourceFile?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6099

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

`string`

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getText`](UnaryExpression.md#gettext)

***

### getWidth()

> **getWidth**(`sourceFile?`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6095

#### Parameters

##### sourceFile?

[`SourceFileLike`](SourceFileLike.md)

#### Returns

`number`

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`getWidth`](UnaryExpression.md#getwidth)



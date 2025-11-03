

============================================================
## FILE: `classes/ArkMethod.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkMethod

# Class: ArkMethod

Defined in: src/core/model/ArkMethod.ts:64

## Extends

- `ArkBaseModel`

## Implements

- `ArkExport`

## Constructors

### Constructor

> **new ArkMethod**(): `ArkMethod`

Defined in: src/core/model/ArkMethod.ts:87

#### Returns

`ArkMethod`

#### Overrides

`ArkBaseModel.constructor`

## Properties

### decorators?

> `protected` `optional` **decorators**: `Set`\<[`Decorator`](Decorator.md)\>

Defined in: src/core/model/ArkBaseModel.ts:115

#### Inherited from

`ArkBaseModel.decorators`

***

### metadata?

> `protected` `optional` **metadata**: `ArkMetadata`

Defined in: src/core/model/ArkBaseModel.ts:116

#### Inherited from

`ArkBaseModel.metadata`

***

### modifiers?

> `protected` `optional` **modifiers**: `number`

Defined in: src/core/model/ArkBaseModel.ts:114

#### Inherited from

`ArkBaseModel.modifiers`

## Methods

### addDecorator()

> **addDecorator**(`decorator`): `void`

Defined in: src/core/model/ArkBaseModel.ts:215

#### Parameters

##### decorator

[`Decorator`](Decorator.md)

#### Returns

`void`

#### Inherited from

`ArkBaseModel.addDecorator`

***

### addModifier()

> **addModifier**(`modifier`): `void`

Defined in: src/core/model/ArkBaseModel.ts:142

#### Parameters

##### modifier

`number`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.addModifier`

***

### buildBody()

> **buildBody**(): `void`

Defined in: src/core/model/ArkMethod.ts:563

#### Returns

`void`

***

### containsModifier()

> **containsModifier**(`modifierType`): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:194

#### Parameters

##### modifierType

`ModifierType`

#### Returns

`boolean`

#### Implementation of

`ArkExport.containsModifier`

#### Inherited from

`ArkBaseModel.containsModifier`

***

### freeBodyBuilder()

> **freeBodyBuilder**(): `void`

Defined in: src/core/model/ArkMethod.ts:559

#### Returns

`void`

***

### getAsteriskToken()

> **getAsteriskToken**(): `boolean`

Defined in: src/core/model/ArkMethod.ts:584

#### Returns

`boolean`

***

### getBody()

> **getBody**(): `undefined` \| [`ArkBody`](ArkBody.md)

Defined in: src/core/model/ArkMethod.ts:417

Get [ArkBody](ArkBody.md) of a Method.
A [ArkBody](ArkBody.md) contains the CFG and actual instructions or operations to be executed for a method.
It is analogous to the body of a function or method in high-level programming languages,
which contains the statements and expressions that define what the function does.

#### Returns

`undefined` \| [`ArkBody`](ArkBody.md)

The [ArkBody](ArkBody.md) of a method.

#### Example

1. Get cfg or stmt through ArkBody.

```typescript
let cfg = this.scene.getMethod()?.getBody().getCfg();
const body = arkMethod.getBody()
```

2. Get local variable through ArkBody.

```typescript
arkClass.getDefaultArkMethod()?.getBody().getLocals.forEach(local=>{...})
let locals = arkFile().getDefaultClass().getDefaultArkMethod()?.getBody()?.getLocals();
```

***

### getBodyBuilder()

> **getBodyBuilder**(): `undefined` \| `BodyBuilder`

Defined in: src/core/model/ArkMethod.ts:392

#### Returns

`undefined` \| `BodyBuilder`

***

### getCfg()

> **getCfg**(): `undefined` \| [`Cfg`](Cfg.md)

Defined in: src/core/model/ArkMethod.ts:460

Get the CFG (i.e., control flow graph) of a method.
The CFG is a graphical representation of all possible control flow paths within a method's body.
A CFG consists of blocks, statements and goto control jumps.

#### Returns

`undefined` \| [`Cfg`](Cfg.md)

The CFG (i.e., control flow graph) of a method.

#### Example

1. get stmt through ArkBody cfg.

```typescript
body = arkMethod.getBody();
const cfg = body.getCfg();
for (const threeAddressStmt of cfg.getStmts()) {
... ...
}
```

2. get blocks through ArkBody cfg.

```typescript
const body = arkMethod.getBody();
const blocks = [...body.getCfg().getBlocks()];
for (let i=0; i<blocks.length; i++) {
const block = blocks[i];
... ...
for (const stmt of block.getStmts()) {
... ...
}
let text = "next;"
for (const next of block.getSuccessors()) {
text += blocks.indexOf(next) + ' ';
}
// ... ...
}
```

***

### getCode()

> **getCode**(): `undefined` \| `string`

Defined in: src/core/model/ArkMethod.ts:110

Returns the codes of method as a **string.**

#### Returns

`undefined` \| `string`

the codes of method.

***

### getColumn()

> **getColumn**(): `null` \| `number`

Defined in: src/core/model/ArkMethod.ts:213

Get column of the method's implementation or null if the method has no implementation.

#### Returns

`null` \| `number`

null or the number of the column.

***

### getDeclareColumns()

> **getDeclareColumns**(): `null` \| `number`[]

Defined in: src/core/model/ArkMethod.ts:137

Get all columns of the method's declarations or null if the method has no seperated declaration.

#### Returns

`null` \| `number`[]

null or the columns of the method's declarations with number type.

***

### getDeclareLineCols()

> **getDeclareLineCols**(): `null` \| `number`[]

Defined in: src/core/model/ArkMethod.ts:181

Get encoded lines and columns of the method's declarations or null if the method has no seperated declaration.

#### Returns

`null` \| `number`[]

null or the encoded lines and columns of the method's declarations with LineCol type.

***

### getDeclareLines()

> **getDeclareLines**(): `null` \| `number`[]

Defined in: src/core/model/ArkMethod.ts:122

Get all lines of the method's declarations or null if the method has no seperated declaration.

#### Returns

`null` \| `number`[]

null or the lines of the method's declarations with number type.

***

### getDeclareSignatureIndex()

> **getDeclareSignatureIndex**(`targetSignature`): `number`

Defined in: src/core/model/ArkMethod.ts:297

Get the index of the matched method declare signature among all declare signatures.
The index will be -1 if there is no matched signature found.

#### Parameters

##### targetSignature

[`MethodSignature`](MethodSignature.md)

the target declare signature want to search.

#### Returns

`number`

-1 or the index of the matched signature.

***

### getDeclareSignatures()

> **getDeclareSignatures**(): `null` \| [`MethodSignature`](MethodSignature.md)[]

Defined in: src/core/model/ArkMethod.ts:287

Get all declare signatures.
The results could be null if there is no seperated declaration of the method.

#### Returns

`null` \| [`MethodSignature`](MethodSignature.md)[]

null or the method declare signatures.

***

### getDeclaringArkClass()

> **getDeclaringArkClass**(): [`ArkClass`](ArkClass.md)

Defined in: src/core/model/ArkMethod.ts:254

Returns the declaring class of the method.

#### Returns

[`ArkClass`](ArkClass.md)

The declaring class of the method.

***

### getDeclaringArkFile()

> **getDeclaringArkFile**(): [`ArkFile`](ArkFile.md)

Defined in: src/core/model/ArkMethod.ts:262

#### Returns

[`ArkFile`](ArkFile.md)

***

### getDecorators()

> **getDecorators**(): [`Decorator`](Decorator.md)[]

Defined in: src/core/model/ArkBaseModel.ts:202

#### Returns

[`Decorator`](Decorator.md)[]

#### Inherited from

`ArkBaseModel.getDecorators`

***

### getExportType()

> **getExportType**(): `ExportType`

Defined in: src/core/model/ArkMethod.ts:98

#### Returns

`ExportType`

#### Implementation of

`ArkExport.getExportType`

***

### getFunctionLocal()

> **getFunctionLocal**(`name`): `null` \| [`Local`](Local.md)

Defined in: src/core/model/ArkMethod.ts:713

#### Parameters

##### name

`string`

#### Returns

`null` \| [`Local`](Local.md)

***

### getGenericTypes()

> **getGenericTypes**(): `undefined` \| [`GenericType`](GenericType.md)[]

Defined in: src/core/model/ArkMethod.ts:380

#### Returns

`undefined` \| [`GenericType`](GenericType.md)[]

***

### getImplementationSignature()

> **getImplementationSignature**(): `null` \| [`MethodSignature`](MethodSignature.md)

Defined in: src/core/model/ArkMethod.ts:315

Get the method signature of the implementation.
The signature could be null if the method is only a declaration which body is undefined.

#### Returns

`null` \| [`MethodSignature`](MethodSignature.md)

null or the method implementation signature.

***

### getLanguage()

> **getLanguage**(): `Language`

Defined in: src/core/model/ArkMethod.ts:94

Returns the program language of the file where this method defined.

#### Returns

`Language`

***

### getLine()

> **getLine**(): `null` \| `number`

Defined in: src/core/model/ArkMethod.ts:189

Get line of the method's implementation or null if the method has no implementation.

#### Returns

`null` \| `number`

null or the number of the line.

***

### getLineCol()

> **getLineCol**(): `null` \| `number`

Defined in: src/core/model/ArkMethod.ts:237

Get encoded line and column of the method's implementation or null if the method has no implementation.

#### Returns

`null` \| `number`

null or the encoded line and column of the method's implementation with LineCol type.

***

### getMetadata()

> **getMetadata**(`kind`): `undefined` \| `ArkMetadataType`

Defined in: src/core/model/ArkBaseModel.ts:118

#### Parameters

##### kind

`ArkMetadataKind`

#### Returns

`undefined` \| `ArkMetadataType`

#### Inherited from

`ArkBaseModel.getMetadata`

***

### getModifiers()

> **getModifiers**(): `number`

Defined in: src/core/model/ArkBaseModel.ts:129

#### Returns

`number`

#### Implementation of

`ArkExport.getModifiers`

#### Inherited from

`ArkBaseModel.getModifiers`

***

### getName()

> **getName**(): `string`

Defined in: src/core/model/ArkMethod.ts:102

#### Returns

`string`

#### Implementation of

`ArkExport.getName`

***

### getOriginalCfg()

> **getOriginalCfg**(): `undefined` \| [`Cfg`](Cfg.md)

Defined in: src/core/model/ArkMethod.ts:464

#### Returns

`undefined` \| [`Cfg`](Cfg.md)

***

### getOuterMethod()

> **getOuterMethod**(): `undefined` \| `ArkMethod`

Defined in: src/core/model/ArkMethod.ts:705

#### Returns

`undefined` \| `ArkMethod`

***

### getParameterInstances()

> **getParameterInstances**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/model/ArkMethod.ts:483

#### Returns

[`Value`](../interfaces/Value.md)[]

***

### getParameterRefs()

> **getParameterRefs**(): `null` \| [`ArkParameterRef`](ArkParameterRef.md)[]

Defined in: src/core/model/ArkMethod.ts:468

#### Returns

`null` \| [`ArkParameterRef`](ArkParameterRef.md)[]

***

### getParameters()

> **getParameters**(): `MethodParameter`[]

Defined in: src/core/model/ArkMethod.ts:274

#### Returns

`MethodParameter`[]

***

### getQuestionToken()

> **getQuestionToken**(): `boolean`

Defined in: src/core/model/ArkMethod.ts:722

#### Returns

`boolean`

***

### getReturnStmt()

> **getReturnStmt**(): [`Stmt`](Stmt.md)[]

Defined in: src/core/model/ArkMethod.ts:534

#### Returns

[`Stmt`](Stmt.md)[]

***

### getReturnType()

> **getReturnType**(): [`Type`](Type.md)

Defined in: src/core/model/ArkMethod.ts:278

#### Returns

[`Type`](Type.md)

***

### getReturnValues()

> **getReturnValues**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/model/ArkMethod.ts:521

#### Returns

[`Value`](../interfaces/Value.md)[]

***

### getSignature()

> **getSignature**(): [`MethodSignature`](MethodSignature.md)

Defined in: src/core/model/ArkMethod.ts:334

Get the method signature of the implementation or the first declaration if there is no implementation.
For a method, the implementation and declaration signatures must not be undefined at the same time.
A [MethodSignature](MethodSignature.md) includes:
- Class Signature: indicates which class this method belong to.
- Method SubSignature: indicates the detail info of this method such as method name, parameters, returnType, etc.

#### Returns

[`MethodSignature`](MethodSignature.md)

The method signature.

#### Example

1. Get the signature of method mtd.

```typescript
let signature = mtd.getSignature();
// ... ...
```

#### Implementation of

`ArkExport.getSignature`

***

### getStateDecorators()

> **getStateDecorators**(): [`Decorator`](Decorator.md)[]

Defined in: src/core/model/ArkBaseModel.ts:234

#### Returns

[`Decorator`](Decorator.md)[]

#### Inherited from

`ArkBaseModel.getStateDecorators`

***

### getSubSignature()

> **getSubSignature**(): [`MethodSubSignature`](MethodSubSignature.md)

Defined in: src/core/model/ArkMethod.ts:376

#### Returns

[`MethodSubSignature`](MethodSubSignature.md)

***

### getThisInstance()

> **getThisInstance**(): `null` \| [`Value`](../interfaces/Value.md)

Defined in: src/core/model/ArkMethod.ts:504

#### Returns

`null` \| [`Value`](../interfaces/Value.md)

***

### getViewTree()

> **getViewTree**(): `undefined` \| [`ViewTree`](../interfaces/ViewTree.md)

Defined in: src/core/model/ArkMethod.ts:544

#### Returns

`undefined` \| [`ViewTree`](../interfaces/ViewTree.md)

***

### hasBuilderDecorator()

> **hasBuilderDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:230

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasBuilderDecorator`

***

### hasBuilderParamDecorator()

> **hasBuilderParamDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:243

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasBuilderParamDecorator`

***

### hasComponentDecorator()

> **hasComponentDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:251

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasComponentDecorator`

***

### hasDecorator()

> **hasDecorator**(`kind`): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:255

#### Parameters

##### kind

`string` | `Set`\<`string`\>

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasDecorator`

***

### hasEntryDecorator()

> **hasEntryDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:247

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasEntryDecorator`

***

### hasViewTree()

> **hasViewTree**(): `boolean`

Defined in: src/core/model/ArkMethod.ts:548

#### Returns

`boolean`

***

### isAbstract()

> **isAbstract**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:173

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isAbstract`

***

### isAnonymousMethod()

> **isAnonymousMethod**(): `boolean`

Defined in: src/core/model/ArkMethod.ts:270

#### Returns

`boolean`

***

### isDeclare()

> **isDeclare**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:190

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isDeclare`

***

### isDefault()

> **isDefault**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:181

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isDefault`

***

### isDefaultArkMethod()

> **isDefaultArkMethod**(): `boolean`

Defined in: src/core/model/ArkMethod.ts:266

#### Returns

`boolean`

***

### isExport()

> **isExport**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:177

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isExport`

***

### ~~isExported()~~

> **isExported**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:186

#### Returns

`boolean`

#### Deprecated

Use [isExport](ArkNamespace.md#isexport) instead.

#### Inherited from

`ArkBaseModel.isExported`

***

### isGenerated()

> **isGenerated**(): `boolean`

Defined in: src/core/model/ArkMethod.ts:576

#### Returns

`boolean`

***

### isGenericsMethod()

> **isGenericsMethod**(): `boolean`

Defined in: src/core/model/ArkMethod.ts:384

#### Returns

`boolean`

***

### isPrivate()

> **isPrivate**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:161

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isPrivate`

***

### isProtected()

> **isProtected**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:157

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isProtected`

***

### isPublic()

> **isPublic**(): `boolean`

Defined in: src/core/model/ArkMethod.ts:727

#### Returns

`boolean`

#### Overrides

`ArkBaseModel.isPublic`

***

### isReadonly()

> **isReadonly**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:169

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isReadonly`

***

### isStatic()

> **isStatic**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:153

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isStatic`

***

### matchMethodSignature()

> **matchMethodSignature**(`args`): [`MethodSignature`](MethodSignature.md)

Defined in: src/core/model/ArkMethod.ts:625

#### Parameters

##### args

[`Value`](../interfaces/Value.md)[]

#### Returns

[`MethodSignature`](MethodSignature.md)

***

### removeDecorator()

> **removeDecorator**(`kind`): `void`

Defined in: src/core/model/ArkBaseModel.ts:222

#### Parameters

##### kind

`string`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.removeDecorator`

***

### removeModifier()

> **removeModifier**(`modifier`): `void`

Defined in: src/core/model/ArkBaseModel.ts:146

#### Parameters

##### modifier

`ModifierType`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.removeModifier`

***

### setAsteriskToken()

> **setAsteriskToken**(`asteriskToken`): `void`

Defined in: src/core/model/ArkMethod.ts:588

#### Parameters

##### asteriskToken

`boolean`

#### Returns

`void`

***

### setBody()

> **setBody**(`body`): `void`

Defined in: src/core/model/ArkMethod.ts:421

#### Parameters

##### body

[`ArkBody`](ArkBody.md)

#### Returns

`void`

***

### setBodyBuilder()

> **setBodyBuilder**(`bodyBuilder`): `void`

Defined in: src/core/model/ArkMethod.ts:552

#### Parameters

##### bodyBuilder

`BodyBuilder`

#### Returns

`void`

***

### setCode()

> **setCode**(`code`): `void`

Defined in: src/core/model/ArkMethod.ts:114

#### Parameters

##### code

`string`

#### Returns

`void`

***

### setColumn()

> **setColumn**(`column`): `void`

Defined in: src/core/model/ArkMethod.ts:226

Set column of the implementation with column number input.
The column number will be encoded together with the original line number.

#### Parameters

##### column

`number`

the column number of the method implementation.

#### Returns

`void`

***

### setDeclareLineCols()

> **setDeclareLineCols**(`lineCols`): `void`

Defined in: src/core/model/ArkMethod.ts:173

Set lineCols of the declarations directly with LineCol type input.

#### Parameters

##### lineCols

`number`[]

the encoded lines and columns with LineCol type.

#### Returns

`void`

***

### setDeclareLinesAndCols()

> **setDeclareLinesAndCols**(`lines`, `columns`): `void`

Defined in: src/core/model/ArkMethod.ts:155

Set lines and columns of the declarations with number type inputs and then encoded them to LineCol type.
The length of lines and columns should be the same otherwise they cannot be encoded together.

#### Parameters

##### lines

`number`[]

the number of lines.

##### columns

`number`[]

the number of columns.

#### Returns

`void`

***

### setDeclareSignatures()

> **setDeclareSignatures**(`signatures`): `void`

Defined in: src/core/model/ArkMethod.ts:344

Set signatures of all declarations.
It will reset the declaration signatures if they are already defined before.

#### Parameters

##### signatures

one signature or a list of signatures.

[`MethodSignature`](MethodSignature.md) | [`MethodSignature`](MethodSignature.md)[]

#### Returns

`void`

***

### setDeclareSignatureWithIndex()

> **setDeclareSignatureWithIndex**(`signature`, `index`): `void`

Defined in: src/core/model/ArkMethod.ts:359

Reset signature of one declaration with the specified index.
Will do nothing if the index doesn't exist.

#### Parameters

##### signature

[`MethodSignature`](MethodSignature.md)

new signature want to set.

##### index

`number`

index of signature want to set.

#### Returns

`void`

***

### setDeclaringArkClass()

> **setDeclaringArkClass**(`declaringArkClass`): `void`

Defined in: src/core/model/ArkMethod.ts:258

#### Parameters

##### declaringArkClass

[`ArkClass`](ArkClass.md)

#### Returns

`void`

***

### setDecorators()

> **setDecorators**(`decorators`): `void`

Defined in: src/core/model/ArkBaseModel.ts:209

#### Parameters

##### decorators

`Set`\<[`Decorator`](Decorator.md)\>

#### Returns

`void`

#### Inherited from

`ArkBaseModel.setDecorators`

***

### setGenericTypes()

> **setGenericTypes**(`genericTypes`): `void`

Defined in: src/core/model/ArkMethod.ts:388

#### Parameters

##### genericTypes

[`GenericType`](GenericType.md)[]

#### Returns

`void`

***

### setImplementationSignature()

> **setImplementationSignature**(`signature`): `void`

Defined in: src/core/model/ArkMethod.ts:372

Set signature of implementation.
It will reset the implementation signature if it is already defined before.

#### Parameters

##### signature

[`MethodSignature`](MethodSignature.md)

signature of implementation.

#### Returns

`void`

***

### setIsGeneratedFlag()

> **setIsGeneratedFlag**(`isGeneratedFlag`): `void`

Defined in: src/core/model/ArkMethod.ts:580

#### Parameters

##### isGeneratedFlag

`boolean`

#### Returns

`void`

***

### setLine()

> **setLine**(`line`): `void`

Defined in: src/core/model/ArkMethod.ts:202

Set line of the implementation with line number input.
The line number will be encoded together with the original column number.

#### Parameters

##### line

`number`

the line number of the method implementation.

#### Returns

`void`

***

### setLineCol()

> **setLineCol**(`lineCol`): `void`

Defined in: src/core/model/ArkMethod.ts:246

Set lineCol of the implementation directly with LineCol type input.

#### Parameters

##### lineCol

`number`

the encoded line and column with LineCol type.

#### Returns

`void`

***

### setMetadata()

> **setMetadata**(`kind`, `value`): `void`

Defined in: src/core/model/ArkBaseModel.ts:122

#### Parameters

##### kind

`ArkMetadataKind`

##### value

`ArkMetadataType`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.setMetadata`

***

### setModifiers()

> **setModifiers**(`modifiers`): `void`

Defined in: src/core/model/ArkBaseModel.ts:136

#### Parameters

##### modifiers

`number`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.setModifiers`

***

### setOuterMethod()

> **setOuterMethod**(`method`): `void`

Defined in: src/core/model/ArkMethod.ts:709

#### Parameters

##### method

`ArkMethod`

#### Returns

`void`

***

### setQuestionToken()

> **setQuestionToken**(`questionToken`): `void`

Defined in: src/core/model/ArkMethod.ts:718

#### Parameters

##### questionToken

`boolean`

#### Returns

`void`

***

### setViewTree()

> **setViewTree**(`viewTree`): `void`

Defined in: src/core/model/ArkMethod.ts:540

#### Parameters

##### viewTree

[`ViewTree`](../interfaces/ViewTree.md)

#### Returns

`void`

***

### validate()

> **validate**(): `ArkError`

Defined in: src/core/model/ArkMethod.ts:592

#### Returns

`ArkError`

#### Overrides

`ArkBaseModel.validate`

***

### validateFields()

> `protected` **validateFields**(`fields`): `ArkError`

Defined in: src/core/model/ArkBaseModel.ts:267

#### Parameters

##### fields

`string`[]

#### Returns

`ArkError`

#### Inherited from

`ArkBaseModel.validateFields`




============================================================
## FILE: `classes/ArkNamespace.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkNamespace

# Class: ArkNamespace

Defined in: src/core/model/ArkNamespace.ts:29

## Extends

- `ArkBaseModel`

## Implements

- `ArkExport`

## Constructors

### Constructor

> **new ArkNamespace**(): `ArkNamespace`

Defined in: src/core/model/ArkNamespace.ts:50

#### Returns

`ArkNamespace`

#### Overrides

`ArkBaseModel.constructor`

## Properties

### decorators?

> `protected` `optional` **decorators**: `Set`\<[`Decorator`](Decorator.md)\>

Defined in: src/core/model/ArkBaseModel.ts:115

#### Inherited from

`ArkBaseModel.decorators`

***

### metadata?

> `protected` `optional` **metadata**: `ArkMetadata`

Defined in: src/core/model/ArkBaseModel.ts:116

#### Inherited from

`ArkBaseModel.metadata`

***

### modifiers?

> `protected` `optional` **modifiers**: `number`

Defined in: src/core/model/ArkBaseModel.ts:114

#### Inherited from

`ArkBaseModel.modifiers`

## Methods

### addArkClass()

> **addArkClass**(`arkClass`): `void`

Defined in: src/core/model/ArkNamespace.ts:189

#### Parameters

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`void`

***

### addCode()

> **addCode**(`sourceCode`): `void`

Defined in: src/core/model/ArkNamespace.ts:117

#### Parameters

##### sourceCode

`string`

#### Returns

`void`

***

### addDecorator()

> **addDecorator**(`decorator`): `void`

Defined in: src/core/model/ArkBaseModel.ts:215

#### Parameters

##### decorator

[`Decorator`](Decorator.md)

#### Returns

`void`

#### Inherited from

`ArkBaseModel.addDecorator`

***

### addExportInfo()

> **addExportInfo**(`exportInfo`): `void`

Defined in: src/core/model/ArkNamespace.ts:207

#### Parameters

##### exportInfo

[`ExportInfo`](ExportInfo.md)

#### Returns

`void`

***

### addModifier()

> **addModifier**(`modifier`): `void`

Defined in: src/core/model/ArkBaseModel.ts:142

#### Parameters

##### modifier

`number`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.addModifier`

***

### addNamespace()

> **addNamespace**(`namespace`): `void`

Defined in: src/core/model/ArkNamespace.ts:61

#### Parameters

##### namespace

`ArkNamespace`

#### Returns

`void`

***

### containsModifier()

> **containsModifier**(`modifierType`): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:194

#### Parameters

##### modifierType

`ModifierType`

#### Returns

`boolean`

#### Implementation of

`ArkExport.containsModifier`

#### Inherited from

`ArkBaseModel.containsModifier`

***

### getAllClassesUnderThisNamespace()

> **getAllClassesUnderThisNamespace**(): [`ArkClass`](ArkClass.md)[]

Defined in: src/core/model/ArkNamespace.ts:230

#### Returns

[`ArkClass`](ArkClass.md)[]

***

### getAllMethodsUnderThisNamespace()

> **getAllMethodsUnderThisNamespace**(): [`ArkMethod`](ArkMethod.md)[]

Defined in: src/core/model/ArkNamespace.ts:219

#### Returns

[`ArkMethod`](ArkMethod.md)[]

***

### getAllNamespacesUnderThisNamespace()

> **getAllNamespacesUnderThisNamespace**(): `ArkNamespace`[]

Defined in: src/core/model/ArkNamespace.ts:239

#### Returns

`ArkNamespace`[]

***

### getAnonymousClassNumber()

> **getAnonymousClassNumber**(): `number`

Defined in: src/core/model/ArkNamespace.ts:248

#### Returns

`number`

***

### getClass()

> **getClass**(`classSignature`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/core/model/ArkNamespace.ts:176

#### Parameters

##### classSignature

[`ClassSignature`](ClassSignature.md)

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

***

### getClasses()

> **getClasses**(): [`ArkClass`](ArkClass.md)[]

Defined in: src/core/model/ArkNamespace.ts:185

#### Returns

[`ArkClass`](ArkClass.md)[]

***

### getClassWithName()

> **getClassWithName**(`Class`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/core/model/ArkNamespace.ts:181

#### Parameters

##### Class

`string`

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

***

### getCode()

> **getCode**(): `string`

Defined in: src/core/model/ArkNamespace.ts:94

#### Returns

`string`

***

### getCodes()

> **getCodes**(): `string`[]

Defined in: src/core/model/ArkNamespace.ts:105

#### Returns

`string`[]

***

### getColumn()

> **getColumn**(): `number`

Defined in: src/core/model/ArkNamespace.ts:129

#### Returns

`number`

***

### getDeclaringArkFile()

> **getDeclaringArkFile**(): [`ArkFile`](ArkFile.md)

Defined in: src/core/model/ArkNamespace.ts:160

#### Returns

[`ArkFile`](ArkFile.md)

***

### getDeclaringArkNamespace()

> **getDeclaringArkNamespace**(): `null` \| `ArkNamespace`

Defined in: src/core/model/ArkNamespace.ts:168

#### Returns

`null` \| `ArkNamespace`

***

### getDeclaringInstance()

> **getDeclaringInstance**(): [`ArkFile`](ArkFile.md) \| `ArkNamespace`

Defined in: src/core/model/ArkNamespace.ts:152

#### Returns

[`ArkFile`](ArkFile.md) \| `ArkNamespace`

***

### getDecorators()

> **getDecorators**(): [`Decorator`](Decorator.md)[]

Defined in: src/core/model/ArkBaseModel.ts:202

#### Returns

[`Decorator`](Decorator.md)[]

#### Inherited from

`ArkBaseModel.getDecorators`

***

### getDefaultClass()

> **getDefaultClass**(): [`ArkClass`](ArkClass.md)

Defined in: src/core/model/ArkNamespace.ts:211

#### Returns

[`ArkClass`](ArkClass.md)

***

### getExportInfoBy()

> **getExportInfoBy**(`name`): `undefined` \| [`ExportInfo`](ExportInfo.md)

Defined in: src/core/model/ArkNamespace.ts:203

#### Parameters

##### name

`string`

#### Returns

`undefined` \| [`ExportInfo`](ExportInfo.md)

***

### getExportInfos()

> **getExportInfos**(): [`ExportInfo`](ExportInfo.md)[]

Defined in: src/core/model/ArkNamespace.ts:193

#### Returns

[`ExportInfo`](ExportInfo.md)[]

***

### getExportType()

> **getExportType**(): `ExportType`

Defined in: src/core/model/ArkNamespace.ts:252

#### Returns

`ExportType`

#### Implementation of

`ArkExport.getExportType`

***

### getLanguage()

> **getLanguage**(): `Language`

Defined in: src/core/model/ArkNamespace.ts:57

Returns the program language of the file where this namespace defined.

#### Returns

`Language`

***

### getLine()

> **getLine**(): `number`

Defined in: src/core/model/ArkNamespace.ts:121

#### Returns

`number`

***

### getLineColPairs()

> **getLineColPairs**(): \[`number`, `number`\][]

Defined in: src/core/model/ArkNamespace.ts:137

#### Returns

\[`number`, `number`\][]

***

### getMetadata()

> **getMetadata**(`kind`): `undefined` \| `ArkMetadataType`

Defined in: src/core/model/ArkBaseModel.ts:118

#### Parameters

##### kind

`ArkMetadataKind`

#### Returns

`undefined` \| `ArkMetadataType`

#### Inherited from

`ArkBaseModel.getMetadata`

***

### getModifiers()

> **getModifiers**(): `number`

Defined in: src/core/model/ArkBaseModel.ts:129

#### Returns

`number`

#### Implementation of

`ArkExport.getModifiers`

#### Inherited from

`ArkBaseModel.getModifiers`

***

### getName()

> **getName**(): `string`

Defined in: src/core/model/ArkNamespace.ts:90

#### Returns

`string`

#### Implementation of

`ArkExport.getName`

***

### getNamespace()

> **getNamespace**(`namespaceSignature`): `null` \| `ArkNamespace`

Defined in: src/core/model/ArkNamespace.ts:65

#### Parameters

##### namespaceSignature

[`NamespaceSignature`](NamespaceSignature.md)

#### Returns

`null` \| `ArkNamespace`

***

### getNamespaces()

> **getNamespaces**(): `ArkNamespace`[]

Defined in: src/core/model/ArkNamespace.ts:74

#### Returns

`ArkNamespace`[]

***

### getNamespaceSignature()

> **getNamespaceSignature**(): [`NamespaceSignature`](NamespaceSignature.md)

Defined in: src/core/model/ArkNamespace.ts:86

#### Returns

[`NamespaceSignature`](NamespaceSignature.md)

***

### getNamespaceWithName()

> **getNamespaceWithName**(`namespaceName`): `null` \| `ArkNamespace`

Defined in: src/core/model/ArkNamespace.ts:70

#### Parameters

##### namespaceName

`string`

#### Returns

`null` \| `ArkNamespace`

***

### getSignature()

> **getSignature**(): [`NamespaceSignature`](NamespaceSignature.md)

Defined in: src/core/model/ArkNamespace.ts:82

#### Returns

[`NamespaceSignature`](NamespaceSignature.md)

#### Implementation of

`ArkExport.getSignature`

***

### getStateDecorators()

> **getStateDecorators**(): [`Decorator`](Decorator.md)[]

Defined in: src/core/model/ArkBaseModel.ts:234

#### Returns

[`Decorator`](Decorator.md)[]

#### Inherited from

`ArkBaseModel.getStateDecorators`

***

### hasBuilderDecorator()

> **hasBuilderDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:230

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasBuilderDecorator`

***

### hasBuilderParamDecorator()

> **hasBuilderParamDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:243

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasBuilderParamDecorator`

***

### hasComponentDecorator()

> **hasComponentDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:251

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasComponentDecorator`

***

### hasDecorator()

> **hasDecorator**(`kind`): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:255

#### Parameters

##### kind

`string` | `Set`\<`string`\>

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasDecorator`

***

### hasEntryDecorator()

> **hasEntryDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:247

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasEntryDecorator`

***

### isAbstract()

> **isAbstract**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:173

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isAbstract`

***

### isDeclare()

> **isDeclare**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:190

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isDeclare`

***

### isDefault()

> **isDefault**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:181

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isDefault`

***

### isExport()

> **isExport**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:177

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isExport`

***

### ~~isExported()~~

> **isExported**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:186

#### Returns

`boolean`

#### Deprecated

Use [isExport](#isexport) instead.

#### Inherited from

`ArkBaseModel.isExported`

***

### isPrivate()

> **isPrivate**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:161

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isPrivate`

***

### isProtected()

> **isProtected**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:157

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isProtected`

***

### isPublic()

> **isPublic**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:165

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isPublic`

***

### isReadonly()

> **isReadonly**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:169

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isReadonly`

***

### isStatic()

> **isStatic**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:153

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isStatic`

***

### removeArkClass()

> **removeArkClass**(`arkClass`): `boolean`

Defined in: src/core/model/ArkNamespace.ts:256

#### Parameters

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`boolean`

***

### removeDecorator()

> **removeDecorator**(`kind`): `void`

Defined in: src/core/model/ArkBaseModel.ts:222

#### Parameters

##### kind

`string`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.removeDecorator`

***

### removeModifier()

> **removeModifier**(`modifier`): `void`

Defined in: src/core/model/ArkBaseModel.ts:146

#### Parameters

##### modifier

`ModifierType`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.removeModifier`

***

### removeNamespace()

> **removeNamespace**(`namespace`): `boolean`

Defined in: src/core/model/ArkNamespace.ts:262

#### Parameters

##### namespace

`ArkNamespace`

#### Returns

`boolean`

***

### setCode()

> **setCode**(`sourceCode`): `void`

Defined in: src/core/model/ArkNamespace.ts:98

#### Parameters

##### sourceCode

`string`

#### Returns

`void`

***

### setCodes()

> **setCodes**(`sourceCodes`): `void`

Defined in: src/core/model/ArkNamespace.ts:112

#### Parameters

##### sourceCodes

`string`[]

#### Returns

`void`

***

### setColumn()

> **setColumn**(`column`): `void`

Defined in: src/core/model/ArkNamespace.ts:133

#### Parameters

##### column

`number`

#### Returns

`void`

***

### setDeclaringArkFile()

> **setDeclaringArkFile**(`declaringArkFile`): `void`

Defined in: src/core/model/ArkNamespace.ts:164

#### Parameters

##### declaringArkFile

[`ArkFile`](ArkFile.md)

#### Returns

`void`

***

### setDeclaringArkNamespace()

> **setDeclaringArkNamespace**(`declaringArkNamespace`): `void`

Defined in: src/core/model/ArkNamespace.ts:172

#### Parameters

##### declaringArkNamespace

`ArkNamespace`

#### Returns

`void`

***

### setDeclaringInstance()

> **setDeclaringInstance**(`declaringInstance`): `void`

Defined in: src/core/model/ArkNamespace.ts:156

#### Parameters

##### declaringInstance

[`ArkFile`](ArkFile.md) | `ArkNamespace`

#### Returns

`void`

***

### setDecorators()

> **setDecorators**(`decorators`): `void`

Defined in: src/core/model/ArkBaseModel.ts:209

#### Parameters

##### decorators

`Set`\<[`Decorator`](Decorator.md)\>

#### Returns

`void`

#### Inherited from

`ArkBaseModel.setDecorators`

***

### setDefaultClass()

> **setDefaultClass**(`defaultClass`): `void`

Defined in: src/core/model/ArkNamespace.ts:215

#### Parameters

##### defaultClass

[`ArkClass`](ArkClass.md)

#### Returns

`void`

***

### setLine()

> **setLine**(`line`): `void`

Defined in: src/core/model/ArkNamespace.ts:125

#### Parameters

##### line

`number`

#### Returns

`void`

***

### setLineCols()

> **setLineCols**(`lineColPairs`): `void`

Defined in: src/core/model/ArkNamespace.ts:145

#### Parameters

##### lineColPairs

\[`number`, `number`\][]

#### Returns

`void`

***

### setMetadata()

> **setMetadata**(`kind`, `value`): `void`

Defined in: src/core/model/ArkBaseModel.ts:122

#### Parameters

##### kind

`ArkMetadataKind`

##### value

`ArkMetadataType`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.setMetadata`

***

### setModifiers()

> **setModifiers**(`modifiers`): `void`

Defined in: src/core/model/ArkBaseModel.ts:136

#### Parameters

##### modifiers

`number`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.setModifiers`

***

### setSignature()

> **setSignature**(`namespaceSignature`): `void`

Defined in: src/core/model/ArkNamespace.ts:78

#### Parameters

##### namespaceSignature

[`NamespaceSignature`](NamespaceSignature.md)

#### Returns

`void`

***

### validate()

> **validate**(): `ArkError`

Defined in: src/core/model/ArkNamespace.ts:268

#### Returns

`ArkError`

#### Overrides

`ArkBaseModel.validate`

***

### validateFields()

> `protected` **validateFields**(`fields`): `ArkError`

Defined in: src/core/model/ArkBaseModel.ts:267

#### Parameters

##### fields

`string`[]

#### Returns

`ArkError`

#### Inherited from

`ArkBaseModel.validateFields`




============================================================
## FILE: `classes/ArkNewArrayExpr.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkNewArrayExpr

# Class: ArkNewArrayExpr

Defined in: src/core/base/Expr.ts:372

## Extends

- [`AbstractExpr`](AbstractExpr.md)

## Constructors

### Constructor

> **new ArkNewArrayExpr**(`baseType`, `size`, `fromLiteral`): `ArkNewArrayExpr`

Defined in: src/core/base/Expr.ts:378

#### Parameters

##### baseType

[`Type`](Type.md)

##### size

[`Value`](../interfaces/Value.md)

##### fromLiteral

`boolean` = `false`

#### Returns

`ArkNewArrayExpr`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`constructor`](AbstractExpr.md#constructor)

## Methods

### getBaseType()

> **getBaseType**(): [`Type`](Type.md)

Defined in: src/core/base/Expr.ts:397

#### Returns

[`Type`](Type.md)

***

### getSize()

> **getSize**(): [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Expr.ts:385

#### Returns

[`Value`](../interfaces/Value.md)

***

### getType()

> **getType**(): [`ArrayType`](ArrayType.md)

Defined in: src/core/base/Expr.ts:393

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`ArrayType`](ArrayType.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`getType`](AbstractExpr.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Expr.ts:417

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`getUses`](AbstractExpr.md#getuses)

***

### inferType()

> **inferType**(`arkMethod`): `ArkNewArrayExpr`

Defined in: src/core/base/Expr.ts:409

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

`ArkNewArrayExpr`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`inferType`](AbstractExpr.md#infertype)

***

### isFromLiteral()

> **isFromLiteral**(): `boolean`

Defined in: src/core/base/Expr.ts:405

#### Returns

`boolean`

***

### setBaseType()

> **setBaseType**(`newType`): `void`

Defined in: src/core/base/Expr.ts:401

#### Parameters

##### newType

[`Type`](Type.md)

#### Returns

`void`

***

### setSize()

> **setSize**(`newSize`): `void`

Defined in: src/core/base/Expr.ts:389

#### Parameters

##### newSize

[`Value`](../interfaces/Value.md)

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Expr.ts:423

Returns a string representation of an object.

#### Returns

`string`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`toString`](AbstractExpr.md#tostring)




============================================================
## FILE: `classes/ArkNewExpr.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkNewExpr

# Class: ArkNewExpr

Defined in: src/core/base/Expr.ts:318

## Extends

- [`AbstractExpr`](AbstractExpr.md)

## Constructors

### Constructor

> **new ArkNewExpr**(`classType`): `ArkNewExpr`

Defined in: src/core/base/Expr.ts:321

#### Parameters

##### classType

[`ClassType`](ClassType.md)

#### Returns

`ArkNewExpr`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`constructor`](AbstractExpr.md#constructor)

## Methods

### getClassType()

> **getClassType**(): [`ClassType`](ClassType.md)

Defined in: src/core/base/Expr.ts:326

#### Returns

[`ClassType`](ClassType.md)

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Expr.ts:334

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`Type`](Type.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`getType`](AbstractExpr.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Expr.ts:330

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`getUses`](AbstractExpr.md#getuses)

***

### inferType()

> **inferType**(`arkMethod`): `ArkNewExpr`

Defined in: src/core/base/Expr.ts:342

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

`ArkNewExpr`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`inferType`](AbstractExpr.md#infertype)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Expr.ts:338

Returns a string representation of an object.

#### Returns

`string`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`toString`](AbstractExpr.md#tostring)




============================================================
## FILE: `classes/ArkNormalBinopExpr.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkNormalBinopExpr

# Class: ArkNormalBinopExpr

Defined in: src/core/base/Expr.ts:767

## Extends

- [`AbstractBinopExpr`](AbstractBinopExpr.md)

## Constructors

### Constructor

> **new ArkNormalBinopExpr**(`op1`, `op2`, `operator`): `ArkNormalBinopExpr`

Defined in: src/core/base/Expr.ts:768

#### Parameters

##### op1

[`Value`](../interfaces/Value.md)

##### op2

[`Value`](../interfaces/Value.md)

##### operator

[`NormalBinaryOperator`](../enumerations/NormalBinaryOperator.md)

#### Returns

`ArkNormalBinopExpr`

#### Overrides

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`constructor`](AbstractBinopExpr.md#constructor)

## Properties

### op1

> `protected` **op1**: [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Expr.ts:580

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`op1`](AbstractBinopExpr.md#op1)

***

### op2

> `protected` **op2**: [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Expr.ts:581

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`op2`](AbstractBinopExpr.md#op2)

***

### operator

> `protected` **operator**: [`BinaryOperator`](../type-aliases/BinaryOperator.md)

Defined in: src/core/base/Expr.ts:582

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`operator`](AbstractBinopExpr.md#operator)

***

### type

> `protected` **type**: [`Type`](Type.md)

Defined in: src/core/base/Expr.ts:584

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`type`](AbstractBinopExpr.md#type)

## Methods

### getOp1()

> **getOp1**(): [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Expr.ts:598

Returns the first operand in the binary operation expression.
For example, the first operand in `a + b;` is `a`.

#### Returns

[`Value`](../interfaces/Value.md)

The first operand in the binary operation expression.

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`getOp1`](AbstractBinopExpr.md#getop1)

***

### getOp2()

> **getOp2**(): [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Expr.ts:611

Returns the second operand in the binary operation expression.
For example, the second operand in `a + b;` is `b`.

#### Returns

[`Value`](../interfaces/Value.md)

The second operand in the binary operation expression.

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`getOp2`](AbstractBinopExpr.md#getop2)

***

### getOperator()

> **getOperator**(): [`BinaryOperator`](../type-aliases/BinaryOperator.md)

Defined in: src/core/base/Expr.ts:634

Get the binary operator from the statement.
The binary operator can be divided into two categories,
one is the normal binary operator and the other is relational binary operator.

#### Returns

[`BinaryOperator`](../type-aliases/BinaryOperator.md)

The binary operator from the statement.

#### Example

```typescript
if (expr instanceof AbstractBinopExpr) {
let op1: Value = expr.getOp1();
let op2: Value = expr.getOp2();
let operator: string = expr.getOperator();
... ...
}
```

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`getOperator`](AbstractBinopExpr.md#getoperator)

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Expr.ts:638

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`Type`](Type.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`getType`](AbstractBinopExpr.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Expr.ts:645

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`getUses`](AbstractBinopExpr.md#getuses)

***

### inferOpType()

> `protected` **inferOpType**(`op`, `arkMethod`): `void`

Defined in: src/core/base/Expr.ts:658

#### Parameters

##### op

[`Value`](../interfaces/Value.md)

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

`void`

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`inferOpType`](AbstractBinopExpr.md#inferoptype)

***

### inferType()

> **inferType**(`arkMethod`): [`AbstractBinopExpr`](AbstractBinopExpr.md)

Defined in: src/core/base/Expr.ts:735

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

[`AbstractBinopExpr`](AbstractBinopExpr.md)

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`inferType`](AbstractBinopExpr.md#infertype)

***

### setOp1()

> **setOp1**(`newOp1`): `void`

Defined in: src/core/base/Expr.ts:602

#### Parameters

##### newOp1

[`Value`](../interfaces/Value.md)

#### Returns

`void`

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`setOp1`](AbstractBinopExpr.md#setop1)

***

### setOp2()

> **setOp2**(`newOp2`): `void`

Defined in: src/core/base/Expr.ts:615

#### Parameters

##### newOp2

[`Value`](../interfaces/Value.md)

#### Returns

`void`

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`setOp2`](AbstractBinopExpr.md#setop2)

***

### setType()

> `protected` **setType**(): `void`

Defined in: src/core/base/Expr.ts:664

#### Returns

`void`

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`setType`](AbstractBinopExpr.md#settype)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Expr.ts:654

Returns a string representation of an object.

#### Returns

`string`

#### Inherited from

[`AbstractBinopExpr`](AbstractBinopExpr.md).[`toString`](AbstractBinopExpr.md#tostring)




============================================================
## FILE: `classes/ArkParameterRef.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkParameterRef

# Class: ArkParameterRef

Defined in: src/core/base/Ref.ts:235

## Extends

- [`AbstractRef`](AbstractRef.md)

## Constructors

### Constructor

> **new ArkParameterRef**(`index`, `paramType`): `ArkParameterRef`

Defined in: src/core/base/Ref.ts:239

#### Parameters

##### index

`number`

##### paramType

[`Type`](Type.md)

#### Returns

`ArkParameterRef`

#### Overrides

[`AbstractRef`](AbstractRef.md).[`constructor`](AbstractRef.md#constructor)

## Methods

### getIndex()

> **getIndex**(): `number`

Defined in: src/core/base/Ref.ts:245

#### Returns

`number`

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Ref.ts:253

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`Type`](Type.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Overrides

[`AbstractRef`](AbstractRef.md).[`getType`](AbstractRef.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Ref.ts:265

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Overrides

[`AbstractRef`](AbstractRef.md).[`getUses`](AbstractRef.md#getuses)

***

### inferType()

> **inferType**(`arkMethod`): [`AbstractRef`](AbstractRef.md)

Defined in: src/core/base/Ref.ts:261

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

[`AbstractRef`](AbstractRef.md)

#### Overrides

[`AbstractRef`](AbstractRef.md).[`inferType`](AbstractRef.md#infertype)

***

### setIndex()

> **setIndex**(`index`): `void`

Defined in: src/core/base/Ref.ts:249

#### Parameters

##### index

`number`

#### Returns

`void`

***

### setType()

> **setType**(`newType`): `void`

Defined in: src/core/base/Ref.ts:257

#### Parameters

##### newType

[`Type`](Type.md)

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Ref.ts:269

Returns a string representation of an object.

#### Returns

`string`




============================================================
## FILE: `classes/ArkPhiExpr.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkPhiExpr

# Class: ArkPhiExpr

Defined in: src/core/base/Expr.ts:907

## Extends

- [`AbstractExpr`](AbstractExpr.md)

## Constructors

### Constructor

> **new ArkPhiExpr**(): `ArkPhiExpr`

Defined in: src/core/base/Expr.ts:911

#### Returns

`ArkPhiExpr`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`constructor`](AbstractExpr.md#constructor)

## Methods

### getArgs()

> **getArgs**(): [`Local`](Local.md)[]

Defined in: src/core/base/Expr.ts:923

#### Returns

[`Local`](Local.md)[]

***

### getArgToBlock()

> **getArgToBlock**(): `Map`\<[`Local`](Local.md), [`BasicBlock`](BasicBlock.md)\>

Defined in: src/core/base/Expr.ts:931

#### Returns

`Map`\<[`Local`](Local.md), [`BasicBlock`](BasicBlock.md)\>

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Expr.ts:939

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`Type`](Type.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`getType`](AbstractExpr.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Expr.ts:917

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`getUses`](AbstractExpr.md#getuses)

***

### inferType()

> **inferType**(`arkMethod`): [`AbstractExpr`](AbstractExpr.md)

Defined in: src/core/base/Expr.ts:57

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

[`AbstractExpr`](AbstractExpr.md)

#### Inherited from

[`AbstractExpr`](AbstractExpr.md).[`inferType`](AbstractExpr.md#infertype)

***

### setArgs()

> **setArgs**(`args`): `void`

Defined in: src/core/base/Expr.ts:927

#### Parameters

##### args

[`Local`](Local.md)[]

#### Returns

`void`

***

### setArgToBlock()

> **setArgToBlock**(`argToBlock`): `void`

Defined in: src/core/base/Expr.ts:935

#### Parameters

##### argToBlock

`Map`\<[`Local`](Local.md), [`BasicBlock`](BasicBlock.md)\>

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Expr.ts:943

Returns a string representation of an object.

#### Returns

`string`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`toString`](AbstractExpr.md#tostring)




============================================================
## FILE: `classes/ArkPtrInvokeExpr.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkPtrInvokeExpr

# Class: ArkPtrInvokeExpr

Defined in: src/core/base/Expr.ts:267

1. Local PtrInvokeExpr

     ```typescript
     func foo():void {
     }
     let ptr = foo;
     ptr();
     ```
    2. FieldRef PtrInvokeExpr

     ```typescript
     class A {
         b:()=> void()
     }
     new A().b()
     ```

## Extends

- [`AbstractInvokeExpr`](AbstractInvokeExpr.md)

## Constructors

### Constructor

> **new ArkPtrInvokeExpr**(`methodSignature`, `ptr`, `args`, `realGenericTypes?`): `ArkPtrInvokeExpr`

Defined in: src/core/base/Expr.ts:270

#### Parameters

##### methodSignature

[`MethodSignature`](MethodSignature.md)

##### ptr

[`Local`](Local.md) | [`AbstractFieldRef`](AbstractFieldRef.md)

##### args

[`Value`](../interfaces/Value.md)[]

##### realGenericTypes?

[`Type`](Type.md)[]

#### Returns

`ArkPtrInvokeExpr`

#### Overrides

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`constructor`](AbstractInvokeExpr.md#constructor)

## Methods

### getArg()

> **getArg**(`index`): [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Expr.ts:101

Returns an argument used in the expression according to its index.

#### Parameters

##### index

`number`

the index of the argument.

#### Returns

[`Value`](../interfaces/Value.md)

An argument used in the expression.

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`getArg`](AbstractInvokeExpr.md#getarg)

***

### getArgs()

> **getArgs**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Expr.ts:127

Returns an **array** of arguments used in the expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of arguments used in the expression.

#### Example

1. get args number.

```typescript
const argsNum = expr.getArgs().length;
if (argsNum < 5) {
... ...
}
```

2. iterate arg based on expression

```typescript
for (const arg of this.getArgs()) {
strs.push(arg.toString());
strs.push(', ');
}
```

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`getArgs`](AbstractInvokeExpr.md#getargs)

***

### getFuncPtrLocal()

> **getFuncPtrLocal**(): [`Local`](Local.md) \| [`AbstractFieldRef`](AbstractFieldRef.md)

Defined in: src/core/base/Expr.ts:279

#### Returns

[`Local`](Local.md) \| [`AbstractFieldRef`](AbstractFieldRef.md)

***

### getMethodSignature()

> **getMethodSignature**(): [`MethodSignature`](MethodSignature.md)

Defined in: src/core/base/Expr.ts:88

Get method Signature. The method signature is consist of ClassSignature and MethodSubSignature.
It is the unique flag of a method. It is usually used to compose a expression string in ArkIRTransformer.

#### Returns

[`MethodSignature`](MethodSignature.md)

The class method signature, such as ArkStaticInvokeExpr.

#### Example

1. 3AC information composed of getMethodSignature ().

```typescript
let strs: string[] = [];
strs.push('staticinvoke <');
strs.push(this.getMethodSignature().toString());
strs.push('>(');
```

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`getMethodSignature`](AbstractInvokeExpr.md#getmethodsignature)

***

### getRealGenericTypes()

> **getRealGenericTypes**(): `undefined` \| [`Type`](Type.md)[]

Defined in: src/core/base/Expr.ts:143

#### Returns

`undefined` \| [`Type`](Type.md)[]

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`getRealGenericTypes`](AbstractInvokeExpr.md#getrealgenerictypes)

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Expr.ts:135

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`Type`](Type.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`getType`](AbstractInvokeExpr.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Expr.ts:307

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Overrides

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`getUses`](AbstractInvokeExpr.md#getuses)

***

### inferType()

> **inferType**(`arkMethod`): [`AbstractExpr`](AbstractExpr.md)

Defined in: src/core/base/Expr.ts:57

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

[`AbstractExpr`](AbstractExpr.md)

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`inferType`](AbstractInvokeExpr.md#infertype)

***

### setArgs()

> **setArgs**(`newArgs`): `void`

Defined in: src/core/base/Expr.ts:131

#### Parameters

##### newArgs

[`Value`](../interfaces/Value.md)[]

#### Returns

`void`

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`setArgs`](AbstractInvokeExpr.md#setargs)

***

### setFunPtrLocal()

> **setFunPtrLocal**(`ptr`): `void`

Defined in: src/core/base/Expr.ts:275

#### Parameters

##### ptr

[`Local`](Local.md) | [`AbstractFieldRef`](AbstractFieldRef.md)

#### Returns

`void`

***

### setMethodSignature()

> **setMethodSignature**(`newMethodSignature`): `void`

Defined in: src/core/base/Expr.ts:92

#### Parameters

##### newMethodSignature

[`MethodSignature`](MethodSignature.md)

#### Returns

`void`

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`setMethodSignature`](AbstractInvokeExpr.md#setmethodsignature)

***

### setRealGenericTypes()

> **setRealGenericTypes**(`realTypes`): `void`

Defined in: src/core/base/Expr.ts:147

#### Parameters

##### realTypes

`undefined` | [`Type`](Type.md)[]

#### Returns

`void`

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`setRealGenericTypes`](AbstractInvokeExpr.md#setrealgenerictypes)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Expr.ts:283

Returns a string representation of an object.

#### Returns

`string`

#### Overrides

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`toString`](AbstractInvokeExpr.md#tostring)




============================================================
## FILE: `classes/ArkReturnStmt.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkReturnStmt

# Class: ArkReturnStmt

Defined in: src/core/base/Stmt.ts:455

## Extends

- [`Stmt`](Stmt.md)

## Constructors

### Constructor

> **new ArkReturnStmt**(`op`): `ArkReturnStmt`

Defined in: src/core/base/Stmt.ts:458

#### Parameters

##### op

[`Value`](../interfaces/Value.md)

#### Returns

`ArkReturnStmt`

#### Overrides

[`Stmt`](Stmt.md).[`constructor`](Stmt.md#constructor)

## Properties

### cfg

> `protected` **cfg**: [`Cfg`](Cfg.md)

Defined in: src/core/base/Stmt.ts:36

#### Inherited from

[`Stmt`](Stmt.md).[`cfg`](Stmt.md#cfg)

***

### metadata?

> `optional` **metadata**: `ArkMetadata`

Defined in: src/core/base/Stmt.ts:39

#### Inherited from

[`Stmt`](Stmt.md).[`metadata`](Stmt.md#metadata)

***

### operandOriginalPositions?

> `protected` `optional` **operandOriginalPositions**: [`FullPosition`](FullPosition.md)[]

Defined in: src/core/base/Stmt.ts:37

#### Inherited from

[`Stmt`](Stmt.md).[`operandOriginalPositions`](Stmt.md#operandoriginalpositions)

***

### originalPosition

> `protected` **originalPosition**: [`LineColPosition`](LineColPosition.md) = `LineColPosition.DEFAULT`

Defined in: src/core/base/Stmt.ts:35

#### Inherited from

[`Stmt`](Stmt.md).[`originalPosition`](Stmt.md#originalposition)

***

### originalText?

> `protected` `optional` **originalText**: `string`

Defined in: src/core/base/Stmt.ts:34

#### Inherited from

[`Stmt`](Stmt.md).[`originalText`](Stmt.md#originaltext)

***

### text?

> `protected` `optional` **text**: `string`

Defined in: src/core/base/Stmt.ts:33

#### Inherited from

[`Stmt`](Stmt.md).[`text`](Stmt.md#text)

## Methods

### containsArrayRef()

> **containsArrayRef**(): `boolean`

Defined in: src/core/base/Stmt.ts:199

#### Returns

`boolean`

#### Inherited from

[`Stmt`](Stmt.md).[`containsArrayRef`](Stmt.md#containsarrayref)

***

### containsFieldRef()

> **containsFieldRef**(): `boolean`

Defined in: src/core/base/Stmt.ts:225

#### Returns

`boolean`

#### Inherited from

[`Stmt`](Stmt.md).[`containsFieldRef`](Stmt.md#containsfieldref)

***

### containsInvokeExpr()

> **containsInvokeExpr**(): `boolean`

Defined in: src/core/base/Stmt.ts:137

#### Returns

`boolean`

#### Inherited from

[`Stmt`](Stmt.md).[`containsInvokeExpr`](Stmt.md#containsinvokeexpr)

***

### getArrayRef()

> **getArrayRef**(): `undefined` \| [`ArkArrayRef`](ArkArrayRef.md)

Defined in: src/core/base/Stmt.ts:211

#### Returns

`undefined` \| [`ArkArrayRef`](ArkArrayRef.md)

#### Inherited from

[`Stmt`](Stmt.md).[`getArrayRef`](Stmt.md#getarrayref)

***

### getCfg()

> **getCfg**(): [`Cfg`](Cfg.md)

Defined in: src/core/base/Stmt.ts:116

Get the CFG (i.e., control flow graph) of an [ArkBody](ArkBody.md) in which the statement is.
A CFG contains a set of basic blocks and statements corresponding to each basic block.
Note that, "source code" and "three-address" are two types of [Stmt](Stmt.md) in ArkAnalyzer.
Source code [Stmt](Stmt.md) represents the statement of ets/ts source code, while three-address code [Stmt](Stmt.md)
represents the statement after it has been converted into three-address code.  Since the source code [Stmt](Stmt.md) does not save its CFG reference, it returns **null**, while the `getCfg()` of the third address code
[Stmt](Stmt.md) will return its CFG reference.

#### Returns

[`Cfg`](Cfg.md)

The CFG (i.e., control flow graph) of an [ArkBody](ArkBody.md) in which the statement is.

#### Example

1. get the ArkFile based on stmt.
```typescript
const arkFile = stmt.getCfg()?.getDeclaringMethod().getDeclaringArkFile();
```
2. get the ArkMethod based on stmt.
```typescript
let sourceMethod: ArkMethod = stmt.getCfg()?.getDeclaringMethod();
```

#### Inherited from

[`Stmt`](Stmt.md).[`getCfg`](Stmt.md#getcfg)

***

### getDef()

> **getDef**(): `null` \| [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Stmt.ts:78

Return the definition which is uesd in this statement. Generally, the definition is the left value of `=` in
3AC.  For example, the definition in 3AC of `value = parameter0: @project-1/sample-1.ets: AnonymousClass-0` is
`value`,  and the definition in `$temp0 = staticinvoke <@_ProjectName/_FileName: xxx.create()>()` is `\$temp0`.

#### Returns

`null` \| [`Value`](../interfaces/Value.md)

The definition in 3AC (may be a **null**).

#### Example

1. get the def in stmt.
```typescript
for (const block of this.blocks) {
for (const stmt of block.getStmts()) {
   const defValue = stmt.getDef();
   ...
   }
}
```

#### Inherited from

[`Stmt`](Stmt.md).[`getDef`](Stmt.md#getdef)

***

### getDefAndUses()

> **getDefAndUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Stmt.ts:87

#### Returns

[`Value`](../interfaces/Value.md)[]

#### Inherited from

[`Stmt`](Stmt.md).[`getDefAndUses`](Stmt.md#getdefanduses)

***

### getExpectedSuccessorCount()

> **getExpectedSuccessorCount**(): `number`

Defined in: src/core/base/Stmt.ts:463

Return the number of statements which this statement may go to

#### Returns

`number`

#### Overrides

[`Stmt`](Stmt.md).[`getExpectedSuccessorCount`](Stmt.md#getexpectedsuccessorcount)

***

### getExprs()

> **getExprs**(): [`AbstractExpr`](AbstractExpr.md)[]

Defined in: src/core/base/Stmt.ts:178

Returns an array of expressions in the statement.

#### Returns

[`AbstractExpr`](AbstractExpr.md)[]

An array of expressions in the statement.

#### Example

1. Traverse expression of statement.

```typescript
for (const expr of stmt.getExprs()) {
   ...
}
```

#### Inherited from

[`Stmt`](Stmt.md).[`getExprs`](Stmt.md#getexprs)

***

### getFieldRef()

> **getFieldRef**(): `undefined` \| [`AbstractFieldRef`](AbstractFieldRef.md)

Defined in: src/core/base/Stmt.ts:238

#### Returns

`undefined` \| [`AbstractFieldRef`](AbstractFieldRef.md)

#### Inherited from

[`Stmt`](Stmt.md).[`getFieldRef`](Stmt.md#getfieldref)

***

### getInvokeExpr()

> **getInvokeExpr**(): `undefined` \| [`AbstractInvokeExpr`](AbstractInvokeExpr.md)

Defined in: src/core/base/Stmt.ts:157

Returns the method's invocation expression (including method signature and its arguments) 
in the current statement. An **undefined** will be returned if there is no method used in this statement.

#### Returns

`undefined` \| [`AbstractInvokeExpr`](AbstractInvokeExpr.md)

the method's invocation expression from the statement. An **undefined** will be returned if there is
    no method can be found in this statement.

#### Example

1. get invoke expr based on stmt.
```typescript
let invoke = stmt.getInvokeExpr();
```

#### Inherited from

[`Stmt`](Stmt.md).[`getInvokeExpr`](Stmt.md#getinvokeexpr)

***

### getMetadata()

> **getMetadata**(`kind`): `undefined` \| `ArkMetadataType`

Defined in: src/core/base/Stmt.ts:41

#### Parameters

##### kind

`ArkMetadataKind`

#### Returns

`undefined` \| `ArkMetadataType`

#### Inherited from

[`Stmt`](Stmt.md).[`getMetadata`](Stmt.md#getmetadata)

***

### getOp()

> **getOp**(): [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Stmt.ts:467

#### Returns

[`Value`](../interfaces/Value.md)

***

### getOperandOriginalPosition()

> **getOperandOriginalPosition**(`indexOrOperand`): `null` \| [`FullPosition`](FullPosition.md)

Defined in: src/core/base/Stmt.ts:299

#### Parameters

##### indexOrOperand

`number` | [`Value`](../interfaces/Value.md)

#### Returns

`null` \| [`FullPosition`](FullPosition.md)

#### Inherited from

[`Stmt`](Stmt.md).[`getOperandOriginalPosition`](Stmt.md#getoperandoriginalposition)

***

### getOperandOriginalPositions()

> **getOperandOriginalPositions**(): `undefined` \| [`FullPosition`](FullPosition.md)[]

Defined in: src/core/base/Stmt.ts:295

#### Returns

`undefined` \| [`FullPosition`](FullPosition.md)[]

#### Inherited from

[`Stmt`](Stmt.md).[`getOperandOriginalPositions`](Stmt.md#getoperandoriginalpositions)

***

### getOriginalText()

> **getOriginalText**(): `undefined` \| `string`

Defined in: src/core/base/Stmt.ts:287

#### Returns

`undefined` \| `string`

#### Inherited from

[`Stmt`](Stmt.md).[`getOriginalText`](Stmt.md#getoriginaltext)

***

### getOriginPositionInfo()

> **getOriginPositionInfo**(): [`LineColPosition`](LineColPosition.md)

Defined in: src/core/base/Stmt.ts:273

Returns the original position of the statement. 
The position consists of two parts: line number and column number. 
In the source file, the former (i.e., line number) indicates which line the statement is in, 
and the latter (i.e., column number) indicates the position of the statement in the line. 
The position is described as `LineColPosition(lineNo,colNum)` in ArkAnalyzer, 
and its default value is LineColPosition(-1,-1).

#### Returns

[`LineColPosition`](LineColPosition.md)

The original location of the statement.

#### Example

1. Get the stmt position info to make some condition judgements.
```typescript
for (const stmt of stmts) {
   if (stmt.getOriginPositionInfo().getLineNo() === -1) {
       stmt.setOriginPositionInfo(originalStmt.getOriginPositionInfo());
       this.stmtToOriginalStmt.set(stmt, originalStmt);
   }
}
```

#### Inherited from

[`Stmt`](Stmt.md).[`getOriginPositionInfo`](Stmt.md#getoriginpositioninfo)

***

### getTypeExprs()

> **getTypeExprs**(): `AbstractTypeExpr`[]

Defined in: src/core/base/Stmt.ts:188

#### Returns

`AbstractTypeExpr`[]

#### Inherited from

[`Stmt`](Stmt.md).[`getTypeExprs`](Stmt.md#gettypeexprs)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Stmt.ts:480

Return a list of values which are uesd in this statement

#### Returns

[`Value`](../interfaces/Value.md)[]

#### Overrides

[`Stmt`](Stmt.md).[`getUses`](Stmt.md#getuses)

***

### isBranch()

> **isBranch**(): `boolean`

Defined in: src/core/base/Stmt.ts:128

Return true if the following statement may not execute after this statement.
The ArkIfStmt and ArkGotoStmt will return true.

#### Returns

`boolean`

#### Inherited from

[`Stmt`](Stmt.md).[`isBranch`](Stmt.md#isbranch)

***

### replaceDef()

> **replaceDef**(`oldDef`, `newDef`): `void`

Defined in: src/core/base/Stmt.ts:82

#### Parameters

##### oldDef

[`Value`](../interfaces/Value.md)

##### newDef

[`Value`](../interfaces/Value.md)

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`replaceDef`](Stmt.md#replacedef)

***

### replaceUse()

> **replaceUse**(`oldUse`, `newUse`): `void`

Defined in: src/core/base/Stmt.ts:57

#### Parameters

##### oldUse

[`Value`](../interfaces/Value.md)

##### newUse

[`Value`](../interfaces/Value.md)

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`replaceUse`](Stmt.md#replaceuse)

***

### setCfg()

> **setCfg**(`cfg`): `void`

Defined in: src/core/base/Stmt.ts:120

#### Parameters

##### cfg

[`Cfg`](Cfg.md)

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setCfg`](Stmt.md#setcfg)

***

### setMetadata()

> **setMetadata**(`kind`, `value`): `void`

Defined in: src/core/base/Stmt.ts:45

#### Parameters

##### kind

`ArkMetadataKind`

##### value

`ArkMetadataType`

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setMetadata`](Stmt.md#setmetadata)

***

### setOperandOriginalPositions()

> **setOperandOriginalPositions**(`operandOriginalPositions`): `void`

Defined in: src/core/base/Stmt.ts:291

#### Parameters

##### operandOriginalPositions

[`FullPosition`](FullPosition.md)[]

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setOperandOriginalPositions`](Stmt.md#setoperandoriginalpositions)

***

### setOriginalText()

> **setOriginalText**(`originalText`): `void`

Defined in: src/core/base/Stmt.ts:283

#### Parameters

##### originalText

`string`

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setOriginalText`](Stmt.md#setoriginaltext)

***

### setOriginPositionInfo()

> **setOriginPositionInfo**(`originPositionInfo`): `void`

Defined in: src/core/base/Stmt.ts:250

#### Parameters

##### originPositionInfo

[`LineColPosition`](LineColPosition.md)

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setOriginPositionInfo`](Stmt.md#setoriginpositioninfo)

***

### setReturnValue()

> **setReturnValue**(`returnValue`): `void`

Defined in: src/core/base/Stmt.ts:471

#### Parameters

##### returnValue

[`Value`](../interfaces/Value.md)

#### Returns

`void`

***

### setText()

> **setText**(`text`): `void`

Defined in: src/core/base/Stmt.ts:279

#### Parameters

##### text

`string`

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setText`](Stmt.md#settext)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Stmt.ts:475

#### Returns

`string`

#### Overrides

[`Stmt`](Stmt.md).[`toString`](Stmt.md#tostring)




============================================================
## FILE: `classes/ArkReturnVoidStmt.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkReturnVoidStmt

# Class: ArkReturnVoidStmt

Defined in: src/core/base/Stmt.ts:488

## Extends

- [`Stmt`](Stmt.md)

## Constructors

### Constructor

> **new ArkReturnVoidStmt**(): `ArkReturnVoidStmt`

Defined in: src/core/base/Stmt.ts:489

#### Returns

`ArkReturnVoidStmt`

#### Overrides

[`Stmt`](Stmt.md).[`constructor`](Stmt.md#constructor)

## Properties

### cfg

> `protected` **cfg**: [`Cfg`](Cfg.md)

Defined in: src/core/base/Stmt.ts:36

#### Inherited from

[`Stmt`](Stmt.md).[`cfg`](Stmt.md#cfg)

***

### metadata?

> `optional` **metadata**: `ArkMetadata`

Defined in: src/core/base/Stmt.ts:39

#### Inherited from

[`Stmt`](Stmt.md).[`metadata`](Stmt.md#metadata)

***

### operandOriginalPositions?

> `protected` `optional` **operandOriginalPositions**: [`FullPosition`](FullPosition.md)[]

Defined in: src/core/base/Stmt.ts:37

#### Inherited from

[`Stmt`](Stmt.md).[`operandOriginalPositions`](Stmt.md#operandoriginalpositions)

***

### originalPosition

> `protected` **originalPosition**: [`LineColPosition`](LineColPosition.md) = `LineColPosition.DEFAULT`

Defined in: src/core/base/Stmt.ts:35

#### Inherited from

[`Stmt`](Stmt.md).[`originalPosition`](Stmt.md#originalposition)

***

### originalText?

> `protected` `optional` **originalText**: `string`

Defined in: src/core/base/Stmt.ts:34

#### Inherited from

[`Stmt`](Stmt.md).[`originalText`](Stmt.md#originaltext)

***

### text?

> `protected` `optional` **text**: `string`

Defined in: src/core/base/Stmt.ts:33

#### Inherited from

[`Stmt`](Stmt.md).[`text`](Stmt.md#text)

## Methods

### containsArrayRef()

> **containsArrayRef**(): `boolean`

Defined in: src/core/base/Stmt.ts:199

#### Returns

`boolean`

#### Inherited from

[`Stmt`](Stmt.md).[`containsArrayRef`](Stmt.md#containsarrayref)

***

### containsFieldRef()

> **containsFieldRef**(): `boolean`

Defined in: src/core/base/Stmt.ts:225

#### Returns

`boolean`

#### Inherited from

[`Stmt`](Stmt.md).[`containsFieldRef`](Stmt.md#containsfieldref)

***

### containsInvokeExpr()

> **containsInvokeExpr**(): `boolean`

Defined in: src/core/base/Stmt.ts:137

#### Returns

`boolean`

#### Inherited from

[`Stmt`](Stmt.md).[`containsInvokeExpr`](Stmt.md#containsinvokeexpr)

***

### getArrayRef()

> **getArrayRef**(): `undefined` \| [`ArkArrayRef`](ArkArrayRef.md)

Defined in: src/core/base/Stmt.ts:211

#### Returns

`undefined` \| [`ArkArrayRef`](ArkArrayRef.md)

#### Inherited from

[`Stmt`](Stmt.md).[`getArrayRef`](Stmt.md#getarrayref)

***

### getCfg()

> **getCfg**(): [`Cfg`](Cfg.md)

Defined in: src/core/base/Stmt.ts:116

Get the CFG (i.e., control flow graph) of an [ArkBody](ArkBody.md) in which the statement is.
A CFG contains a set of basic blocks and statements corresponding to each basic block.
Note that, "source code" and "three-address" are two types of [Stmt](Stmt.md) in ArkAnalyzer.
Source code [Stmt](Stmt.md) represents the statement of ets/ts source code, while three-address code [Stmt](Stmt.md)
represents the statement after it has been converted into three-address code.  Since the source code [Stmt](Stmt.md) does not save its CFG reference, it returns **null**, while the `getCfg()` of the third address code
[Stmt](Stmt.md) will return its CFG reference.

#### Returns

[`Cfg`](Cfg.md)

The CFG (i.e., control flow graph) of an [ArkBody](ArkBody.md) in which the statement is.

#### Example

1. get the ArkFile based on stmt.
```typescript
const arkFile = stmt.getCfg()?.getDeclaringMethod().getDeclaringArkFile();
```
2. get the ArkMethod based on stmt.
```typescript
let sourceMethod: ArkMethod = stmt.getCfg()?.getDeclaringMethod();
```

#### Inherited from

[`Stmt`](Stmt.md).[`getCfg`](Stmt.md#getcfg)

***

### getDef()

> **getDef**(): `null` \| [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Stmt.ts:78

Return the definition which is uesd in this statement. Generally, the definition is the left value of `=` in
3AC.  For example, the definition in 3AC of `value = parameter0: @project-1/sample-1.ets: AnonymousClass-0` is
`value`,  and the definition in `$temp0 = staticinvoke <@_ProjectName/_FileName: xxx.create()>()` is `\$temp0`.

#### Returns

`null` \| [`Value`](../interfaces/Value.md)

The definition in 3AC (may be a **null**).

#### Example

1. get the def in stmt.
```typescript
for (const block of this.blocks) {
for (const stmt of block.getStmts()) {
   const defValue = stmt.getDef();
   ...
   }
}
```

#### Inherited from

[`Stmt`](Stmt.md).[`getDef`](Stmt.md#getdef)

***

### getDefAndUses()

> **getDefAndUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Stmt.ts:87

#### Returns

[`Value`](../interfaces/Value.md)[]

#### Inherited from

[`Stmt`](Stmt.md).[`getDefAndUses`](Stmt.md#getdefanduses)

***

### getExpectedSuccessorCount()

> **getExpectedSuccessorCount**(): `number`

Defined in: src/core/base/Stmt.ts:493

Return the number of statements which this statement may go to

#### Returns

`number`

#### Overrides

[`Stmt`](Stmt.md).[`getExpectedSuccessorCount`](Stmt.md#getexpectedsuccessorcount)

***

### getExprs()

> **getExprs**(): [`AbstractExpr`](AbstractExpr.md)[]

Defined in: src/core/base/Stmt.ts:178

Returns an array of expressions in the statement.

#### Returns

[`AbstractExpr`](AbstractExpr.md)[]

An array of expressions in the statement.

#### Example

1. Traverse expression of statement.

```typescript
for (const expr of stmt.getExprs()) {
   ...
}
```

#### Inherited from

[`Stmt`](Stmt.md).[`getExprs`](Stmt.md#getexprs)

***

### getFieldRef()

> **getFieldRef**(): `undefined` \| [`AbstractFieldRef`](AbstractFieldRef.md)

Defined in: src/core/base/Stmt.ts:238

#### Returns

`undefined` \| [`AbstractFieldRef`](AbstractFieldRef.md)

#### Inherited from

[`Stmt`](Stmt.md).[`getFieldRef`](Stmt.md#getfieldref)

***

### getInvokeExpr()

> **getInvokeExpr**(): `undefined` \| [`AbstractInvokeExpr`](AbstractInvokeExpr.md)

Defined in: src/core/base/Stmt.ts:157

Returns the method's invocation expression (including method signature and its arguments) 
in the current statement. An **undefined** will be returned if there is no method used in this statement.

#### Returns

`undefined` \| [`AbstractInvokeExpr`](AbstractInvokeExpr.md)

the method's invocation expression from the statement. An **undefined** will be returned if there is
    no method can be found in this statement.

#### Example

1. get invoke expr based on stmt.
```typescript
let invoke = stmt.getInvokeExpr();
```

#### Inherited from

[`Stmt`](Stmt.md).[`getInvokeExpr`](Stmt.md#getinvokeexpr)

***

### getMetadata()

> **getMetadata**(`kind`): `undefined` \| `ArkMetadataType`

Defined in: src/core/base/Stmt.ts:41

#### Parameters

##### kind

`ArkMetadataKind`

#### Returns

`undefined` \| `ArkMetadataType`

#### Inherited from

[`Stmt`](Stmt.md).[`getMetadata`](Stmt.md#getmetadata)

***

### getOperandOriginalPosition()

> **getOperandOriginalPosition**(`indexOrOperand`): `null` \| [`FullPosition`](FullPosition.md)

Defined in: src/core/base/Stmt.ts:299

#### Parameters

##### indexOrOperand

`number` | [`Value`](../interfaces/Value.md)

#### Returns

`null` \| [`FullPosition`](FullPosition.md)

#### Inherited from

[`Stmt`](Stmt.md).[`getOperandOriginalPosition`](Stmt.md#getoperandoriginalposition)

***

### getOperandOriginalPositions()

> **getOperandOriginalPositions**(): `undefined` \| [`FullPosition`](FullPosition.md)[]

Defined in: src/core/base/Stmt.ts:295

#### Returns

`undefined` \| [`FullPosition`](FullPosition.md)[]

#### Inherited from

[`Stmt`](Stmt.md).[`getOperandOriginalPositions`](Stmt.md#getoperandoriginalpositions)

***

### getOriginalText()

> **getOriginalText**(): `undefined` \| `string`

Defined in: src/core/base/Stmt.ts:287

#### Returns

`undefined` \| `string`

#### Inherited from

[`Stmt`](Stmt.md).[`getOriginalText`](Stmt.md#getoriginaltext)

***

### getOriginPositionInfo()

> **getOriginPositionInfo**(): [`LineColPosition`](LineColPosition.md)

Defined in: src/core/base/Stmt.ts:273

Returns the original position of the statement. 
The position consists of two parts: line number and column number. 
In the source file, the former (i.e., line number) indicates which line the statement is in, 
and the latter (i.e., column number) indicates the position of the statement in the line. 
The position is described as `LineColPosition(lineNo,colNum)` in ArkAnalyzer, 
and its default value is LineColPosition(-1,-1).

#### Returns

[`LineColPosition`](LineColPosition.md)

The original location of the statement.

#### Example

1. Get the stmt position info to make some condition judgements.
```typescript
for (const stmt of stmts) {
   if (stmt.getOriginPositionInfo().getLineNo() === -1) {
       stmt.setOriginPositionInfo(originalStmt.getOriginPositionInfo());
       this.stmtToOriginalStmt.set(stmt, originalStmt);
   }
}
```

#### Inherited from

[`Stmt`](Stmt.md).[`getOriginPositionInfo`](Stmt.md#getoriginpositioninfo)

***

### getTypeExprs()

> **getTypeExprs**(): `AbstractTypeExpr`[]

Defined in: src/core/base/Stmt.ts:188

#### Returns

`AbstractTypeExpr`[]

#### Inherited from

[`Stmt`](Stmt.md).[`getTypeExprs`](Stmt.md#gettypeexprs)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Stmt.ts:53

Return a list of values which are uesd in this statement

#### Returns

[`Value`](../interfaces/Value.md)[]

#### Inherited from

[`Stmt`](Stmt.md).[`getUses`](Stmt.md#getuses)

***

### isBranch()

> **isBranch**(): `boolean`

Defined in: src/core/base/Stmt.ts:128

Return true if the following statement may not execute after this statement.
The ArkIfStmt and ArkGotoStmt will return true.

#### Returns

`boolean`

#### Inherited from

[`Stmt`](Stmt.md).[`isBranch`](Stmt.md#isbranch)

***

### replaceDef()

> **replaceDef**(`oldDef`, `newDef`): `void`

Defined in: src/core/base/Stmt.ts:82

#### Parameters

##### oldDef

[`Value`](../interfaces/Value.md)

##### newDef

[`Value`](../interfaces/Value.md)

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`replaceDef`](Stmt.md#replacedef)

***

### replaceUse()

> **replaceUse**(`oldUse`, `newUse`): `void`

Defined in: src/core/base/Stmt.ts:57

#### Parameters

##### oldUse

[`Value`](../interfaces/Value.md)

##### newUse

[`Value`](../interfaces/Value.md)

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`replaceUse`](Stmt.md#replaceuse)

***

### setCfg()

> **setCfg**(`cfg`): `void`

Defined in: src/core/base/Stmt.ts:120

#### Parameters

##### cfg

[`Cfg`](Cfg.md)

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setCfg`](Stmt.md#setcfg)

***

### setMetadata()

> **setMetadata**(`kind`, `value`): `void`

Defined in: src/core/base/Stmt.ts:45

#### Parameters

##### kind

`ArkMetadataKind`

##### value

`ArkMetadataType`

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setMetadata`](Stmt.md#setmetadata)

***

### setOperandOriginalPositions()

> **setOperandOriginalPositions**(`operandOriginalPositions`): `void`

Defined in: src/core/base/Stmt.ts:291

#### Parameters

##### operandOriginalPositions

[`FullPosition`](FullPosition.md)[]

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setOperandOriginalPositions`](Stmt.md#setoperandoriginalpositions)

***

### setOriginalText()

> **setOriginalText**(`originalText`): `void`

Defined in: src/core/base/Stmt.ts:283

#### Parameters

##### originalText

`string`

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setOriginalText`](Stmt.md#setoriginaltext)

***

### setOriginPositionInfo()

> **setOriginPositionInfo**(`originPositionInfo`): `void`

Defined in: src/core/base/Stmt.ts:250

#### Parameters

##### originPositionInfo

[`LineColPosition`](LineColPosition.md)

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setOriginPositionInfo`](Stmt.md#setoriginpositioninfo)

***

### setText()

> **setText**(`text`): `void`

Defined in: src/core/base/Stmt.ts:279

#### Parameters

##### text

`string`

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setText`](Stmt.md#settext)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Stmt.ts:497

#### Returns

`string`

#### Overrides

[`Stmt`](Stmt.md).[`toString`](Stmt.md#tostring)




============================================================
## FILE: `classes/ArkSignatureBuilder.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkSignatureBuilder

# Class: ArkSignatureBuilder

Defined in: src/core/model/builder/ArkSignatureBuilder.ts:19

## Constructors

### Constructor

> **new ArkSignatureBuilder**(): `ArkSignatureBuilder`

#### Returns

`ArkSignatureBuilder`

## Methods

### buildClassSignatureFromClassName()

> `static` **buildClassSignatureFromClassName**(`className`): [`ClassSignature`](ClassSignature.md)

Defined in: src/core/model/builder/ArkSignatureBuilder.ts:35

#### Parameters

##### className

`string`

#### Returns

[`ClassSignature`](ClassSignature.md)

***

### buildFieldSignatureFromFieldName()

> `static` **buildFieldSignatureFromFieldName**(`fieldName`, `staticFlag`): [`FieldSignature`](FieldSignature.md)

Defined in: src/core/model/builder/ArkSignatureBuilder.ts:39

#### Parameters

##### fieldName

`string`

##### staticFlag

`boolean` = `false`

#### Returns

[`FieldSignature`](FieldSignature.md)

***

### buildMethodSignatureFromClassNameAndMethodName()

> `static` **buildMethodSignatureFromClassNameAndMethodName**(`className`, `methodName`, `staticFlag`): [`MethodSignature`](MethodSignature.md)

Defined in: src/core/model/builder/ArkSignatureBuilder.ts:20

#### Parameters

##### className

`string`

##### methodName

`string`

##### staticFlag

`boolean` = `false`

#### Returns

[`MethodSignature`](MethodSignature.md)

***

### buildMethodSignatureFromMethodName()

> `static` **buildMethodSignatureFromMethodName**(`methodName`, `staticFlag`): [`MethodSignature`](MethodSignature.md)

Defined in: src/core/model/builder/ArkSignatureBuilder.ts:26

#### Parameters

##### methodName

`string`

##### staticFlag

`boolean` = `false`

#### Returns

[`MethodSignature`](MethodSignature.md)

***

### buildMethodSubSignatureFromMethodName()

> `static` **buildMethodSubSignatureFromMethodName**(`methodName`, `staticFlag`): [`MethodSubSignature`](MethodSubSignature.md)

Defined in: src/core/model/builder/ArkSignatureBuilder.ts:31

#### Parameters

##### methodName

`string`

##### staticFlag

`boolean` = `false`

#### Returns

[`MethodSubSignature`](MethodSubSignature.md)




============================================================
## FILE: `classes/ArkStaticFieldRef.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkStaticFieldRef

# Class: ArkStaticFieldRef

Defined in: src/core/base/Ref.ts:221

## Extends

- [`AbstractFieldRef`](AbstractFieldRef.md)

## Constructors

### Constructor

> **new ArkStaticFieldRef**(`fieldSignature`): `ArkStaticFieldRef`

Defined in: src/core/base/Ref.ts:222

#### Parameters

##### fieldSignature

[`FieldSignature`](FieldSignature.md)

#### Returns

`ArkStaticFieldRef`

#### Overrides

[`AbstractFieldRef`](AbstractFieldRef.md).[`constructor`](AbstractFieldRef.md#constructor)

## Methods

### getFieldName()

> **getFieldName**(): `string`

Defined in: src/core/base/Ref.ts:134

Returns the the field name as a **string**.

#### Returns

`string`

The the field name.

#### Inherited from

[`AbstractFieldRef`](AbstractFieldRef.md).[`getFieldName`](AbstractFieldRef.md#getfieldname)

***

### getFieldSignature()

> **getFieldSignature**(): [`FieldSignature`](FieldSignature.md)

Defined in: src/core/base/Ref.ts:156

Returns a field signature, which consists of a class signature,
a **string** field name, and a **boolean** label indicating whether it is static or not.

#### Returns

[`FieldSignature`](FieldSignature.md)

The field signature.

#### Example

1. Compare two Fields

```typescript
const fieldSignature = new FieldSignature();
fieldSignature.setFieldName(...);
const fieldRef = new ArkInstanceFieldRef(baseValue as Local, fieldSignature);
...
if (fieldRef.getFieldSignature().getFieldName() ===
targetField.getFieldSignature().getFieldName()) {
...
}
```

#### Inherited from

[`AbstractFieldRef`](AbstractFieldRef.md).[`getFieldSignature`](AbstractFieldRef.md#getfieldsignature)

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Ref.ts:164

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`Type`](Type.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Inherited from

[`AbstractFieldRef`](AbstractFieldRef.md).[`getType`](AbstractFieldRef.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Ref.ts:226

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Overrides

[`AbstractFieldRef`](AbstractFieldRef.md).[`getUses`](AbstractFieldRef.md#getuses)

***

### inferType()

> **inferType**(`arkMethod`): [`AbstractRef`](AbstractRef.md)

Defined in: src/core/base/Ref.ts:36

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

[`AbstractRef`](AbstractRef.md)

#### Inherited from

[`AbstractFieldRef`](AbstractFieldRef.md).[`inferType`](AbstractFieldRef.md#infertype)

***

### setFieldSignature()

> **setFieldSignature**(`newFieldSignature`): `void`

Defined in: src/core/base/Ref.ts:160

#### Parameters

##### newFieldSignature

[`FieldSignature`](FieldSignature.md)

#### Returns

`void`

#### Inherited from

[`AbstractFieldRef`](AbstractFieldRef.md).[`setFieldSignature`](AbstractFieldRef.md#setfieldsignature)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Ref.ts:230

Returns a string representation of an object.

#### Returns

`string`




============================================================
## FILE: `classes/ArkStaticInvokeExpr.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkStaticInvokeExpr

# Class: ArkStaticInvokeExpr

Defined in: src/core/base/Expr.ts:223

## Extends

- [`AbstractInvokeExpr`](AbstractInvokeExpr.md)

## Constructors

### Constructor

> **new ArkStaticInvokeExpr**(`methodSignature`, `args`, `realGenericTypes?`): `ArkStaticInvokeExpr`

Defined in: src/core/base/Expr.ts:224

#### Parameters

##### methodSignature

[`MethodSignature`](MethodSignature.md)

##### args

[`Value`](../interfaces/Value.md)[]

##### realGenericTypes?

[`Type`](Type.md)[]

#### Returns

`ArkStaticInvokeExpr`

#### Overrides

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`constructor`](AbstractInvokeExpr.md#constructor)

## Methods

### getArg()

> **getArg**(`index`): [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Expr.ts:101

Returns an argument used in the expression according to its index.

#### Parameters

##### index

`number`

the index of the argument.

#### Returns

[`Value`](../interfaces/Value.md)

An argument used in the expression.

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`getArg`](AbstractInvokeExpr.md#getarg)

***

### getArgs()

> **getArgs**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Expr.ts:127

Returns an **array** of arguments used in the expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of arguments used in the expression.

#### Example

1. get args number.

```typescript
const argsNum = expr.getArgs().length;
if (argsNum < 5) {
... ...
}
```

2. iterate arg based on expression

```typescript
for (const arg of this.getArgs()) {
strs.push(arg.toString());
strs.push(', ');
}
```

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`getArgs`](AbstractInvokeExpr.md#getargs)

***

### getMethodSignature()

> **getMethodSignature**(): [`MethodSignature`](MethodSignature.md)

Defined in: src/core/base/Expr.ts:88

Get method Signature. The method signature is consist of ClassSignature and MethodSubSignature.
It is the unique flag of a method. It is usually used to compose a expression string in ArkIRTransformer.

#### Returns

[`MethodSignature`](MethodSignature.md)

The class method signature, such as ArkStaticInvokeExpr.

#### Example

1. 3AC information composed of getMethodSignature ().

```typescript
let strs: string[] = [];
strs.push('staticinvoke <');
strs.push(this.getMethodSignature().toString());
strs.push('>(');
```

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`getMethodSignature`](AbstractInvokeExpr.md#getmethodsignature)

***

### getRealGenericTypes()

> **getRealGenericTypes**(): `undefined` \| [`Type`](Type.md)[]

Defined in: src/core/base/Expr.ts:143

#### Returns

`undefined` \| [`Type`](Type.md)[]

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`getRealGenericTypes`](AbstractInvokeExpr.md#getrealgenerictypes)

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Expr.ts:135

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`Type`](Type.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`getType`](AbstractInvokeExpr.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Expr.ts:153

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`getUses`](AbstractInvokeExpr.md#getuses)

***

### inferType()

> **inferType**(`arkMethod`): [`AbstractInvokeExpr`](AbstractInvokeExpr.md)

Defined in: src/core/base/Expr.ts:244

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

[`AbstractInvokeExpr`](AbstractInvokeExpr.md)

#### Overrides

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`inferType`](AbstractInvokeExpr.md#infertype)

***

### setArgs()

> **setArgs**(`newArgs`): `void`

Defined in: src/core/base/Expr.ts:131

#### Parameters

##### newArgs

[`Value`](../interfaces/Value.md)[]

#### Returns

`void`

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`setArgs`](AbstractInvokeExpr.md#setargs)

***

### setMethodSignature()

> **setMethodSignature**(`newMethodSignature`): `void`

Defined in: src/core/base/Expr.ts:92

#### Parameters

##### newMethodSignature

[`MethodSignature`](MethodSignature.md)

#### Returns

`void`

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`setMethodSignature`](AbstractInvokeExpr.md#setmethodsignature)

***

### setRealGenericTypes()

> **setRealGenericTypes**(`realTypes`): `void`

Defined in: src/core/base/Expr.ts:147

#### Parameters

##### realTypes

`undefined` | [`Type`](Type.md)[]

#### Returns

`void`

#### Inherited from

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`setRealGenericTypes`](AbstractInvokeExpr.md#setrealgenerictypes)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Expr.ts:228

Returns a string representation of an object.

#### Returns

`string`

#### Overrides

[`AbstractInvokeExpr`](AbstractInvokeExpr.md).[`toString`](AbstractInvokeExpr.md#tostring)




============================================================
## FILE: `classes/ArkThisRef.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkThisRef

# Class: ArkThisRef

Defined in: src/core/base/Ref.ts:274

## Extends

- [`AbstractRef`](AbstractRef.md)

## Constructors

### Constructor

> **new ArkThisRef**(`type`): `ArkThisRef`

Defined in: src/core/base/Ref.ts:277

#### Parameters

##### type

[`ClassType`](ClassType.md)

#### Returns

`ArkThisRef`

#### Overrides

[`AbstractRef`](AbstractRef.md).[`constructor`](AbstractRef.md#constructor)

## Methods

### getType()

> **getType**(): [`ClassType`](ClassType.md)

Defined in: src/core/base/Ref.ts:282

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`ClassType`](ClassType.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Overrides

[`AbstractRef`](AbstractRef.md).[`getType`](AbstractRef.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Ref.ts:286

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Overrides

[`AbstractRef`](AbstractRef.md).[`getUses`](AbstractRef.md#getuses)

***

### inferType()

> **inferType**(`arkMethod`): [`AbstractRef`](AbstractRef.md)

Defined in: src/core/base/Ref.ts:36

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

[`AbstractRef`](AbstractRef.md)

#### Inherited from

[`AbstractRef`](AbstractRef.md).[`inferType`](AbstractRef.md#infertype)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Ref.ts:290

Returns a string representation of an object.

#### Returns

`string`




============================================================
## FILE: `classes/ArkThrowStmt.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkThrowStmt

# Class: ArkThrowStmt

Defined in: src/core/base/Stmt.ts:503

## Extends

- [`Stmt`](Stmt.md)

## Constructors

### Constructor

> **new ArkThrowStmt**(`op`): `ArkThrowStmt`

Defined in: src/core/base/Stmt.ts:506

#### Parameters

##### op

[`Value`](../interfaces/Value.md)

#### Returns

`ArkThrowStmt`

#### Overrides

[`Stmt`](Stmt.md).[`constructor`](Stmt.md#constructor)

## Properties

### cfg

> `protected` **cfg**: [`Cfg`](Cfg.md)

Defined in: src/core/base/Stmt.ts:36

#### Inherited from

[`Stmt`](Stmt.md).[`cfg`](Stmt.md#cfg)

***

### metadata?

> `optional` **metadata**: `ArkMetadata`

Defined in: src/core/base/Stmt.ts:39

#### Inherited from

[`Stmt`](Stmt.md).[`metadata`](Stmt.md#metadata)

***

### operandOriginalPositions?

> `protected` `optional` **operandOriginalPositions**: [`FullPosition`](FullPosition.md)[]

Defined in: src/core/base/Stmt.ts:37

#### Inherited from

[`Stmt`](Stmt.md).[`operandOriginalPositions`](Stmt.md#operandoriginalpositions)

***

### originalPosition

> `protected` **originalPosition**: [`LineColPosition`](LineColPosition.md) = `LineColPosition.DEFAULT`

Defined in: src/core/base/Stmt.ts:35

#### Inherited from

[`Stmt`](Stmt.md).[`originalPosition`](Stmt.md#originalposition)

***

### originalText?

> `protected` `optional` **originalText**: `string`

Defined in: src/core/base/Stmt.ts:34

#### Inherited from

[`Stmt`](Stmt.md).[`originalText`](Stmt.md#originaltext)

***

### text?

> `protected` `optional` **text**: `string`

Defined in: src/core/base/Stmt.ts:33

#### Inherited from

[`Stmt`](Stmt.md).[`text`](Stmt.md#text)

## Methods

### containsArrayRef()

> **containsArrayRef**(): `boolean`

Defined in: src/core/base/Stmt.ts:199

#### Returns

`boolean`

#### Inherited from

[`Stmt`](Stmt.md).[`containsArrayRef`](Stmt.md#containsarrayref)

***

### containsFieldRef()

> **containsFieldRef**(): `boolean`

Defined in: src/core/base/Stmt.ts:225

#### Returns

`boolean`

#### Inherited from

[`Stmt`](Stmt.md).[`containsFieldRef`](Stmt.md#containsfieldref)

***

### containsInvokeExpr()

> **containsInvokeExpr**(): `boolean`

Defined in: src/core/base/Stmt.ts:137

#### Returns

`boolean`

#### Inherited from

[`Stmt`](Stmt.md).[`containsInvokeExpr`](Stmt.md#containsinvokeexpr)

***

### getArrayRef()

> **getArrayRef**(): `undefined` \| [`ArkArrayRef`](ArkArrayRef.md)

Defined in: src/core/base/Stmt.ts:211

#### Returns

`undefined` \| [`ArkArrayRef`](ArkArrayRef.md)

#### Inherited from

[`Stmt`](Stmt.md).[`getArrayRef`](Stmt.md#getarrayref)

***

### getCfg()

> **getCfg**(): [`Cfg`](Cfg.md)

Defined in: src/core/base/Stmt.ts:116

Get the CFG (i.e., control flow graph) of an [ArkBody](ArkBody.md) in which the statement is.
A CFG contains a set of basic blocks and statements corresponding to each basic block.
Note that, "source code" and "three-address" are two types of [Stmt](Stmt.md) in ArkAnalyzer.
Source code [Stmt](Stmt.md) represents the statement of ets/ts source code, while three-address code [Stmt](Stmt.md)
represents the statement after it has been converted into three-address code.  Since the source code [Stmt](Stmt.md) does not save its CFG reference, it returns **null**, while the `getCfg()` of the third address code
[Stmt](Stmt.md) will return its CFG reference.

#### Returns

[`Cfg`](Cfg.md)

The CFG (i.e., control flow graph) of an [ArkBody](ArkBody.md) in which the statement is.

#### Example

1. get the ArkFile based on stmt.
```typescript
const arkFile = stmt.getCfg()?.getDeclaringMethod().getDeclaringArkFile();
```
2. get the ArkMethod based on stmt.
```typescript
let sourceMethod: ArkMethod = stmt.getCfg()?.getDeclaringMethod();
```

#### Inherited from

[`Stmt`](Stmt.md).[`getCfg`](Stmt.md#getcfg)

***

### getDef()

> **getDef**(): `null` \| [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Stmt.ts:78

Return the definition which is uesd in this statement. Generally, the definition is the left value of `=` in
3AC.  For example, the definition in 3AC of `value = parameter0: @project-1/sample-1.ets: AnonymousClass-0` is
`value`,  and the definition in `$temp0 = staticinvoke <@_ProjectName/_FileName: xxx.create()>()` is `\$temp0`.

#### Returns

`null` \| [`Value`](../interfaces/Value.md)

The definition in 3AC (may be a **null**).

#### Example

1. get the def in stmt.
```typescript
for (const block of this.blocks) {
for (const stmt of block.getStmts()) {
   const defValue = stmt.getDef();
   ...
   }
}
```

#### Inherited from

[`Stmt`](Stmt.md).[`getDef`](Stmt.md#getdef)

***

### getDefAndUses()

> **getDefAndUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Stmt.ts:87

#### Returns

[`Value`](../interfaces/Value.md)[]

#### Inherited from

[`Stmt`](Stmt.md).[`getDefAndUses`](Stmt.md#getdefanduses)

***

### getExpectedSuccessorCount()

> **getExpectedSuccessorCount**(): `number`

Defined in: src/core/base/Stmt.ts:133

Return the number of statements which this statement may go to

#### Returns

`number`

#### Inherited from

[`Stmt`](Stmt.md).[`getExpectedSuccessorCount`](Stmt.md#getexpectedsuccessorcount)

***

### getExprs()

> **getExprs**(): [`AbstractExpr`](AbstractExpr.md)[]

Defined in: src/core/base/Stmt.ts:178

Returns an array of expressions in the statement.

#### Returns

[`AbstractExpr`](AbstractExpr.md)[]

An array of expressions in the statement.

#### Example

1. Traverse expression of statement.

```typescript
for (const expr of stmt.getExprs()) {
   ...
}
```

#### Inherited from

[`Stmt`](Stmt.md).[`getExprs`](Stmt.md#getexprs)

***

### getFieldRef()

> **getFieldRef**(): `undefined` \| [`AbstractFieldRef`](AbstractFieldRef.md)

Defined in: src/core/base/Stmt.ts:238

#### Returns

`undefined` \| [`AbstractFieldRef`](AbstractFieldRef.md)

#### Inherited from

[`Stmt`](Stmt.md).[`getFieldRef`](Stmt.md#getfieldref)

***

### getInvokeExpr()

> **getInvokeExpr**(): `undefined` \| [`AbstractInvokeExpr`](AbstractInvokeExpr.md)

Defined in: src/core/base/Stmt.ts:157

Returns the method's invocation expression (including method signature and its arguments) 
in the current statement. An **undefined** will be returned if there is no method used in this statement.

#### Returns

`undefined` \| [`AbstractInvokeExpr`](AbstractInvokeExpr.md)

the method's invocation expression from the statement. An **undefined** will be returned if there is
    no method can be found in this statement.

#### Example

1. get invoke expr based on stmt.
```typescript
let invoke = stmt.getInvokeExpr();
```

#### Inherited from

[`Stmt`](Stmt.md).[`getInvokeExpr`](Stmt.md#getinvokeexpr)

***

### getMetadata()

> **getMetadata**(`kind`): `undefined` \| `ArkMetadataType`

Defined in: src/core/base/Stmt.ts:41

#### Parameters

##### kind

`ArkMetadataKind`

#### Returns

`undefined` \| `ArkMetadataType`

#### Inherited from

[`Stmt`](Stmt.md).[`getMetadata`](Stmt.md#getmetadata)

***

### getOp()

> **getOp**(): [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Stmt.ts:511

#### Returns

[`Value`](../interfaces/Value.md)

***

### getOperandOriginalPosition()

> **getOperandOriginalPosition**(`indexOrOperand`): `null` \| [`FullPosition`](FullPosition.md)

Defined in: src/core/base/Stmt.ts:299

#### Parameters

##### indexOrOperand

`number` | [`Value`](../interfaces/Value.md)

#### Returns

`null` \| [`FullPosition`](FullPosition.md)

#### Inherited from

[`Stmt`](Stmt.md).[`getOperandOriginalPosition`](Stmt.md#getoperandoriginalposition)

***

### getOperandOriginalPositions()

> **getOperandOriginalPositions**(): `undefined` \| [`FullPosition`](FullPosition.md)[]

Defined in: src/core/base/Stmt.ts:295

#### Returns

`undefined` \| [`FullPosition`](FullPosition.md)[]

#### Inherited from

[`Stmt`](Stmt.md).[`getOperandOriginalPositions`](Stmt.md#getoperandoriginalpositions)

***

### getOriginalText()

> **getOriginalText**(): `undefined` \| `string`

Defined in: src/core/base/Stmt.ts:287

#### Returns

`undefined` \| `string`

#### Inherited from

[`Stmt`](Stmt.md).[`getOriginalText`](Stmt.md#getoriginaltext)

***

### getOriginPositionInfo()

> **getOriginPositionInfo**(): [`LineColPosition`](LineColPosition.md)

Defined in: src/core/base/Stmt.ts:273

Returns the original position of the statement. 
The position consists of two parts: line number and column number. 
In the source file, the former (i.e., line number) indicates which line the statement is in, 
and the latter (i.e., column number) indicates the position of the statement in the line. 
The position is described as `LineColPosition(lineNo,colNum)` in ArkAnalyzer, 
and its default value is LineColPosition(-1,-1).

#### Returns

[`LineColPosition`](LineColPosition.md)

The original location of the statement.

#### Example

1. Get the stmt position info to make some condition judgements.
```typescript
for (const stmt of stmts) {
   if (stmt.getOriginPositionInfo().getLineNo() === -1) {
       stmt.setOriginPositionInfo(originalStmt.getOriginPositionInfo());
       this.stmtToOriginalStmt.set(stmt, originalStmt);
   }
}
```

#### Inherited from

[`Stmt`](Stmt.md).[`getOriginPositionInfo`](Stmt.md#getoriginpositioninfo)

***

### getTypeExprs()

> **getTypeExprs**(): `AbstractTypeExpr`[]

Defined in: src/core/base/Stmt.ts:188

#### Returns

`AbstractTypeExpr`[]

#### Inherited from

[`Stmt`](Stmt.md).[`getTypeExprs`](Stmt.md#gettypeexprs)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Stmt.ts:524

Return a list of values which are uesd in this statement

#### Returns

[`Value`](../interfaces/Value.md)[]

#### Overrides

[`Stmt`](Stmt.md).[`getUses`](Stmt.md#getuses)

***

### isBranch()

> **isBranch**(): `boolean`

Defined in: src/core/base/Stmt.ts:128

Return true if the following statement may not execute after this statement.
The ArkIfStmt and ArkGotoStmt will return true.

#### Returns

`boolean`

#### Inherited from

[`Stmt`](Stmt.md).[`isBranch`](Stmt.md#isbranch)

***

### replaceDef()

> **replaceDef**(`oldDef`, `newDef`): `void`

Defined in: src/core/base/Stmt.ts:82

#### Parameters

##### oldDef

[`Value`](../interfaces/Value.md)

##### newDef

[`Value`](../interfaces/Value.md)

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`replaceDef`](Stmt.md#replacedef)

***

### replaceUse()

> **replaceUse**(`oldUse`, `newUse`): `void`

Defined in: src/core/base/Stmt.ts:57

#### Parameters

##### oldUse

[`Value`](../interfaces/Value.md)

##### newUse

[`Value`](../interfaces/Value.md)

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`replaceUse`](Stmt.md#replaceuse)

***

### setCfg()

> **setCfg**(`cfg`): `void`

Defined in: src/core/base/Stmt.ts:120

#### Parameters

##### cfg

[`Cfg`](Cfg.md)

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setCfg`](Stmt.md#setcfg)

***

### setMetadata()

> **setMetadata**(`kind`, `value`): `void`

Defined in: src/core/base/Stmt.ts:45

#### Parameters

##### kind

`ArkMetadataKind`

##### value

`ArkMetadataType`

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setMetadata`](Stmt.md#setmetadata)

***

### setOp()

> **setOp**(`newOp`): `void`

Defined in: src/core/base/Stmt.ts:515

#### Parameters

##### newOp

[`Value`](../interfaces/Value.md)

#### Returns

`void`

***

### setOperandOriginalPositions()

> **setOperandOriginalPositions**(`operandOriginalPositions`): `void`

Defined in: src/core/base/Stmt.ts:291

#### Parameters

##### operandOriginalPositions

[`FullPosition`](FullPosition.md)[]

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setOperandOriginalPositions`](Stmt.md#setoperandoriginalpositions)

***

### setOriginalText()

> **setOriginalText**(`originalText`): `void`

Defined in: src/core/base/Stmt.ts:283

#### Parameters

##### originalText

`string`

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setOriginalText`](Stmt.md#setoriginaltext)

***

### setOriginPositionInfo()

> **setOriginPositionInfo**(`originPositionInfo`): `void`

Defined in: src/core/base/Stmt.ts:250

#### Parameters

##### originPositionInfo

[`LineColPosition`](LineColPosition.md)

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setOriginPositionInfo`](Stmt.md#setoriginpositioninfo)

***

### setText()

> **setText**(`text`): `void`

Defined in: src/core/base/Stmt.ts:279

#### Parameters

##### text

`string`

#### Returns

`void`

#### Inherited from

[`Stmt`](Stmt.md).[`setText`](Stmt.md#settext)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Stmt.ts:519

#### Returns

`string`

#### Overrides

[`Stmt`](Stmt.md).[`toString`](Stmt.md#tostring)




============================================================
## FILE: `classes/ArkTypeOfExpr.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkTypeOfExpr

# Class: ArkTypeOfExpr

Defined in: src/core/base/Expr.ts:773

## Extends

- [`AbstractExpr`](AbstractExpr.md)

## Constructors

### Constructor

> **new ArkTypeOfExpr**(`op`): `ArkTypeOfExpr`

Defined in: src/core/base/Expr.ts:776

#### Parameters

##### op

[`Value`](../interfaces/Value.md)

#### Returns

`ArkTypeOfExpr`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`constructor`](AbstractExpr.md#constructor)

## Methods

### getOp()

> **getOp**(): [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Expr.ts:781

#### Returns

[`Value`](../interfaces/Value.md)

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Expr.ts:796

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`Type`](Type.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`getType`](AbstractExpr.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Expr.ts:789

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`getUses`](AbstractExpr.md#getuses)

***

### inferType()

> **inferType**(`arkMethod`): [`AbstractExpr`](AbstractExpr.md)

Defined in: src/core/base/Expr.ts:804

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

[`AbstractExpr`](AbstractExpr.md)

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`inferType`](AbstractExpr.md#infertype)

***

### setOp()

> **setOp**(`newOp`): `void`

Defined in: src/core/base/Expr.ts:785

#### Parameters

##### newOp

[`Value`](../interfaces/Value.md)

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Expr.ts:800

Returns a string representation of an object.

#### Returns

`string`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`toString`](AbstractExpr.md#tostring)




============================================================
## FILE: `classes/ArkUnopExpr.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkUnopExpr

# Class: ArkUnopExpr

Defined in: src/core/base/Expr.ts:965

## Extends

- [`AbstractExpr`](AbstractExpr.md)

## Constructors

### Constructor

> **new ArkUnopExpr**(`op`, `operator`): `ArkUnopExpr`

Defined in: src/core/base/Expr.ts:969

#### Parameters

##### op

[`Value`](../interfaces/Value.md)

##### operator

[`UnaryOperator`](../enumerations/UnaryOperator.md)

#### Returns

`ArkUnopExpr`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`constructor`](AbstractExpr.md#constructor)

## Methods

### getOp()

> **getOp**(): [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Expr.ts:982

#### Returns

[`Value`](../interfaces/Value.md)

***

### getOperator()

> **getOperator**(): [`UnaryOperator`](../enumerations/UnaryOperator.md)

Defined in: src/core/base/Expr.ts:998

Get the unary operator from the statement, such as `-`,`~`,`!`.

#### Returns

[`UnaryOperator`](../enumerations/UnaryOperator.md)

the unary operator of a statement.

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Expr.ts:990

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`Type`](Type.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`getType`](AbstractExpr.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Expr.ts:975

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`getUses`](AbstractExpr.md#getuses)

***

### inferType()

> **inferType**(`arkMethod`): [`AbstractExpr`](AbstractExpr.md)

Defined in: src/core/base/Expr.ts:57

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

[`AbstractExpr`](AbstractExpr.md)

#### Inherited from

[`AbstractExpr`](AbstractExpr.md).[`inferType`](AbstractExpr.md#infertype)

***

### setOp()

> **setOp**(`newOp`): `void`

Defined in: src/core/base/Expr.ts:986

#### Parameters

##### newOp

[`Value`](../interfaces/Value.md)

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Expr.ts:1002

Returns a string representation of an object.

#### Returns

`string`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`toString`](AbstractExpr.md#tostring)




============================================================
## FILE: `classes/ArkYieldExpr.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkYieldExpr

# Class: ArkYieldExpr

Defined in: src/core/base/Expr.ts:504

## Extends

- [`AbstractExpr`](AbstractExpr.md)

## Constructors

### Constructor

> **new ArkYieldExpr**(`yieldValue`): `ArkYieldExpr`

Defined in: src/core/base/Expr.ts:507

#### Parameters

##### yieldValue

[`Value`](../interfaces/Value.md)

#### Returns

`ArkYieldExpr`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`constructor`](AbstractExpr.md#constructor)

## Methods

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Expr.ts:520

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`Type`](Type.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`getType`](AbstractExpr.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Expr.ts:524

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`getUses`](AbstractExpr.md#getuses)

***

### getYieldValue()

> **getYieldValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Expr.ts:512

#### Returns

[`Value`](../interfaces/Value.md)

***

### inferType()

> **inferType**(`arkMethod`): [`AbstractExpr`](AbstractExpr.md)

Defined in: src/core/base/Expr.ts:57

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

[`AbstractExpr`](AbstractExpr.md)

#### Inherited from

[`AbstractExpr`](AbstractExpr.md).[`inferType`](AbstractExpr.md#infertype)

***

### setYieldValue()

> **setYieldValue**(`newYieldValue`): `void`

Defined in: src/core/base/Expr.ts:516

#### Parameters

##### newYieldValue

[`Value`](../interfaces/Value.md)

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Expr.ts:531

Returns a string representation of an object.

#### Returns

`string`

#### Overrides

[`AbstractExpr`](AbstractExpr.md).[`toString`](AbstractExpr.md#tostring)




============================================================
## FILE: `classes/ArrayType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArrayType

# Class: ArrayType

Defined in: src/core/base/Type.ts:462

Array type

## Example

```typescript
// baseType is number, dimension is 1, readonlyFlag is true
let a: readonly number[] = [1, 2, 3];

// baseType is number, dimension is 1, readonlyFlag is undefined
let a: number[] = [1, 2, 3];
```

## Extends

- [`Type`](Type.md)

## Constructors

### Constructor

> **new ArrayType**(`baseType`, `dimension`): `ArrayType`

Defined in: src/core/base/Type.ts:467

#### Parameters

##### baseType

[`Type`](Type.md)

##### dimension

`number`

#### Returns

`ArrayType`

#### Overrides

[`Type`](Type.md).[`constructor`](Type.md#constructor)

## Methods

### getBaseType()

> **getBaseType**(): [`Type`](Type.md)

Defined in: src/core/base/Type.ts:477

Returns the base type of this array, such as `Any`, `Unknown`, `TypeParameter`, etc.

#### Returns

[`Type`](Type.md)

The base type of array.

***

### getDimension()

> **getDimension**(): `number`

Defined in: src/core/base/Type.ts:485

#### Returns

`number`

***

### getReadonlyFlag()

> **getReadonlyFlag**(): `undefined` \| `boolean`

Defined in: src/core/base/Type.ts:493

#### Returns

`undefined` \| `boolean`

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:497

#### Returns

`string`

#### Overrides

[`Type`](Type.md).[`getTypeString`](Type.md#gettypestring)

***

### setBaseType()

> **setBaseType**(`newType`): `void`

Defined in: src/core/base/Type.ts:481

#### Parameters

##### newType

[`Type`](Type.md)

#### Returns

`void`

***

### setReadonlyFlag()

> **setReadonlyFlag**(`readonlyFlag`): `void`

Defined in: src/core/base/Type.ts:489

#### Parameters

##### readonlyFlag

`boolean`

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`Type`](Type.md).[`toString`](Type.md#tostring)




============================================================
## FILE: `classes/AstTreeUtils.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / AstTreeUtils

# Class: AstTreeUtils

Defined in: src/utils/AstTreeUtils.ts:22

## Constructors

### Constructor

> **new AstTreeUtils**(): `AstTreeUtils`

#### Returns

`AstTreeUtils`

## Methods

### createSourceFile()

> `static` **createSourceFile**(`fileName`, `code`): [`SourceFile`](../ArkAnalyzer/namespaces/ts/interfaces/SourceFile.md)

Defined in: src/utils/AstTreeUtils.ts:57

#### Parameters

##### fileName

`string`

##### code

`string`

#### Returns

[`SourceFile`](../ArkAnalyzer/namespaces/ts/interfaces/SourceFile.md)

***

### getASTNode()

> `static` **getASTNode**(`fileName`, `code`): [`SourceFile`](../ArkAnalyzer/namespaces/ts/interfaces/SourceFile.md)

Defined in: src/utils/AstTreeUtils.ts:29

get source file from code segment

#### Parameters

##### fileName

`string`

source file name

##### code

`string`

source code

#### Returns

[`SourceFile`](../ArkAnalyzer/namespaces/ts/interfaces/SourceFile.md)

ts.SourceFile

***

### getSourceFileFromArkFile()

> `static` **getSourceFileFromArkFile**(`arkFile`): [`SourceFile`](../ArkAnalyzer/namespaces/ts/interfaces/SourceFile.md)

Defined in: src/utils/AstTreeUtils.ts:45

get source file from ArkFile

#### Parameters

##### arkFile

[`ArkFile`](ArkFile.md)

ArkFile

#### Returns

[`SourceFile`](../ArkAnalyzer/namespaces/ts/interfaces/SourceFile.md)

ts.SourceFile




============================================================
## FILE: `classes/BaseEdge.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BaseEdge

# Class: `abstract` BaseEdge

Defined in: src/core/graph/BaseExplicitGraph.ts:19

## Extended by

- [`CallGraphEdge`](CallGraphEdge.md)
- [`PagEdge`](PagEdge.md)

## Constructors

### Constructor

> **new BaseEdge**(`s`, `d`, `k`): `BaseEdge`

Defined in: src/core/graph/BaseExplicitGraph.ts:24

#### Parameters

##### s

[`BaseNode`](BaseNode.md)

##### d

[`BaseNode`](BaseNode.md)

##### k

`number`

#### Returns

`BaseEdge`

## Properties

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:22

## Methods

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/core/graph/BaseExplicitGraph.ts:61

#### Returns

`string`

***

### getDstID()

> **getDstID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:34

#### Returns

`number`

***

### getDstNode()

> **getDstNode**(): [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:42

#### Returns

[`BaseNode`](BaseNode.md)

***

### getEndPoints()

> **getEndPoints**(): `object`

Defined in: src/core/graph/BaseExplicitGraph.ts:54

#### Returns

`object`

##### dst

> **dst**: `number`

##### src

> **src**: `number`

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:46

#### Returns

`number`

***

### getSrcID()

> **getSrcID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:30

#### Returns

`number`

***

### getSrcNode()

> **getSrcNode**(): [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:38

#### Returns

[`BaseNode`](BaseNode.md)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:50

#### Parameters

##### kind

`number`

#### Returns

`void`




============================================================
## FILE: `classes/BaseExplicitGraph.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BaseExplicitGraph

# Class: `abstract` BaseExplicitGraph

Defined in: src/core/graph/BaseExplicitGraph.ts:136

## Extended by

- [`CallGraph`](CallGraph.md)
- [`Pag`](Pag.md)
- [`DVFG`](DVFG.md)

## Implements

- `GraphTraits`\<[`BaseNode`](BaseNode.md)\>

## Constructors

### Constructor

> **new BaseExplicitGraph**(): `BaseExplicitGraph`

Defined in: src/core/graph/BaseExplicitGraph.ts:142

#### Returns

`BaseExplicitGraph`

## Properties

### edgeMarkSet

> `protected` **edgeMarkSet**: `Set`\<`string`\>

Defined in: src/core/graph/BaseExplicitGraph.ts:140

***

### edgeNum

> `protected` **edgeNum**: `number` = `0`

Defined in: src/core/graph/BaseExplicitGraph.ts:137

***

### idToNodeMap

> `protected` **idToNodeMap**: `Map`\<`number`, [`BaseNode`](BaseNode.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:139

***

### nodeNum

> `protected` **nodeNum**: `number` = `0`

Defined in: src/core/graph/BaseExplicitGraph.ts:138

## Methods

### addNode()

> **addNode**(`n`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:155

#### Parameters

##### n

[`BaseNode`](BaseNode.md)

#### Returns

`void`

***

### getGraphName()

> `abstract` **getGraphName**(): `string`

Defined in: src/core/graph/BaseExplicitGraph.ts:204

#### Returns

`string`

#### Implementation of

`GraphTraits.getGraphName`

***

### getNode()

> **getNode**(`id`): `undefined` \| [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:160

#### Parameters

##### id

`number`

#### Returns

`undefined` \| [`BaseNode`](BaseNode.md)

#### Implementation of

`GraphTraits.getNode`

***

### getNodeNum()

> **getNodeNum**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:147

#### Returns

`number`

***

### getNodesIter()

> **getNodesIter**(): `IterableIterator`\<[`BaseNode`](BaseNode.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:200

#### Returns

`IterableIterator`\<[`BaseNode`](BaseNode.md)\>

***

### hasEdge()

> **hasEdge**(`src`, `dst`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:180

#### Parameters

##### src

[`BaseNode`](BaseNode.md)

##### dst

[`BaseNode`](BaseNode.md)

#### Returns

`boolean`

***

### hasNode()

> **hasNode**(`id`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:168

#### Parameters

##### id

`number`

#### Returns

`boolean`

***

### ifEdgeExisting()

> **ifEdgeExisting**(`edge`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:190

#### Parameters

##### edge

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

***

### nodesItor()

> **nodesItor**(): `IterableIterator`\<[`BaseNode`](BaseNode.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:151

#### Returns

`IterableIterator`\<[`BaseNode`](BaseNode.md)\>

#### Implementation of

`GraphTraits.nodesItor`

***

### removeNode()

> **removeNode**(`id`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:172

#### Parameters

##### id

`number`

#### Returns

`boolean`




============================================================
## FILE: `classes/BaseNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BaseNode

# Class: `abstract` BaseNode

Defined in: src/core/graph/BaseExplicitGraph.ts:66

## Extended by

- [`CallGraphNode`](CallGraphNode.md)
- [`PagNode`](PagNode.md)

## Constructors

### Constructor

> **new BaseNode**(`id`, `k`): `BaseNode`

Defined in: src/core/graph/BaseExplicitGraph.ts:72

#### Parameters

##### id

`number`

##### k

`number`

#### Returns

`BaseNode`

## Properties

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:68

## Methods

### addIncomingEdge()

> **addIncomingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:105

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

***

### addOutgoingEdge()

> **addOutgoingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:109

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/core/graph/BaseExplicitGraph.ts:129

#### Returns

`string`

***

### getDotLabel()

> `abstract` **getDotLabel**(): `string`

Defined in: src/core/graph/BaseExplicitGraph.ts:133

#### Returns

`string`

***

### getID()

> **getID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:77

#### Returns

`number`

***

### getIncomingEdge()

> **getIncomingEdge**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:121

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:81

#### Returns

`number`

***

### getOutgoingEdges()

> **getOutgoingEdges**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:125

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

***

### hasIncomingEdge()

> **hasIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:97

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

***

### hasIncomingEdges()

> **hasIncomingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:89

#### Returns

`boolean`

***

### hasOutgoingEdge()

> **hasOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:101

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

***

### hasOutgoingEdges()

> **hasOutgoingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:93

#### Returns

`boolean`

***

### removeIncomingEdge()

> **removeIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:113

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

***

### removeOutgoingEdge()

> **removeOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:117

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:85

#### Parameters

##### kind

`number`

#### Returns

`void`




============================================================
## FILE: `classes/BasicBlock.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BasicBlock

# Class: BasicBlock

Defined in: src/core/graph/BasicBlock.ts:31

## Constructors

### Constructor

> **new BasicBlock**(): `BasicBlock`

Defined in: src/core/graph/BasicBlock.ts:38

#### Returns

`BasicBlock`

## Methods

### addExceptionalSuccessorBlock()

> **addExceptionalSuccessorBlock**(`block`): `void`

Defined in: src/core/graph/BasicBlock.ts:282

#### Parameters

##### block

`BasicBlock`

#### Returns

`void`

***

### addHead()

> **addHead**(`stmt`): `void`

Defined in: src/core/graph/BasicBlock.ts:64

Adds the given stmt at the beginning of the basic block.

#### Parameters

##### stmt

[`Stmt`](Stmt.md) | [`Stmt`](Stmt.md)[]

#### Returns

`void`

***

### addPredecessorBlock()

> **addPredecessorBlock**(`block`): `void`

Defined in: src/core/graph/BasicBlock.ts:184

#### Parameters

##### block

`BasicBlock`

#### Returns

`void`

***

### addStmt()

> **addStmt**(`stmt`): `void`

Defined in: src/core/graph/BasicBlock.ts:56

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`void`

***

### addStmtToFirst()

> **addStmtToFirst**(`stmt`): `void`

Defined in: src/core/graph/BasicBlock.ts:205

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`void`

***

### addSuccessorBlock()

> **addSuccessorBlock**(`block`): `void`

Defined in: src/core/graph/BasicBlock.ts:210

#### Parameters

##### block

`BasicBlock`

#### Returns

`void`

***

### addTail()

> **addTail**(`stmt`): `void`

Defined in: src/core/graph/BasicBlock.ts:76

Adds the given stmt at the end of the basic block.

#### Parameters

##### stmt

[`Stmt`](Stmt.md) | [`Stmt`](Stmt.md)[]

#### Returns

`void`

***

### getExceptionalSuccessorBlocks()

> **getExceptionalSuccessorBlocks**(): `undefined` \| `BasicBlock`[]

Defined in: src/core/graph/BasicBlock.ts:278

#### Returns

`undefined` \| `BasicBlock`[]

***

### getHead()

> **getHead**(): `null` \| [`Stmt`](Stmt.md)

Defined in: src/core/graph/BasicBlock.ts:139

#### Returns

`null` \| [`Stmt`](Stmt.md)

***

### getId()

> **getId**(): `number`

Defined in: src/core/graph/BasicBlock.ts:40

#### Returns

`number`

***

### getPredecessors()

> **getPredecessors**(): `BasicBlock`[]

Defined in: src/core/graph/BasicBlock.ts:180

Returns predecessors of the current basic block, whose types are also basic blocks.

#### Returns

`BasicBlock`[]

An array of basic blocks.

***

### getStmts()

> **getStmts**(): [`Stmt`](Stmt.md)[]

Defined in: src/core/graph/BasicBlock.ts:52

Returns an array of the statements in a basic block.

#### Returns

[`Stmt`](Stmt.md)[]

An array of statements in a basic block.

***

### getSuccessors()

> **getSuccessors**(): `BasicBlock`[]

Defined in: src/core/graph/BasicBlock.ts:172

Returns successors of the current basic block, whose types are also basic blocks (i.e.BasicBlock).

#### Returns

`BasicBlock`[]

Successors of the current basic block.

#### Example

1. get block successors.

```typescript
const body = arkMethod.getBody();
const blocks = [...body.getCfg().getBlocks()]
for (let i = 0; i < blocks.length; i++) {
const block = blocks[i]
   ...
   for (const next of block.getSuccessors()) {
   ...
   }
} 
```

***

### getTail()

> **getTail**(): `null` \| [`Stmt`](Stmt.md)

Defined in: src/core/graph/BasicBlock.ts:146

#### Returns

`null` \| [`Stmt`](Stmt.md)

***

### insertAfter()

> **insertAfter**(`toInsert`, `point`): `number`

Defined in: src/core/graph/BasicBlock.ts:90

Inserts toInsert in the basic block after point.

#### Parameters

##### toInsert

[`Stmt`](Stmt.md) | [`Stmt`](Stmt.md)[]

##### point

[`Stmt`](Stmt.md)

#### Returns

`number`

The number of successfully inserted statements

***

### insertBefore()

> **insertBefore**(`toInsert`, `point`): `number`

Defined in: src/core/graph/BasicBlock.ts:104

Inserts toInsert in the basic block befor point.

#### Parameters

##### toInsert

[`Stmt`](Stmt.md) | [`Stmt`](Stmt.md)[]

##### point

[`Stmt`](Stmt.md)

#### Returns

`number`

The number of successfully inserted statements

***

### remove()

> **remove**(`stmt`): `void`

Defined in: src/core/graph/BasicBlock.ts:117

Removes the given stmt from this basic block.

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`void`

***

### removeHead()

> **removeHead**(): `void`

Defined in: src/core/graph/BasicBlock.ts:128

Removes the first stmt from this basic block.

#### Returns

`void`

***

### removePredecessorBlock()

> **removePredecessorBlock**(`block`): `boolean`

Defined in: src/core/graph/BasicBlock.ts:214

#### Parameters

##### block

`BasicBlock`

#### Returns

`boolean`

***

### removeSuccessorBlock()

> **removeSuccessorBlock**(`block`): `boolean`

Defined in: src/core/graph/BasicBlock.ts:223

#### Parameters

##### block

`BasicBlock`

#### Returns

`boolean`

***

### removeTail()

> **removeTail**(): `void`

Defined in: src/core/graph/BasicBlock.ts:135

Removes the last stmt from this basic block.

#### Returns

`void`

***

### setId()

> **setId**(`id`): `void`

Defined in: src/core/graph/BasicBlock.ts:44

#### Parameters

##### id

`number`

#### Returns

`void`

***

### setPredecessorBlock()

> **setPredecessorBlock**(`idx`, `block`): `boolean`

Defined in: src/core/graph/BasicBlock.ts:188

#### Parameters

##### idx

`number`

##### block

`BasicBlock`

#### Returns

`boolean`

***

### setSuccessorBlock()

> **setSuccessorBlock**(`idx`, `block`): `boolean`

Defined in: src/core/graph/BasicBlock.ts:196

#### Parameters

##### idx

`number`

##### block

`BasicBlock`

#### Returns

`boolean`

***

### toString()

> **toString**(): `string`

Defined in: src/core/graph/BasicBlock.ts:232

#### Returns

`string`

***

### validate()

> **validate**(): `ArkError`

Defined in: src/core/graph/BasicBlock.ts:240

#### Returns

`ArkError`




============================================================
## FILE: `classes/BigIntType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BigIntType

# Class: BigIntType

Defined in: src/core/base/Type.ts:165

bigint type

## Extends

- [`PrimitiveType`](PrimitiveType.md)

## Methods

### getName()

> **getName**(): `string`

Defined in: src/core/base/Type.ts:128

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`getName`](PrimitiveType.md#getname)

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:132

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`getTypeString`](PrimitiveType.md#gettypestring)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`toString`](PrimitiveType.md#tostring)

***

### getInstance()

> `static` **getInstance**(): `BigIntType`

Defined in: src/core/base/Type.ts:172

#### Returns

`BigIntType`




============================================================
## FILE: `classes/BooleanType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BooleanType

# Class: BooleanType

Defined in: src/core/base/Type.ts:137

primitive type

## Extends

- [`PrimitiveType`](PrimitiveType.md)

## Methods

### getName()

> **getName**(): `string`

Defined in: src/core/base/Type.ts:128

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`getName`](PrimitiveType.md#getname)

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:132

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`getTypeString`](PrimitiveType.md#gettypestring)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`toString`](PrimitiveType.md#tostring)

***

### getInstance()

> `static` **getInstance**(): `BooleanType`

Defined in: src/core/base/Type.ts:144

#### Returns

`BooleanType`




============================================================
## FILE: `classes/CGStat.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / CGStat

# Class: CGStat

Defined in: src/callgraph/common/Statistics.ts:192

## Extends

- `StatTraits`

## Constructors

### Constructor

> **new CGStat**(): `CGStat`

#### Returns

`CGStat`

#### Inherited from

`StatTraits.constructor`

## Properties

### endTime

> **endTime**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:27

#### Inherited from

`StatTraits.endTime`

***

### numBlank

> **numBlank**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:199

***

### numConstructor

> **numConstructor**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:198

***

### numIntrinsic

> **numIntrinsic**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:197

***

### numReal

> **numReal**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:195

***

### numTotalNode

> **numTotalNode**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:194

***

### numVirtual

> **numVirtual**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:196

***

### startTime

> **startTime**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:26

#### Inherited from

`StatTraits.startTime`

***

### TotalTime

> **TotalTime**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:25

#### Inherited from

`StatTraits.TotalTime`

## Methods

### addNodeStat()

> **addNodeStat**(`kind`): `void`

Defined in: src/callgraph/common/Statistics.ts:210

#### Parameters

##### kind

[`CallGraphNodeKind`](../enumerations/CallGraphNodeKind.md)

#### Returns

`void`

***

### endStat()

> **endStat**(): `void`

Defined in: src/callgraph/common/Statistics.ts:205

#### Returns

`void`

***

### getStat()

> **getStat**(): `string`

Defined in: src/callgraph/common/Statistics.ts:230

#### Returns

`string`

#### Overrides

`StatTraits.getStat`

***

### printStat()

> **printStat**(): `void`

Defined in: src/callgraph/common/Statistics.ts:33

#### Returns

`void`

#### Inherited from

`StatTraits.printStat`

***

### startStat()

> **startStat**(): `void`

Defined in: src/callgraph/common/Statistics.ts:201

#### Returns

`void`




============================================================
## FILE: `classes/CSFuncID.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / CSFuncID

# Class: CSFuncID

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:64

## Constructors

### Constructor

> **new CSFuncID**(`cid`, `fid`): `CSFuncID`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:68

#### Parameters

##### cid

`number`

##### fid

`number`

#### Returns

`CSFuncID`

## Properties

### cid

> **cid**: `number`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:65

***

### funcID

> **funcID**: `number`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:66




============================================================
## FILE: `classes/CallGraph.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / CallGraph

# Class: CallGraph

Defined in: src/callgraph/model/CallGraph.ts:122

## Extends

- [`BaseExplicitGraph`](BaseExplicitGraph.md)

## Constructors

### Constructor

> **new CallGraph**(`s`): `CallGraph`

Defined in: src/callgraph/model/CallGraph.ts:136

#### Parameters

##### s

[`Scene`](Scene.md)

#### Returns

`CallGraph`

#### Overrides

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`constructor`](BaseExplicitGraph.md#constructor)

## Properties

### edgeMarkSet

> `protected` **edgeMarkSet**: `Set`\<`string`\>

Defined in: src/core/graph/BaseExplicitGraph.ts:140

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`edgeMarkSet`](BaseExplicitGraph.md#edgemarkset)

***

### edgeNum

> `protected` **edgeNum**: `number` = `0`

Defined in: src/core/graph/BaseExplicitGraph.ts:137

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`edgeNum`](BaseExplicitGraph.md#edgenum)

***

### idToNodeMap

> `protected` **idToNodeMap**: `Map`\<`number`, [`BaseNode`](BaseNode.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:139

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`idToNodeMap`](BaseExplicitGraph.md#idtonodemap)

***

### nodeNum

> `protected` **nodeNum**: `number` = `0`

Defined in: src/core/graph/BaseExplicitGraph.ts:138

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`nodeNum`](BaseExplicitGraph.md#nodenum)

## Methods

### addCallGraphNode()

> **addCallGraphNode**(`method`, `kind`): [`CallGraphNode`](CallGraphNode.md)

Defined in: src/callgraph/model/CallGraph.ts:151

#### Parameters

##### method

[`MethodSignature`](MethodSignature.md)

##### kind

[`CallGraphNodeKind`](../enumerations/CallGraphNodeKind.md) = `CallGraphNodeKind.real`

#### Returns

[`CallGraphNode`](CallGraphNode.md)

***

### addDirectOrSpecialCallEdge()

> **addDirectOrSpecialCallEdge**(`caller`, `callee`, `callStmt`, `isDirectCall`): `void`

Defined in: src/callgraph/model/CallGraph.ts:188

#### Parameters

##### caller

[`MethodSignature`](MethodSignature.md)

##### callee

[`MethodSignature`](MethodSignature.md)

##### callStmt

[`Stmt`](Stmt.md)

##### isDirectCall

`boolean` = `true`

#### Returns

`void`

***

### addDynamicCallEdge()

> **addDynamicCallEdge**(`callerID`, `calleeID`, `callStmt`): `void`

Defined in: src/callgraph/model/CallGraph.ts:246

#### Parameters

##### callerID

`number`

##### calleeID

`number`

##### callStmt

[`Stmt`](Stmt.md)

#### Returns

`void`

***

### addDynamicCallInfo()

> **addDynamicCallInfo**(`callStmt`, `caller`, `protentialCallee?`): `void`

Defined in: src/callgraph/model/CallGraph.ts:234

#### Parameters

##### callStmt

[`Stmt`](Stmt.md)

##### caller

[`MethodSignature`](MethodSignature.md)

##### protentialCallee?

[`MethodSignature`](MethodSignature.md)

#### Returns

`void`

***

### addMethodToCallSiteMap()

> **addMethodToCallSiteMap**(`funcID`, `cs`): `void`

Defined in: src/callgraph/model/CallGraph.ts:278

#### Parameters

##### funcID

`number`

##### cs

[`CallSite`](CallSite.md)

#### Returns

`void`

***

### addNode()

> **addNode**(`n`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:155

#### Parameters

##### n

[`BaseNode`](BaseNode.md)

#### Returns

`void`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`addNode`](BaseExplicitGraph.md#addnode)

***

### addStmtToCallSiteMap()

> **addStmtToCallSiteMap**(`stmt`, `cs`): `boolean`

Defined in: src/callgraph/model/CallGraph.ts:264

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

##### cs

[`CallSite`](CallSite.md)

#### Returns

`boolean`

***

### detectReachable()

> **detectReachable**(`fromID`, `dstID`): `boolean`

Defined in: src/callgraph/model/CallGraph.ts:359

#### Parameters

##### fromID

`number`

##### dstID

`number`

#### Returns

`boolean`

***

### dump()

> **dump**(`name`, `entry?`): `void`

Defined in: src/callgraph/model/CallGraph.ts:351

#### Parameters

##### name

`string`

##### entry?

`number`

#### Returns

`void`

***

### endStat()

> **endStat**(): `void`

Defined in: src/callgraph/model/CallGraph.ts:389

#### Returns

`void`

***

### getArkMethodByFuncID()

> **getArkMethodByFuncID**(`id`): `null` \| [`ArkMethod`](ArkMethod.md)

Defined in: src/callgraph/model/CallGraph.ts:333

#### Parameters

##### id

`number`

#### Returns

`null` \| [`ArkMethod`](ArkMethod.md)

***

### getCallEdgeByPair()

> **getCallEdgeByPair**(`srcID`, `dstID`): `undefined` \| [`CallGraphEdge`](CallGraphEdge.md)

Defined in: src/callgraph/model/CallGraph.ts:146

#### Parameters

##### srcID

`number`

##### dstID

`number`

#### Returns

`undefined` \| [`CallGraphEdge`](CallGraphEdge.md)

***

### getCallGraphNodeByMethod()

> **getCallGraphNodeByMethod**(`method`): [`CallGraphNode`](CallGraphNode.md)

Defined in: src/callgraph/model/CallGraph.ts:172

#### Parameters

##### method

[`MethodSignature`](MethodSignature.md)

#### Returns

[`CallGraphNode`](CallGraphNode.md)

***

### getCallSiteByStmt()

> **getCallSiteByStmt**(`stmt`): [`CallSite`](CallSite.md)[]

Defined in: src/callgraph/model/CallGraph.ts:274

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

[`CallSite`](CallSite.md)[]

***

### getCallSitesByMethod()

> **getCallSitesByMethod**(`func`): `Set`\<[`CallSite`](CallSite.md)\>

Defined in: src/callgraph/model/CallGraph.ts:286

#### Parameters

##### func

`number` | [`MethodSignature`](MethodSignature.md)

#### Returns

`Set`\<[`CallSite`](CallSite.md)\>

***

### getDummyMainFuncID()

> **getDummyMainFuncID**(): `undefined` \| `number`

Defined in: src/callgraph/model/CallGraph.ts:405

#### Returns

`undefined` \| `number`

***

### getDynCallsiteByStmt()

> **getDynCallsiteByStmt**(`stmt`): `undefined` \| [`DynCallSite`](DynCallSite.md)

Defined in: src/callgraph/model/CallGraph.ts:260

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`undefined` \| [`DynCallSite`](DynCallSite.md)

***

### getDynEdges()

> **getDynEdges**(): `Map`\<[`MethodSignature`](MethodSignature.md), `Set`\<[`MethodSignature`](MethodSignature.md)\>\>

Defined in: src/callgraph/model/CallGraph.ts:307

#### Returns

`Map`\<[`MethodSignature`](MethodSignature.md), `Set`\<[`MethodSignature`](MethodSignature.md)\>\>

***

### getEntries()

> **getEntries**(): `number`[]

Defined in: src/callgraph/model/CallGraph.ts:343

#### Returns

`number`[]

***

### getGraphName()

> **getGraphName**(): `string`

Defined in: src/callgraph/model/CallGraph.ts:421

#### Returns

`string`

#### Overrides

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`getGraphName`](BaseExplicitGraph.md#getgraphname)

***

### getInvokeStmtByMethod()

> **getInvokeStmtByMethod**(`func`): [`Stmt`](Stmt.md)[]

Defined in: src/callgraph/model/CallGraph.ts:297

#### Parameters

##### func

`number` | [`MethodSignature`](MethodSignature.md)

#### Returns

[`Stmt`](Stmt.md)[]

***

### getMethodByFuncID()

> **getMethodByFuncID**(`id`): `null` \| [`MethodSignature`](MethodSignature.md)

Defined in: src/callgraph/model/CallGraph.ts:325

#### Parameters

##### id

`number`

#### Returns

`null` \| [`MethodSignature`](MethodSignature.md)

***

### getNode()

> **getNode**(`id`): `undefined` \| [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:160

#### Parameters

##### id

`number`

#### Returns

`undefined` \| [`BaseNode`](BaseNode.md)

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`getNode`](BaseExplicitGraph.md#getnode)

***

### getNodeNum()

> **getNodeNum**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:147

#### Returns

`number`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`getNodeNum`](BaseExplicitGraph.md#getnodenum)

***

### getNodesIter()

> **getNodesIter**(): `IterableIterator`\<[`BaseNode`](BaseNode.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:200

#### Returns

`IterableIterator`\<[`BaseNode`](BaseNode.md)\>

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`getNodesIter`](BaseExplicitGraph.md#getnodesiter)

***

### getStat()

> **getStat**(): `string`

Defined in: src/callgraph/model/CallGraph.ts:397

#### Returns

`string`

***

### hasEdge()

> **hasEdge**(`src`, `dst`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:180

#### Parameters

##### src

[`BaseNode`](BaseNode.md)

##### dst

[`BaseNode`](BaseNode.md)

#### Returns

`boolean`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`hasEdge`](BaseExplicitGraph.md#hasedge)

***

### hasNode()

> **hasNode**(`id`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:168

#### Parameters

##### id

`number`

#### Returns

`boolean`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`hasNode`](BaseExplicitGraph.md#hasnode)

***

### ifEdgeExisting()

> **ifEdgeExisting**(`edge`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:190

#### Parameters

##### edge

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`ifEdgeExisting`](BaseExplicitGraph.md#ifedgeexisting)

***

### isUnknownMethod()

> **isUnknownMethod**(`funcID`): `boolean`

Defined in: src/callgraph/model/CallGraph.ts:409

#### Parameters

##### funcID

`number`

#### Returns

`boolean`

***

### nodesItor()

> **nodesItor**(): `IterableIterator`\<[`BaseNode`](BaseNode.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:151

#### Returns

`IterableIterator`\<[`BaseNode`](BaseNode.md)\>

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`nodesItor`](BaseExplicitGraph.md#nodesitor)

***

### printStat()

> **printStat**(): `void`

Defined in: src/callgraph/model/CallGraph.ts:393

#### Returns

`void`

***

### removeCallGraphEdge()

> **removeCallGraphEdge**(`nodeID`): `void`

Defined in: src/callgraph/model/CallGraph.ts:222

#### Parameters

##### nodeID

`number`

#### Returns

`void`

***

### removeCallGraphNode()

> **removeCallGraphNode**(`nodeID`): `void`

Defined in: src/callgraph/model/CallGraph.ts:163

#### Parameters

##### nodeID

`number`

#### Returns

`void`

***

### removeNode()

> **removeNode**(`id`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:172

#### Parameters

##### id

`number`

#### Returns

`boolean`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`removeNode`](BaseExplicitGraph.md#removenode)

***

### setDummyMainFuncID()

> **setDummyMainFuncID**(`dummyMainMethodID`): `void`

Defined in: src/callgraph/model/CallGraph.ts:401

#### Parameters

##### dummyMainMethodID

`number`

#### Returns

`void`

***

### setEntries()

> **setEntries**(`n`): `void`

Defined in: src/callgraph/model/CallGraph.ts:347

#### Parameters

##### n

`number`[]

#### Returns

`void`

***

### startStat()

> **startStat**(): `void`

Defined in: src/callgraph/model/CallGraph.ts:385

#### Returns

`void`




============================================================
## FILE: `classes/CallGraphBuilder.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / CallGraphBuilder

# Class: CallGraphBuilder

Defined in: src/callgraph/model/builder/CallGraphBuilder.ts:24

## Constructors

### Constructor

> **new CallGraphBuilder**(`c`, `s`): `CallGraphBuilder`

Defined in: src/callgraph/model/builder/CallGraphBuilder.ts:28

#### Parameters

##### c

[`CallGraph`](CallGraph.md)

##### s

[`Scene`](Scene.md)

#### Returns

`CallGraphBuilder`

## Methods

### buildCGNodes()

> **buildCGNodes**(`methods`): `void`

Defined in: src/callgraph/model/builder/CallGraphBuilder.ts:44

#### Parameters

##### methods

[`ArkMethod`](ArkMethod.md)[]

#### Returns

`void`

***

### buildCHA4WholeProject()

> **buildCHA4WholeProject**(`displayGeneratedMethod`): `void`

Defined in: src/callgraph/model/builder/CallGraphBuilder.ts:103

#### Parameters

##### displayGeneratedMethod

`boolean` = `false`

#### Returns

`void`

***

### buildClassHierarchyCallGraph()

> **buildClassHierarchyCallGraph**(`entries`, `displayGeneratedMethod`): `void`

Defined in: src/callgraph/model/builder/CallGraphBuilder.ts:92

#### Parameters

##### entries

[`MethodSignature`](MethodSignature.md)[]

##### displayGeneratedMethod

`boolean` = `false`

#### Returns

`void`

***

### buildDirectCallGraph()

> **buildDirectCallGraph**(`methods`): `void`

Defined in: src/callgraph/model/builder/CallGraphBuilder.ts:60

#### Parameters

##### methods

[`ArkMethod`](ArkMethod.md)[]

#### Returns

`void`

***

### buildDirectCallGraphForScene()

> **buildDirectCallGraphForScene**(): `void`

Defined in: src/callgraph/model/builder/CallGraphBuilder.ts:33

#### Returns

`void`

***

### buildRapidTypeCallGraph()

> **buildRapidTypeCallGraph**(`entries`, `displayGeneratedMethod`): `void`

Defined in: src/callgraph/model/builder/CallGraphBuilder.ts:108

#### Parameters

##### entries

[`MethodSignature`](MethodSignature.md)[]

##### displayGeneratedMethod

`boolean` = `false`

#### Returns

`void`

***

### setEntries()

> **setEntries**(): `void`

Defined in: src/callgraph/model/builder/CallGraphBuilder.ts:128

#### Returns

`void`




============================================================
## FILE: `classes/CallGraphEdge.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / CallGraphEdge

# Class: CallGraphEdge

Defined in: src/callgraph/model/CallGraph.ts:41

## Extends

- [`BaseEdge`](BaseEdge.md)

## Constructors

### Constructor

> **new CallGraphEdge**(`src`, `dst`): `CallGraphEdge`

Defined in: src/callgraph/model/CallGraph.ts:47

#### Parameters

##### src

[`CallGraphNode`](CallGraphNode.md)

##### dst

[`CallGraphNode`](CallGraphNode.md)

#### Returns

`CallGraphEdge`

#### Overrides

[`BaseEdge`](BaseEdge.md).[`constructor`](BaseEdge.md#constructor)

## Properties

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:22

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`kind`](BaseEdge.md#kind)

## Methods

### addDirectCallSite()

> **addDirectCallSite**(`stmt`): `void`

Defined in: src/callgraph/model/CallGraph.ts:51

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`void`

***

### addInDirectCallSite()

> **addInDirectCallSite**(`stmt`): `void`

Defined in: src/callgraph/model/CallGraph.ts:59

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`void`

***

### addSpecialCallSite()

> **addSpecialCallSite**(`stmt`): `void`

Defined in: src/callgraph/model/CallGraph.ts:55

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`void`

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/model/CallGraph.ts:63

#### Returns

`string`

#### Overrides

[`BaseEdge`](BaseEdge.md).[`getDotAttr`](BaseEdge.md#getdotattr)

***

### getDstID()

> **getDstID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:34

#### Returns

`number`

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`getDstID`](BaseEdge.md#getdstid)

***

### getDstNode()

> **getDstNode**(): [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:42

#### Returns

[`BaseNode`](BaseNode.md)

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`getDstNode`](BaseEdge.md#getdstnode)

***

### getEndPoints()

> **getEndPoints**(): `object`

Defined in: src/core/graph/BaseExplicitGraph.ts:54

#### Returns

`object`

##### dst

> **dst**: `number`

##### src

> **src**: `number`

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`getEndPoints`](BaseEdge.md#getendpoints)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:46

#### Returns

`number`

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`getKind`](BaseEdge.md#getkind)

***

### getSrcID()

> **getSrcID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:30

#### Returns

`number`

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`getSrcID`](BaseEdge.md#getsrcid)

***

### getSrcNode()

> **getSrcNode**(): [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:38

#### Returns

[`BaseNode`](BaseNode.md)

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`getSrcNode`](BaseEdge.md#getsrcnode)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:50

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`setKind`](BaseEdge.md#setkind)




============================================================
## FILE: `classes/CallGraphNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / CallGraphNode

# Class: CallGraphNode

Defined in: src/callgraph/model/CallGraph.ts:83

## Extends

- [`BaseNode`](BaseNode.md)

## Constructors

### Constructor

> **new CallGraphNode**(`id`, `m`, `k`): `CallGraphNode`

Defined in: src/callgraph/model/CallGraph.ts:87

#### Parameters

##### id

`number`

##### m

[`MethodSignature`](MethodSignature.md)

##### k

[`CallGraphNodeKind`](../enumerations/CallGraphNodeKind.md) = `CallGraphNodeKind.real`

#### Returns

`CallGraphNode`

#### Overrides

[`BaseNode`](BaseNode.md).[`constructor`](BaseNode.md#constructor)

## Properties

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:68

#### Inherited from

[`BaseNode`](BaseNode.md).[`kind`](BaseNode.md#kind)

## Accessors

### isBlankMethod

#### Get Signature

> **get** **isBlankMethod**(): `boolean`

Defined in: src/callgraph/model/CallGraph.ts:104

##### Returns

`boolean`

## Methods

### addIncomingEdge()

> **addIncomingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:105

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`BaseNode`](BaseNode.md).[`addIncomingEdge`](BaseNode.md#addincomingedge)

***

### addOutgoingEdge()

> **addOutgoingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:109

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`BaseNode`](BaseNode.md).[`addOutgoingEdge`](BaseNode.md#addoutgoingedge)

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/model/CallGraph.ts:108

#### Returns

`string`

#### Overrides

[`BaseNode`](BaseNode.md).[`getDotAttr`](BaseNode.md#getdotattr)

***

### getDotLabel()

> **getDotLabel**(): `string`

Defined in: src/callgraph/model/CallGraph.ts:115

#### Returns

`string`

#### Overrides

[`BaseNode`](BaseNode.md).[`getDotLabel`](BaseNode.md#getdotlabel)

***

### getID()

> **getID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:77

#### Returns

`number`

#### Inherited from

[`BaseNode`](BaseNode.md).[`getID`](BaseNode.md#getid)

***

### getIncomingEdge()

> **getIncomingEdge**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:121

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`BaseNode`](BaseNode.md).[`getIncomingEdge`](BaseNode.md#getincomingedge)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:81

#### Returns

`number`

#### Inherited from

[`BaseNode`](BaseNode.md).[`getKind`](BaseNode.md#getkind)

***

### getMethod()

> **getMethod**(): [`MethodSignature`](MethodSignature.md)

Defined in: src/callgraph/model/CallGraph.ts:92

#### Returns

[`MethodSignature`](MethodSignature.md)

***

### getOutgoingEdges()

> **getOutgoingEdges**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:125

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`BaseNode`](BaseNode.md).[`getOutgoingEdges`](BaseNode.md#getoutgoingedges)

***

### hasIncomingEdge()

> **hasIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:97

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`BaseNode`](BaseNode.md).[`hasIncomingEdge`](BaseNode.md#hasincomingedge)

***

### hasIncomingEdges()

> **hasIncomingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:89

#### Returns

`boolean`

#### Inherited from

[`BaseNode`](BaseNode.md).[`hasIncomingEdges`](BaseNode.md#hasincomingedges)

***

### hasOutgoingEdge()

> **hasOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:101

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`BaseNode`](BaseNode.md).[`hasOutgoingEdge`](BaseNode.md#hasoutgoingedge)

***

### hasOutgoingEdges()

> **hasOutgoingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:93

#### Returns

`boolean`

#### Inherited from

[`BaseNode`](BaseNode.md).[`hasOutgoingEdges`](BaseNode.md#hasoutgoingedges)

***

### isSdkMethod()

> **isSdkMethod**(): `boolean`

Defined in: src/callgraph/model/CallGraph.ts:100

#### Returns

`boolean`

***

### removeIncomingEdge()

> **removeIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:113

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`BaseNode`](BaseNode.md).[`removeIncomingEdge`](BaseNode.md#removeincomingedge)

***

### removeOutgoingEdge()

> **removeOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:117

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`BaseNode`](BaseNode.md).[`removeOutgoingEdge`](BaseNode.md#removeoutgoingedge)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:85

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`BaseNode`](BaseNode.md).[`setKind`](BaseNode.md#setkind)

***

### setSdkMethod()

> **setSdkMethod**(`v`): `void`

Defined in: src/callgraph/model/CallGraph.ts:96

#### Parameters

##### v

`boolean`

#### Returns

`void`




============================================================
## FILE: `classes/CallSite.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / CallSite

# Class: CallSite

Defined in: src/callgraph/model/CallSite.ts:29

## Implements

- [`ICallSite`](../interfaces/ICallSite.md)

## Constructors

### Constructor

> **new CallSite**(`s`, `a`, `ce`, `cr`): `CallSite`

Defined in: src/callgraph/model/CallSite.ts:35

#### Parameters

##### s

[`Stmt`](Stmt.md)

##### a

`undefined` | [`Value`](../interfaces/Value.md)[]

##### ce

`number`

##### cr

`number`

#### Returns

`CallSite`

## Properties

### args

> **args**: `undefined` \| [`Value`](../interfaces/Value.md)[]

Defined in: src/callgraph/model/CallSite.ts:31

#### Implementation of

[`ICallSite`](../interfaces/ICallSite.md).[`args`](../interfaces/ICallSite.md#args)

***

### calleeFuncID

> **calleeFuncID**: `number`

Defined in: src/callgraph/model/CallSite.ts:32

***

### callerFuncID

> **callerFuncID**: `number`

Defined in: src/callgraph/model/CallSite.ts:33

#### Implementation of

[`ICallSite`](../interfaces/ICallSite.md).[`callerFuncID`](../interfaces/ICallSite.md#callerfuncid)

***

### callStmt

> **callStmt**: [`Stmt`](Stmt.md)

Defined in: src/callgraph/model/CallSite.ts:30

#### Implementation of

[`ICallSite`](../interfaces/ICallSite.md).[`callStmt`](../interfaces/ICallSite.md#callstmt)




============================================================
## FILE: `classes/Cfg.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Cfg

# Class: Cfg

Defined in: src/core/graph/Cfg.ts:30

## Constructors

### Constructor

> **new Cfg**(): `Cfg`

Defined in: src/core/graph/Cfg.ts:38

#### Returns

`Cfg`

## Methods

### addBlock()

> **addBlock**(`block`): `void`

Defined in: src/core/graph/Cfg.ts:114

#### Parameters

##### block

[`BasicBlock`](BasicBlock.md)

#### Returns

`void`

***

### buildDefUseChain()

> **buildDefUseChain**(): `void`

Defined in: src/core/graph/Cfg.ts:230

#### Returns

`void`

***

### buildDefUseStmt()

> **buildDefUseStmt**(`locals`): `void`

Defined in: src/core/graph/Cfg.ts:155

#### Parameters

##### locals

`Set`\<[`Local`](Local.md)\>

#### Returns

`void`

***

### getBlocks()

> **getBlocks**(): `Set`\<[`BasicBlock`](BasicBlock.md)\>

Defined in: src/core/graph/Cfg.ts:122

#### Returns

`Set`\<[`BasicBlock`](BasicBlock.md)\>

***

### getDeclaringMethod()

> **getDeclaringMethod**(): [`ArkMethod`](ArkMethod.md)

Defined in: src/core/graph/Cfg.ts:138

#### Returns

[`ArkMethod`](ArkMethod.md)

***

### getDefUseChains()

> **getDefUseChains**(): [`DefUseChain`](DefUseChain.md)[]

Defined in: src/core/graph/Cfg.ts:146

#### Returns

[`DefUseChain`](DefUseChain.md)[]

***

### getStartingBlock()

> **getStartingBlock**(): `undefined` \| [`BasicBlock`](BasicBlock.md)

Defined in: src/core/graph/Cfg.ts:126

#### Returns

`undefined` \| [`BasicBlock`](BasicBlock.md)

***

### getStartingStmt()

> **getStartingStmt**(): [`Stmt`](Stmt.md)

Defined in: src/core/graph/Cfg.ts:130

#### Returns

[`Stmt`](Stmt.md)

***

### getStmts()

> **getStmts**(): [`Stmt`](Stmt.md)[]

Defined in: src/core/graph/Cfg.ts:40

#### Returns

[`Stmt`](Stmt.md)[]

***

### getUnreachableBlocks()

> **getUnreachableBlocks**(): `Set`\<[`BasicBlock`](BasicBlock.md)\>

Defined in: src/core/graph/Cfg.ts:241

#### Returns

`Set`\<[`BasicBlock`](BasicBlock.md)\>

***

### insertAfter()

> **insertAfter**(`toInsert`, `point`): `number`

Defined in: src/core/graph/Cfg.ts:54

Inserts toInsert in the basic block in CFG after point.

#### Parameters

##### toInsert

[`Stmt`](Stmt.md) | [`Stmt`](Stmt.md)[]

##### point

[`Stmt`](Stmt.md)

#### Returns

`number`

The number of successfully inserted statements

***

### insertBefore()

> **insertBefore**(`toInsert`, `point`): `number`

Defined in: src/core/graph/Cfg.ts:70

Inserts toInsert in the basic block in CFG befor point.

#### Parameters

##### toInsert

[`Stmt`](Stmt.md) | [`Stmt`](Stmt.md)[]

##### point

[`Stmt`](Stmt.md)

#### Returns

`number`

The number of successfully inserted statements

***

### remove()

> **remove**(`stmt`): `void`

Defined in: src/core/graph/Cfg.ts:85

Removes the given stmt from the basic block in CFG.

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`void`

***

### setDeclaringMethod()

> **setDeclaringMethod**(`method`): `void`

Defined in: src/core/graph/Cfg.ts:142

#### Parameters

##### method

[`ArkMethod`](ArkMethod.md)

#### Returns

`void`

***

### setStartingStmt()

> **setStartingStmt**(`newStartingStmt`): `void`

Defined in: src/core/graph/Cfg.ts:134

#### Parameters

##### newStartingStmt

[`Stmt`](Stmt.md)

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/graph/Cfg.ts:151

#### Returns

`string`

***

### updateStmt2BlockMap()

> **updateStmt2BlockMap**(`block`, `changed?`): `void`

Defined in: src/core/graph/Cfg.ts:99

Update stmtToBlock Map

#### Parameters

##### block

[`BasicBlock`](BasicBlock.md)

##### changed?

[`Stmt`](Stmt.md) | [`Stmt`](Stmt.md)[]

#### Returns

`void`

***

### validate()

> **validate**(): `ArkError`

Defined in: src/core/graph/Cfg.ts:256

#### Returns

`ArkError`




============================================================
## FILE: `classes/ClassHierarchyAnalysis.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ClassHierarchyAnalysis

# Class: ClassHierarchyAnalysis

Defined in: src/callgraph/algorithm/ClassHierarchyAnalysis.ts:25

## Extends

- [`AbstractAnalysis`](AbstractAnalysis.md)

## Constructors

### Constructor

> **new ClassHierarchyAnalysis**(`scene`, `cg`, `cb`): `ClassHierarchyAnalysis`

Defined in: src/callgraph/algorithm/ClassHierarchyAnalysis.ts:26

#### Parameters

##### scene

[`Scene`](Scene.md)

##### cg

[`CallGraph`](CallGraph.md)

##### cb

[`CallGraphBuilder`](CallGraphBuilder.md)

#### Returns

`ClassHierarchyAnalysis`

#### Overrides

[`AbstractAnalysis`](AbstractAnalysis.md).[`constructor`](AbstractAnalysis.md#constructor)

## Properties

### cg

> `protected` **cg**: [`CallGraph`](CallGraph.md)

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:33

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`cg`](AbstractAnalysis.md#cg)

***

### cgBuilder

> `protected` **cgBuilder**: [`CallGraphBuilder`](CallGraphBuilder.md)

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:34

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`cgBuilder`](AbstractAnalysis.md#cgbuilder)

***

### processedMethod

> `protected` **processedMethod**: `IPtsCollection`\<`number`\>

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:36

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`processedMethod`](AbstractAnalysis.md#processedmethod)

***

### scene

> `protected` **scene**: [`Scene`](Scene.md)

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:32

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`scene`](AbstractAnalysis.md#scene)

***

### workList

> `protected` **workList**: `number`[] = `[]`

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:35

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`workList`](AbstractAnalysis.md#worklist)

## Methods

### addCallGraphEdge()

> `protected` **addCallGraphEdge**(`caller`, `callee`, `cs`, `displayGeneratedMethod`): `void`

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:186

#### Parameters

##### caller

`number`

##### callee

`null` | [`ArkMethod`](ArkMethod.md)

##### cs

[`CallSite`](CallSite.md)

##### displayGeneratedMethod

`boolean`

#### Returns

`void`

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`addCallGraphEdge`](AbstractAnalysis.md#addcallgraphedge)

***

### getCallGraph()

> **getCallGraph**(): [`CallGraph`](CallGraph.md)

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:47

#### Returns

[`CallGraph`](CallGraph.md)

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`getCallGraph`](AbstractAnalysis.md#getcallgraph)

***

### getClassHierarchy()

> **getClassHierarchy**(`arkClass`): [`ArkClass`](ArkClass.md)[]

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:62

#### Parameters

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

[`ArkClass`](ArkClass.md)[]

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`getClassHierarchy`](AbstractAnalysis.md#getclasshierarchy)

***

### getParamAnonymousMethod()

> `protected` **getParamAnonymousMethod**(`invokeExpr`): [`MethodSignature`](MethodSignature.md)[]

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:173

#### Parameters

##### invokeExpr

[`AbstractInvokeExpr`](AbstractInvokeExpr.md)

#### Returns

[`MethodSignature`](MethodSignature.md)[]

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`getParamAnonymousMethod`](AbstractAnalysis.md#getparamanonymousmethod)

***

### getScene()

> **getScene**(): [`Scene`](Scene.md)

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:43

#### Returns

[`Scene`](Scene.md)

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`getScene`](AbstractAnalysis.md#getscene)

***

### init()

> `protected` **init**(): `void`

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:140

#### Returns

`void`

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`init`](AbstractAnalysis.md#init)

***

### preProcessMethod()

> `protected` **preProcessMethod**(): [`CallSite`](CallSite.md)[]

Defined in: src/callgraph/algorithm/ClassHierarchyAnalysis.ts:81

#### Returns

[`CallSite`](CallSite.md)[]

#### Overrides

[`AbstractAnalysis`](AbstractAnalysis.md).[`preProcessMethod`](AbstractAnalysis.md#preprocessmethod)

***

### processMethod()

> `protected` **processMethod**(`methodID`): [`CallSite`](CallSite.md)[]

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:147

#### Parameters

##### methodID

`number`

#### Returns

[`CallSite`](CallSite.md)[]

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`processMethod`](AbstractAnalysis.md#processmethod)

***

### projectStart()

> **projectStart**(`displayGeneratedMethod`): `void`

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:99

#### Parameters

##### displayGeneratedMethod

`boolean`

#### Returns

`void`

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`projectStart`](AbstractAnalysis.md#projectstart)

***

### resolveCall()

> **resolveCall**(`callerMethod`, `invokeStmt`): [`CallSite`](CallSite.md)[]

Defined in: src/callgraph/algorithm/ClassHierarchyAnalysis.ts:31

#### Parameters

##### callerMethod

`number`

##### invokeStmt

[`Stmt`](Stmt.md)

#### Returns

[`CallSite`](CallSite.md)[]

#### Overrides

[`AbstractAnalysis`](AbstractAnalysis.md).[`resolveCall`](AbstractAnalysis.md#resolvecall)

***

### resolveInvokeExpr()

> **resolveInvokeExpr**(`invokeExpr`): `undefined` \| [`ArkMethod`](ArkMethod.md)

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:54

#### Parameters

##### invokeExpr

[`AbstractInvokeExpr`](AbstractInvokeExpr.md)

#### Returns

`undefined` \| [`ArkMethod`](ArkMethod.md)

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`resolveInvokeExpr`](AbstractAnalysis.md#resolveinvokeexpr)

***

### start()

> **start**(`displayGeneratedMethod`): `void`

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:78

#### Parameters

##### displayGeneratedMethod

`boolean`

#### Returns

`void`

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`start`](AbstractAnalysis.md#start)




============================================================
## FILE: `classes/ClassSignature.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ClassSignature

# Class: ClassSignature

Defined in: src/core/model/ArkSignature.ts:112

## Extended by

- [`AliasClassSignature`](AliasClassSignature.md)

## Constructors

### Constructor

> **new ClassSignature**(`className`, `declaringFileSignature`, `declaringNamespaceSignature`): `ClassSignature`

Defined in: src/core/model/ArkSignature.ts:119

#### Parameters

##### className

`string`

##### declaringFileSignature

[`FileSignature`](FileSignature.md)

##### declaringNamespaceSignature

`null` | [`NamespaceSignature`](NamespaceSignature.md)

#### Returns

`ClassSignature`

## Properties

### DEFAULT

> `readonly` `static` **DEFAULT**: `ClassSignature`

Defined in: src/core/model/ArkSignature.ts:117

## Methods

### getClassName()

> **getClassName**(): `string`

Defined in: src/core/model/ArkSignature.ts:145

Get the **string** name of class from the the class signature. The default value is `""`.

#### Returns

`string`

The name of this class.

***

### getDeclaringClassName()

> **getDeclaringClassName**(): `string`

Defined in: src/core/model/ArkSignature.ts:153

#### Returns

`string`

The name of the declare class.

***

### getDeclaringFileSignature()

> **getDeclaringFileSignature**(): [`FileSignature`](FileSignature.md)

Defined in: src/core/model/ArkSignature.ts:129

Returns the declaring file signature.

#### Returns

[`FileSignature`](FileSignature.md)

The declaring file signature.

***

### getDeclaringNamespaceSignature()

> **getDeclaringNamespaceSignature**(): `null` \| [`NamespaceSignature`](NamespaceSignature.md)

Defined in: src/core/model/ArkSignature.ts:137

Get the declaring namespace's signature.

#### Returns

`null` \| [`NamespaceSignature`](NamespaceSignature.md)

the declaring namespace's signature.

***

### getType()

> **getType**(): [`ClassType`](ClassType.md)

Defined in: src/core/model/ArkSignature.ts:168

#### Returns

[`ClassType`](ClassType.md)

***

### setClassName()

> **setClassName**(`className`): `void`

Defined in: src/core/model/ArkSignature.ts:164

#### Parameters

##### className

`string`

#### Returns

`void`

***

### toMapKey()

> **toMapKey**(): `string`

Defined in: src/core/model/ArkSignature.ts:180

#### Returns

`string`

***

### toString()

> **toString**(): `string`

Defined in: src/core/model/ArkSignature.ts:172

#### Returns

`string`




============================================================
## FILE: `classes/ClassType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ClassType

# Class: ClassType

Defined in: src/core/base/Type.ts:413

type of an object

## Extends

- [`Type`](Type.md)

## Constructors

### Constructor

> **new ClassType**(`classSignature`, `realGenericTypes?`): `ClassType`

Defined in: src/core/base/Type.ts:417

#### Parameters

##### classSignature

[`ClassSignature`](ClassSignature.md)

##### realGenericTypes?

[`Type`](Type.md)[]

#### Returns

`ClassType`

#### Overrides

[`Type`](Type.md).[`constructor`](Type.md#constructor)

## Methods

### getClassSignature()

> **getClassSignature**(): [`ClassSignature`](ClassSignature.md)

Defined in: src/core/base/Type.ts:423

#### Returns

[`ClassSignature`](ClassSignature.md)

***

### getRealGenericTypes()

> **getRealGenericTypes**(): `undefined` \| [`Type`](Type.md)[]

Defined in: src/core/base/Type.ts:431

#### Returns

`undefined` \| [`Type`](Type.md)[]

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:439

#### Returns

`string`

#### Overrides

[`Type`](Type.md).[`getTypeString`](Type.md#gettypestring)

***

### setClassSignature()

> **setClassSignature**(`newClassSignature`): `void`

Defined in: src/core/base/Type.ts:427

#### Parameters

##### newClassSignature

[`ClassSignature`](ClassSignature.md)

#### Returns

`void`

***

### setRealGenericTypes()

> **setRealGenericTypes**(`types`): `void`

Defined in: src/core/base/Type.ts:435

#### Parameters

##### types

`undefined` | [`Type`](Type.md)[]

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`Type`](Type.md).[`toString`](Type.md#tostring)




============================================================
## FILE: `classes/ClosureFieldRef.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ClosureFieldRef

# Class: ClosureFieldRef

Defined in: src/core/base/Ref.ts:365

## Extends

- [`AbstractRef`](AbstractRef.md)

## Constructors

### Constructor

> **new ClosureFieldRef**(`base`, `fieldName`, `type`): `ClosureFieldRef`

Defined in: src/core/base/Ref.ts:370

#### Parameters

##### base

[`Local`](Local.md)

##### fieldName

`string`

##### type

[`Type`](Type.md)

#### Returns

`ClosureFieldRef`

#### Overrides

[`AbstractRef`](AbstractRef.md).[`constructor`](AbstractRef.md#constructor)

## Methods

### getBase()

> **getBase**(): [`Local`](Local.md)

Defined in: src/core/base/Ref.ts:381

#### Returns

[`Local`](Local.md)

***

### getFieldName()

> **getFieldName**(): `string`

Defined in: src/core/base/Ref.ts:389

#### Returns

`string`

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Ref.ts:385

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`Type`](Type.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Overrides

[`AbstractRef`](AbstractRef.md).[`getType`](AbstractRef.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Ref.ts:377

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Overrides

[`AbstractRef`](AbstractRef.md).[`getUses`](AbstractRef.md#getuses)

***

### inferType()

> **inferType**(`arkMethod`): [`AbstractRef`](AbstractRef.md)

Defined in: src/core/base/Ref.ts:397

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

[`AbstractRef`](AbstractRef.md)

#### Overrides

[`AbstractRef`](AbstractRef.md).[`inferType`](AbstractRef.md#infertype)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Ref.ts:393

Returns a string representation of an object.

#### Returns

`string`




============================================================
## FILE: `classes/ClosureType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ClosureType

# Class: ClosureType

Defined in: src/core/base/Type.ts:392

types for closures which is a special FunctionType with a lexical env

## Extends

- [`FunctionType`](FunctionType.md)

## Constructors

### Constructor

> **new ClosureType**(`lexicalEnv`, `methodSignature`, `realGenericTypes?`): `ClosureType`

Defined in: src/core/base/Type.ts:395

#### Parameters

##### lexicalEnv

[`LexicalEnvType`](LexicalEnvType.md)

##### methodSignature

[`MethodSignature`](MethodSignature.md)

##### realGenericTypes?

[`Type`](Type.md)[]

#### Returns

`ClosureType`

#### Overrides

[`FunctionType`](FunctionType.md).[`constructor`](FunctionType.md#constructor)

## Methods

### getLexicalEnv()

> **getLexicalEnv**(): [`LexicalEnvType`](LexicalEnvType.md)

Defined in: src/core/base/Type.ts:400

#### Returns

[`LexicalEnvType`](LexicalEnvType.md)

***

### getMethodSignature()

> **getMethodSignature**(): [`MethodSignature`](MethodSignature.md)

Defined in: src/core/base/Type.ts:375

#### Returns

[`MethodSignature`](MethodSignature.md)

#### Inherited from

[`FunctionType`](FunctionType.md).[`getMethodSignature`](FunctionType.md#getmethodsignature)

***

### getRealGenericTypes()

> **getRealGenericTypes**(): `undefined` \| [`Type`](Type.md)[]

Defined in: src/core/base/Type.ts:379

#### Returns

`undefined` \| [`Type`](Type.md)[]

#### Inherited from

[`FunctionType`](FunctionType.md).[`getRealGenericTypes`](FunctionType.md#getrealgenerictypes)

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:404

#### Returns

`string`

#### Overrides

[`FunctionType`](FunctionType.md).[`getTypeString`](FunctionType.md#gettypestring)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`FunctionType`](FunctionType.md).[`toString`](FunctionType.md#tostring)




============================================================
## FILE: `classes/Constant.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Constant

# Class: Constant

Defined in: src/core/base/Constant.ts:23

## Implements

- [`Value`](../interfaces/Value.md)

## Constructors

### Constructor

> **new Constant**(`value`, `type`): `Constant`

Defined in: src/core/base/Constant.ts:27

#### Parameters

##### value

`string`

##### type

[`Type`](Type.md)

#### Returns

`Constant`

## Methods

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Constant.ts:48

Returns the type of this constant.

#### Returns

[`Type`](Type.md)

The type of this constant.

#### Implementation of

[`Value`](../interfaces/Value.md).[`getType`](../interfaces/Value.md#gettype)

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Constant.ts:40

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Implementation of

[`Value`](../interfaces/Value.md).[`getUses`](../interfaces/Value.md#getuses)

***

### getValue()

> **getValue**(): `string`

Defined in: src/core/base/Constant.ts:36

Returns the constant's value as a **string**.

#### Returns

`string`

The constant's value.

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Constant.ts:56

Get a string of constant value in Constant.

#### Returns

`string`

The string of constant value.




============================================================
## FILE: `classes/CopyPagEdge.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / CopyPagEdge

# Class: CopyPagEdge

Defined in: src/callgraph/pointerAnalysis/Pag.ts:104

## Extends

- [`PagEdge`](PagEdge.md)

## Constructors

### Constructor

> **new CopyPagEdge**(`n`, `d`, `s`): `CopyPagEdge`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:105

#### Parameters

##### n

[`PagNode`](PagNode.md)

##### d

[`PagNode`](PagNode.md)

##### s

[`Stmt`](Stmt.md)

#### Returns

`CopyPagEdge`

#### Overrides

[`PagEdge`](PagEdge.md).[`constructor`](PagEdge.md#constructor)

## Properties

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:22

#### Inherited from

[`PagEdge`](PagEdge.md).[`kind`](PagEdge.md#kind)

## Methods

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:75

#### Returns

`string`

#### Inherited from

[`PagEdge`](PagEdge.md).[`getDotAttr`](PagEdge.md#getdotattr)

***

### getDstID()

> **getDstID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:34

#### Returns

`number`

#### Inherited from

[`PagEdge`](PagEdge.md).[`getDstID`](PagEdge.md#getdstid)

***

### getDstNode()

> **getDstNode**(): [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:42

#### Returns

[`BaseNode`](BaseNode.md)

#### Inherited from

[`PagEdge`](PagEdge.md).[`getDstNode`](PagEdge.md#getdstnode)

***

### getEndPoints()

> **getEndPoints**(): `object`

Defined in: src/core/graph/BaseExplicitGraph.ts:54

#### Returns

`object`

##### dst

> **dst**: `number`

##### src

> **src**: `number`

#### Inherited from

[`PagEdge`](PagEdge.md).[`getEndPoints`](PagEdge.md#getendpoints)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:46

#### Returns

`number`

#### Inherited from

[`PagEdge`](PagEdge.md).[`getKind`](PagEdge.md#getkind)

***

### getSrcID()

> **getSrcID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:30

#### Returns

`number`

#### Inherited from

[`PagEdge`](PagEdge.md).[`getSrcID`](PagEdge.md#getsrcid)

***

### getSrcNode()

> **getSrcNode**(): [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:38

#### Returns

[`BaseNode`](BaseNode.md)

#### Inherited from

[`PagEdge`](PagEdge.md).[`getSrcNode`](PagEdge.md#getsrcnode)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:50

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`PagEdge`](PagEdge.md).[`setKind`](PagEdge.md#setkind)




============================================================
## FILE: `classes/DVFG.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DVFG

# Class: DVFG

Defined in: src/VFG/DVFG.ts:25

Direct value flow graph
Consist of stmt(node) and direct Def-Use edge
Is basic of VFG. And VFG is building on DVFG

## Extends

- [`BaseExplicitGraph`](BaseExplicitGraph.md)

## Constructors

### Constructor

> **new DVFG**(`cg`): `DVFG`

Defined in: src/VFG/DVFG.ts:28

#### Parameters

##### cg

[`CallGraph`](CallGraph.md)

#### Returns

`DVFG`

#### Overrides

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`constructor`](BaseExplicitGraph.md#constructor)

## Properties

### edgeMarkSet

> `protected` **edgeMarkSet**: `Set`\<`string`\>

Defined in: src/core/graph/BaseExplicitGraph.ts:140

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`edgeMarkSet`](BaseExplicitGraph.md#edgemarkset)

***

### edgeNum

> `protected` **edgeNum**: `number` = `0`

Defined in: src/core/graph/BaseExplicitGraph.ts:137

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`edgeNum`](BaseExplicitGraph.md#edgenum)

***

### idToNodeMap

> `protected` **idToNodeMap**: `Map`\<`number`, [`BaseNode`](BaseNode.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:139

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`idToNodeMap`](BaseExplicitGraph.md#idtonodemap)

***

### nodeNum

> `protected` **nodeNum**: `number` = `0`

Defined in: src/core/graph/BaseExplicitGraph.ts:138

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`nodeNum`](BaseExplicitGraph.md#nodenum)

## Methods

### addDVFGEdge()

> **addDVFGEdge**(`src`, `dst`): `boolean`

Defined in: src/VFG/DVFG.ts:68

#### Parameters

##### src

`DVFGNode`

##### dst

`DVFGNode`

#### Returns

`boolean`

***

### addDVFGNode()

> **addDVFGNode**(`stmt`, `kind`): `DVFGNode`

Defined in: src/VFG/DVFG.ts:59

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

##### kind

`DVFGNodeKind`

#### Returns

`DVFGNode`

***

### addNode()

> **addNode**(`n`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:155

#### Parameters

##### n

[`BaseNode`](BaseNode.md)

#### Returns

`void`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`addNode`](BaseExplicitGraph.md#addnode)

***

### dump()

> **dump**(`name`): `void`

Defined in: src/VFG/DVFG.ts:81

#### Parameters

##### name

`string`

#### Returns

`void`

***

### getCG()

> **getCG**(): [`CallGraph`](CallGraph.md)

Defined in: src/VFG/DVFG.ts:34

#### Returns

[`CallGraph`](CallGraph.md)

***

### getGraphName()

> **getGraphName**(): `string`

Defined in: src/VFG/DVFG.ts:38

#### Returns

`string`

#### Overrides

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`getGraphName`](BaseExplicitGraph.md#getgraphname)

***

### getNode()

> **getNode**(`id`): `undefined` \| [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:160

#### Parameters

##### id

`number`

#### Returns

`undefined` \| [`BaseNode`](BaseNode.md)

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`getNode`](BaseExplicitGraph.md#getnode)

***

### getNodeNum()

> **getNodeNum**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:147

#### Returns

`number`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`getNodeNum`](BaseExplicitGraph.md#getnodenum)

***

### getNodesIter()

> **getNodesIter**(): `IterableIterator`\<[`BaseNode`](BaseNode.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:200

#### Returns

`IterableIterator`\<[`BaseNode`](BaseNode.md)\>

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`getNodesIter`](BaseExplicitGraph.md#getnodesiter)

***

### getOrNewDVFGNode()

> **getOrNewDVFGNode**(`stmt`): `DVFGNode`

Defined in: src/VFG/DVFG.ts:42

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`DVFGNode`

***

### hasEdge()

> **hasEdge**(`src`, `dst`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:180

#### Parameters

##### src

[`BaseNode`](BaseNode.md)

##### dst

[`BaseNode`](BaseNode.md)

#### Returns

`boolean`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`hasEdge`](BaseExplicitGraph.md#hasedge)

***

### hasNode()

> **hasNode**(`id`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:168

#### Parameters

##### id

`number`

#### Returns

`boolean`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`hasNode`](BaseExplicitGraph.md#hasnode)

***

### ifEdgeExisting()

> **ifEdgeExisting**(`edge`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:190

#### Parameters

##### edge

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`ifEdgeExisting`](BaseExplicitGraph.md#ifedgeexisting)

***

### nodesItor()

> **nodesItor**(): `IterableIterator`\<[`BaseNode`](BaseNode.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:151

#### Returns

`IterableIterator`\<[`BaseNode`](BaseNode.md)\>

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`nodesItor`](BaseExplicitGraph.md#nodesitor)

***

### removeNode()

> **removeNode**(`id`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:172

#### Parameters

##### id

`number`

#### Returns

`boolean`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`removeNode`](BaseExplicitGraph.md#removenode)




============================================================
## FILE: `classes/DVFGBuilder.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DVFGBuilder

# Class: DVFGBuilder

Defined in: src/VFG/builder/DVFGBuilder.ts:29

## Constructors

### Constructor

> **new DVFGBuilder**(`dvfg`, `s`): `DVFGBuilder`

Defined in: src/VFG/builder/DVFGBuilder.ts:33

#### Parameters

##### dvfg

[`DVFG`](DVFG.md)

##### s

[`Scene`](Scene.md)

#### Returns

`DVFGBuilder`

## Methods

### addDVFGEdges()

> **addDVFGEdges**(): `void`

Defined in: src/VFG/builder/DVFGBuilder.ts:131

#### Returns

`void`

***

### addDVFGNodes()

> **addDVFGNodes**(): `void`

Defined in: src/VFG/builder/DVFGBuilder.ts:129

#### Returns

`void`

***

### build()

> **build**(): `void`

Defined in: src/VFG/builder/DVFGBuilder.ts:38

#### Returns

`void`

***

### buildForSingleMethod()

> **buildForSingleMethod**(`m`): `void`

Defined in: src/VFG/builder/DVFGBuilder.ts:46

#### Parameters

##### m

[`ArkMethod`](ArkMethod.md)

#### Returns

`void`

***

### getOrNewDVFGNode()

> **getOrNewDVFGNode**(`stmt`): `DVFGNode`

Defined in: src/VFG/builder/DVFGBuilder.ts:125

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`DVFGNode`




============================================================
## FILE: `classes/DataflowProblem.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DataflowProblem

# Class: `abstract` DataflowProblem\<D\>

Defined in: src/core/dataflow/DataflowProblem.ts:19

## Extended by

- [`UndefinedVariableChecker`](UndefinedVariableChecker.md)

## Type Parameters

### D

`D`

## Constructors

### Constructor

> **new DataflowProblem**\<`D`\>(): `DataflowProblem`\<`D`\>

#### Returns

`DataflowProblem`\<`D`\>

## Methods

### createZeroValue()

> `abstract` **createZeroValue**(): `D`

Defined in: src/core/dataflow/DataflowProblem.ts:43

#### Returns

`D`

***

### factEqual()

> `abstract` **factEqual**(`d1`, `d2`): `boolean`

Defined in: src/core/dataflow/DataflowProblem.ts:49

#### Parameters

##### d1

`D`

##### d2

`D`

#### Returns

`boolean`

***

### getCallFlowFunction()

> `abstract` **getCallFlowFunction**(`srcStmt`, `method`): [`FlowFunction`](../interfaces/FlowFunction.md)\<`D`\>

Defined in: src/core/dataflow/DataflowProblem.ts:37

#### Parameters

##### srcStmt

[`Stmt`](Stmt.md)

##### method

[`ArkMethod`](ArkMethod.md)

#### Returns

[`FlowFunction`](../interfaces/FlowFunction.md)\<`D`\>

***

### getCallToReturnFlowFunction()

> `abstract` **getCallToReturnFlowFunction**(`srcStmt`, `tgtStmt`): [`FlowFunction`](../interfaces/FlowFunction.md)\<`D`\>

Defined in: src/core/dataflow/DataflowProblem.ts:41

#### Parameters

##### srcStmt

[`Stmt`](Stmt.md)

##### tgtStmt

[`Stmt`](Stmt.md)

#### Returns

[`FlowFunction`](../interfaces/FlowFunction.md)\<`D`\>

***

### getEntryMethod()

> `abstract` **getEntryMethod**(): [`ArkMethod`](ArkMethod.md)

Defined in: src/core/dataflow/DataflowProblem.ts:47

#### Returns

[`ArkMethod`](ArkMethod.md)

***

### getEntryPoint()

> `abstract` **getEntryPoint**(): [`Stmt`](Stmt.md)

Defined in: src/core/dataflow/DataflowProblem.ts:45

#### Returns

[`Stmt`](Stmt.md)

***

### getExitToReturnFlowFunction()

> `abstract` **getExitToReturnFlowFunction**(`srcStmt`, `tgtStmt`, `callStmt`): [`FlowFunction`](../interfaces/FlowFunction.md)\<`D`\>

Defined in: src/core/dataflow/DataflowProblem.ts:39

#### Parameters

##### srcStmt

[`Stmt`](Stmt.md)

##### tgtStmt

[`Stmt`](Stmt.md)

##### callStmt

[`Stmt`](Stmt.md)

#### Returns

[`FlowFunction`](../interfaces/FlowFunction.md)\<`D`\>

***

### getNormalFlowFunction()

> `abstract` **getNormalFlowFunction**(`srcStmt`, `tgtStmt`): [`FlowFunction`](../interfaces/FlowFunction.md)\<`D`\>

Defined in: src/core/dataflow/DataflowProblem.ts:35

Transfer the outFact of srcStmt to the inFact of tgtStmt

Return true if keeping progagation (i.e., tgtStmt will be added to the WorkList for further analysis)

#### Parameters

##### srcStmt

[`Stmt`](Stmt.md)

##### tgtStmt

[`Stmt`](Stmt.md)

#### Returns

[`FlowFunction`](../interfaces/FlowFunction.md)\<`D`\>




============================================================
## FILE: `classes/DataflowResult.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DataflowResult

# Class: DataflowResult

Defined in: src/core/dataflow/DataflowResult.ts:19

## Constructors

### Constructor

> **new DataflowResult**(): `DataflowResult`

#### Returns

`DataflowResult`

## Properties

### globalFacts

> **globalFacts**: `Set`\<[`Fact`](Fact.md)\>

Defined in: src/core/dataflow/DataflowResult.ts:24

***

### stmt2InFacts

> **stmt2InFacts**: `Map`\<[`Stmt`](Stmt.md), [`Fact`](Fact.md)\>

Defined in: src/core/dataflow/DataflowResult.ts:20

***

### stmt2OutFacts

> **stmt2OutFacts**: `Map`\<[`Stmt`](Stmt.md), [`Fact`](Fact.md)\>

Defined in: src/core/dataflow/DataflowResult.ts:21




============================================================
## FILE: `classes/DataflowSolver.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DataflowSolver

# Class: `abstract` DataflowSolver\<D\>

Defined in: src/core/dataflow/DataflowSolver.ts:40

## Extended by

- [`UndefinedVariableSolver`](UndefinedVariableSolver.md)

## Type Parameters

### D

`D`

## Constructors

### Constructor

> **new DataflowSolver**\<`D`\>(`problem`, `scene`): `DataflowSolver`\<`D`\>

Defined in: src/core/dataflow/DataflowSolver.ts:53

#### Parameters

##### problem

[`DataflowProblem`](DataflowProblem.md)\<`D`\>

##### scene

[`Scene`](Scene.md)

#### Returns

`DataflowSolver`\<`D`\>

## Properties

### CHA

> `protected` **CHA**: [`ClassHierarchyAnalysis`](ClassHierarchyAnalysis.md)

Defined in: src/core/dataflow/DataflowSolver.ts:49

***

### endSummary

> `protected` **endSummary**: `Map`\<[`PathEdgePoint`](PathEdgePoint.md)\<`D`\>, `Set`\<[`PathEdgePoint`](PathEdgePoint.md)\<`D`\>\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:46

***

### inComing

> `protected` **inComing**: `Map`\<[`PathEdgePoint`](PathEdgePoint.md)\<`D`\>, `Set`\<[`PathEdgePoint`](PathEdgePoint.md)\<`D`\>\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:45

***

### laterEdges

> `protected` **laterEdges**: `Set`\<[`PathEdge`](PathEdge.md)\<`D`\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:51

***

### pathEdgeSet

> `protected` **pathEdgeSet**: `Set`\<[`PathEdge`](PathEdge.md)\<`D`\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:43

***

### problem

> `protected` **problem**: [`DataflowProblem`](DataflowProblem.md)\<`D`\>

Defined in: src/core/dataflow/DataflowSolver.ts:41

***

### scene

> `protected` **scene**: [`Scene`](Scene.md)

Defined in: src/core/dataflow/DataflowSolver.ts:48

***

### stmtNexts

> `protected` **stmtNexts**: `Map`\<[`Stmt`](Stmt.md), `Set`\<[`Stmt`](Stmt.md)\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:50

***

### summaryEdge

> `protected` **summaryEdge**: `Set`\<`CallToReturnCacheEdge`\<`D`\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:47

***

### workList

> `protected` **workList**: [`PathEdge`](PathEdge.md)\<`D`\>[]

Defined in: src/core/dataflow/DataflowSolver.ts:42

***

### zeroFact

> `protected` **zeroFact**: `D`

Defined in: src/core/dataflow/DataflowSolver.ts:44

## Methods

### buildStmtMapInBlock()

> `protected` **buildStmtMapInBlock**(`block`): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:113

#### Parameters

##### block

[`BasicBlock`](BasicBlock.md)

#### Returns

`void`

***

### buildStmtMapInClass()

> `protected` **buildStmtMapInClass**(): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:98

#### Returns

`void`

***

### callNodeFactPropagate()

> `protected` **callNodeFactPropagate**(`edge`, `firstStmt`, `fact`, `returnSite`): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:288

#### Parameters

##### edge

[`PathEdge`](PathEdge.md)\<`D`\>

##### firstStmt

[`Stmt`](Stmt.md)

##### fact

`D`

##### returnSite

[`Stmt`](Stmt.md)

#### Returns

`void`

***

### computeResult()

> `protected` **computeResult**(`stmt`, `d`): `boolean`

Defined in: src/core/dataflow/DataflowSolver.ts:71

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

##### d

`D`

#### Returns

`boolean`

***

### doSolve()

> `protected` **doSolve**(): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:320

#### Returns

`void`

***

### getAllCalleeMethods()

> `protected` **getAllCalleeMethods**(`callNode`): `Set`\<[`ArkMethod`](ArkMethod.md)\>

Defined in: src/core/dataflow/DataflowSolver.ts:137

#### Parameters

##### callNode

[`ArkInvokeStmt`](ArkInvokeStmt.md)

#### Returns

`Set`\<[`ArkMethod`](ArkMethod.md)\>

***

### getChildren()

> `protected` **getChildren**(`stmt`): [`Stmt`](Stmt.md)[]

Defined in: src/core/dataflow/DataflowSolver.ts:80

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

[`Stmt`](Stmt.md)[]

***

### getPathEdgeSet()

> **getPathEdgeSet**(): `Set`\<[`PathEdge`](PathEdge.md)\<`D`\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:355

#### Returns

`Set`\<[`PathEdge`](PathEdge.md)\<`D`\>\>

***

### getReturnSiteOfCall()

> `protected` **getReturnSiteOfCall**(`call`): [`Stmt`](Stmt.md)

Defined in: src/core/dataflow/DataflowSolver.ts:152

#### Parameters

##### call

[`Stmt`](Stmt.md)

#### Returns

[`Stmt`](Stmt.md)

***

### getStartOfCallerMethod()

> `protected` **getStartOfCallerMethod**(`call`): [`Stmt`](Stmt.md)

Defined in: src/core/dataflow/DataflowSolver.ts:156

#### Parameters

##### call

[`Stmt`](Stmt.md)

#### Returns

[`Stmt`](Stmt.md)

***

### init()

> `protected` **init**(): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:84

#### Returns

`void`

***

### isCallStatement()

> `protected` **isCallStatement**(`stmt`): `boolean`

Defined in: src/core/dataflow/DataflowSolver.ts:337

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`boolean`

***

### isExitStatement()

> `protected` **isExitStatement**(`stmt`): `boolean`

Defined in: src/core/dataflow/DataflowSolver.ts:351

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`boolean`

***

### pathEdgeSetHasEdge()

> `protected` **pathEdgeSetHasEdge**(`edge`): `boolean`

Defined in: src/core/dataflow/DataflowSolver.ts:162

#### Parameters

##### edge

[`PathEdge`](PathEdge.md)\<`D`\>

#### Returns

`boolean`

***

### processCallNode()

> `protected` **processCallNode**(`edge`): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:254

#### Parameters

##### edge

[`PathEdge`](PathEdge.md)\<`D`\>

#### Returns

`void`

***

### processExitNode()

> `protected` **processExitNode**(`edge`): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:191

#### Parameters

##### edge

[`PathEdge`](PathEdge.md)\<`D`\>

#### Returns

`void`

***

### processNormalNode()

> `protected` **processNormalNode**(`edge`): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:238

#### Parameters

##### edge

[`PathEdge`](PathEdge.md)\<`D`\>

#### Returns

`void`

***

### propagate()

> `protected` **propagate**(`edge`): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:177

#### Parameters

##### edge

[`PathEdge`](PathEdge.md)\<`D`\>

#### Returns

`void`

***

### setCfg4AllStmt()

> `protected` **setCfg4AllStmt**(): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:129

#### Returns

`void`

***

### solve()

> **solve**(): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:66

#### Returns

`void`




============================================================
## FILE: `classes/Decorator.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Decorator

# Class: Decorator

Defined in: src/core/base/Decorator.ts:19

## Constructors

### Constructor

> **new Decorator**(`name`): `Decorator`

Defined in: src/core/base/Decorator.ts:23

#### Parameters

##### name

`string`

#### Returns

`Decorator`

## Properties

### content

> **content**: `string` = `''`

Defined in: src/core/base/Decorator.ts:21

***

### kind

> **kind**: `string`

Defined in: src/core/base/Decorator.ts:20

***

### param

> **param**: `string` = `''`

Defined in: src/core/base/Decorator.ts:22

## Methods

### getContent()

> **getContent**(): `string`

Defined in: src/core/base/Decorator.ts:32

#### Returns

`string`

***

### getKind()

> **getKind**(): `string`

Defined in: src/core/base/Decorator.ts:26

#### Returns

`string`

***

### getParam()

> **getParam**(): `string`

Defined in: src/core/base/Decorator.ts:38

#### Returns

`string`

***

### setContent()

> **setContent**(`content`): `void`

Defined in: src/core/base/Decorator.ts:29

#### Parameters

##### content

`string`

#### Returns

`void`

***

### setParam()

> **setParam**(`param`): `void`

Defined in: src/core/base/Decorator.ts:35

#### Parameters

##### param

`string`

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Decorator.ts:41

#### Returns

`string`




============================================================
## FILE: `classes/DefUseChain.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DefUseChain

# Class: DefUseChain

Defined in: src/core/base/DefUseChain.ts:19

## Constructors

### Constructor

> **new DefUseChain**(`value`, `def`, `use`): `DefUseChain`

Defined in: src/core/base/DefUseChain.ts:23

#### Parameters

##### value

[`Value`](../interfaces/Value.md)

##### def

[`Stmt`](Stmt.md)

##### use

[`Stmt`](Stmt.md)

#### Returns

`DefUseChain`

## Properties

### def

> **def**: [`Stmt`](Stmt.md)

Defined in: src/core/base/DefUseChain.ts:21

***

### use

> **use**: [`Stmt`](Stmt.md)

Defined in: src/core/base/DefUseChain.ts:22

***

### value

> **value**: [`Value`](../interfaces/Value.md)

Defined in: src/core/base/DefUseChain.ts:20




============================================================
## FILE: `classes/DiffPTData.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DiffPTData

# Class: DiffPTData\<K, D, DS\>

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:222

## Type Parameters

### K

`K`

### D

`D` *extends* `Idx`

### DS

`DS` *extends* `IPtsCollection`\<`D`\>

## Constructors

### Constructor

> **new DiffPTData**\<`K`, `D`, `DS`\>(`DSCreator`): `DiffPTData`\<`K`, `D`, `DS`\>

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:226

#### Parameters

##### DSCreator

() => `DS`

#### Returns

`DiffPTData`\<`K`, `D`, `DS`\>

## Methods

### addPts()

> **addPts**(`v`, `elem`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:236

#### Parameters

##### v

`K`

##### elem

`D`

#### Returns

`boolean`

***

### calculateDiff()

> **calculateDiff**(`src`, `dst`): `DS`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:364

#### Parameters

##### src

`K`

##### dst

`K`

#### Returns

`DS`

***

### clear()

> **clear**(): `void`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:231

#### Returns

`void`

***

### clearDiffPts()

> **clearDiffPts**(`v`): `void`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:350

#### Parameters

##### v

`K`

#### Returns

`void`

***

### clearPropaPts()

> **clearPropaPts**(`v`): `void`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:357

#### Parameters

##### v

`K`

#### Returns

`void`

***

### clearPts()

> **clearPts**(`v`): `void`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:339

#### Parameters

##### v

`K`

#### Returns

`void`

***

### flush()

> **flush**(`v`): `void`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:328

#### Parameters

##### v

`K`

#### Returns

`void`

***

### getAllPropaPts()

> **getAllPropaPts**(): `Map`\<`K`, `DS`\>

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:317

#### Returns

`Map`\<`K`, `DS`\>

***

### getDiffPts()

> **getDiffPts**(`v`): `undefined` \| `DS`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:302

#### Parameters

##### v

`K`

#### Returns

`undefined` \| `DS`

***

### getMutDiffPts()

> **getMutDiffPts**(`v`): `undefined` \| `DS`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:306

#### Parameters

##### v

`K`

#### Returns

`undefined` \| `DS`

***

### getPropaPts()

> **getPropaPts**(`v`): `undefined` \| `DS`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:313

#### Parameters

##### v

`K`

#### Returns

`undefined` \| `DS`

***

### getPropaPtsMut()

> **getPropaPtsMut**(`v`): `DS`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:321

#### Parameters

##### v

`K`

#### Returns

`DS`

***

### removePtsElem()

> **removePtsElem**(`v`, `elem`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:296

#### Parameters

##### v

`K`

##### elem

`D`

#### Returns

`boolean`

***

### resetElem()

> **resetElem**(`v`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:246

#### Parameters

##### v

`K`

#### Returns

`boolean`

***

### unionDiffPts()

> **unionDiffPts**(`dstv`, `srcv`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:255

#### Parameters

##### dstv

`K`

##### srcv

`K`

#### Returns

`boolean`

***

### unionPts()

> **unionPts**(`dstv`, `srcv`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:268

#### Parameters

##### dstv

`K`

##### srcv

`K`

#### Returns

`boolean`

***

### unionPtsTo()

> **unionPtsTo**(`dstv`, `srcDs`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:286

#### Parameters

##### dstv

`K`

##### srcDs

`DS`

#### Returns

`boolean`




============================================================
## FILE: `classes/DominanceFinder.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DominanceFinder

# Class: DominanceFinder

Defined in: src/core/graph/DominanceFinder.ts:19

## Constructors

### Constructor

> **new DominanceFinder**(`cfg`): `DominanceFinder`

Defined in: src/core/graph/DominanceFinder.ts:25

#### Parameters

##### cfg

[`Cfg`](Cfg.md)

#### Returns

`DominanceFinder`

## Methods

### getBlocks()

> **getBlocks**(): [`BasicBlock`](BasicBlock.md)[]

Defined in: src/core/graph/DominanceFinder.ts:97

#### Returns

[`BasicBlock`](BasicBlock.md)[]

***

### getBlockToIdx()

> **getBlockToIdx**(): `Map`\<[`BasicBlock`](BasicBlock.md), `number`\>

Defined in: src/core/graph/DominanceFinder.ts:101

#### Returns

`Map`\<[`BasicBlock`](BasicBlock.md), `number`\>

***

### getDominanceFrontiers()

> **getDominanceFrontiers**(`block`): `Set`\<[`BasicBlock`](BasicBlock.md)\>

Defined in: src/core/graph/DominanceFinder.ts:84

#### Parameters

##### block

[`BasicBlock`](BasicBlock.md)

#### Returns

`Set`\<[`BasicBlock`](BasicBlock.md)\>

***

### getImmediateDominators()

> **getImmediateDominators**(): `number`[]

Defined in: src/core/graph/DominanceFinder.ts:105

#### Returns

`number`[]




============================================================
## FILE: `classes/DominanceTree.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DominanceTree

# Class: DominanceTree

Defined in: src/core/graph/DominanceTree.ts:19

## Constructors

### Constructor

> **new DominanceTree**(`dominanceFinder`): `DominanceTree`

Defined in: src/core/graph/DominanceTree.ts:25

#### Parameters

##### dominanceFinder

[`DominanceFinder`](DominanceFinder.md)

#### Returns

`DominanceTree`

## Methods

### getAllNodesDFS()

> **getAllNodesDFS**(): [`BasicBlock`](BasicBlock.md)[]

Defined in: src/core/graph/DominanceTree.ts:46

#### Returns

[`BasicBlock`](BasicBlock.md)[]

***

### getChildren()

> **getChildren**(`block`): [`BasicBlock`](BasicBlock.md)[]

Defined in: src/core/graph/DominanceTree.ts:63

#### Parameters

##### block

[`BasicBlock`](BasicBlock.md)

#### Returns

[`BasicBlock`](BasicBlock.md)[]

***

### getRoot()

> **getRoot**(): [`BasicBlock`](BasicBlock.md)

Defined in: src/core/graph/DominanceTree.ts:72

#### Returns

[`BasicBlock`](BasicBlock.md)




============================================================
## FILE: `classes/DotClassPrinter.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DotClassPrinter

# Class: DotClassPrinter

Defined in: src/save/DotPrinter.ts:106

## Extends

- [`Printer`](Printer.md)

## Constructors

### Constructor

> **new DotClassPrinter**(`cls`, `nesting`): `DotClassPrinter`

Defined in: src/save/DotPrinter.ts:110

#### Parameters

##### cls

[`ArkClass`](ArkClass.md)

##### nesting

`boolean` = `false`

#### Returns

`DotClassPrinter`

#### Overrides

[`Printer`](Printer.md).[`constructor`](Printer.md#constructor)

## Properties

### cls

> **cls**: [`ArkClass`](ArkClass.md)

Defined in: src/save/DotPrinter.ts:107

***

### nesting

> **nesting**: `boolean`

Defined in: src/save/DotPrinter.ts:108

***

### printer

> `protected` **printer**: `ArkCodeBuffer`

Defined in: src/save/Printer.ts:22

#### Inherited from

[`Printer`](Printer.md).[`printer`](Printer.md#printer)

## Methods

### dump()

> **dump**(): `string`

Defined in: src/save/DotPrinter.ts:116

ArkIR dump

#### Returns

`string`

#### Overrides

[`Printer`](Printer.md).[`dump`](Printer.md#dump)




============================================================
## FILE: `classes/DotFilePrinter.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DotFilePrinter

# Class: DotFilePrinter

Defined in: src/save/DotPrinter.ts:174

## Extends

- [`Printer`](Printer.md)

## Constructors

### Constructor

> **new DotFilePrinter**(`arkFile`): `DotFilePrinter`

Defined in: src/save/DotPrinter.ts:177

#### Parameters

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

`DotFilePrinter`

#### Overrides

[`Printer`](Printer.md).[`constructor`](Printer.md#constructor)

## Properties

### arkFile

> **arkFile**: [`ArkFile`](ArkFile.md)

Defined in: src/save/DotPrinter.ts:175

***

### printer

> `protected` **printer**: `ArkCodeBuffer`

Defined in: src/save/Printer.ts:22

#### Inherited from

[`Printer`](Printer.md).[`printer`](Printer.md#printer)

## Methods

### dump()

> **dump**(): `string`

Defined in: src/save/DotPrinter.ts:182

ArkIR dump

#### Returns

`string`

#### Overrides

[`Printer`](Printer.md).[`dump`](Printer.md#dump)




============================================================
## FILE: `classes/DotMethodPrinter.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DotMethodPrinter

# Class: DotMethodPrinter

Defined in: src/save/DotPrinter.ts:27

## Extends

- [`Printer`](Printer.md)

## Constructors

### Constructor

> **new DotMethodPrinter**(`method`, `nesting`): `DotMethodPrinter`

Defined in: src/save/DotPrinter.ts:31

#### Parameters

##### method

[`ArkMethod`](ArkMethod.md)

##### nesting

`boolean` = `false`

#### Returns

`DotMethodPrinter`

#### Overrides

[`Printer`](Printer.md).[`constructor`](Printer.md#constructor)

## Properties

### method

> **method**: [`ArkMethod`](ArkMethod.md)

Defined in: src/save/DotPrinter.ts:28

***

### nesting

> **nesting**: `boolean`

Defined in: src/save/DotPrinter.ts:29

***

### printer

> `protected` **printer**: `ArkCodeBuffer`

Defined in: src/save/Printer.ts:22

#### Inherited from

[`Printer`](Printer.md).[`printer`](Printer.md#printer)

## Methods

### dump()

> **dump**(): `string`

Defined in: src/save/DotPrinter.ts:37

ArkIR dump

#### Returns

`string`

#### Overrides

[`Printer`](Printer.md).[`dump`](Printer.md#dump)

***

### stringHashCode()

> `protected` **stringHashCode**(`name`): `number`

Defined in: src/save/DotPrinter.ts:57

#### Parameters

##### name

`string`

#### Returns

`number`




============================================================
## FILE: `classes/DotNamespacePrinter.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DotNamespacePrinter

# Class: DotNamespacePrinter

Defined in: src/save/DotPrinter.ts:140

## Extends

- [`Printer`](Printer.md)

## Constructors

### Constructor

> **new DotNamespacePrinter**(`ns`, `nesting`): `DotNamespacePrinter`

Defined in: src/save/DotPrinter.ts:144

#### Parameters

##### ns

[`ArkNamespace`](ArkNamespace.md)

##### nesting

`boolean` = `false`

#### Returns

`DotNamespacePrinter`

#### Overrides

[`Printer`](Printer.md).[`constructor`](Printer.md#constructor)

## Properties

### nesting

> **nesting**: `boolean`

Defined in: src/save/DotPrinter.ts:142

***

### ns

> **ns**: [`ArkNamespace`](ArkNamespace.md)

Defined in: src/save/DotPrinter.ts:141

***

### printer

> `protected` **printer**: `ArkCodeBuffer`

Defined in: src/save/Printer.ts:22

#### Inherited from

[`Printer`](Printer.md).[`printer`](Printer.md#printer)

## Methods

### dump()

> **dump**(): `string`

Defined in: src/save/DotPrinter.ts:150

ArkIR dump

#### Returns

`string`

#### Overrides

[`Printer`](Printer.md).[`dump`](Printer.md#dump)




============================================================
## FILE: `classes/DummyCallCreator.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DummyCallCreator

# Class: DummyCallCreator

Defined in: src/callgraph/pointerAnalysis/DummyCallCreator.ts:30

TODO: constructor pointer and cid

## Constructors

### Constructor

> **new DummyCallCreator**(`scene`): `DummyCallCreator`

Defined in: src/callgraph/pointerAnalysis/DummyCallCreator.ts:36

#### Parameters

##### scene

[`Scene`](Scene.md)

#### Returns

`DummyCallCreator`

## Methods

### getDummyCallByComponent()

> **getDummyCallByComponent**(`classSig`, `baseComponent`): `Set`\<[`Stmt`](Stmt.md)\>

Defined in: src/callgraph/pointerAnalysis/DummyCallCreator.ts:54

#### Parameters

##### classSig

[`ClassSignature`](ClassSignature.md)

##### baseComponent

[`Local`](Local.md)

#### Returns

`Set`\<[`Stmt`](Stmt.md)\>

***

### getDummyCallByPage()

> **getDummyCallByPage**(`classSig`, `basePage`): `Set`\<[`Stmt`](Stmt.md)\>

Defined in: src/callgraph/pointerAnalysis/DummyCallCreator.ts:42

#### Parameters

##### classSig

[`ClassSignature`](ClassSignature.md)

##### basePage

[`Local`](Local.md)

#### Returns

`Set`\<[`Stmt`](Stmt.md)\>




============================================================
## FILE: `classes/DummyMainCreater.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DummyMainCreater

# Class: DummyMainCreater

Defined in: src/core/common/DummyMainCreater.ts:59

收集所有的onCreate，onStart等函数，构造一个虚拟函数，具体为：
%statInit()
...
count = 0
while (true) {
    if (count === 1) {
        temp1 = new ability
        temp2 = new want
        temp1.onCreate(temp2)
    }
    if (count === 2) {
        onDestroy()
    }
    ...
    if (count === *) {
        callbackMethod1()
    }
    ...
}
return
如果是instanceInvoke还要先实例化对象，如果是其他文件的类或者方法还要添加import信息

## Constructors

### Constructor

> **new DummyMainCreater**(`scene`): `DummyMainCreater`

Defined in: src/core/common/DummyMainCreater.ts:66

#### Parameters

##### scene

[`Scene`](Scene.md)

#### Returns

`DummyMainCreater`

## Methods

### createDummyMain()

> **createDummyMain**(): `void`

Defined in: src/core/common/DummyMainCreater.ts:79

#### Returns

`void`

***

### getCallbackMethods()

> **getCallbackMethods**(): [`ArkMethod`](ArkMethod.md)[]

Defined in: src/core/common/DummyMainCreater.ts:322

#### Returns

[`ArkMethod`](ArkMethod.md)[]

***

### getDummyMain()

> **getDummyMain**(): [`ArkMethod`](ArkMethod.md)

Defined in: src/core/common/DummyMainCreater.ts:272

#### Returns

[`ArkMethod`](ArkMethod.md)

***

### getMethodsFromAllAbilities()

> **getMethodsFromAllAbilities**(): [`ArkMethod`](ArkMethod.md)[]

Defined in: src/core/common/DummyMainCreater.ts:311

#### Returns

[`ArkMethod`](ArkMethod.md)[]

***

### setEntryMethods()

> **setEntryMethods**(`methods`): `void`

Defined in: src/core/common/DummyMainCreater.ts:75

#### Parameters

##### methods

[`ArkMethod`](ArkMethod.md)[]

#### Returns

`void`




============================================================
## FILE: `classes/DynCallSite.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DynCallSite

# Class: DynCallSite

Defined in: src/callgraph/model/CallSite.ts:43

## Implements

- [`ICallSite`](../interfaces/ICallSite.md)

## Constructors

### Constructor

> **new DynCallSite**(`s`, `a`, `ptcCallee`, `caller`): `DynCallSite`

Defined in: src/callgraph/model/CallSite.ts:49

#### Parameters

##### s

[`Stmt`](Stmt.md)

##### a

`undefined` | [`Value`](../interfaces/Value.md)[]

##### ptcCallee

`undefined` | `number`

##### caller

`number`

#### Returns

`DynCallSite`

## Properties

### args

> **args**: `undefined` \| [`Value`](../interfaces/Value.md)[]

Defined in: src/callgraph/model/CallSite.ts:45

#### Implementation of

[`ICallSite`](../interfaces/ICallSite.md).[`args`](../interfaces/ICallSite.md#args)

***

### callerFuncID

> **callerFuncID**: `number`

Defined in: src/callgraph/model/CallSite.ts:47

#### Implementation of

[`ICallSite`](../interfaces/ICallSite.md).[`callerFuncID`](../interfaces/ICallSite.md#callerfuncid)

***

### callStmt

> **callStmt**: [`Stmt`](Stmt.md)

Defined in: src/callgraph/model/CallSite.ts:44

#### Implementation of

[`ICallSite`](../interfaces/ICallSite.md).[`callStmt`](../interfaces/ICallSite.md#callstmt)

***

### protentialCalleeFuncID

> **protentialCalleeFuncID**: `undefined` \| `number`

Defined in: src/callgraph/model/CallSite.ts:46




============================================================
## FILE: `classes/EnumValueType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / EnumValueType

# Class: EnumValueType

Defined in: src/core/base/Type.ts:797

## Extends

- [`Type`](Type.md)

## Constructors

### Constructor

> **new EnumValueType**(`signature`, `constant?`): `EnumValueType`

Defined in: src/core/base/Type.ts:801

#### Parameters

##### signature

[`FieldSignature`](FieldSignature.md)

##### constant?

[`Constant`](Constant.md)

#### Returns

`EnumValueType`

#### Overrides

[`Type`](Type.md).[`constructor`](Type.md#constructor)

## Methods

### getConstant()

> **getConstant**(): `undefined` \| [`Constant`](Constant.md)

Defined in: src/core/base/Type.ts:811

#### Returns

`undefined` \| [`Constant`](Constant.md)

***

### getFieldSignature()

> **getFieldSignature**(): [`FieldSignature`](FieldSignature.md)

Defined in: src/core/base/Type.ts:807

#### Returns

[`FieldSignature`](FieldSignature.md)

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:815

#### Returns

`string`

#### Overrides

[`Type`](Type.md).[`getTypeString`](Type.md#gettypestring)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`Type`](Type.md).[`toString`](Type.md#tostring)




============================================================
## FILE: `classes/ExportInfo.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ExportInfo

# Class: ExportInfo

Defined in: src/core/model/ArkExport.ts:58

## Extends

- `ArkBaseModel`

## Implements

- `FromInfo`

## Properties

### decorators?

> `protected` `optional` **decorators**: `Set`\<[`Decorator`](Decorator.md)\>

Defined in: src/core/model/ArkBaseModel.ts:115

#### Inherited from

`ArkBaseModel.decorators`

***

### metadata?

> `protected` `optional` **metadata**: `ArkMetadata`

Defined in: src/core/model/ArkBaseModel.ts:116

#### Inherited from

`ArkBaseModel.metadata`

***

### modifiers?

> `protected` `optional` **modifiers**: `number`

Defined in: src/core/model/ArkBaseModel.ts:114

#### Inherited from

`ArkBaseModel.modifiers`

***

### Builder

> `static` **Builder**: *typeof* `ArkExportBuilder`

Defined in: src/core/model/ArkExport.ts:140

## Methods

### addDecorator()

> **addDecorator**(`decorator`): `void`

Defined in: src/core/model/ArkBaseModel.ts:215

#### Parameters

##### decorator

[`Decorator`](Decorator.md)

#### Returns

`void`

#### Inherited from

`ArkBaseModel.addDecorator`

***

### addModifier()

> **addModifier**(`modifier`): `void`

Defined in: src/core/model/ArkBaseModel.ts:142

#### Parameters

##### modifier

`number`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.addModifier`

***

### containsModifier()

> **containsModifier**(`modifierType`): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:194

#### Parameters

##### modifierType

`ModifierType`

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.containsModifier`

***

### getArkExport()

> **getArkExport**(): `undefined` \| `null` \| `ArkExport`

Defined in: src/core/model/ArkExport.ts:110

#### Returns

`undefined` \| `null` \| `ArkExport`

***

### getDeclaringArkFile()

> **getDeclaringArkFile**(): [`ArkFile`](ArkFile.md)

Defined in: src/core/model/ArkExport.ts:132

#### Returns

[`ArkFile`](ArkFile.md)

#### Implementation of

`FromInfo.getDeclaringArkFile`

***

### getDeclaringArkNamespace()

> **getDeclaringArkNamespace**(): `undefined` \| [`ArkNamespace`](ArkNamespace.md)

Defined in: src/core/model/ArkExport.ts:136

#### Returns

`undefined` \| [`ArkNamespace`](ArkNamespace.md)

***

### getDecorators()

> **getDecorators**(): [`Decorator`](Decorator.md)[]

Defined in: src/core/model/ArkBaseModel.ts:202

#### Returns

[`Decorator`](Decorator.md)[]

#### Inherited from

`ArkBaseModel.getDecorators`

***

### getExportClauseName()

> **getExportClauseName**(): `string`

Defined in: src/core/model/ArkExport.ts:90

#### Returns

`string`

***

### getExportClauseType()

> **getExportClauseType**(): `ExportType`

Defined in: src/core/model/ArkExport.ts:98

#### Returns

`ExportType`

***

### getFrom()

> **getFrom**(): `undefined` \| `string`

Defined in: src/core/model/ArkExport.ts:82

#### Returns

`undefined` \| `string`

#### Implementation of

`FromInfo.getFrom`

***

### getLanguage()

> **getLanguage**(): `Language`

Defined in: src/core/model/ArkExport.ts:78

Returns the program language of the file where this export info defined.

#### Returns

`Language`

***

### getMetadata()

> **getMetadata**(`kind`): `undefined` \| `ArkMetadataType`

Defined in: src/core/model/ArkBaseModel.ts:118

#### Parameters

##### kind

`ArkMetadataKind`

#### Returns

`undefined` \| `ArkMetadataType`

#### Inherited from

`ArkBaseModel.getMetadata`

***

### getModifiers()

> **getModifiers**(): `number`

Defined in: src/core/model/ArkBaseModel.ts:129

#### Returns

`number`

#### Inherited from

`ArkBaseModel.getModifiers`

***

### getNameBeforeAs()

> **getNameBeforeAs**(): `undefined` \| `string`

Defined in: src/core/model/ArkExport.ts:102

#### Returns

`undefined` \| `string`

***

### getOriginName()

> **getOriginName**(): `string`

Defined in: src/core/model/ArkExport.ts:86

#### Returns

`string`

#### Implementation of

`FromInfo.getOriginName`

***

### getOriginTsPosition()

> **getOriginTsPosition**(): [`LineColPosition`](LineColPosition.md)

Defined in: src/core/model/ArkExport.ts:124

#### Returns

[`LineColPosition`](LineColPosition.md)

***

### getStateDecorators()

> **getStateDecorators**(): [`Decorator`](Decorator.md)[]

Defined in: src/core/model/ArkBaseModel.ts:234

#### Returns

[`Decorator`](Decorator.md)[]

#### Inherited from

`ArkBaseModel.getStateDecorators`

***

### getTsSourceCode()

> **getTsSourceCode**(): `string`

Defined in: src/core/model/ArkExport.ts:128

#### Returns

`string`

***

### hasBuilderDecorator()

> **hasBuilderDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:230

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasBuilderDecorator`

***

### hasBuilderParamDecorator()

> **hasBuilderParamDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:243

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasBuilderParamDecorator`

***

### hasComponentDecorator()

> **hasComponentDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:251

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasComponentDecorator`

***

### hasDecorator()

> **hasDecorator**(`kind`): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:255

#### Parameters

##### kind

`string` | `Set`\<`string`\>

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasDecorator`

***

### hasEntryDecorator()

> **hasEntryDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:247

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasEntryDecorator`

***

### isAbstract()

> **isAbstract**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:173

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isAbstract`

***

### isDeclare()

> **isDeclare**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:190

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isDeclare`

***

### isDefault()

> **isDefault**(): `boolean`

Defined in: src/core/model/ArkExport.ts:114

#### Returns

`boolean`

#### Implementation of

`FromInfo.isDefault`

#### Overrides

`ArkBaseModel.isDefault`

***

### isExport()

> **isExport**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:177

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isExport`

***

### ~~isExported()~~

> **isExported**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:186

#### Returns

`boolean`

#### Deprecated

Use [isExport](ArkNamespace.md#isexport) instead.

#### Inherited from

`ArkBaseModel.isExported`

***

### isPrivate()

> **isPrivate**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:161

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isPrivate`

***

### isProtected()

> **isProtected**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:157

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isProtected`

***

### isPublic()

> **isPublic**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:165

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isPublic`

***

### isReadonly()

> **isReadonly**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:169

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isReadonly`

***

### isStatic()

> **isStatic**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:153

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isStatic`

***

### removeDecorator()

> **removeDecorator**(`kind`): `void`

Defined in: src/core/model/ArkBaseModel.ts:222

#### Parameters

##### kind

`string`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.removeDecorator`

***

### removeModifier()

> **removeModifier**(`modifier`): `void`

Defined in: src/core/model/ArkBaseModel.ts:146

#### Parameters

##### modifier

`ModifierType`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.removeModifier`

***

### setArkExport()

> **setArkExport**(`value`): `void`

Defined in: src/core/model/ArkExport.ts:106

#### Parameters

##### value

`null` | `ArkExport`

#### Returns

`void`

***

### setDecorators()

> **setDecorators**(`decorators`): `void`

Defined in: src/core/model/ArkBaseModel.ts:209

#### Parameters

##### decorators

`Set`\<[`Decorator`](Decorator.md)\>

#### Returns

`void`

#### Inherited from

`ArkBaseModel.setDecorators`

***

### setExportClauseType()

> **setExportClauseType**(`exportClauseType`): `void`

Defined in: src/core/model/ArkExport.ts:94

#### Parameters

##### exportClauseType

`ExportType`

#### Returns

`void`

***

### setMetadata()

> **setMetadata**(`kind`, `value`): `void`

Defined in: src/core/model/ArkBaseModel.ts:122

#### Parameters

##### kind

`ArkMetadataKind`

##### value

`ArkMetadataType`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.setMetadata`

***

### setModifiers()

> **setModifiers**(`modifiers`): `void`

Defined in: src/core/model/ArkBaseModel.ts:136

#### Parameters

##### modifiers

`number`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.setModifiers`

***

### validate()

> **validate**(): `ArkError`

Defined in: src/core/model/ArkExport.ts:214

#### Returns

`ArkError`

#### Overrides

`ArkBaseModel.validate`

***

### validateFields()

> `protected` **validateFields**(`fields`): `ArkError`

Defined in: src/core/model/ArkBaseModel.ts:267

#### Parameters

##### fields

`string`[]

#### Returns

`ArkError`

#### Inherited from

`ArkBaseModel.validateFields`




============================================================
## FILE: `classes/ExprUseReplacer.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ExprUseReplacer

# Class: ExprUseReplacer

Defined in: src/core/common/ExprUseReplacer.ts:38

Replace old use of a Expr inplace

## Constructors

### Constructor

> **new ExprUseReplacer**(`oldUse`, `newUse`): `ExprUseReplacer`

Defined in: src/core/common/ExprUseReplacer.ts:42

#### Parameters

##### oldUse

[`Value`](../interfaces/Value.md)

##### newUse

[`Value`](../interfaces/Value.md)

#### Returns

`ExprUseReplacer`

## Methods

### caseExpr()

> **caseExpr**(`expr`): `void`

Defined in: src/core/common/ExprUseReplacer.ts:47

#### Parameters

##### expr

[`AbstractExpr`](AbstractExpr.md)

#### Returns

`void`




============================================================
## FILE: `classes/Fact.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Fact

# Class: Fact

Defined in: src/core/dataflow/Fact.ts:19

## Constructors

### Constructor

> **new Fact**(): `Fact`

#### Returns

`Fact`

## Properties

### valueMap

> **valueMap**: `Map`\<[`Value`](../interfaces/Value.md), [`Stmt`](Stmt.md)\>

Defined in: src/core/dataflow/Fact.ts:21

***

### values

> **values**: `Set`\<[`Value`](../interfaces/Value.md)\>

Defined in: src/core/dataflow/Fact.ts:20




============================================================
## FILE: `classes/FieldSignature.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / FieldSignature

# Class: FieldSignature

Defined in: src/core/model/ArkSignature.ts:217

## Constructors

### Constructor

> **new FieldSignature**(`fieldName`, `declaringSignature`, `type`, `staticFlag`): `FieldSignature`

Defined in: src/core/model/ArkSignature.ts:223

#### Parameters

##### fieldName

`string`

##### declaringSignature

[`BaseSignature`](../type-aliases/BaseSignature.md)

##### type

[`Type`](Type.md)

##### staticFlag

`boolean` = `false`

#### Returns

`FieldSignature`

## Methods

### getBaseName()

> **getBaseName**(): `string`

Defined in: src/core/model/ArkSignature.ts:234

#### Returns

`string`

***

### getDeclaringSignature()

> **getDeclaringSignature**(): [`BaseSignature`](../type-aliases/BaseSignature.md)

Defined in: src/core/model/ArkSignature.ts:230

#### Returns

[`BaseSignature`](../type-aliases/BaseSignature.md)

***

### getFieldName()

> **getFieldName**(): `string`

Defined in: src/core/model/ArkSignature.ts:238

#### Returns

`string`

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/model/ArkSignature.ts:242

#### Returns

[`Type`](Type.md)

***

### isStatic()

> **isStatic**(): `boolean`

Defined in: src/core/model/ArkSignature.ts:246

#### Returns

`boolean`

***

### setStaticFlag()

> **setStaticFlag**(`flag`): `void`

Defined in: src/core/model/ArkSignature.ts:256

#### Parameters

##### flag

`boolean`

#### Returns

`void`

***

### setType()

> **setType**(`type`): `void`

Defined in: src/core/model/ArkSignature.ts:251

#### Parameters

##### type

[`Type`](Type.md)

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/model/ArkSignature.ts:260

#### Returns

`string`




============================================================
## FILE: `classes/FileSignature.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / FileSignature

# Class: FileSignature

Defined in: src/core/model/ArkSignature.ts:40

## Constructors

### Constructor

> **new FileSignature**(`projectName`, `fileName`): `FileSignature`

Defined in: src/core/model/ArkSignature.ts:47

#### Parameters

##### projectName

`string`

##### fileName

`string`

#### Returns

`FileSignature`

## Properties

### DEFAULT

> `readonly` `static` **DEFAULT**: `FileSignature`

Defined in: src/core/model/ArkSignature.ts:45

## Methods

### getFileName()

> **getFileName**(): `string`

Defined in: src/core/model/ArkSignature.ts:57

#### Returns

`string`

***

### getProjectName()

> **getProjectName**(): `string`

Defined in: src/core/model/ArkSignature.ts:53

#### Returns

`string`

***

### toMapKey()

> **toMapKey**(): `string`

Defined in: src/core/model/ArkSignature.ts:65

#### Returns

`string`

***

### toString()

> **toString**(): `string`

Defined in: src/core/model/ArkSignature.ts:61

#### Returns

`string`




============================================================
## FILE: `classes/FileUtils.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / FileUtils

# Class: FileUtils

Defined in: src/utils/FileUtils.ts:25

## Constructors

### Constructor

> **new FileUtils**(): `FileUtils`

#### Returns

`FileUtils`

## Properties

### FILE\_FILTER

> `readonly` `static` **FILE\_FILTER**: `object`

Defined in: src/utils/FileUtils.ts:26

#### ignores

> **ignores**: `string`[]

#### include

> **include**: `RegExp`

## Methods

### generateModuleMap()

> `static` **generateModuleMap**(`ohPkgContentMap`): `Map`\<`string`, [`ModulePath`](ModulePath.md)\>

Defined in: src/utils/FileUtils.ts:51

#### Parameters

##### ohPkgContentMap

`Map`\<`string`, \{[`k`: `string`]: `unknown`; \}\>

#### Returns

`Map`\<`string`, [`ModulePath`](ModulePath.md)\>

***

### getFileLanguage()

> `static` **getFileLanguage**(`file`, `fileTags?`): `Language`

Defined in: src/utils/FileUtils.ts:79

#### Parameters

##### file

`string`

##### fileTags?

`Map`\<`string`, `Language`\>

#### Returns

`Language`

***

### getIndexFileName()

> `static` **getIndexFileName**(`srcPath`): `string`

Defined in: src/utils/FileUtils.ts:31

#### Parameters

##### srcPath

`string`

#### Returns

`string`

***

### isAbsolutePath()

> `static` **isAbsolutePath**(`path`): `boolean`

Defined in: src/utils/FileUtils.ts:47

#### Parameters

##### path

`string`

#### Returns

`boolean`

***

### isDirectory()

> `static` **isDirectory**(`srcPath`): `boolean`

Defined in: src/utils/FileUtils.ts:40

#### Parameters

##### srcPath

`string`

#### Returns

`boolean`




============================================================
## FILE: `classes/FullPosition.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / FullPosition

# Class: FullPosition

Defined in: src/core/base/Position.ts:104

## Constructors

### Constructor

> **new FullPosition**(`firstLine`, `firstCol`, `lastLine`, `lastCol`): `FullPosition`

Defined in: src/core/base/Position.ts:110

#### Parameters

##### firstLine

`number`

##### firstCol

`number`

##### lastLine

`number`

##### lastCol

`number`

#### Returns

`FullPosition`

## Properties

### DEFAULT

> `readonly` `static` **DEFAULT**: `FullPosition`

Defined in: src/core/base/Position.ts:108

## Methods

### getFirstCol()

> **getFirstCol**(): `number`

Defined in: src/core/base/Position.ts:123

#### Returns

`number`

***

### getFirstLine()

> **getFirstLine**(): `number`

Defined in: src/core/base/Position.ts:115

#### Returns

`number`

***

### getLastCol()

> **getLastCol**(): `number`

Defined in: src/core/base/Position.ts:127

#### Returns

`number`

***

### getLastLine()

> **getLastLine**(): `number`

Defined in: src/core/base/Position.ts:119

#### Returns

`number`

***

### buildFromNode()

> `static` **buildFromNode**(`node`, `sourceFile`): `FullPosition`

Defined in: src/core/base/Position.ts:131

#### Parameters

##### node

[`Node`](../ArkAnalyzer/namespaces/ts/interfaces/Node.md)

##### sourceFile

[`SourceFile`](../ArkAnalyzer/namespaces/ts/interfaces/SourceFile.md)

#### Returns

`FullPosition`

***

### merge()

> `static` **merge**(`leftMostPosition`, `rightMostPosition`): `FullPosition`

Defined in: src/core/base/Position.ts:139

#### Parameters

##### leftMostPosition

`FullPosition`

##### rightMostPosition

`FullPosition`

#### Returns

`FullPosition`




============================================================
## FILE: `classes/FuncPag.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / FuncPag

# Class: FuncPag

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1053

## Constructors

### Constructor

> **new FuncPag**(): `FuncPag`

#### Returns

`FuncPag`

## Methods

### addDynamicCallSite()

> **addDynamicCallSite**(`cs`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1073

#### Parameters

##### cs

[`DynCallSite`](DynCallSite.md)

#### Returns

`void`

***

### addInternalEdge()

> **addInternalEdge**(`stmt`, `k`): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1093

#### Parameters

##### stmt

[`ArkAssignStmt`](ArkAssignStmt.md)

##### k

[`PagEdgeKind`](../enumerations/PagEdgeKind.md)

#### Returns

`boolean`

***

### addNormalCallSite()

> **addNormalCallSite**(`cs`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1063

#### Parameters

##### cs

[`CallSite`](CallSite.md)

#### Returns

`void`

***

### addUnknownCallSite()

> **addUnknownCallSite**(`cs`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1083

#### Parameters

##### cs

[`CallSite`](CallSite.md)

#### Returns

`void`

***

### getDynamicCallSites()

> **getDynamicCallSites**(): `Set`\<[`DynCallSite`](DynCallSite.md)\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1078

#### Returns

`Set`\<[`DynCallSite`](DynCallSite.md)\>

***

### getInternalEdges()

> **getInternalEdges**(): `undefined` \| `Set`\<[`IntraProceduralEdge`](../type-aliases/IntraProceduralEdge.md)\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1059

#### Returns

`undefined` \| `Set`\<[`IntraProceduralEdge`](../type-aliases/IntraProceduralEdge.md)\>

***

### getNormalCallSites()

> **getNormalCallSites**(): `Set`\<[`CallSite`](CallSite.md)\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1068

#### Returns

`Set`\<[`CallSite`](CallSite.md)\>

***

### getUnknownCallSites()

> **getUnknownCallSites**(): `Set`\<[`CallSite`](CallSite.md)\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1088

#### Returns

`Set`\<[`CallSite`](CallSite.md)\>




============================================================
## FILE: `classes/FunctionType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / FunctionType

# Class: FunctionType

Defined in: src/core/base/Type.ts:365

function type

## Extends

- [`Type`](Type.md)

## Extended by

- [`ClosureType`](ClosureType.md)

## Constructors

### Constructor

> **new FunctionType**(`methodSignature`, `realGenericTypes?`): `FunctionType`

Defined in: src/core/base/Type.ts:369

#### Parameters

##### methodSignature

[`MethodSignature`](MethodSignature.md)

##### realGenericTypes?

[`Type`](Type.md)[]

#### Returns

`FunctionType`

#### Overrides

[`Type`](Type.md).[`constructor`](Type.md#constructor)

## Methods

### getMethodSignature()

> **getMethodSignature**(): [`MethodSignature`](MethodSignature.md)

Defined in: src/core/base/Type.ts:375

#### Returns

[`MethodSignature`](MethodSignature.md)

***

### getRealGenericTypes()

> **getRealGenericTypes**(): `undefined` \| [`Type`](Type.md)[]

Defined in: src/core/base/Type.ts:379

#### Returns

`undefined` \| [`Type`](Type.md)[]

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:383

#### Returns

`string`

#### Overrides

[`Type`](Type.md).[`getTypeString`](Type.md#gettypestring)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`Type`](Type.md).[`toString`](Type.md#tostring)




============================================================
## FILE: `classes/GenericType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / GenericType

# Class: GenericType

Defined in: src/core/base/Type.ts:668

## Extends

- [`Type`](Type.md)

## Constructors

### Constructor

> **new GenericType**(`name`, `defaultType?`, `constraint?`): `GenericType`

Defined in: src/core/base/Type.ts:674

#### Parameters

##### name

`string`

##### defaultType?

[`Type`](Type.md)

##### constraint?

[`Type`](Type.md)

#### Returns

`GenericType`

#### Overrides

[`Type`](Type.md).[`constructor`](Type.md#constructor)

## Methods

### getConstraint()

> **getConstraint**(): `undefined` \| [`Type`](Type.md)

Defined in: src/core/base/Type.ts:693

#### Returns

`undefined` \| [`Type`](Type.md)

***

### getDefaultType()

> **getDefaultType**(): `undefined` \| [`Type`](Type.md)

Defined in: src/core/base/Type.ts:685

#### Returns

`undefined` \| [`Type`](Type.md)

***

### getIndex()

> **getIndex**(): `number`

Defined in: src/core/base/Type.ts:705

#### Returns

`number`

***

### getName()

> **getName**(): `string`

Defined in: src/core/base/Type.ts:681

#### Returns

`string`

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:709

#### Returns

`string`

#### Overrides

[`Type`](Type.md).[`getTypeString`](Type.md#gettypestring)

***

### setConstraint()

> **setConstraint**(`type`): `void`

Defined in: src/core/base/Type.ts:697

#### Parameters

##### type

[`Type`](Type.md)

#### Returns

`void`

***

### setDefaultType()

> **setDefaultType**(`type`): `void`

Defined in: src/core/base/Type.ts:689

#### Parameters

##### type

[`Type`](Type.md)

#### Returns

`void`

***

### setIndex()

> **setIndex**(`index`): `void`

Defined in: src/core/base/Type.ts:701

#### Parameters

##### index

`number`

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`Type`](Type.md).[`toString`](Type.md#tostring)




============================================================
## FILE: `classes/GlobalRef.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / GlobalRef

# Class: GlobalRef

Defined in: src/core/base/Ref.ts:316

## Extends

- [`AbstractRef`](AbstractRef.md)

## Constructors

### Constructor

> **new GlobalRef**(`name`, `ref?`): `GlobalRef`

Defined in: src/core/base/Ref.ts:321

#### Parameters

##### name

`string`

##### ref?

[`Value`](../interfaces/Value.md)

#### Returns

`GlobalRef`

#### Overrides

[`AbstractRef`](AbstractRef.md).[`constructor`](AbstractRef.md#constructor)

## Methods

### addUsedStmts()

> **addUsedStmts**(`usedStmts`): `void`

Defined in: src/core/base/Ref.ts:352

#### Parameters

##### usedStmts

[`Stmt`](Stmt.md) | [`Stmt`](Stmt.md)[]

#### Returns

`void`

***

### getName()

> **getName**(): `string`

Defined in: src/core/base/Ref.ts:328

#### Returns

`string`

***

### getRef()

> **getRef**(): `null` \| [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Ref.ts:340

#### Returns

`null` \| [`Value`](../interfaces/Value.md)

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Ref.ts:336

Return the type of this value. The interface is encapsulated in [Value](../interfaces/Value.md). 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`Type`](Type.md)

The type of this value.

#### Example

1. In the declaration statement, determine the left-value type and right-value type.

```typescript
let leftValue:Value;
let rightValue:Value;
...
if (leftValue.getType() instanceof UnknownType && 
   !(rightValue.getType() instanceof UnknownType) &&
   !(rightValue.getType() instanceof UndefinedType)) {
   ...
}
```

#### Overrides

[`AbstractRef`](AbstractRef.md).[`getType`](AbstractRef.md#gettype)

***

### getUsedStmts()

> **getUsedStmts**(): [`Stmt`](Stmt.md)[]

Defined in: src/core/base/Ref.ts:348

#### Returns

[`Stmt`](Stmt.md)[]

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Ref.ts:332

Return a list of values which are contained in this [Value](../interfaces/Value.md).
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this value.

#### Overrides

[`AbstractRef`](AbstractRef.md).[`getUses`](AbstractRef.md#getuses)

***

### inferType()

> **inferType**(`arkMethod`): [`AbstractRef`](AbstractRef.md)

Defined in: src/core/base/Ref.ts:36

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

[`AbstractRef`](AbstractRef.md)

#### Inherited from

[`AbstractRef`](AbstractRef.md).[`inferType`](AbstractRef.md#infertype)

***

### setRef()

> **setRef**(`value`): `void`

Defined in: src/core/base/Ref.ts:344

#### Parameters

##### value

[`Value`](../interfaces/Value.md)

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Ref.ts:360

Returns a string representation of an object.

#### Returns

`string`




============================================================
## FILE: `classes/GraphPrinter.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / GraphPrinter

# Class: GraphPrinter\<GraphType\>

Defined in: src/save/GraphPrinter.ts:64

## Extends

- [`Printer`](Printer.md)

## Type Parameters

### GraphType

`GraphType` *extends* `GraphTraits`\<[`BaseNode`](BaseNode.md)\>

## Constructors

### Constructor

> **new GraphPrinter**\<`GraphType`\>(`g`, `t?`): `GraphPrinter`\<`GraphType`\>

Defined in: src/save/GraphPrinter.ts:69

#### Parameters

##### g

`GraphType`

##### t?

`string`

#### Returns

`GraphPrinter`\<`GraphType`\>

#### Overrides

[`Printer`](Printer.md).[`constructor`](Printer.md#constructor)

## Properties

### graph

> **graph**: `GraphType`

Defined in: src/save/GraphPrinter.ts:65

***

### printer

> `protected` **printer**: `ArkCodeBuffer`

Defined in: src/save/Printer.ts:22

#### Inherited from

[`Printer`](Printer.md).[`printer`](Printer.md#printer)

***

### startID

> **startID**: `undefined` \| `number` = `undefined`

Defined in: src/save/GraphPrinter.ts:67

***

### title

> **title**: `string`

Defined in: src/save/GraphPrinter.ts:66

## Methods

### dump()

> **dump**(): `string`

Defined in: src/save/GraphPrinter.ts:81

ArkIR dump

#### Returns

`string`

#### Overrides

[`Printer`](Printer.md).[`dump`](Printer.md#dump)

***

### setStartID()

> **setStartID**(`n`): `void`

Defined in: src/save/GraphPrinter.ts:77

#### Parameters

##### n

`number`

#### Returns

`void`

***

### writeEdge()

> **writeEdge**(`edge`): `void`

Defined in: src/save/GraphPrinter.ts:126

#### Parameters

##### edge

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

***

### writeFooter()

> **writeFooter**(): `void`

Defined in: src/save/GraphPrinter.ts:146

#### Returns

`void`

***

### writeGraph()

> **writeGraph**(): `void`

Defined in: src/save/GraphPrinter.ts:87

#### Returns

`void`

***

### writeHeader()

> **writeHeader**(): `void`

Defined in: src/save/GraphPrinter.ts:134

#### Returns

`void`

***

### writeNodes()

> **writeNodes**(): `void`

Defined in: src/save/GraphPrinter.ts:93

#### Returns

`void`




============================================================
## FILE: `classes/IRUtils.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / IRUtils

# Class: IRUtils

Defined in: src/core/common/IRUtils.ts:29

## Constructors

### Constructor

> **new IRUtils**(): `IRUtils`

#### Returns

`IRUtils`

## Methods

### adjustOperandOriginalPositions()

> `static` **adjustOperandOriginalPositions**(`stmt`, `oldValue`, `newValue`): `void`

Defined in: src/core/common/IRUtils.ts:110

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

##### oldValue

[`Value`](../interfaces/Value.md)

##### newValue

[`Value`](../interfaces/Value.md)

#### Returns

`void`

***

### findOperandIdx()

> `static` **findOperandIdx**(`stmt`, `operand`): `number`

Defined in: src/core/common/IRUtils.ts:98

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

##### operand

[`Value`](../interfaces/Value.md)

#### Returns

`number`

***

### generateDefaultPositions()

> `static` **generateDefaultPositions**(`count`): [`FullPosition`](FullPosition.md)[]

Defined in: src/core/common/IRUtils.ts:147

#### Parameters

##### count

`number`

#### Returns

[`FullPosition`](FullPosition.md)[]

***

### generateTextForStmt()

> `static` **generateTextForStmt**(`scene`): `void`

Defined in: src/core/common/IRUtils.ts:44

#### Parameters

##### scene

[`Scene`](Scene.md)

#### Returns

`void`

***

### getCommentsMetadata()

> `static` **getCommentsMetadata**(`node`, `sourceFile`, `options`, `isLeading`): `CommentsMetadata`

Defined in: src/core/common/IRUtils.ts:67

#### Parameters

##### node

[`Node`](../ArkAnalyzer/namespaces/ts/interfaces/Node.md)

##### sourceFile

[`SourceFile`](../ArkAnalyzer/namespaces/ts/interfaces/SourceFile.md)

##### options

`SceneOptions`

##### isLeading

`boolean`

#### Returns

`CommentsMetadata`

***

### isTempLocal()

> `static` **isTempLocal**(`value`): `boolean`

Defined in: src/core/common/IRUtils.ts:94

#### Parameters

##### value

[`Value`](../interfaces/Value.md)

#### Returns

`boolean`

***

### moreThanOneAddress()

> `static` **moreThanOneAddress**(`value`): `boolean`

Defined in: src/core/common/IRUtils.ts:30

#### Parameters

##### value

[`Value`](../interfaces/Value.md)

#### Returns

`boolean`

***

### setComments()

> `static` **setComments**(`metadata`, `node`, `sourceFile`, `options`): `void`

Defined in: src/core/common/IRUtils.ts:55

#### Parameters

##### metadata

`ArkBaseModel` | [`Stmt`](Stmt.md)

##### node

[`Node`](../ArkAnalyzer/namespaces/ts/interfaces/Node.md)

##### sourceFile

[`SourceFile`](../ArkAnalyzer/namespaces/ts/interfaces/SourceFile.md)

##### options

`SceneOptions`

#### Returns

`void`




============================================================
## FILE: `classes/ImportInfo.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ImportInfo

# Class: ImportInfo

Defined in: src/core/model/ArkImport.ts:26

## Extends

- `ArkBaseModel`

## Implements

- `FromInfo`

## Constructors

### Constructor

> **new ImportInfo**(): `ImportInfo`

Defined in: src/core/model/ArkImport.ts:37

#### Returns

`ImportInfo`

#### Overrides

`ArkBaseModel.constructor`

## Properties

### decorators?

> `protected` `optional` **decorators**: `Set`\<[`Decorator`](Decorator.md)\>

Defined in: src/core/model/ArkBaseModel.ts:115

#### Inherited from

`ArkBaseModel.decorators`

***

### metadata?

> `protected` `optional` **metadata**: `ArkMetadata`

Defined in: src/core/model/ArkBaseModel.ts:116

#### Inherited from

`ArkBaseModel.metadata`

***

### modifiers?

> `protected` `optional` **modifiers**: `number`

Defined in: src/core/model/ArkBaseModel.ts:114

#### Inherited from

`ArkBaseModel.modifiers`

## Methods

### addDecorator()

> **addDecorator**(`decorator`): `void`

Defined in: src/core/model/ArkBaseModel.ts:215

#### Parameters

##### decorator

[`Decorator`](Decorator.md)

#### Returns

`void`

#### Inherited from

`ArkBaseModel.addDecorator`

***

### addModifier()

> **addModifier**(`modifier`): `void`

Defined in: src/core/model/ArkBaseModel.ts:142

#### Parameters

##### modifier

`number`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.addModifier`

***

### build()

> **build**(`importClauseName`, `importType`, `importFrom`, `originTsPosition`, `modifiers`, `nameBeforeAs?`): `void`

Defined in: src/core/model/ArkImport.ts:48

#### Parameters

##### importClauseName

`string`

##### importType

`string`

##### importFrom

`string`

##### originTsPosition

[`LineColPosition`](LineColPosition.md)

##### modifiers

`number`

##### nameBeforeAs?

`string`

#### Returns

`void`

***

### containsModifier()

> **containsModifier**(`modifierType`): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:194

#### Parameters

##### modifierType

`ModifierType`

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.containsModifier`

***

### getDeclaringArkFile()

> **getDeclaringArkFile**(): [`ArkFile`](ArkFile.md)

Defined in: src/core/model/ArkImport.ts:85

#### Returns

[`ArkFile`](ArkFile.md)

#### Implementation of

`FromInfo.getDeclaringArkFile`

***

### getDecorators()

> **getDecorators**(): [`Decorator`](Decorator.md)[]

Defined in: src/core/model/ArkBaseModel.ts:202

#### Returns

[`Decorator`](Decorator.md)[]

#### Inherited from

`ArkBaseModel.getDecorators`

***

### getFrom()

> **getFrom**(): `undefined` \| `string`

Defined in: src/core/model/ArkImport.ts:133

#### Returns

`undefined` \| `string`

#### Implementation of

`FromInfo.getFrom`

***

### getImportClauseName()

> **getImportClauseName**(): `string`

Defined in: src/core/model/ArkImport.ts:89

#### Returns

`string`

***

### getImportType()

> **getImportType**(): `string`

Defined in: src/core/model/ArkImport.ts:97

#### Returns

`string`

***

### getLanguage()

> **getLanguage**(): `Language`

Defined in: src/core/model/ArkImport.ts:44

Returns the program language of the file where this import info defined.

#### Returns

`Language`

***

### getLazyExportInfo()

> **getLazyExportInfo**(): `null` \| [`ExportInfo`](ExportInfo.md)

Defined in: src/core/model/ArkImport.ts:74

Returns the export information, i.e., the actual reference generated at the time of call.
The export information includes: clause's name, clause's type, modifiers, location
where it is exported from, etc. If the export information could not be found, **null** will be returned.

#### Returns

`null` \| [`ExportInfo`](ExportInfo.md)

The export information. If there is no export information, the return will be a **null**.

***

### getMetadata()

> **getMetadata**(`kind`): `undefined` \| `ArkMetadataType`

Defined in: src/core/model/ArkBaseModel.ts:118

#### Parameters

##### kind

`ArkMetadataKind`

#### Returns

`undefined` \| `ArkMetadataType`

#### Inherited from

`ArkBaseModel.getMetadata`

***

### getModifiers()

> **getModifiers**(): `number`

Defined in: src/core/model/ArkBaseModel.ts:129

#### Returns

`number`

#### Inherited from

`ArkBaseModel.getModifiers`

***

### getNameBeforeAs()

> **getNameBeforeAs**(): `undefined` \| `string`

Defined in: src/core/model/ArkImport.ts:109

#### Returns

`undefined` \| `string`

***

### getOriginName()

> **getOriginName**(): `string`

Defined in: src/core/model/ArkImport.ts:64

#### Returns

`string`

#### Implementation of

`FromInfo.getOriginName`

***

### getOriginTsPosition()

> **getOriginTsPosition**(): [`LineColPosition`](LineColPosition.md)

Defined in: src/core/model/ArkImport.ts:121

#### Returns

[`LineColPosition`](LineColPosition.md)

***

### getStateDecorators()

> **getStateDecorators**(): [`Decorator`](Decorator.md)[]

Defined in: src/core/model/ArkBaseModel.ts:234

#### Returns

[`Decorator`](Decorator.md)[]

#### Inherited from

`ArkBaseModel.getStateDecorators`

***

### getTsSourceCode()

> **getTsSourceCode**(): `string`

Defined in: src/core/model/ArkImport.ts:129

#### Returns

`string`

***

### hasBuilderDecorator()

> **hasBuilderDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:230

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasBuilderDecorator`

***

### hasBuilderParamDecorator()

> **hasBuilderParamDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:243

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasBuilderParamDecorator`

***

### hasComponentDecorator()

> **hasComponentDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:251

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasComponentDecorator`

***

### hasDecorator()

> **hasDecorator**(`kind`): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:255

#### Parameters

##### kind

`string` | `Set`\<`string`\>

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasDecorator`

***

### hasEntryDecorator()

> **hasEntryDecorator**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:247

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.hasEntryDecorator`

***

### isAbstract()

> **isAbstract**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:173

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isAbstract`

***

### isDeclare()

> **isDeclare**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:190

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isDeclare`

***

### isDefault()

> **isDefault**(): `boolean`

Defined in: src/core/model/ArkImport.ts:137

#### Returns

`boolean`

#### Implementation of

`FromInfo.isDefault`

#### Overrides

`ArkBaseModel.isDefault`

***

### isExport()

> **isExport**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:177

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isExport`

***

### ~~isExported()~~

> **isExported**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:186

#### Returns

`boolean`

#### Deprecated

Use [isExport](ArkNamespace.md#isexport) instead.

#### Inherited from

`ArkBaseModel.isExported`

***

### isPrivate()

> **isPrivate**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:161

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isPrivate`

***

### isProtected()

> **isProtected**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:157

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isProtected`

***

### isPublic()

> **isPublic**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:165

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isPublic`

***

### isReadonly()

> **isReadonly**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:169

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isReadonly`

***

### isStatic()

> **isStatic**(): `boolean`

Defined in: src/core/model/ArkBaseModel.ts:153

#### Returns

`boolean`

#### Inherited from

`ArkBaseModel.isStatic`

***

### removeDecorator()

> **removeDecorator**(`kind`): `void`

Defined in: src/core/model/ArkBaseModel.ts:222

#### Parameters

##### kind

`string`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.removeDecorator`

***

### removeModifier()

> **removeModifier**(`modifier`): `void`

Defined in: src/core/model/ArkBaseModel.ts:146

#### Parameters

##### modifier

`ModifierType`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.removeModifier`

***

### setDeclaringArkFile()

> **setDeclaringArkFile**(`declaringArkFile`): `void`

Defined in: src/core/model/ArkImport.ts:81

#### Parameters

##### declaringArkFile

[`ArkFile`](ArkFile.md)

#### Returns

`void`

***

### setDecorators()

> **setDecorators**(`decorators`): `void`

Defined in: src/core/model/ArkBaseModel.ts:209

#### Parameters

##### decorators

`Set`\<[`Decorator`](Decorator.md)\>

#### Returns

`void`

#### Inherited from

`ArkBaseModel.setDecorators`

***

### setImportClauseName()

> **setImportClauseName**(`importClauseName`): `void`

Defined in: src/core/model/ArkImport.ts:93

#### Parameters

##### importClauseName

`string`

#### Returns

`void`

***

### setImportFrom()

> **setImportFrom**(`importFrom`): `void`

Defined in: src/core/model/ArkImport.ts:105

#### Parameters

##### importFrom

`string`

#### Returns

`void`

***

### setImportType()

> **setImportType**(`importType`): `void`

Defined in: src/core/model/ArkImport.ts:101

#### Parameters

##### importType

`string`

#### Returns

`void`

***

### setMetadata()

> **setMetadata**(`kind`, `value`): `void`

Defined in: src/core/model/ArkBaseModel.ts:122

#### Parameters

##### kind

`ArkMetadataKind`

##### value

`ArkMetadataType`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.setMetadata`

***

### setModifiers()

> **setModifiers**(`modifiers`): `void`

Defined in: src/core/model/ArkBaseModel.ts:136

#### Parameters

##### modifiers

`number`

#### Returns

`void`

#### Inherited from

`ArkBaseModel.setModifiers`

***

### setNameBeforeAs()

> **setNameBeforeAs**(`nameBeforeAs`): `void`

Defined in: src/core/model/ArkImport.ts:113

#### Parameters

##### nameBeforeAs

`undefined` | `string`

#### Returns

`void`

***

### setOriginTsPosition()

> **setOriginTsPosition**(`originTsPosition`): `void`

Defined in: src/core/model/ArkImport.ts:117

#### Parameters

##### originTsPosition

[`LineColPosition`](LineColPosition.md)

#### Returns

`void`

***

### setTsSourceCode()

> **setTsSourceCode**(`tsSourceCode`): `void`

Defined in: src/core/model/ArkImport.ts:125

#### Parameters

##### tsSourceCode

`string`

#### Returns

`void`

***

### validate()

> **validate**(): `ArkError`

Defined in: src/core/model/ArkImport.ts:144

#### Returns

`ArkError`

#### Overrides

`ArkBaseModel.validate`

***

### validateFields()

> `protected` **validateFields**(`fields`): `ArkError`

Defined in: src/core/model/ArkBaseModel.ts:267

#### Parameters

##### fields

`string`[]

#### Returns

`ArkError`

#### Inherited from

`ArkBaseModel.validateFields`




============================================================
## FILE: `classes/InterFuncPag.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / InterFuncPag

# Class: InterFuncPag

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1114

## Constructors

### Constructor

> **new InterFuncPag**(): `InterFuncPag`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1117

#### Returns

`InterFuncPag`

## Methods

### addToInterProceduralEdgeSet()

> **addToInterProceduralEdgeSet**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1125

#### Parameters

##### e

[`InterProceduralEdge`](../type-aliases/InterProceduralEdge.md)

#### Returns

`void`

***

### getInterProceduralEdges()

> **getInterProceduralEdges**(): `Set`\<[`InterProceduralEdge`](../type-aliases/InterProceduralEdge.md)\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1121

#### Returns

`Set`\<[`InterProceduralEdge`](../type-aliases/InterProceduralEdge.md)\>




============================================================
## FILE: `classes/IntersectionType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / IntersectionType

# Class: IntersectionType

Defined in: src/core/base/Type.ts:300

intersection type

## Extends

- [`Type`](Type.md)

## Constructors

### Constructor

> **new IntersectionType**(`types`): `IntersectionType`

Defined in: src/core/base/Type.ts:303

#### Parameters

##### types

[`Type`](Type.md)[]

#### Returns

`IntersectionType`

#### Overrides

[`Type`](Type.md).[`constructor`](Type.md#constructor)

## Methods

### getTypes()

> **getTypes**(): [`Type`](Type.md)[]

Defined in: src/core/base/Type.ts:308

#### Returns

[`Type`](Type.md)[]

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:312

#### Returns

`string`

#### Overrides

[`Type`](Type.md).[`getTypeString`](Type.md#gettypestring)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`Type`](Type.md).[`toString`](Type.md#tostring)




============================================================
## FILE: `classes/JsonPrinter.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / JsonPrinter

# Class: JsonPrinter

Defined in: src/save/JsonPrinter.ts:87

## Extends

- [`Printer`](Printer.md)

## Constructors

### Constructor

> **new JsonPrinter**(`arkFile`): `JsonPrinter`

Defined in: src/save/JsonPrinter.ts:88

#### Parameters

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

`JsonPrinter`

#### Overrides

[`Printer`](Printer.md).[`constructor`](Printer.md#constructor)

## Properties

### printer

> `protected` **printer**: `ArkCodeBuffer`

Defined in: src/save/Printer.ts:22

#### Inherited from

[`Printer`](Printer.md).[`printer`](Printer.md#printer)

## Methods

### dump()

> **dump**(): `string`

Defined in: src/save/JsonPrinter.ts:92

ArkIR dump

#### Returns

`string`

#### Overrides

[`Printer`](Printer.md).[`dump`](Printer.md#dump)




============================================================
## FILE: `classes/KLimitedContextSensitive.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / KLimitedContextSensitive

# Class: KLimitedContextSensitive

Defined in: src/callgraph/pointerAnalysis/Context.ts:131

## Constructors

### Constructor

> **new KLimitedContextSensitive**(`k`): `KLimitedContextSensitive`

Defined in: src/callgraph/pointerAnalysis/Context.ts:135

#### Parameters

##### k

`number`

#### Returns

`KLimitedContextSensitive`

## Properties

### ctxCache

> **ctxCache**: `ContextCache`

Defined in: src/callgraph/pointerAnalysis/Context.ts:133

***

### k

> **k**: `number`

Defined in: src/callgraph/pointerAnalysis/Context.ts:132

## Methods

### emptyContext()

> **emptyContext**(): `Context`

Defined in: src/callgraph/pointerAnalysis/Context.ts:142

#### Returns

`Context`

***

### getContextByID()

> **getContextByID**(`context_id`): `undefined` \| `Context`

Defined in: src/callgraph/pointerAnalysis/Context.ts:154

#### Parameters

##### context\_id

`number`

#### Returns

`undefined` \| `Context`

***

### getContextID()

> **getContextID**(`context`): `number`

Defined in: src/callgraph/pointerAnalysis/Context.ts:150

#### Parameters

##### context

`Context`

#### Returns

`number`

***

### getEmptyContextID()

> **getEmptyContextID**(): `number`

Defined in: src/callgraph/pointerAnalysis/Context.ts:146

#### Returns

`number`

***

### getNewContextID()

> **getNewContextID**(`callerFuncId`): `number`

Defined in: src/callgraph/pointerAnalysis/Context.ts:158

#### Parameters

##### callerFuncId

`number`

#### Returns

`number`

***

### getOrNewContext()

> **getOrNewContext**(`callerCid`, `calleeFuncId`, `findCalleeAsTop`): `number`

Defined in: src/callgraph/pointerAnalysis/Context.ts:162

#### Parameters

##### callerCid

`number`

##### calleeFuncId

`number`

##### findCalleeAsTop

`boolean` = `false`

#### Returns

`number`




============================================================
## FILE: `classes/LexicalEnvType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / LexicalEnvType

# Class: LexicalEnvType

Defined in: src/core/base/Type.ts:770

## Extends

- [`Type`](Type.md)

## Constructors

### Constructor

> **new LexicalEnvType**(`nestedMethod`, `closures?`): `LexicalEnvType`

Defined in: src/core/base/Type.ts:774

#### Parameters

##### nestedMethod

[`MethodSignature`](MethodSignature.md)

##### closures?

[`Local`](Local.md)[]

#### Returns

`LexicalEnvType`

#### Overrides

[`Type`](Type.md).[`constructor`](Type.md#constructor)

## Methods

### addClosure()

> **addClosure**(`closure`): `void`

Defined in: src/core/base/Type.ts:788

#### Parameters

##### closure

[`Local`](Local.md)

#### Returns

`void`

***

### getClosures()

> **getClosures**(): [`Local`](Local.md)[]

Defined in: src/core/base/Type.ts:784

#### Returns

[`Local`](Local.md)[]

***

### getNestedMethod()

> **getNestedMethod**(): [`MethodSignature`](MethodSignature.md)

Defined in: src/core/base/Type.ts:780

#### Returns

[`MethodSignature`](MethodSignature.md)

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:792

#### Returns

`string`

#### Overrides

[`Type`](Type.md).[`getTypeString`](Type.md#gettypestring)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`Type`](Type.md).[`toString`](Type.md#tostring)




============================================================
## FILE: `classes/LineColPosition.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / LineColPosition

# Class: LineColPosition

Defined in: src/core/base/Position.ts:80

## Constructors

### Constructor

> **new LineColPosition**(`lineNo`, `colNo`): `LineColPosition`

Defined in: src/core/base/Position.ts:85

#### Parameters

##### lineNo

`number`

##### colNo

`number`

#### Returns

`LineColPosition`

## Properties

### DEFAULT

> `readonly` `static` **DEFAULT**: `LineColPosition`

Defined in: src/core/base/Position.ts:83

## Methods

### getColNo()

> **getColNo**(): `number`

Defined in: src/core/base/Position.ts:93

#### Returns

`number`

***

### getLineNo()

> **getLineNo**(): `number`

Defined in: src/core/base/Position.ts:89

#### Returns

`number`

***

### buildFromNode()

> `static` **buildFromNode**(`node`, `sourceFile`): `LineColPosition`

Defined in: src/core/base/Position.ts:97

#### Parameters

##### node

[`Node`](../ArkAnalyzer/namespaces/ts/interfaces/Node.md)

##### sourceFile

[`SourceFile`](../ArkAnalyzer/namespaces/ts/interfaces/SourceFile.md)

#### Returns

`LineColPosition`




============================================================
## FILE: `classes/LiteralType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / LiteralType

# Class: LiteralType

Defined in: src/core/base/Type.ts:225

literal type

## Extends

- [`PrimitiveType`](PrimitiveType.md)

## Constructors

### Constructor

> **new LiteralType**(`literalName`): `LiteralType`

Defined in: src/core/base/Type.ts:231

#### Parameters

##### literalName

`string` | `number` | `boolean`

#### Returns

`LiteralType`

#### Overrides

[`PrimitiveType`](PrimitiveType.md).[`constructor`](PrimitiveType.md#constructor)

## Properties

### FALSE

> `readonly` `static` **FALSE**: `LiteralType`

Defined in: src/core/base/Type.ts:227

***

### TRUE

> `readonly` `static` **TRUE**: `LiteralType`

Defined in: src/core/base/Type.ts:226

## Methods

### getLiteralName()

> **getLiteralName**(): `string` \| `number` \| `boolean`

Defined in: src/core/base/Type.ts:236

#### Returns

`string` \| `number` \| `boolean`

***

### getName()

> **getName**(): `string`

Defined in: src/core/base/Type.ts:128

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`getName`](PrimitiveType.md#getname)

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:240

#### Returns

`string`

#### Overrides

[`PrimitiveType`](PrimitiveType.md).[`getTypeString`](PrimitiveType.md#gettypestring)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`toString`](PrimitiveType.md#tostring)




============================================================
## FILE: `classes/LoadPagEdge.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / LoadPagEdge

# Class: LoadPagEdge

Defined in: src/callgraph/pointerAnalysis/Pag.ts:110

## Extends

- [`PagEdge`](PagEdge.md)

## Constructors

### Constructor

> **new LoadPagEdge**(`n`, `d`, `s`): `LoadPagEdge`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:111

#### Parameters

##### n

[`PagNode`](PagNode.md)

##### d

[`PagNode`](PagNode.md)

##### s

[`Stmt`](Stmt.md)

#### Returns

`LoadPagEdge`

#### Overrides

[`PagEdge`](PagEdge.md).[`constructor`](PagEdge.md#constructor)

## Properties

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:22

#### Inherited from

[`PagEdge`](PagEdge.md).[`kind`](PagEdge.md#kind)

## Methods

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:75

#### Returns

`string`

#### Inherited from

[`PagEdge`](PagEdge.md).[`getDotAttr`](PagEdge.md#getdotattr)

***

### getDstID()

> **getDstID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:34

#### Returns

`number`

#### Inherited from

[`PagEdge`](PagEdge.md).[`getDstID`](PagEdge.md#getdstid)

***

### getDstNode()

> **getDstNode**(): [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:42

#### Returns

[`BaseNode`](BaseNode.md)

#### Inherited from

[`PagEdge`](PagEdge.md).[`getDstNode`](PagEdge.md#getdstnode)

***

### getEndPoints()

> **getEndPoints**(): `object`

Defined in: src/core/graph/BaseExplicitGraph.ts:54

#### Returns

`object`

##### dst

> **dst**: `number`

##### src

> **src**: `number`

#### Inherited from

[`PagEdge`](PagEdge.md).[`getEndPoints`](PagEdge.md#getendpoints)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:46

#### Returns

`number`

#### Inherited from

[`PagEdge`](PagEdge.md).[`getKind`](PagEdge.md#getkind)

***

### getSrcID()

> **getSrcID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:30

#### Returns

`number`

#### Inherited from

[`PagEdge`](PagEdge.md).[`getSrcID`](PagEdge.md#getsrcid)

***

### getSrcNode()

> **getSrcNode**(): [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:38

#### Returns

[`BaseNode`](BaseNode.md)

#### Inherited from

[`PagEdge`](PagEdge.md).[`getSrcNode`](PagEdge.md#getsrcnode)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:50

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`PagEdge`](PagEdge.md).[`setKind`](PagEdge.md#setkind)




============================================================
## FILE: `classes/Local.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Local

# Class: Local

Defined in: src/core/base/Local.ts:32

## Implements

- [`Value`](../interfaces/Value.md)
- `ArkExport`

## Constructors

### Constructor

> **new Local**(`name`, `type`): `Local`

Defined in: src/core/base/Local.ts:43

#### Parameters

##### name

`string`

##### type

[`Type`](Type.md) = `...`

#### Returns

`Local`

## Methods

### addUsedStmt()

> **addUsedStmt**(`usedStmt`): `void`

Defined in: src/core/base/Local.ts:151

#### Parameters

##### usedStmt

[`Stmt`](Stmt.md)

#### Returns

`void`

***

### containsModifier()

> **containsModifier**(`modifierType`): `boolean`

Defined in: src/core/base/Local.ts:191

#### Parameters

##### modifierType

`ModifierType`

#### Returns

`boolean`

#### Implementation of

`ArkExport.containsModifier`

***

### getConstFlag()

> **getConstFlag**(): `boolean`

Defined in: src/core/base/Local.ts:212

#### Returns

`boolean`

***

### getDeclaringStmt()

> **getDeclaringStmt**(): `null` \| [`Stmt`](Stmt.md)

Defined in: src/core/base/Local.ts:135

Returns the declaring statement, which may also be a **null**.
For example, if the code snippet in a function is `let dd = cc + 5;` where `cc` is a **number**
and `dd` is not defined before, then the declaring statemet of local `dd`:
- its **string** text is "dd = cc + 5".
- the **strings** of right operand and left operand are "cc + 5" and "dd", respectively.
- three values are used in this statement: `cc + 5` (i.e., a normal binary operation expression), `cc` (a local), and `5` (a constant), respectively.

#### Returns

`null` \| [`Stmt`](Stmt.md)

The declaring statement (maybe a **null**) of the local.

#### Example

1. get the statement that defines the local for the first time.

```typescript
let stmt = local.getDeclaringStmt();
if (stmt !== null) {
...
}
```

***

### getExportType()

> **getExportType**(): `ExportType`

Defined in: src/core/base/Local.ts:183

#### Returns

`ExportType`

#### Implementation of

`ArkExport.getExportType`

***

### getModifiers()

> **getModifiers**(): `number`

Defined in: src/core/base/Local.ts:187

#### Returns

`number`

#### Implementation of

`ArkExport.getModifiers`

***

### getName()

> **getName**(): `string`

Defined in: src/core/base/Local.ts:89

Returns the name of local value.

#### Returns

`string`

The name of local value.

#### Example

1. get the name of local value.

```typescript
arkClass.getDefaultArkMethod()?.getBody().getLocals().forEach(local => {
const arkField = new ArkField();
arkField.setFieldType(ArkField.DEFAULT_ARK_Field);
arkField.setDeclaringClass(defaultClass);
arkField.setType(local.getType());
arkField.setName(local.getName());
arkField.genSignature();
defaultClass.addField(arkField);
});
```

#### Implementation of

`ArkExport.getName`

***

### getOriginalValue()

> **getOriginalValue**(): `null` \| [`Value`](../interfaces/Value.md)

Defined in: src/core/base/Local.ts:109

#### Returns

`null` \| [`Value`](../interfaces/Value.md)

***

### getSignature()

> **getSignature**(): [`LocalSignature`](LocalSignature.md)

Defined in: src/core/base/Local.ts:198

#### Returns

[`LocalSignature`](LocalSignature.md)

#### Implementation of

`ArkExport.getSignature`

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/base/Local.ts:101

Returns the type of this local.

#### Returns

[`Type`](Type.md)

The type of this local.

#### Implementation of

[`Value`](../interfaces/Value.md).[`getType`](../interfaces/Value.md#gettype)

***

### getUsedStmts()

> **getUsedStmts**(): [`Stmt`](Stmt.md)[]

Defined in: src/core/base/Local.ts:162

Returns an array of statements used by the local, i.e., the statements in which the local participate.
For example, if the code snippet is `let dd = cc + 5;` where `cc` is a local and `cc` only appears once,
then the length of **array** returned is 1 and `Stmts[0]` will be same as the example described
in the `Local.getDeclaringStmt()`.

#### Returns

[`Stmt`](Stmt.md)[]

An array of statements used by the local.

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Local.ts:147

Returns an **array** of values which are contained in this local.

#### Returns

[`Value`](../interfaces/Value.md)[]

An **array** of values used by this local.

#### Implementation of

[`Value`](../interfaces/Value.md).[`getUses`](../interfaces/Value.md#getuses)

***

### inferType()

> **inferType**(`arkMethod`): `Local`

Defined in: src/core/base/Local.ts:52

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

`Local`

***

### setConstFlag()

> **setConstFlag**(`newConstFlag`): `void`

Defined in: src/core/base/Local.ts:219

#### Parameters

##### newConstFlag

`boolean`

#### Returns

`void`

***

### setDeclaringStmt()

> **setDeclaringStmt**(`declaringStmt`): `void`

Defined in: src/core/base/Local.ts:139

#### Parameters

##### declaringStmt

[`Stmt`](Stmt.md)

#### Returns

`void`

***

### setName()

> **setName**(`name`): `void`

Defined in: src/core/base/Local.ts:93

#### Parameters

##### name

`string`

#### Returns

`void`

***

### setOriginalValue()

> **setOriginalValue**(`originalValue`): `void`

Defined in: src/core/base/Local.ts:113

#### Parameters

##### originalValue

[`Value`](../interfaces/Value.md)

#### Returns

`void`

***

### setSignature()

> **setSignature**(`signature`): `void`

Defined in: src/core/base/Local.ts:208

#### Parameters

##### signature

[`LocalSignature`](LocalSignature.md)

#### Returns

`void`

***

### setType()

> **setType**(`newType`): `void`

Defined in: src/core/base/Local.ts:105

#### Parameters

##### newType

[`Type`](Type.md)

#### Returns

`void`

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Local.ts:179

Get a string of local name in Local

#### Returns

`string`

The string of local name.

#### Example

1. get a name string.

```typescript
for (const value of stmt.getUses()) {
const name = value.toString();
...
}
```




============================================================
## FILE: `classes/LocalSignature.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / LocalSignature

# Class: LocalSignature

Defined in: src/core/model/ArkSignature.ts:389

## Constructors

### Constructor

> **new LocalSignature**(`name`, `declaringMethodSignature`): `LocalSignature`

Defined in: src/core/model/ArkSignature.ts:393

#### Parameters

##### name

`string`

##### declaringMethodSignature

[`MethodSignature`](MethodSignature.md)

#### Returns

`LocalSignature`

## Methods

### getDeclaringMethodSignature()

> **getDeclaringMethodSignature**(): [`MethodSignature`](MethodSignature.md)

Defined in: src/core/model/ArkSignature.ts:402

#### Returns

[`MethodSignature`](MethodSignature.md)

***

### getName()

> **getName**(): `string`

Defined in: src/core/model/ArkSignature.ts:398

#### Returns

`string`

***

### toString()

> **toString**(): `string`

Defined in: src/core/model/ArkSignature.ts:406

#### Returns

`string`




============================================================
## FILE: `classes/Logger.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Logger

# Class: Logger

Defined in: src/utils/logger.ts:34

## Constructors

### Constructor

> **new Logger**(): `ConsoleLogger`

#### Returns

`ConsoleLogger`

## Methods

### configure()

> `static` **configure**(`logFilePath`, `arkanalyzer_level`, `tool_level`, `use_console`): `void`

Defined in: src/utils/logger.ts:35

#### Parameters

##### logFilePath

`string`

##### arkanalyzer\_level

[`LOG_LEVEL`](../enumerations/LOG_LEVEL.md) = `LOG_LEVEL.ERROR`

##### tool\_level

[`LOG_LEVEL`](../enumerations/LOG_LEVEL.md) = `LOG_LEVEL.INFO`

##### use\_console

`boolean` = `false`

#### Returns

`void`

***

### getLogger()

> `static` **getLogger**(`log_type`, `tag`): `Logger`

Defined in: src/utils/logger.ts:90

#### Parameters

##### log\_type

[`LOG_MODULE_TYPE`](../enumerations/LOG_MODULE_TYPE.md)

##### tag

`string` = `'-'`

#### Returns

`Logger`




============================================================
## FILE: `classes/MethodSignature.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / MethodSignature

# Class: MethodSignature

Defined in: src/core/model/ArkSignature.ts:327

## Constructors

### Constructor

> **new MethodSignature**(`declaringClassSignature`, `methodSubSignature`): `MethodSignature`

Defined in: src/core/model/ArkSignature.ts:331

#### Parameters

##### declaringClassSignature

[`ClassSignature`](ClassSignature.md)

##### methodSubSignature

[`MethodSubSignature`](MethodSubSignature.md)

#### Returns

`MethodSignature`

## Methods

### getDeclaringClassSignature()

> **getDeclaringClassSignature**(): [`ClassSignature`](ClassSignature.md)

Defined in: src/core/model/ArkSignature.ts:354

Return the declaring class signature.
A [ClassSignature](ClassSignature.md) includes:
- File Signature: including the **string** names of the project and file, respectively.
The default value of project's name is "%unk" and the default value of file's name is "%unk".
- Namespace Signature | **null**:  it may be a namespace signature or **null**.
A namespace signature can indicate its **string** name of namespace and its file signature.
- Class Name: the **string** name of this class.

#### Returns

[`ClassSignature`](ClassSignature.md)

The declaring class signature.

#### Example

1. get class signature from ArkMethod.

```typescript
let methodSignature = expr.getMethodSignature();
let name = methodSignature.getDeclaringClassSignature().getClassName();
```

***

### getMethodSubSignature()

> **getMethodSubSignature**(): [`MethodSubSignature`](MethodSubSignature.md)

Defined in: src/core/model/ArkSignature.ts:364

Returns the sub-signature of this method signature.
The sub-signature is part of the method signature, which is used to
identify the name of the method, its parameters and the return value type.

#### Returns

[`MethodSubSignature`](MethodSubSignature.md)

The sub-signature of this method signature.

***

### getParamLength()

> **getParamLength**(): `number`

Defined in: src/core/model/ArkSignature.ts:384

#### Returns

`number`

***

### getType()

> **getType**(): [`Type`](Type.md)

Defined in: src/core/model/ArkSignature.ts:368

#### Returns

[`Type`](Type.md)

***

### isMatch()

> **isMatch**(`signature`): `boolean`

Defined in: src/core/model/ArkSignature.ts:380

#### Parameters

##### signature

`MethodSignature`

#### Returns

`boolean`

***

### toMapKey()

> **toMapKey**(): `string`

Defined in: src/core/model/ArkSignature.ts:376

#### Returns

`string`

***

### toString()

> **toString**(`ptrName?`): `string`

Defined in: src/core/model/ArkSignature.ts:372

#### Parameters

##### ptrName?

`string`

#### Returns

`string`




============================================================
## FILE: `classes/MethodSignatureManager.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / MethodSignatureManager

# Class: MethodSignatureManager

Defined in: src/utils/callGraphUtils.ts:25

## Constructors

### Constructor

> **new MethodSignatureManager**(): `MethodSignatureManager`

#### Returns

`MethodSignatureManager`

## Accessors

### processedList

#### Get Signature

> **get** **processedList**(): [`MethodSignature`](MethodSignature.md)[]

Defined in: src/utils/callGraphUtils.ts:37

##### Returns

[`MethodSignature`](MethodSignature.md)[]

#### Set Signature

> **set** **processedList**(`list`): `void`

Defined in: src/utils/callGraphUtils.ts:41

##### Parameters

###### list

[`MethodSignature`](MethodSignature.md)[]

##### Returns

`void`

***

### workList

#### Get Signature

> **get** **workList**(): [`MethodSignature`](MethodSignature.md)[]

Defined in: src/utils/callGraphUtils.ts:29

##### Returns

[`MethodSignature`](MethodSignature.md)[]

#### Set Signature

> **set** **workList**(`list`): `void`

Defined in: src/utils/callGraphUtils.ts:33

##### Parameters

###### list

[`MethodSignature`](MethodSignature.md)[]

##### Returns

`void`

## Methods

### addToProcessedList()

> **addToProcessedList**(`signature`): `void`

Defined in: src/utils/callGraphUtils.ts:60

#### Parameters

##### signature

[`MethodSignature`](MethodSignature.md)

#### Returns

`void`

***

### addToWorkList()

> **addToWorkList**(`signature`): `void`

Defined in: src/utils/callGraphUtils.ts:54

#### Parameters

##### signature

[`MethodSignature`](MethodSignature.md)

#### Returns

`void`

***

### findInProcessedList()

> **findInProcessedList**(`signature`): `boolean`

Defined in: src/utils/callGraphUtils.ts:49

#### Parameters

##### signature

[`MethodSignature`](MethodSignature.md)

#### Returns

`boolean`

***

### findInWorkList()

> **findInWorkList**(`signature`): `undefined` \| [`MethodSignature`](MethodSignature.md)

Defined in: src/utils/callGraphUtils.ts:45

#### Parameters

##### signature

[`MethodSignature`](MethodSignature.md)

#### Returns

`undefined` \| [`MethodSignature`](MethodSignature.md)

***

### removeFromProcessedList()

> **removeFromProcessedList**(`signature`): `void`

Defined in: src/utils/callGraphUtils.ts:70

#### Parameters

##### signature

[`MethodSignature`](MethodSignature.md)

#### Returns

`void`

***

### removeFromWorkList()

> **removeFromWorkList**(`signature`): `void`

Defined in: src/utils/callGraphUtils.ts:66

#### Parameters

##### signature

[`MethodSignature`](MethodSignature.md)

#### Returns

`void`




============================================================
## FILE: `classes/MethodSubSignature.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / MethodSubSignature

# Class: MethodSubSignature

Defined in: src/core/model/ArkSignature.ts:269

## Constructors

### Constructor

> **new MethodSubSignature**(`methodName`, `parameters`, `returnType`, `staticFlag`): `MethodSubSignature`

Defined in: src/core/model/ArkSignature.ts:275

#### Parameters

##### methodName

`string`

##### parameters

`MethodParameter`[]

##### returnType

[`Type`](Type.md)

##### staticFlag

`boolean` = `false`

#### Returns

`MethodSubSignature`

## Methods

### getMethodName()

> **getMethodName**(): `string`

Defined in: src/core/model/ArkSignature.ts:282

#### Returns

`string`

***

### getParameters()

> **getParameters**(): `MethodParameter`[]

Defined in: src/core/model/ArkSignature.ts:286

#### Returns

`MethodParameter`[]

***

### getParameterTypes()

> **getParameterTypes**(): [`Type`](Type.md)[]

Defined in: src/core/model/ArkSignature.ts:290

#### Returns

[`Type`](Type.md)[]

***

### getReturnType()

> **getReturnType**(): [`Type`](Type.md)

Defined in: src/core/model/ArkSignature.ts:298

#### Returns

[`Type`](Type.md)

***

### isStatic()

> **isStatic**(): `boolean`

Defined in: src/core/model/ArkSignature.ts:306

#### Returns

`boolean`

***

### setReturnType()

> **setReturnType**(`returnType`): `void`

Defined in: src/core/model/ArkSignature.ts:302

#### Parameters

##### returnType

[`Type`](Type.md)

#### Returns

`void`

***

### toString()

> **toString**(`ptrName?`): `string`

Defined in: src/core/model/ArkSignature.ts:310

#### Parameters

##### ptrName?

`string`

#### Returns

`string`




============================================================
## FILE: `classes/ModelUtils.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ModelUtils

# Class: ModelUtils

Defined in: src/core/common/ModelUtils.ts:56

## Constructors

### Constructor

> **new ModelUtils**(): `ModelUtils`

#### Returns

`ModelUtils`

## Properties

### implicitArkUIBuilderMethods

> `static` **implicitArkUIBuilderMethods**: `Set`\<[`ArkMethod`](ArkMethod.md)\>

Defined in: src/core/common/ModelUtils.ts:57

## Methods

### findArkModel()

> `static` **findArkModel**(`baseName`, `arkClass`): `null` \| [`ArkField`](ArkField.md) \| `ArkExport`

Defined in: src/core/common/ModelUtils.ts:424

#### Parameters

##### baseName

`string`

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`ArkField`](ArkField.md) \| `ArkExport`

***

### findArkModelByRefName()

> `static` **findArkModelByRefName**(`refName`, `arkClass`): `null` \| [`ArkField`](ArkField.md) \| `ArkExport`

Defined in: src/core/common/ModelUtils.ts:454

#### Parameters

##### refName

`string`

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`ArkField`](ArkField.md) \| `ArkExport`

***

### findArkModelBySignature()

> `static` **findArkModelBySignature**(`signature`, `scene`): `null` \| [`ArkField`](ArkField.md) \| `ArkExport`

Defined in: src/core/common/ModelUtils.ts:481

#### Parameters

##### signature

[`Signature`](../type-aliases/Signature.md)

##### scene

[`Scene`](Scene.md)

#### Returns

`null` \| [`ArkField`](ArkField.md) \| `ArkExport`

***

### findDeclaredLocal()

> `static` **findDeclaredLocal**(`local`, `arkMethod`, `times`): `null` \| [`Local`](Local.md)

Defined in: src/core/common/ModelUtils.ts:377

#### Parameters

##### local

[`Local`](Local.md)

##### arkMethod

[`ArkMethod`](ArkMethod.md)

##### times

`number` = `0`

#### Returns

`null` \| [`Local`](Local.md)

***

### findGlobalRef()

> `static` **findGlobalRef**(`refName`, `method`): `null` \| `ArkExport`

Defined in: src/core/common/ModelUtils.ts:446

#### Parameters

##### refName

`string`

##### method

[`ArkMethod`](ArkMethod.md)

#### Returns

`null` \| `ArkExport`

***

### findPropertyInClass()

> `static` **findPropertyInClass**(`name`, `arkClass`): `null` \| [`ArkField`](ArkField.md) \| `ArkExport`

Defined in: src/core/common/ModelUtils.ts:356

#### Parameters

##### name

`string`

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`ArkField`](ArkField.md) \| `ArkExport`

***

### findPropertyInNamespace()

> `static` **findPropertyInNamespace**(`name`, `namespace`): `undefined` \| `ArkExport`

Defined in: src/core/common/ModelUtils.ts:345

#### Parameters

##### name

`string`

##### namespace

[`ArkNamespace`](ArkNamespace.md)

#### Returns

`undefined` \| `ArkExport`

***

### getAllClassesInFile()

> `static` **getAllClassesInFile**(`arkFile`): [`ArkClass`](ArkClass.md)[]

Defined in: src/core/common/ModelUtils.ts:276

#### Parameters

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

[`ArkClass`](ArkClass.md)[]

***

### getAllMethodsInFile()

> `static` **getAllMethodsInFile**(`arkFile`): [`ArkMethod`](ArkMethod.md)[]

Defined in: src/core/common/ModelUtils.ts:284

#### Parameters

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

[`ArkMethod`](ArkMethod.md)[]

***

### getAllNamespacesInFile()

> `static` **getAllNamespacesInFile**(`arkFile`): [`ArkNamespace`](ArkNamespace.md)[]

Defined in: src/core/common/ModelUtils.ts:260

#### Parameters

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

[`ArkNamespace`](ArkNamespace.md)[]

***

### getAllNamespacesInNamespace()

> `static` **getAllNamespacesInNamespace**(`arkNamespace`, `allNamespaces`): `void`

Defined in: src/core/common/ModelUtils.ts:269

#### Parameters

##### arkNamespace

[`ArkNamespace`](ArkNamespace.md)

##### allNamespaces

[`ArkNamespace`](ArkNamespace.md)[]

#### Returns

`void`

***

### getArkClassInBuild()

> `static` **getArkClassInBuild**(`scene`, `classType`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/core/common/ModelUtils.ts:304

#### Parameters

##### scene

[`Scene`](Scene.md)

##### classType

[`ClassType`](ClassType.md)

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

***

### getArkExportInImportInfoWithName()

> `static` **getArkExportInImportInfoWithName**(`name`, `arkFile`): `null` \| `ArkExport`

Defined in: src/core/common/ModelUtils.ts:142

search type within the given file import infos

#### Parameters

##### name

`string`

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

`null` \| `ArkExport`

***

### getClass()

> `static` **getClass**(`method`, `signature`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/core/common/ModelUtils.ts:318

#### Parameters

##### method

[`ArkMethod`](ArkMethod.md)

##### signature

[`ClassSignature`](ClassSignature.md)

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

***

### getClassInFileWithName()

> `static` **getClassInFileWithName**(`className`, `arkFile`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/core/common/ModelUtils.ts:125

search class within the given file

#### Parameters

##### className

`string`

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

***

### getClassInImportInfoWithName()

> `static` **getClassInImportInfoWithName**(`className`, `arkFile`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/core/common/ModelUtils.ts:133

#### Parameters

##### className

`string`

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

***

### getClassWithName()

> `static` **getClassWithName**(`className`, `thisClass`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/core/common/ModelUtils.ts:113

search class within the file that contain the given method

#### Parameters

##### className

`string`

##### thisClass

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

***

### getClassWithNameFromClass()

> `static` **getClassWithNameFromClass**(`className`, `startFrom`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/core/common/ModelUtils.ts:85

#### Parameters

##### className

`string`

##### startFrom

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

***

### getClassWithNameInNamespaceRecursively()

> `static` **getClassWithNameInNamespaceRecursively**(`className`, `ns`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/core/common/ModelUtils.ts:68

#### Parameters

##### className

`string`

##### ns

[`ArkNamespace`](ArkNamespace.md)

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

***

### getDefaultClass()

> `static` **getDefaultClass**(`arkClass`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/core/common/ModelUtils.ts:314

#### Parameters

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

***

### getLocalInImportInfoWithName()

> `static` **getLocalInImportInfoWithName**(`localName`, `arkFile`): `null` \| [`Local`](Local.md)

Defined in: src/core/common/ModelUtils.ts:251

#### Parameters

##### localName

`string`

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

`null` \| [`Local`](Local.md)

***

### getMethodSignatureFromArkClass()

> `static` **getMethodSignatureFromArkClass**(`arkClass`, `methodName`): `null` \| [`MethodSignature`](MethodSignature.md)

Defined in: src/core/common/ModelUtils.ts:59

#### Parameters

##### arkClass

[`ArkClass`](ArkClass.md)

##### methodName

`string`

#### Returns

`null` \| [`MethodSignature`](MethodSignature.md)

***

### getMethodWithName()

> `static` **getMethodWithName**(`methodName`, `startFrom`): `null` \| [`ArkMethod`](ArkMethod.md)

Defined in: src/core/common/ModelUtils.ts:147

search method within the file that contain the given method

#### Parameters

##### methodName

`string`

##### startFrom

[`ArkMethod`](ArkMethod.md)

#### Returns

`null` \| [`ArkMethod`](ArkMethod.md)

***

### getNamespaceInFileWithName()

> `static` **getNamespaceInFileWithName**(`namespaceName`, `arkFile`): `null` \| [`ArkNamespace`](ArkNamespace.md)

Defined in: src/core/common/ModelUtils.ts:201

#### Parameters

##### namespaceName

`string`

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

`null` \| [`ArkNamespace`](ArkNamespace.md)

***

### getNamespaceInImportInfoWithName()

> `static` **getNamespaceInImportInfoWithName**(`namespaceName`, `arkFile`): `null` \| [`ArkNamespace`](ArkNamespace.md)

Defined in: src/core/common/ModelUtils.ts:210

#### Parameters

##### namespaceName

`string`

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

`null` \| [`ArkNamespace`](ArkNamespace.md)

***

### getNamespaceWithName()

> `static` **getNamespaceWithName**(`namespaceName`, `thisClass`): `null` \| [`ArkNamespace`](ArkNamespace.md)

Defined in: src/core/common/ModelUtils.ts:188

#### Parameters

##### namespaceName

`string`

##### thisClass

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`ArkNamespace`](ArkNamespace.md)

***

### getNamespaceWithNameFromClass()

> `static` **getNamespaceWithNameFromClass**(`namespaceName`, `startFrom`): `null` \| [`ArkNamespace`](ArkNamespace.md)

Defined in: src/core/common/ModelUtils.ts:174

#### Parameters

##### namespaceName

`string`

##### startFrom

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`ArkNamespace`](ArkNamespace.md)

***

### getStaticMethodInFileWithName()

> `static` **getStaticMethodInFileWithName**(`methodName`, `arkFile`): `null` \| [`ArkMethod`](ArkMethod.md)

Defined in: src/core/common/ModelUtils.ts:232

#### Parameters

##### methodName

`string`

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

`null` \| [`ArkMethod`](ArkMethod.md)

***

### getStaticMethodInImportInfoWithName()

> `static` **getStaticMethodInImportInfoWithName**(`methodName`, `arkFile`): `null` \| [`ArkMethod`](ArkMethod.md)

Defined in: src/core/common/ModelUtils.ts:243

#### Parameters

##### methodName

`string`

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

`null` \| [`ArkMethod`](ArkMethod.md)

***

### getStaticMethodWithName()

> `static` **getStaticMethodWithName**(`methodName`, `thisClass`): `null` \| [`ArkMethod`](ArkMethod.md)

Defined in: src/core/common/ModelUtils.ts:218

#### Parameters

##### methodName

`string`

##### thisClass

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`ArkMethod`](ArkMethod.md)

***

### isArkUIBuilderMethod()

> `static` **isArkUIBuilderMethod**(`arkMethod`): `boolean`

Defined in: src/core/common/ModelUtils.ts:292

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

`boolean`

***

### parseArkBaseModel2Type()

> `static` **parseArkBaseModel2Type**(`arkBaseModel`): `null` \| [`Type`](Type.md)

Defined in: src/core/common/ModelUtils.ts:506

#### Parameters

##### arkBaseModel

`ArkBaseModel`

#### Returns

`null` \| [`Type`](Type.md)




============================================================
## FILE: `classes/ModulePath.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ModulePath

# Class: ModulePath

Defined in: src/utils/FileUtils.ts:97

## Constructors

### Constructor

> **new ModulePath**(`path`, `main`): `ModulePath`

Defined in: src/utils/FileUtils.ts:101

#### Parameters

##### path

`string`

##### main

`string`

#### Returns

`ModulePath`

## Properties

### main

> **main**: `string`

Defined in: src/utils/FileUtils.ts:99

***

### path

> **path**: `string`

Defined in: src/utils/FileUtils.ts:98




============================================================
## FILE: `classes/NamespaceSignature.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / NamespaceSignature

# Class: NamespaceSignature

Defined in: src/core/model/ArkSignature.ts:70

## Constructors

### Constructor

> **new NamespaceSignature**(`namespaceName`, `declaringFileSignature`, `declaringNamespaceSignature`): `NamespaceSignature`

Defined in: src/core/model/ArkSignature.ts:77

#### Parameters

##### namespaceName

`string`

##### declaringFileSignature

[`FileSignature`](FileSignature.md)

##### declaringNamespaceSignature

`null` | `NamespaceSignature`

#### Returns

`NamespaceSignature`

## Properties

### DEFAULT

> `readonly` `static` **DEFAULT**: `NamespaceSignature`

Defined in: src/core/model/ArkSignature.ts:75

## Methods

### getDeclaringFileSignature()

> **getDeclaringFileSignature**(): [`FileSignature`](FileSignature.md)

Defined in: src/core/model/ArkSignature.ts:87

#### Returns

[`FileSignature`](FileSignature.md)

***

### getDeclaringNamespaceSignature()

> **getDeclaringNamespaceSignature**(): `null` \| `NamespaceSignature`

Defined in: src/core/model/ArkSignature.ts:91

#### Returns

`null` \| `NamespaceSignature`

***

### getNamespaceName()

> **getNamespaceName**(): `string`

Defined in: src/core/model/ArkSignature.ts:83

#### Returns

`string`

***

### toMapKey()

> **toMapKey**(): `string`

Defined in: src/core/model/ArkSignature.ts:103

#### Returns

`string`

***

### toString()

> **toString**(): `string`

Defined in: src/core/model/ArkSignature.ts:95

#### Returns

`string`




============================================================
## FILE: `classes/NeverType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / NeverType

# Class: NeverType

Defined in: src/core/base/Type.ts:345

## Extends

- [`Type`](Type.md)

## Methods

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:356

#### Returns

`string`

#### Overrides

[`Type`](Type.md).[`getTypeString`](Type.md#gettypestring)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`Type`](Type.md).[`toString`](Type.md#tostring)

***

### getInstance()

> `static` **getInstance**(): `NeverType`

Defined in: src/core/base/Type.ts:348

#### Returns

`NeverType`




============================================================
## FILE: `classes/NullType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / NullType

# Class: NullType

Defined in: src/core/base/Type.ts:193

null type

## Extends

- [`PrimitiveType`](PrimitiveType.md)

## Methods

### getName()

> **getName**(): `string`

Defined in: src/core/base/Type.ts:128

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`getName`](PrimitiveType.md#getname)

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:132

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`getTypeString`](PrimitiveType.md#gettypestring)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`toString`](PrimitiveType.md#tostring)

***

### getInstance()

> `static` **getInstance**(): `NullType`

Defined in: src/core/base/Type.ts:196

#### Returns

`NullType`




============================================================
## FILE: `classes/NumberType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / NumberType

# Class: NumberType

Defined in: src/core/base/Type.ts:149

primitive type

## Extends

- [`PrimitiveType`](PrimitiveType.md)

## Methods

### getName()

> **getName**(): `string`

Defined in: src/core/base/Type.ts:128

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`getName`](PrimitiveType.md#getname)

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:132

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`getTypeString`](PrimitiveType.md#gettypestring)

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`

#### Inherited from

[`PrimitiveType`](PrimitiveType.md).[`toString`](PrimitiveType.md#tostring)

***

### getInstance()

> `static` **getInstance**(): `NumberType`

Defined in: src/core/base/Type.ts:156

#### Returns

`NumberType`




============================================================
## FILE: `classes/PAGStat.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PAGStat

# Class: PAGStat

Defined in: src/callgraph/common/Statistics.ts:173

## Extends

- `StatTraits`

## Constructors

### Constructor

> **new PAGStat**(): `PAGStat`

#### Returns

`PAGStat`

#### Inherited from

`StatTraits.constructor`

## Properties

### endTime

> **endTime**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:27

#### Inherited from

`StatTraits.endTime`

***

### numDynamicCall

> **numDynamicCall**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:174

***

### numTotalFunction

> **numTotalFunction**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:175

***

### numTotalNode

> **numTotalNode**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:176

***

### startTime

> **startTime**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:26

#### Inherited from

`StatTraits.startTime`

***

### TotalTime

> **TotalTime**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:25

#### Inherited from

`StatTraits.TotalTime`

## Methods

### getStat()

> **getStat**(): `string`

Defined in: src/callgraph/common/Statistics.ts:178

#### Returns

`string`

#### Overrides

`StatTraits.getStat`

***

### printStat()

> **printStat**(): `void`

Defined in: src/callgraph/common/Statistics.ts:187

#### Returns

`void`

#### Overrides

`StatTraits.printStat`




============================================================
## FILE: `classes/PTAStat.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PTAStat

# Class: PTAStat

Defined in: src/callgraph/common/Statistics.ts:38

## Extends

- `StatTraits`

## Constructors

### Constructor

> **new PTAStat**(`pta`): `PTAStat`

Defined in: src/callgraph/common/Statistics.ts:69

#### Parameters

##### pta

[`PointerAnalysis`](PointerAnalysis.md)

#### Returns

`PTAStat`

#### Overrides

`StatTraits.constructor`

## Properties

### endMemUsage

> **endMemUsage**: `any`

Defined in: src/callgraph/common/Statistics.ts:65

***

### endTime

> **endTime**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:27

#### Inherited from

`StatTraits.endTime`

***

### heapUsed

> **heapUsed**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:67

***

### iterTimes

> **iterTimes**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:62

***

### numInferedDiffTypeValue

> **numInferedDiffTypeValue**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:55

***

### numInferedUnknownValue

> **numInferedUnknownValue**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:53

***

### numNotInferedUnknownValue

> **numNotInferedUnknownValue**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:59

***

### numProcessedAddr

> **numProcessedAddr**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:40

***

### numProcessedCopy

> **numProcessedCopy**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:41

***

### numProcessedLoad

> **numProcessedLoad**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:42

***

### numProcessedThis

> **numProcessedThis**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:44

***

### numProcessedWrite

> **numProcessedWrite**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:43

***

### numRealLoad

> **numRealLoad**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:46

***

### numRealWrite

> **numRealWrite**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:45

***

### numTotalHandledValue

> **numTotalHandledValue**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:50

***

### numTotalValuesInHandedFun

> **numTotalValuesInHandedFun**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:49

***

### numUnhandledFun

> **numUnhandledFun**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:48

***

### numUnhandledFunc

> **numUnhandledFunc**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:60

***

### pta

> **pta**: [`PointerAnalysis`](PointerAnalysis.md)

Defined in: src/callgraph/common/Statistics.ts:39

***

### rssUsed

> **rssUsed**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:66

***

### startMemUsage

> **startMemUsage**: `any`

Defined in: src/callgraph/common/Statistics.ts:64

***

### startTime

> **startTime**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:26

#### Inherited from

`StatTraits.startTime`

***

### TotalTime

> **TotalTime**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:25

#### Inherited from

`StatTraits.TotalTime`

***

### totalValuesInVisitedFunc

> **totalValuesInVisitedFunc**: `number` = `0`

Defined in: src/callgraph/common/Statistics.ts:57

## Methods

### endStat()

> **endStat**(): `void`

Defined in: src/callgraph/common/Statistics.ts:79

#### Returns

`void`

***

### getNow()

> **getNow**(): `number`

Defined in: src/callgraph/common/Statistics.ts:89

#### Returns

`number`

***

### getStat()

> **getStat**(): `string`

Defined in: src/callgraph/common/Statistics.ts:147

#### Returns

`string`

#### Overrides

`StatTraits.getStat`

***

### printStat()

> **printStat**(): `void`

Defined in: src/callgraph/common/Statistics.ts:168

#### Returns

`void`

#### Overrides

`StatTraits.printStat`

***

### startStat()

> **startStat**(): `void`

Defined in: src/callgraph/common/Statistics.ts:74

#### Returns

`void`




============================================================
## FILE: `classes/Pag.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Pag

# Class: Pag

Defined in: src/callgraph/pointerAnalysis/Pag.ts:650

## Extends

- [`BaseExplicitGraph`](BaseExplicitGraph.md)

## Constructors

### Constructor

> **new Pag**(): `Pag`

Defined in: src/core/graph/BaseExplicitGraph.ts:142

#### Returns

`Pag`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`constructor`](BaseExplicitGraph.md#constructor)

## Properties

### edgeMarkSet

> `protected` **edgeMarkSet**: `Set`\<`string`\>

Defined in: src/core/graph/BaseExplicitGraph.ts:140

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`edgeMarkSet`](BaseExplicitGraph.md#edgemarkset)

***

### edgeNum

> `protected` **edgeNum**: `number` = `0`

Defined in: src/core/graph/BaseExplicitGraph.ts:137

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`edgeNum`](BaseExplicitGraph.md#edgenum)

***

### idToNodeMap

> `protected` **idToNodeMap**: `Map`\<`number`, [`BaseNode`](BaseNode.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:139

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`idToNodeMap`](BaseExplicitGraph.md#idtonodemap)

***

### nodeNum

> `protected` **nodeNum**: `number` = `0`

Defined in: src/core/graph/BaseExplicitGraph.ts:138

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`nodeNum`](BaseExplicitGraph.md#nodenum)

## Methods

### addNode()

> **addNode**(`n`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:155

#### Parameters

##### n

[`BaseNode`](BaseNode.md)

#### Returns

`void`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`addNode`](BaseExplicitGraph.md#addnode)

***

### addPagEdge()

> **addPagEdge**(`src`, `dst`, `kind`, `stmt?`): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:982

#### Parameters

##### src

[`PagNode`](PagNode.md)

##### dst

[`PagNode`](PagNode.md)

##### kind

[`PagEdgeKind`](../enumerations/PagEdgeKind.md)

##### stmt?

[`Stmt`](Stmt.md)

#### Returns

`boolean`

***

### addPagNode()

> **addPagNode**(`cid`, `value`, `stmt?`, `refresh?`): [`PagNode`](PagNode.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:764

#### Parameters

##### cid

`number`

##### value

[`Value`](../interfaces/Value.md)

##### stmt?

[`Stmt`](Stmt.md)

##### refresh?

`boolean` = `true`

#### Returns

[`PagNode`](PagNode.md)

***

### addPagThisLocalNode()

> **addPagThisLocalNode**(`ptNode`, `value`): [`PagNode`](PagNode.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:900

#### Parameters

##### ptNode

`number`

##### value

[`Local`](Local.md)

#### Returns

[`PagNode`](PagNode.md)

***

### addPagThisRefNode()

> **addPagThisRefNode**(`value`): [`PagNode`](PagNode.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:892

#### Parameters

##### value

[`ArkThisRef`](ArkThisRef.md)

#### Returns

[`PagNode`](PagNode.md)

***

### dump()

> **dump**(`name`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1034

#### Parameters

##### name

`string`

#### Returns

`void`

***

### getAddrEdges()

> **getAddrEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1022

#### Returns

`PagEdgeSet`

***

### getCG()

> **getCG**(): [`CallGraph`](CallGraph.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:662

#### Returns

[`CallGraph`](CallGraph.md)

***

### getGraphName()

> **getGraphName**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1030

#### Returns

`string`

#### Overrides

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`getGraphName`](BaseExplicitGraph.md#getgraphname)

***

### getNode()

> **getNode**(`id`): `undefined` \| [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:160

#### Parameters

##### id

`number`

#### Returns

`undefined` \| [`BaseNode`](BaseNode.md)

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`getNode`](BaseExplicitGraph.md#getnode)

***

### getNodeNum()

> **getNodeNum**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:147

#### Returns

`number`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`getNodeNum`](BaseExplicitGraph.md#getnodenum)

***

### getNodesByBaseValue()

> **getNodesByBaseValue**(`v`): `undefined` \| `Map`\<`number`, `number`[]\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:978

#### Parameters

##### v

[`Value`](../interfaces/Value.md)

#### Returns

`undefined` \| `Map`\<`number`, `number`[]\>

***

### getNodesByValue()

> **getNodesByValue**(`v`): `undefined` \| `Map`\<`number`, `number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:974

#### Parameters

##### v

[`Value`](../interfaces/Value.md)

#### Returns

`undefined` \| `Map`\<`number`, `number`\>

***

### getNodesIter()

> **getNodesIter**(): `IterableIterator`\<[`BaseNode`](BaseNode.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:200

#### Returns

`IterableIterator`\<[`BaseNode`](BaseNode.md)\>

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`getNodesIter`](BaseExplicitGraph.md#getnodesiter)

***

### getOrClonePagContainerFieldNode()

> **getOrClonePagContainerFieldNode**(`basePt`, `src?`, `base?`): `undefined` \| [`PagInstanceFieldNode`](PagInstanceFieldNode.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:712

#### Parameters

##### basePt

`number`

##### src?

[`PagArrayNode`](PagArrayNode.md)

##### base?

[`Local`](Local.md)

#### Returns

`undefined` \| [`PagInstanceFieldNode`](PagInstanceFieldNode.md)

***

### getOrClonePagFieldNode()

> **getOrClonePagFieldNode**(`src`, `basePt`): `undefined` \| [`PagInstanceFieldNode`](PagInstanceFieldNode.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:693

#### Parameters

##### src

[`PagInstanceFieldNode`](PagInstanceFieldNode.md)

##### basePt

`number`

#### Returns

`undefined` \| [`PagInstanceFieldNode`](PagInstanceFieldNode.md)

***

### getOrClonePagFuncNode()

> **getOrClonePagFuncNode**(`basePt`): `undefined` \| [`PagFuncNode`](PagFuncNode.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:753

#### Parameters

##### basePt

`number`

#### Returns

`undefined` \| [`PagFuncNode`](PagFuncNode.md)

***

### getOrClonePagNode()

> **getOrClonePagNode**(`src`, `basePt`): [`PagNode`](PagNode.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:670

#### Parameters

##### src

[`PagNode`](PagNode.md)

##### basePt

`number`

#### Returns

[`PagNode`](PagNode.md)

***

### getOrNewNode()

> **getOrNewNode**(`cid`, `v`, `s?`): [`PagNode`](PagNode.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:957

#### Parameters

##### cid

`number`

##### v

[`Value`](../interfaces/Value.md)

##### s?

[`Stmt`](Stmt.md)

#### Returns

[`PagNode`](PagNode.md)

***

### getOrNewThisLocalNode()

> **getOrNewThisLocalNode**(`cid`, `ptNode`, `value`, `s?`): [`PagNode`](PagNode.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:917

#### Parameters

##### cid

`number`

##### ptNode

`number`

##### value

[`Local`](Local.md)

##### s?

[`Stmt`](Stmt.md)

#### Returns

[`PagNode`](PagNode.md)

***

### getOrNewThisRefNode()

> **getOrNewThisRefNode**(`thisRefNodeID`, `value`): [`PagNode`](PagNode.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:908

#### Parameters

##### thisRefNodeID

`number`

##### value

[`ArkThisRef`](ArkThisRef.md)

#### Returns

[`PagNode`](PagNode.md)

***

### hasCtxNode()

> **hasCtxNode**(`cid`, `v`): `undefined` \| `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:930

#### Parameters

##### cid

`number`

##### v

[`Value`](../interfaces/Value.md)

#### Returns

`undefined` \| `number`

***

### hasCtxRetNode()

> **hasCtxRetNode**(`cid`, `v`): `undefined` \| `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:944

#### Parameters

##### cid

`number`

##### v

[`Value`](../interfaces/Value.md)

#### Returns

`undefined` \| `number`

***

### hasEdge()

> **hasEdge**(`src`, `dst`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:180

#### Parameters

##### src

[`BaseNode`](BaseNode.md)

##### dst

[`BaseNode`](BaseNode.md)

#### Returns

`boolean`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`hasEdge`](BaseExplicitGraph.md#hasedge)

***

### hasExportNode()

> **hasExportNode**(`v`): `undefined` \| `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:925

#### Parameters

##### v

[`ExportInfo`](ExportInfo.md)

#### Returns

`undefined` \| `number`

***

### hasNode()

> **hasNode**(`id`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:168

#### Parameters

##### id

`number`

#### Returns

`boolean`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`hasNode`](BaseExplicitGraph.md#hasnode)

***

### ifEdgeExisting()

> **ifEdgeExisting**(`edge`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:190

#### Parameters

##### edge

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`ifEdgeExisting`](BaseExplicitGraph.md#ifedgeexisting)

***

### nodesItor()

> **nodesItor**(): `IterableIterator`\<[`BaseNode`](BaseNode.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:151

#### Returns

`IterableIterator`\<[`BaseNode`](BaseNode.md)\>

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`nodesItor`](BaseExplicitGraph.md#nodesitor)

***

### removeNode()

> **removeNode**(`id`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:172

#### Parameters

##### id

`number`

#### Returns

`boolean`

#### Inherited from

[`BaseExplicitGraph`](BaseExplicitGraph.md).[`removeNode`](BaseExplicitGraph.md#removenode)

***

### resetAddrEdges()

> **resetAddrEdges**(): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1026

#### Returns

`void`




============================================================
## FILE: `classes/PagArrayNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagArrayNode

# Class: PagArrayNode

Defined in: src/callgraph/pointerAnalysis/Pag.ts:478

## Extends

- [`PagNode`](PagNode.md)

## Constructors

### Constructor

> **new PagArrayNode**(`id`, `cid`, `expr`, `stmt?`): `PagArrayNode`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:481

#### Parameters

##### id

`number`

##### cid

`undefined` | `number`

##### expr

[`ArkArrayRef`](ArkArrayRef.md)

##### stmt?

[`Stmt`](Stmt.md)

#### Returns

`PagArrayNode`

#### Overrides

[`PagNode`](PagNode.md).[`constructor`](PagNode.md#constructor)

## Properties

### base

> **base**: [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:479

***

### basePt

> `protected` **basePt**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:161

#### Inherited from

[`PagNode`](PagNode.md).[`basePt`](PagNode.md#basept)

***

### clonedFrom

> `protected` **clonedFrom**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:162

#### Inherited from

[`PagNode`](PagNode.md).[`clonedFrom`](PagNode.md#clonedfrom)

***

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:68

#### Inherited from

[`PagNode`](PagNode.md).[`kind`](PagNode.md#kind)

## Methods

### addAddressInEdge()

> **addAddressInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:232

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressInEdge`](PagNode.md#addaddressinedge)

***

### addAddressOutEdge()

> **addAddressOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:238

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressOutEdge`](PagNode.md#addaddressoutedge)

***

### addCopyInEdge()

> **addCopyInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:244

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyInEdge`](PagNode.md#addcopyinedge)

***

### addCopyOutEdge()

> **addCopyOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:250

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyOutEdge`](PagNode.md#addcopyoutedge)

***

### addIncomingEdge()

> **addIncomingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:105

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addIncomingEdge`](PagNode.md#addincomingedge)

***

### addLoadInEdge()

> **addLoadInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:257

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadInEdge`](PagNode.md#addloadinedge)

***

### addLoadOutEdge()

> **addLoadOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:263

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadOutEdge`](PagNode.md#addloadoutedge)

***

### addOutgoingEdge()

> **addOutgoingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:109

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addOutgoingEdge`](PagNode.md#addoutgoingedge)

***

### addPointToElement()

> **addPointToElement**(`node`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:301

#### Parameters

##### node

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addPointToElement`](PagNode.md#addpointtoelement)

***

### addThisInEdge()

> **addThisInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:281

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisInEdge`](PagNode.md#addthisinedge)

***

### addThisOutEdge()

> **addThisOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:287

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisOutEdge`](PagNode.md#addthisoutedge)

***

### addWriteInEdge()

> **addWriteInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:269

#### Parameters

##### e

[`WritePagEdge`](WritePagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteInEdge`](PagNode.md#addwriteinedge)

***

### addWriteOutEdge()

> **addWriteOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:275

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteOutEdge`](PagNode.md#addwriteoutedge)

***

### getBasePt()

> **getBasePt**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:173

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getBasePt`](PagNode.md#getbasept)

***

### getCid()

> **getCid**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:181

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getCid`](PagNode.md#getcid)

***

### getClonedFrom()

> **getClonedFrom**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:323

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getClonedFrom`](PagNode.md#getclonedfrom)

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:331

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotAttr`](PagNode.md#getdotattr)

***

### getDotLabel()

> **getDotLabel**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:352

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotLabel`](PagNode.md#getdotlabel)

***

### getID()

> **getID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:77

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getID`](PagNode.md#getid)

***

### getIncomingCopyEdges()

> **getIncomingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:208

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingCopyEdges`](PagNode.md#getincomingcopyedges)

***

### getIncomingEdge()

> **getIncomingEdge**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:121

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingEdge`](PagNode.md#getincomingedge)

***

### getIncomingThisEdges()

> **getIncomingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:228

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingThisEdges`](PagNode.md#getincomingthisedges)

***

### getIncomingWriteEdges()

> **getIncomingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:220

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingWriteEdges`](PagNode.md#getincomingwriteedges)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:81

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getKind`](PagNode.md#getkind)

***

### getOutEdges()

> **getOutEdges**(): `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:309

#### Returns

`object`

##### AddressEdge

> **AddressEdge**: `PagEdgeSet`

##### CopyEdge

> **CopyEdge**: `PagEdgeSet`

##### LoadEdge

> **LoadEdge**: `PagEdgeSet`

##### WriteEdge

> **WriteEdge**: `PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutEdges`](PagNode.md#getoutedges)

***

### getOutgoingCopyEdges()

> **getOutgoingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:204

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingCopyEdges`](PagNode.md#getoutgoingcopyedges)

***

### getOutgoingEdges()

> **getOutgoingEdges**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:125

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingEdges`](PagNode.md#getoutgoingedges)

***

### getOutgoingLoadEdges()

> **getOutgoingLoadEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:212

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingLoadEdges`](PagNode.md#getoutgoingloadedges)

***

### getOutgoingThisEdges()

> **getOutgoingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:224

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingThisEdges`](PagNode.md#getoutgoingthisedges)

***

### getOutgoingWriteEdges()

> **getOutgoingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:216

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingWriteEdges`](PagNode.md#getoutgoingwriteedges)

***

### getPointTo()

> **getPointTo**(): `IPtsCollection`\<`number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:297

#### Returns

`IPtsCollection`\<`number`\>

#### Inherited from

[`PagNode`](PagNode.md).[`getPointTo`](PagNode.md#getpointto)

***

### getStmt()

> **getStmt**(): `undefined` \| [`Stmt`](Stmt.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:196

#### Returns

`undefined` \| [`Stmt`](Stmt.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getStmt`](PagNode.md#getstmt)

***

### getValue()

> **getValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:293

#### Returns

[`Value`](../interfaces/Value.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getValue`](PagNode.md#getvalue)

***

### hasIncomingEdge()

> **hasIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:97

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdge`](PagNode.md#hasincomingedge)

***

### hasIncomingEdges()

> **hasIncomingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:89

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdges`](PagNode.md#hasincomingedges)

***

### hasOutgoingCopyEdge()

> **hasOutgoingCopyEdge**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:200

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingCopyEdge`](PagNode.md#hasoutgoingcopyedge)

***

### hasOutgoingEdge()

> **hasOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:101

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdge`](PagNode.md#hasoutgoingedge)

***

### hasOutgoingEdges()

> **hasOutgoingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:93

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdges`](PagNode.md#hasoutgoingedges)

***

### removeIncomingEdge()

> **removeIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:113

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeIncomingEdge`](PagNode.md#removeincomingedge)

***

### removeOutgoingEdge()

> **removeOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:117

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeOutgoingEdge`](PagNode.md#removeoutgoingedge)

***

### setBasePt()

> **setBasePt**(`pt`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:177

#### Parameters

##### pt

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setBasePt`](PagNode.md#setbasept)

***

### setCid()

> **setCid**(`cid`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:188

#### Parameters

##### cid

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setCid`](PagNode.md#setcid)

***

### setClonedFrom()

> **setClonedFrom**(`id`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:327

#### Parameters

##### id

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setClonedFrom`](PagNode.md#setclonedfrom)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:85

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setKind`](PagNode.md#setkind)

***

### setPointTo()

> **setPointTo**(`pts`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:305

#### Parameters

##### pts

`IPtsCollection`\<`number`\>

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setPointTo`](PagNode.md#setpointto)

***

### setStmt()

> **setStmt**(`s`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:192

#### Parameters

##### s

[`Stmt`](Stmt.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setStmt`](PagNode.md#setstmt)




============================================================
## FILE: `classes/PagBuilder.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagBuilder

# Class: PagBuilder

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:74

## Constructors

### Constructor

> **new PagBuilder**(`p`, `cg`, `s`, `kLimit`, `scale`): `PagBuilder`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:104

#### Parameters

##### p

[`Pag`](Pag.md)

##### cg

[`CallGraph`](CallGraph.md)

##### s

[`Scene`](Scene.md)

##### kLimit

`number`

##### scale

`PtaAnalysisScale`

#### Returns

`PagBuilder`

## Methods

### addCallReturnPagEdge()

> **addCallReturnPagEdge**(`calleeMethod`, `callStmt`, `callerCid`, `calleeCid`): `number`[]

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1073

process the return value PAG edge for invoke stmt

#### Parameters

##### calleeMethod

[`ArkMethod`](ArkMethod.md)

##### callStmt

[`Stmt`](Stmt.md)

##### callerCid

`number`

##### calleeCid

`number`

#### Returns

`number`[]

***

### addCallsEdgesFromFuncPag()

> **addCallsEdgesFromFuncPag**(`funcPag`, `cid`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:385

#### Parameters

##### funcPag

[`FuncPag`](FuncPag.md)

##### cid

`number`

#### Returns

`boolean`

***

### addDynamicCallEdge()

> **addDynamicCallEdge**(`cs`, `baseClassPTNode`, `cid`): `number`[]

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:498

#### Parameters

##### cs

[`ICallSite`](../interfaces/ICallSite.md)

##### baseClassPTNode

`number`

##### cid

`number`

#### Returns

`number`[]

***

### addDynamicCallSite()

> **addDynamicCallSite**(`funcPag`, `funcID`, `cid`): `void`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:419

#### Parameters

##### funcPag

[`FuncPag`](FuncPag.md)

##### funcID

`number`

##### cid

`number`

#### Returns

`void`

***

### addEdgesFromFuncPag()

> **addEdgesFromFuncPag**(`funcPag`, `cid`, `funcID`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:348

#### Parameters

##### funcPag

[`FuncPag`](FuncPag.md)

##### cid

`number`

##### funcID

`number`

#### Returns

`boolean`

***

### addEdgesFromInterFuncPag()

> **addEdgesFromInterFuncPag**(`interFuncPag`, `cid`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1940

#### Parameters

##### interFuncPag

[`InterFuncPag`](InterFuncPag.md)

##### cid

`number`

#### Returns

`boolean`

***

### addPropertyLinkEdge()

> **addPropertyLinkEdge**(`propertyNode`, `storageObj`, `cid`, `stmt`, `edgeKind`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1332

add PagEdge

#### Parameters

##### propertyNode

[`PagNode`](PagNode.md)

##### storageObj

[`Value`](../interfaces/Value.md)

##### cid

`number`

##### stmt

[`Stmt`](Stmt.md)

##### edgeKind

`number`

#### Returns

`boolean`

***

### addStaticPagCallEdge()

> **addStaticPagCallEdge**(`cs`, `callerCid`, `calleeCid?`, `ptNode?`): `number`[]

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:945

#### Parameters

##### cs

[`CallSite`](CallSite.md)

##### callerCid

`number`

##### calleeCid?

`number`

##### ptNode?

[`PagNode`](PagNode.md)

#### Returns

`number`[]

***

### addStaticPagCallReturnEdge()

> **addStaticPagCallReturnEdge**(`cs`, `callerCid`, `calleeCid`): `number`[]

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1101

#### Parameters

##### cs

[`CallSite`](CallSite.md)

##### callerCid

`number`

##### calleeCid

`number`

#### Returns

`number`[]

***

### addToDynamicCallSite()

> **addToDynamicCallSite**(`funcPag`, `cs`): `void`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1744

#### Parameters

##### funcPag

[`FuncPag`](FuncPag.md)

##### cs

[`DynCallSite`](DynCallSite.md)

#### Returns

`void`

***

### addUnknownCallSite()

> **addUnknownCallSite**(`funcPag`, `funcID`): `void`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:466

#### Parameters

##### funcPag

[`FuncPag`](FuncPag.md)

##### funcID

`number`

#### Returns

`void`

***

### addUpdatedNode()

> **addUpdatedNode**(`nodeID`, `diffPT`): `void`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1968

#### Parameters

##### nodeID

`number`

##### diffPT

`IPtsCollection`\<`number`\>

#### Returns

`void`

***

### build()

> **build**(): `void`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:164

#### Returns

`void`

***

### buildForEntries()

> **buildForEntries**(`funcIDs`): `void`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:136

#### Parameters

##### funcIDs

`number`[]

#### Returns

`void`

***

### buildFuncPag()

> **buildFuncPag**(`funcID`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:174

#### Parameters

##### funcID

`number`

#### Returns

`boolean`

***

### buildPagFromFuncPag()

> **buildPagFromFuncPag**(`funcID`, `cid`): `void`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:326

#### Parameters

##### funcID

`number`

##### cid

`number`

#### Returns

`void`

***

### doStat()

> **doStat**(): `void`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1780

#### Returns

`void`

***

### getExportVariableMap()

> **getExportVariableMap**(`src`): [`Local`](Local.md)[]

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1935

#### Parameters

##### src

[`Local`](Local.md)

#### Returns

[`Local`](Local.md)[]

***

### getGlobalThisValue()

> **getGlobalThisValue**(): [`Local`](Local.md)

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1496

#### Returns

[`Local`](Local.md)

***

### getHandledFuncs()

> **getHandledFuncs**(): `number`[]

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1800

#### Returns

`number`[]

***

### getOrNewGlobalThisNode()

> **getOrNewGlobalThisNode**(`cid`): [`PagNode`](PagNode.md)

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1278

#### Parameters

##### cid

`number`

#### Returns

[`PagNode`](PagNode.md)

***

### getOrNewPagNode()

> **getOrNewPagNode**(`cid`, `v`, `s?`): [`PagNode`](PagNode.md)

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1226

#### Parameters

##### cid

`number`

##### v

[`Value`](../interfaces/Value.md)

##### s?

[`Stmt`](Stmt.md)

#### Returns

[`PagNode`](PagNode.md)

***

### getOrNewPropertyNode()

> **getOrNewPropertyNode**(`storage`, `propertyName`, `stmt`): [`PagNode`](PagNode.md)

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1292

search the storage map to get propertyNode with given storage and propertyFieldName

#### Parameters

##### storage

[`StorageType`](../enumerations/StorageType.md)

storage type: AppStorage, LocalStorage etc.

##### propertyName

`string`

string property key

##### stmt

[`Stmt`](Stmt.md)

#### Returns

[`PagNode`](PagNode.md)

propertyNode: PagLocalNode

***

### getOrNewThisLoalNode()

> **getOrNewThisLoalNode**(`cid`, `v`, `s?`): [`PagNode`](PagNode.md)

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1267

#### Parameters

##### cid

`number`

##### v

[`Local`](Local.md)

##### s?

[`Stmt`](Stmt.md)

#### Returns

[`PagNode`](PagNode.md)

***

### getOrNewThisRefNode()

> **getOrNewThisRefNode**(`cid`, `v`): [`PagNode`](PagNode.md)

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1255

return ThisRef PAG node according to cid, a cid has a unique ThisRef node

#### Parameters

##### cid

`number`

##### v

[`ArkThisRef`](ArkThisRef.md)

#### Returns

[`PagNode`](PagNode.md)

***

### getPropertyNode()

> **getPropertyNode**(`storage`, `propertyName`, `stmt`): `undefined` \| [`PagNode`](PagNode.md)

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1307

#### Parameters

##### storage

[`StorageType`](../enumerations/StorageType.md)

##### propertyName

`string`

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`undefined` \| [`PagNode`](PagNode.md)

***

### getRealInstanceRef()

> **getRealInstanceRef**(`v`): [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1361

#### Parameters

##### v

[`Value`](../interfaces/Value.md)

#### Returns

[`Value`](../interfaces/Value.md)

***

### getRealThisLocal()

> **getRealThisLocal**(`input`, `funcId`): [`Local`](Local.md)

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1759

#### Parameters

##### input

[`Local`](Local.md)

##### funcId

`number`

#### Returns

[`Local`](Local.md)

***

### getRetriggerNodes()

> **getRetriggerNodes**(): `number`[]

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1962

#### Returns

`number`[]

***

### getStat()

> **getStat**(): `string`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1788

#### Returns

`string`

***

### getUnhandledFuncs()

> **getUnhandledFuncs**(): `number`[]

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1792

#### Returns

`number`[]

***

### getUniqThisLocalNode()

> **getUniqThisLocalNode**(`cid`): `undefined` \| `number`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1282

#### Parameters

##### cid

`number`

#### Returns

`undefined` \| `number`

***

### getUpdatedNodes()

> **getUpdatedNodes**(): `Map`\<`number`, `IPtsCollection`\<`number`\>\>

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1975

#### Returns

`Map`\<`number`, `IPtsCollection`\<`number`\>\>

***

### handleReachable()

> **handleReachable**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:149

#### Returns

`boolean`

***

### handleUnkownDynamicCall()

> **handleUnkownDynamicCall**(`cs`, `cid`): `number`[]

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:795

#### Parameters

##### cs

[`DynCallSite`](DynCallSite.md)

##### cid

`number`

#### Returns

`number`[]

***

### handleUnprocessedCallSites()

> **handleUnprocessedCallSites**(`processedCallSites`): `number`[]

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:849

#### Parameters

##### processedCallSites

`Set`\<[`DynCallSite`](DynCallSite.md)\>

#### Returns

`number`[]

***

### isSingletonFunction()

> **isSingletonFunction**(`funcID`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1399

check if a method is singleton function
rule: static method, assign heap obj to global var or static field, return the receiver

#### Parameters

##### funcID

`number`

#### Returns

`boolean`

***

### printStat()

> **printStat**(): `void`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1784

#### Returns

`void`

***

### processBuiltInMethodPagCallEdge()

> **processBuiltInMethodPagCallEdge**(`staticCS`, `cid`, `calleeCid`, `baseClassPTNode`): `number`[]

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:641

include container API, Function API

#### Parameters

##### staticCS

[`CallSite`](CallSite.md)

##### cid

`number`

##### calleeCid

`number`

##### baseClassPTNode

`number`

#### Returns

`number`[]

***

### processNormalMethodPagCallEdge()

> **processNormalMethodPagCallEdge**(`staticCS`, `cid`, `calleeCid`, `baseClassPTNode`): `number`[]

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:605

#### Parameters

##### staticCS

[`CallSite`](CallSite.md)

##### cid

`number`

##### calleeCid

`number`

##### baseClassPTNode

`number`

#### Returns

`number`[]

***

### resetUpdatedNodes()

> **resetUpdatedNodes**(): `void`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1979

#### Returns

`void`

***

### setPtForNode()

> **setPtForNode**(`node`, `pts`): `void`

Defined in: src/callgraph/pointerAnalysis/PagBuilder.ts:1751

#### Parameters

##### node

`number`

##### pts

`undefined` | `IPtsCollection`\<`number`\>

#### Returns

`void`




============================================================
## FILE: `classes/PagEdge.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagEdge

# Class: PagEdge

Defined in: src/callgraph/pointerAnalysis/Pag.ts:67

## Extends

- [`BaseEdge`](BaseEdge.md)

## Extended by

- [`AddrPagEdge`](AddrPagEdge.md)
- [`CopyPagEdge`](CopyPagEdge.md)
- [`LoadPagEdge`](LoadPagEdge.md)
- [`WritePagEdge`](WritePagEdge.md)
- [`ThisPagEdge`](ThisPagEdge.md)

## Constructors

### Constructor

> **new PagEdge**(`n`, `d`, `k`, `s?`): `PagEdge`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:70

#### Parameters

##### n

[`PagNode`](PagNode.md)

##### d

[`PagNode`](PagNode.md)

##### k

[`PagEdgeKind`](../enumerations/PagEdgeKind.md)

##### s?

[`Stmt`](Stmt.md)

#### Returns

`PagEdge`

#### Overrides

[`BaseEdge`](BaseEdge.md).[`constructor`](BaseEdge.md#constructor)

## Properties

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:22

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`kind`](BaseEdge.md#kind)

## Methods

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:75

#### Returns

`string`

#### Overrides

[`BaseEdge`](BaseEdge.md).[`getDotAttr`](BaseEdge.md#getdotattr)

***

### getDstID()

> **getDstID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:34

#### Returns

`number`

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`getDstID`](BaseEdge.md#getdstid)

***

### getDstNode()

> **getDstNode**(): [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:42

#### Returns

[`BaseNode`](BaseNode.md)

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`getDstNode`](BaseEdge.md#getdstnode)

***

### getEndPoints()

> **getEndPoints**(): `object`

Defined in: src/core/graph/BaseExplicitGraph.ts:54

#### Returns

`object`

##### dst

> **dst**: `number`

##### src

> **src**: `number`

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`getEndPoints`](BaseEdge.md#getendpoints)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:46

#### Returns

`number`

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`getKind`](BaseEdge.md#getkind)

***

### getSrcID()

> **getSrcID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:30

#### Returns

`number`

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`getSrcID`](BaseEdge.md#getsrcid)

***

### getSrcNode()

> **getSrcNode**(): [`BaseNode`](BaseNode.md)

Defined in: src/core/graph/BaseExplicitGraph.ts:38

#### Returns

[`BaseNode`](BaseNode.md)

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`getSrcNode`](BaseEdge.md#getsrcnode)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:50

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`BaseEdge`](BaseEdge.md).[`setKind`](BaseEdge.md#setkind)




============================================================
## FILE: `classes/PagFuncNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagFuncNode

# Class: PagFuncNode

Defined in: src/callgraph/pointerAnalysis/Pag.ts:554

## Extends

- [`PagNode`](PagNode.md)

## Constructors

### Constructor

> **new PagFuncNode**(`id`, `cid`, `r`, `stmt?`, `method?`, `thisInstanceID?`): `PagFuncNode`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:564

#### Parameters

##### id

`number`

##### cid

`undefined` | `number`

##### r

[`Value`](../interfaces/Value.md)

##### stmt?

[`Stmt`](Stmt.md)

##### method?

[`MethodSignature`](MethodSignature.md)

##### thisInstanceID?

`number`

#### Returns

`PagFuncNode`

#### Overrides

[`PagNode`](PagNode.md).[`constructor`](PagNode.md#constructor)

## Properties

### basePt

> `protected` **basePt**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:161

#### Inherited from

[`PagNode`](PagNode.md).[`basePt`](PagNode.md#basept)

***

### clonedFrom

> `protected` **clonedFrom**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:162

#### Inherited from

[`PagNode`](PagNode.md).[`clonedFrom`](PagNode.md#clonedfrom)

***

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:68

#### Inherited from

[`PagNode`](PagNode.md).[`kind`](PagNode.md#kind)

## Methods

### addAddressInEdge()

> **addAddressInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:232

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressInEdge`](PagNode.md#addaddressinedge)

***

### addAddressOutEdge()

> **addAddressOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:238

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressOutEdge`](PagNode.md#addaddressoutedge)

***

### addCopyInEdge()

> **addCopyInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:244

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyInEdge`](PagNode.md#addcopyinedge)

***

### addCopyOutEdge()

> **addCopyOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:250

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyOutEdge`](PagNode.md#addcopyoutedge)

***

### addIncomingEdge()

> **addIncomingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:105

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addIncomingEdge`](PagNode.md#addincomingedge)

***

### addLoadInEdge()

> **addLoadInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:257

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadInEdge`](PagNode.md#addloadinedge)

***

### addLoadOutEdge()

> **addLoadOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:263

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadOutEdge`](PagNode.md#addloadoutedge)

***

### addOutgoingEdge()

> **addOutgoingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:109

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addOutgoingEdge`](PagNode.md#addoutgoingedge)

***

### addPointToElement()

> **addPointToElement**(`node`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:301

#### Parameters

##### node

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addPointToElement`](PagNode.md#addpointtoelement)

***

### addThisInEdge()

> **addThisInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:281

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisInEdge`](PagNode.md#addthisinedge)

***

### addThisOutEdge()

> **addThisOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:287

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisOutEdge`](PagNode.md#addthisoutedge)

***

### addWriteInEdge()

> **addWriteInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:269

#### Parameters

##### e

[`WritePagEdge`](WritePagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteInEdge`](PagNode.md#addwriteinedge)

***

### addWriteOutEdge()

> **addWriteOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:275

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteOutEdge`](PagNode.md#addwriteoutedge)

***

### getArgsOffset()

> **getArgsOffset**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:605

#### Returns

`number`

***

### getBasePt()

> **getBasePt**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:173

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getBasePt`](PagNode.md#getbasept)

***

### getCid()

> **getCid**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:181

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getCid`](PagNode.md#getcid)

***

### getClonedFrom()

> **getClonedFrom**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:323

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getClonedFrom`](PagNode.md#getclonedfrom)

***

### getCS()

> **getCS**(): [`CallSite`](CallSite.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:597

#### Returns

[`CallSite`](CallSite.md)

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:331

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotAttr`](PagNode.md#getdotattr)

***

### getDotLabel()

> **getDotLabel**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:352

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotLabel`](PagNode.md#getdotlabel)

***

### getID()

> **getID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:77

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getID`](PagNode.md#getid)

***

### getIncomingCopyEdges()

> **getIncomingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:208

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingCopyEdges`](PagNode.md#getincomingcopyedges)

***

### getIncomingEdge()

> **getIncomingEdge**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:121

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingEdge`](PagNode.md#getincomingedge)

***

### getIncomingThisEdges()

> **getIncomingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:228

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingThisEdges`](PagNode.md#getincomingthisedges)

***

### getIncomingWriteEdges()

> **getIncomingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:220

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingWriteEdges`](PagNode.md#getincomingwriteedges)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:81

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getKind`](PagNode.md#getkind)

***

### getMethod()

> **getMethod**(): [`MethodSignature`](MethodSignature.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:581

#### Returns

[`MethodSignature`](MethodSignature.md)

***

### getMethodType()

> **getMethodType**(): `BuiltApiType`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:609

#### Returns

`BuiltApiType`

***

### getOriginCid()

> **getOriginCid**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:617

#### Returns

`number`

***

### getOutEdges()

> **getOutEdges**(): `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:309

#### Returns

`object`

##### AddressEdge

> **AddressEdge**: `PagEdgeSet`

##### CopyEdge

> **CopyEdge**: `PagEdgeSet`

##### LoadEdge

> **LoadEdge**: `PagEdgeSet`

##### WriteEdge

> **WriteEdge**: `PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutEdges`](PagNode.md#getoutedges)

***

### getOutgoingCopyEdges()

> **getOutgoingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:204

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingCopyEdges`](PagNode.md#getoutgoingcopyedges)

***

### getOutgoingEdges()

> **getOutgoingEdges**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:125

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingEdges`](PagNode.md#getoutgoingedges)

***

### getOutgoingLoadEdges()

> **getOutgoingLoadEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:212

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingLoadEdges`](PagNode.md#getoutgoingloadedges)

***

### getOutgoingThisEdges()

> **getOutgoingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:224

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingThisEdges`](PagNode.md#getoutgoingthisedges)

***

### getOutgoingWriteEdges()

> **getOutgoingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:216

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingWriteEdges`](PagNode.md#getoutgoingwriteedges)

***

### getPointTo()

> **getPointTo**(): `IPtsCollection`\<`number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:297

#### Returns

`IPtsCollection`\<`number`\>

#### Inherited from

[`PagNode`](PagNode.md).[`getPointTo`](PagNode.md#getpointto)

***

### getStmt()

> **getStmt**(): `undefined` \| [`Stmt`](Stmt.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:196

#### Returns

`undefined` \| [`Stmt`](Stmt.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getStmt`](PagNode.md#getstmt)

***

### getThisPt()

> **getThisPt**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:589

#### Returns

`number`

***

### getValue()

> **getValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:293

#### Returns

[`Value`](../interfaces/Value.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getValue`](PagNode.md#getvalue)

***

### hasIncomingEdge()

> **hasIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:97

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdge`](PagNode.md#hasincomingedge)

***

### hasIncomingEdges()

> **hasIncomingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:89

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdges`](PagNode.md#hasincomingedges)

***

### hasOutgoingCopyEdge()

> **hasOutgoingCopyEdge**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:200

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingCopyEdge`](PagNode.md#hasoutgoingcopyedge)

***

### hasOutgoingEdge()

> **hasOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:101

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdge`](PagNode.md#hasoutgoingedge)

***

### hasOutgoingEdges()

> **hasOutgoingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:93

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdges`](PagNode.md#hasoutgoingedges)

***

### removeIncomingEdge()

> **removeIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:113

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeIncomingEdge`](PagNode.md#removeincomingedge)

***

### removeOutgoingEdge()

> **removeOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:117

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeOutgoingEdge`](PagNode.md#removeoutgoingedge)

***

### setArgsOffset()

> **setArgsOffset**(`offset`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:601

#### Parameters

##### offset

`number`

#### Returns

`void`

***

### setBasePt()

> **setBasePt**(`pt`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:177

#### Parameters

##### pt

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setBasePt`](PagNode.md#setbasept)

***

### setCid()

> **setCid**(`cid`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:188

#### Parameters

##### cid

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setCid`](PagNode.md#setcid)

***

### setClonedFrom()

> **setClonedFrom**(`id`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:327

#### Parameters

##### id

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setClonedFrom`](PagNode.md#setclonedfrom)

***

### setCS()

> **setCS**(`callsite`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:593

#### Parameters

##### callsite

[`CallSite`](CallSite.md)

#### Returns

`void`

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:85

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setKind`](PagNode.md#setkind)

***

### setMethod()

> **setMethod**(`method`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:576

#### Parameters

##### method

[`MethodSignature`](MethodSignature.md)

#### Returns

`void`

***

### setOriginCid()

> **setOriginCid**(`cid`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:613

#### Parameters

##### cid

`number`

#### Returns

`void`

***

### setPointTo()

> **setPointTo**(`pts`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:305

#### Parameters

##### pts

`IPtsCollection`\<`number`\>

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setPointTo`](PagNode.md#setpointto)

***

### setStmt()

> **setStmt**(`s`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:192

#### Parameters

##### s

[`Stmt`](Stmt.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setStmt`](PagNode.md#setstmt)

***

### setThisPt()

> **setThisPt**(`thisPt`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:585

#### Parameters

##### thisPt

`number`

#### Returns

`void`




============================================================
## FILE: `classes/PagGlobalThisNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagGlobalThisNode

# Class: PagGlobalThisNode

Defined in: src/callgraph/pointerAnalysis/Pag.ts:625

almost same as PagNewExprNode, used only for globalThis and its field reference

## Extends

- [`PagNode`](PagNode.md)

## Constructors

### Constructor

> **new PagGlobalThisNode**(`id`, `cid`, `r`, `stmt?`): `PagGlobalThisNode`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:628

#### Parameters

##### id

`number`

##### cid

`undefined` | `number`

##### r

[`Value`](../interfaces/Value.md)

##### stmt?

[`Stmt`](Stmt.md)

#### Returns

`PagGlobalThisNode`

#### Overrides

[`PagNode`](PagNode.md).[`constructor`](PagNode.md#constructor)

## Properties

### basePt

> `protected` **basePt**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:161

#### Inherited from

[`PagNode`](PagNode.md).[`basePt`](PagNode.md#basept)

***

### clonedFrom

> `protected` **clonedFrom**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:162

#### Inherited from

[`PagNode`](PagNode.md).[`clonedFrom`](PagNode.md#clonedfrom)

***

### fieldNodes

> **fieldNodes**: `Map`\<`string`, `number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:626

***

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:68

#### Inherited from

[`PagNode`](PagNode.md).[`kind`](PagNode.md#kind)

## Methods

### addAddressInEdge()

> **addAddressInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:232

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressInEdge`](PagNode.md#addaddressinedge)

***

### addAddressOutEdge()

> **addAddressOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:238

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressOutEdge`](PagNode.md#addaddressoutedge)

***

### addCopyInEdge()

> **addCopyInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:244

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyInEdge`](PagNode.md#addcopyinedge)

***

### addCopyOutEdge()

> **addCopyOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:250

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyOutEdge`](PagNode.md#addcopyoutedge)

***

### addFieldNode()

> **addFieldNode**(`fieldSignature`, `nodeID`): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:633

#### Parameters

##### fieldSignature

[`AbstractFieldRef`](AbstractFieldRef.md)

##### nodeID

`number`

#### Returns

`boolean`

***

### addIncomingEdge()

> **addIncomingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:105

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addIncomingEdge`](PagNode.md#addincomingedge)

***

### addLoadInEdge()

> **addLoadInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:257

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadInEdge`](PagNode.md#addloadinedge)

***

### addLoadOutEdge()

> **addLoadOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:263

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadOutEdge`](PagNode.md#addloadoutedge)

***

### addOutgoingEdge()

> **addOutgoingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:109

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addOutgoingEdge`](PagNode.md#addoutgoingedge)

***

### addPointToElement()

> **addPointToElement**(`node`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:301

#### Parameters

##### node

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addPointToElement`](PagNode.md#addpointtoelement)

***

### addThisInEdge()

> **addThisInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:281

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisInEdge`](PagNode.md#addthisinedge)

***

### addThisOutEdge()

> **addThisOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:287

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisOutEdge`](PagNode.md#addthisoutedge)

***

### addWriteInEdge()

> **addWriteInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:269

#### Parameters

##### e

[`WritePagEdge`](WritePagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteInEdge`](PagNode.md#addwriteinedge)

***

### addWriteOutEdge()

> **addWriteOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:275

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteOutEdge`](PagNode.md#addwriteoutedge)

***

### getBasePt()

> **getBasePt**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:173

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getBasePt`](PagNode.md#getbasept)

***

### getCid()

> **getCid**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:181

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getCid`](PagNode.md#getcid)

***

### getClonedFrom()

> **getClonedFrom**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:323

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getClonedFrom`](PagNode.md#getclonedfrom)

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:331

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotAttr`](PagNode.md#getdotattr)

***

### getDotLabel()

> **getDotLabel**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:352

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotLabel`](PagNode.md#getdotlabel)

***

### getFieldNode()

> **getFieldNode**(`fieldSignature`): `undefined` \| `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:641

#### Parameters

##### fieldSignature

[`AbstractFieldRef`](AbstractFieldRef.md)

#### Returns

`undefined` \| `number`

***

### getFieldNodes()

> **getFieldNodes**(): `undefined` \| `Map`\<`string`, `number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:645

#### Returns

`undefined` \| `Map`\<`string`, `number`\>

***

### getID()

> **getID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:77

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getID`](PagNode.md#getid)

***

### getIncomingCopyEdges()

> **getIncomingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:208

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingCopyEdges`](PagNode.md#getincomingcopyedges)

***

### getIncomingEdge()

> **getIncomingEdge**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:121

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingEdge`](PagNode.md#getincomingedge)

***

### getIncomingThisEdges()

> **getIncomingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:228

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingThisEdges`](PagNode.md#getincomingthisedges)

***

### getIncomingWriteEdges()

> **getIncomingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:220

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingWriteEdges`](PagNode.md#getincomingwriteedges)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:81

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getKind`](PagNode.md#getkind)

***

### getOutEdges()

> **getOutEdges**(): `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:309

#### Returns

`object`

##### AddressEdge

> **AddressEdge**: `PagEdgeSet`

##### CopyEdge

> **CopyEdge**: `PagEdgeSet`

##### LoadEdge

> **LoadEdge**: `PagEdgeSet`

##### WriteEdge

> **WriteEdge**: `PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutEdges`](PagNode.md#getoutedges)

***

### getOutgoingCopyEdges()

> **getOutgoingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:204

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingCopyEdges`](PagNode.md#getoutgoingcopyedges)

***

### getOutgoingEdges()

> **getOutgoingEdges**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:125

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingEdges`](PagNode.md#getoutgoingedges)

***

### getOutgoingLoadEdges()

> **getOutgoingLoadEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:212

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingLoadEdges`](PagNode.md#getoutgoingloadedges)

***

### getOutgoingThisEdges()

> **getOutgoingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:224

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingThisEdges`](PagNode.md#getoutgoingthisedges)

***

### getOutgoingWriteEdges()

> **getOutgoingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:216

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingWriteEdges`](PagNode.md#getoutgoingwriteedges)

***

### getPointTo()

> **getPointTo**(): `IPtsCollection`\<`number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:297

#### Returns

`IPtsCollection`\<`number`\>

#### Inherited from

[`PagNode`](PagNode.md).[`getPointTo`](PagNode.md#getpointto)

***

### getStmt()

> **getStmt**(): `undefined` \| [`Stmt`](Stmt.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:196

#### Returns

`undefined` \| [`Stmt`](Stmt.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getStmt`](PagNode.md#getstmt)

***

### getValue()

> **getValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:293

#### Returns

[`Value`](../interfaces/Value.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getValue`](PagNode.md#getvalue)

***

### hasIncomingEdge()

> **hasIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:97

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdge`](PagNode.md#hasincomingedge)

***

### hasIncomingEdges()

> **hasIncomingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:89

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdges`](PagNode.md#hasincomingedges)

***

### hasOutgoingCopyEdge()

> **hasOutgoingCopyEdge**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:200

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingCopyEdge`](PagNode.md#hasoutgoingcopyedge)

***

### hasOutgoingEdge()

> **hasOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:101

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdge`](PagNode.md#hasoutgoingedge)

***

### hasOutgoingEdges()

> **hasOutgoingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:93

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdges`](PagNode.md#hasoutgoingedges)

***

### removeIncomingEdge()

> **removeIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:113

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeIncomingEdge`](PagNode.md#removeincomingedge)

***

### removeOutgoingEdge()

> **removeOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:117

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeOutgoingEdge`](PagNode.md#removeoutgoingedge)

***

### setBasePt()

> **setBasePt**(`pt`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:177

#### Parameters

##### pt

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setBasePt`](PagNode.md#setbasept)

***

### setCid()

> **setCid**(`cid`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:188

#### Parameters

##### cid

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setCid`](PagNode.md#setcid)

***

### setClonedFrom()

> **setClonedFrom**(`id`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:327

#### Parameters

##### id

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setClonedFrom`](PagNode.md#setclonedfrom)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:85

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setKind`](PagNode.md#setkind)

***

### setPointTo()

> **setPointTo**(`pts`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:305

#### Parameters

##### pts

`IPtsCollection`\<`number`\>

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setPointTo`](PagNode.md#setpointto)

***

### setStmt()

> **setStmt**(`s`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:192

#### Parameters

##### s

[`Stmt`](Stmt.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setStmt`](PagNode.md#setstmt)




============================================================
## FILE: `classes/PagInstanceFieldNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagInstanceFieldNode

# Class: PagInstanceFieldNode

Defined in: src/callgraph/pointerAnalysis/Pag.ts:450

## Extends

- [`PagNode`](PagNode.md)

## Constructors

### Constructor

> **new PagInstanceFieldNode**(`id`, `cid`, `instanceFieldRef`, `stmt?`): `PagInstanceFieldNode`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:451

#### Parameters

##### id

`number`

##### cid

`undefined` | `number`

##### instanceFieldRef

[`ArkInstanceFieldRef`](ArkInstanceFieldRef.md)

##### stmt?

[`Stmt`](Stmt.md)

#### Returns

`PagInstanceFieldNode`

#### Overrides

[`PagNode`](PagNode.md).[`constructor`](PagNode.md#constructor)

## Properties

### basePt

> `protected` **basePt**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:161

#### Inherited from

[`PagNode`](PagNode.md).[`basePt`](PagNode.md#basept)

***

### clonedFrom

> `protected` **clonedFrom**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:162

#### Inherited from

[`PagNode`](PagNode.md).[`clonedFrom`](PagNode.md#clonedfrom)

***

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:68

#### Inherited from

[`PagNode`](PagNode.md).[`kind`](PagNode.md#kind)

## Methods

### addAddressInEdge()

> **addAddressInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:232

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressInEdge`](PagNode.md#addaddressinedge)

***

### addAddressOutEdge()

> **addAddressOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:238

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressOutEdge`](PagNode.md#addaddressoutedge)

***

### addCopyInEdge()

> **addCopyInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:244

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyInEdge`](PagNode.md#addcopyinedge)

***

### addCopyOutEdge()

> **addCopyOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:250

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyOutEdge`](PagNode.md#addcopyoutedge)

***

### addIncomingEdge()

> **addIncomingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:105

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addIncomingEdge`](PagNode.md#addincomingedge)

***

### addLoadInEdge()

> **addLoadInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:257

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadInEdge`](PagNode.md#addloadinedge)

***

### addLoadOutEdge()

> **addLoadOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:263

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadOutEdge`](PagNode.md#addloadoutedge)

***

### addOutgoingEdge()

> **addOutgoingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:109

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addOutgoingEdge`](PagNode.md#addoutgoingedge)

***

### addPointToElement()

> **addPointToElement**(`node`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:301

#### Parameters

##### node

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addPointToElement`](PagNode.md#addpointtoelement)

***

### addThisInEdge()

> **addThisInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:281

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisInEdge`](PagNode.md#addthisinedge)

***

### addThisOutEdge()

> **addThisOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:287

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisOutEdge`](PagNode.md#addthisoutedge)

***

### addWriteInEdge()

> **addWriteInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:269

#### Parameters

##### e

[`WritePagEdge`](WritePagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteInEdge`](PagNode.md#addwriteinedge)

***

### addWriteOutEdge()

> **addWriteOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:275

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteOutEdge`](PagNode.md#addwriteoutedge)

***

### getBasePt()

> **getBasePt**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:173

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getBasePt`](PagNode.md#getbasept)

***

### getCid()

> **getCid**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:181

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getCid`](PagNode.md#getcid)

***

### getClonedFrom()

> **getClonedFrom**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:323

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getClonedFrom`](PagNode.md#getclonedfrom)

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:331

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotAttr`](PagNode.md#getdotattr)

***

### getDotLabel()

> **getDotLabel**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:352

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotLabel`](PagNode.md#getdotlabel)

***

### getID()

> **getID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:77

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getID`](PagNode.md#getid)

***

### getIncomingCopyEdges()

> **getIncomingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:208

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingCopyEdges`](PagNode.md#getincomingcopyedges)

***

### getIncomingEdge()

> **getIncomingEdge**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:121

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingEdge`](PagNode.md#getincomingedge)

***

### getIncomingThisEdges()

> **getIncomingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:228

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingThisEdges`](PagNode.md#getincomingthisedges)

***

### getIncomingWriteEdges()

> **getIncomingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:220

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingWriteEdges`](PagNode.md#getincomingwriteedges)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:81

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getKind`](PagNode.md#getkind)

***

### getOutEdges()

> **getOutEdges**(): `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:309

#### Returns

`object`

##### AddressEdge

> **AddressEdge**: `PagEdgeSet`

##### CopyEdge

> **CopyEdge**: `PagEdgeSet`

##### LoadEdge

> **LoadEdge**: `PagEdgeSet`

##### WriteEdge

> **WriteEdge**: `PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutEdges`](PagNode.md#getoutedges)

***

### getOutgoingCopyEdges()

> **getOutgoingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:204

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingCopyEdges`](PagNode.md#getoutgoingcopyedges)

***

### getOutgoingEdges()

> **getOutgoingEdges**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:125

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingEdges`](PagNode.md#getoutgoingedges)

***

### getOutgoingLoadEdges()

> **getOutgoingLoadEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:212

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingLoadEdges`](PagNode.md#getoutgoingloadedges)

***

### getOutgoingThisEdges()

> **getOutgoingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:224

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingThisEdges`](PagNode.md#getoutgoingthisedges)

***

### getOutgoingWriteEdges()

> **getOutgoingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:216

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingWriteEdges`](PagNode.md#getoutgoingwriteedges)

***

### getPointTo()

> **getPointTo**(): `IPtsCollection`\<`number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:297

#### Returns

`IPtsCollection`\<`number`\>

#### Inherited from

[`PagNode`](PagNode.md).[`getPointTo`](PagNode.md#getpointto)

***

### getStmt()

> **getStmt**(): `undefined` \| [`Stmt`](Stmt.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:196

#### Returns

`undefined` \| [`Stmt`](Stmt.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getStmt`](PagNode.md#getstmt)

***

### getValue()

> **getValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:293

#### Returns

[`Value`](../interfaces/Value.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getValue`](PagNode.md#getvalue)

***

### hasIncomingEdge()

> **hasIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:97

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdge`](PagNode.md#hasincomingedge)

***

### hasIncomingEdges()

> **hasIncomingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:89

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdges`](PagNode.md#hasincomingedges)

***

### hasOutgoingCopyEdge()

> **hasOutgoingCopyEdge**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:200

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingCopyEdge`](PagNode.md#hasoutgoingcopyedge)

***

### hasOutgoingEdge()

> **hasOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:101

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdge`](PagNode.md#hasoutgoingedge)

***

### hasOutgoingEdges()

> **hasOutgoingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:93

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdges`](PagNode.md#hasoutgoingedges)

***

### removeIncomingEdge()

> **removeIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:113

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeIncomingEdge`](PagNode.md#removeincomingedge)

***

### removeOutgoingEdge()

> **removeOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:117

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeOutgoingEdge`](PagNode.md#removeoutgoingedge)

***

### setBasePt()

> **setBasePt**(`pt`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:177

#### Parameters

##### pt

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setBasePt`](PagNode.md#setbasept)

***

### setCid()

> **setCid**(`cid`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:188

#### Parameters

##### cid

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setCid`](PagNode.md#setcid)

***

### setClonedFrom()

> **setClonedFrom**(`id`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:327

#### Parameters

##### id

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setClonedFrom`](PagNode.md#setclonedfrom)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:85

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setKind`](PagNode.md#setkind)

***

### setPointTo()

> **setPointTo**(`pts`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:305

#### Parameters

##### pts

`IPtsCollection`\<`number`\>

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setPointTo`](PagNode.md#setpointto)

***

### setStmt()

> **setStmt**(`s`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:192

#### Parameters

##### s

[`Stmt`](Stmt.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setStmt`](PagNode.md#setstmt)




============================================================
## FILE: `classes/PagLocalNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagLocalNode

# Class: PagLocalNode

Defined in: src/callgraph/pointerAnalysis/Pag.ts:391

## Extends

- [`PagNode`](PagNode.md)

## Constructors

### Constructor

> **new PagLocalNode**(`id`, `cid`, `value`, `stmt?`): `PagLocalNode`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:400

#### Parameters

##### id

`number`

##### cid

`undefined` | `number`

##### value

[`Local`](Local.md)

##### stmt?

[`Stmt`](Stmt.md)

#### Returns

`PagLocalNode`

#### Overrides

[`PagNode`](PagNode.md).[`constructor`](PagNode.md#constructor)

## Properties

### basePt

> `protected` **basePt**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:161

#### Inherited from

[`PagNode`](PagNode.md).[`basePt`](PagNode.md#basept)

***

### clonedFrom

> `protected` **clonedFrom**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:162

#### Inherited from

[`PagNode`](PagNode.md).[`clonedFrom`](PagNode.md#clonedfrom)

***

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:68

#### Inherited from

[`PagNode`](PagNode.md).[`kind`](PagNode.md#kind)

## Methods

### addAddressInEdge()

> **addAddressInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:232

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressInEdge`](PagNode.md#addaddressinedge)

***

### addAddressOutEdge()

> **addAddressOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:238

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressOutEdge`](PagNode.md#addaddressoutedge)

***

### addCopyInEdge()

> **addCopyInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:244

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyInEdge`](PagNode.md#addcopyinedge)

***

### addCopyOutEdge()

> **addCopyOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:250

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyOutEdge`](PagNode.md#addcopyoutedge)

***

### addIncomingEdge()

> **addIncomingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:105

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addIncomingEdge`](PagNode.md#addincomingedge)

***

### addLoadInEdge()

> **addLoadInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:257

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadInEdge`](PagNode.md#addloadinedge)

***

### addLoadOutEdge()

> **addLoadOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:263

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadOutEdge`](PagNode.md#addloadoutedge)

***

### addOutgoingEdge()

> **addOutgoingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:109

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addOutgoingEdge`](PagNode.md#addoutgoingedge)

***

### addPointToElement()

> **addPointToElement**(`node`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:301

#### Parameters

##### node

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addPointToElement`](PagNode.md#addpointtoelement)

***

### addRelatedDynCallSite()

> **addRelatedDynCallSite**(`cs`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:404

#### Parameters

##### cs

[`DynCallSite`](DynCallSite.md)

#### Returns

`void`

***

### addRelatedUnknownCallSite()

> **addRelatedUnknownCallSite**(`cs`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:414

#### Parameters

##### cs

[`CallSite`](CallSite.md)

#### Returns

`void`

***

### addThisInEdge()

> **addThisInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:281

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisInEdge`](PagNode.md#addthisinedge)

***

### addThisOutEdge()

> **addThisOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:287

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisOutEdge`](PagNode.md#addthisoutedge)

***

### addWriteInEdge()

> **addWriteInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:269

#### Parameters

##### e

[`WritePagEdge`](WritePagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteInEdge`](PagNode.md#addwriteinedge)

***

### addWriteOutEdge()

> **addWriteOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:275

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteOutEdge`](PagNode.md#addwriteoutedge)

***

### getBasePt()

> **getBasePt**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:173

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getBasePt`](PagNode.md#getbasept)

***

### getCid()

> **getCid**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:181

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getCid`](PagNode.md#getcid)

***

### getClonedFrom()

> **getClonedFrom**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:323

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getClonedFrom`](PagNode.md#getclonedfrom)

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:331

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotAttr`](PagNode.md#getdotattr)

***

### getDotLabel()

> **getDotLabel**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:352

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotLabel`](PagNode.md#getdotlabel)

***

### getID()

> **getID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:77

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getID`](PagNode.md#getid)

***

### getIncomingCopyEdges()

> **getIncomingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:208

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingCopyEdges`](PagNode.md#getincomingcopyedges)

***

### getIncomingEdge()

> **getIncomingEdge**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:121

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingEdge`](PagNode.md#getincomingedge)

***

### getIncomingThisEdges()

> **getIncomingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:228

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingThisEdges`](PagNode.md#getincomingthisedges)

***

### getIncomingWriteEdges()

> **getIncomingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:220

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingWriteEdges`](PagNode.md#getincomingwriteedges)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:81

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getKind`](PagNode.md#getkind)

***

### getOutEdges()

> **getOutEdges**(): `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:309

#### Returns

`object`

##### AddressEdge

> **AddressEdge**: `PagEdgeSet`

##### CopyEdge

> **CopyEdge**: `PagEdgeSet`

##### LoadEdge

> **LoadEdge**: `PagEdgeSet`

##### WriteEdge

> **WriteEdge**: `PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutEdges`](PagNode.md#getoutedges)

***

### getOutgoingCopyEdges()

> **getOutgoingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:204

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingCopyEdges`](PagNode.md#getoutgoingcopyedges)

***

### getOutgoingEdges()

> **getOutgoingEdges**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:125

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingEdges`](PagNode.md#getoutgoingedges)

***

### getOutgoingLoadEdges()

> **getOutgoingLoadEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:212

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingLoadEdges`](PagNode.md#getoutgoingloadedges)

***

### getOutgoingThisEdges()

> **getOutgoingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:224

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingThisEdges`](PagNode.md#getoutgoingthisedges)

***

### getOutgoingWriteEdges()

> **getOutgoingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:216

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingWriteEdges`](PagNode.md#getoutgoingwriteedges)

***

### getPointTo()

> **getPointTo**(): `IPtsCollection`\<`number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:297

#### Returns

`IPtsCollection`\<`number`\>

#### Inherited from

[`PagNode`](PagNode.md).[`getPointTo`](PagNode.md#getpointto)

***

### getRelatedDynCallSites()

> **getRelatedDynCallSites**(): `Set`\<[`DynCallSite`](DynCallSite.md)\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:410

#### Returns

`Set`\<[`DynCallSite`](DynCallSite.md)\>

***

### getRelatedUnknownCallSites()

> **getRelatedUnknownCallSites**(): `Set`\<[`CallSite`](CallSite.md)\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:420

#### Returns

`Set`\<[`CallSite`](CallSite.md)\>

***

### getStmt()

> **getStmt**(): `undefined` \| [`Stmt`](Stmt.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:196

#### Returns

`undefined` \| [`Stmt`](Stmt.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getStmt`](PagNode.md#getstmt)

***

### getStorage()

> **getStorage**(): `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:430

#### Returns

`object`

##### PropertyName

> **PropertyName**: `string`

##### StorageType

> **StorageType**: [`StorageType`](../enumerations/StorageType.md)

***

### getValue()

> **getValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:293

#### Returns

[`Value`](../interfaces/Value.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getValue`](PagNode.md#getvalue)

***

### hasIncomingEdge()

> **hasIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:97

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdge`](PagNode.md#hasincomingedge)

***

### hasIncomingEdges()

> **hasIncomingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:89

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdges`](PagNode.md#hasincomingedges)

***

### hasOutgoingCopyEdge()

> **hasOutgoingCopyEdge**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:200

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingCopyEdge`](PagNode.md#hasoutgoingcopyedge)

***

### hasOutgoingEdge()

> **hasOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:101

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdge`](PagNode.md#hasoutgoingedge)

***

### hasOutgoingEdges()

> **hasOutgoingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:93

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdges`](PagNode.md#hasoutgoingedges)

***

### isSdkParam()

> **isSdkParam**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:445

#### Returns

`boolean`

***

### isStorageLinked()

> **isStorageLinked**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:437

#### Returns

`boolean`

***

### removeIncomingEdge()

> **removeIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:113

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeIncomingEdge`](PagNode.md#removeincomingedge)

***

### removeOutgoingEdge()

> **removeOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:117

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeOutgoingEdge`](PagNode.md#removeoutgoingedge)

***

### setBasePt()

> **setBasePt**(`pt`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:177

#### Parameters

##### pt

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setBasePt`](PagNode.md#setbasept)

***

### setCid()

> **setCid**(`cid`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:188

#### Parameters

##### cid

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setCid`](PagNode.md#setcid)

***

### setClonedFrom()

> **setClonedFrom**(`id`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:327

#### Parameters

##### id

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setClonedFrom`](PagNode.md#setclonedfrom)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:85

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setKind`](PagNode.md#setkind)

***

### setPointTo()

> **setPointTo**(`pts`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:305

#### Parameters

##### pts

`IPtsCollection`\<`number`\>

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setPointTo`](PagNode.md#setpointto)

***

### setSdkParam()

> **setSdkParam**(): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:441

#### Returns

`void`

***

### setStmt()

> **setStmt**(`s`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:192

#### Parameters

##### s

[`Stmt`](Stmt.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setStmt`](PagNode.md#setstmt)

***

### setStorageLink()

> **setStorageLink**(`storageType`, `propertyName`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:424

#### Parameters

##### storageType

[`StorageType`](../enumerations/StorageType.md)

##### propertyName

`string`

#### Returns

`void`




============================================================
## FILE: `classes/PagNewContainerExprNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagNewContainerExprNode

# Class: PagNewContainerExprNode

Defined in: src/callgraph/pointerAnalysis/Pag.ts:524

## Extends

- [`PagNode`](PagNode.md)

## Constructors

### Constructor

> **new PagNewContainerExprNode**(`id`, `cid`, `expr`, `stmt?`): `PagNewContainerExprNode`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:528

#### Parameters

##### id

`number`

##### cid

`undefined` | `number`

##### expr

[`Value`](../interfaces/Value.md)

##### stmt?

[`Stmt`](Stmt.md)

#### Returns

`PagNewContainerExprNode`

#### Overrides

[`PagNode`](PagNode.md).[`constructor`](PagNode.md#constructor)

## Properties

### basePt

> `protected` **basePt**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:161

#### Inherited from

[`PagNode`](PagNode.md).[`basePt`](PagNode.md#basept)

***

### clonedFrom

> `protected` **clonedFrom**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:162

#### Inherited from

[`PagNode`](PagNode.md).[`clonedFrom`](PagNode.md#clonedfrom)

***

### elementNode

> **elementNode**: `undefined` \| `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:526

***

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:68

#### Inherited from

[`PagNode`](PagNode.md).[`kind`](PagNode.md#kind)

## Methods

### addAddressInEdge()

> **addAddressInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:232

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressInEdge`](PagNode.md#addaddressinedge)

***

### addAddressOutEdge()

> **addAddressOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:238

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressOutEdge`](PagNode.md#addaddressoutedge)

***

### addCopyInEdge()

> **addCopyInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:244

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyInEdge`](PagNode.md#addcopyinedge)

***

### addCopyOutEdge()

> **addCopyOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:250

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyOutEdge`](PagNode.md#addcopyoutedge)

***

### addElementNode()

> **addElementNode**(`nodeID`): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:532

#### Parameters

##### nodeID

`number`

#### Returns

`boolean`

***

### addIncomingEdge()

> **addIncomingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:105

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addIncomingEdge`](PagNode.md#addincomingedge)

***

### addLoadInEdge()

> **addLoadInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:257

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadInEdge`](PagNode.md#addloadinedge)

***

### addLoadOutEdge()

> **addLoadOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:263

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadOutEdge`](PagNode.md#addloadoutedge)

***

### addOutgoingEdge()

> **addOutgoingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:109

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addOutgoingEdge`](PagNode.md#addoutgoingedge)

***

### addPointToElement()

> **addPointToElement**(`node`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:301

#### Parameters

##### node

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addPointToElement`](PagNode.md#addpointtoelement)

***

### addThisInEdge()

> **addThisInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:281

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisInEdge`](PagNode.md#addthisinedge)

***

### addThisOutEdge()

> **addThisOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:287

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisOutEdge`](PagNode.md#addthisoutedge)

***

### addWriteInEdge()

> **addWriteInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:269

#### Parameters

##### e

[`WritePagEdge`](WritePagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteInEdge`](PagNode.md#addwriteinedge)

***

### addWriteOutEdge()

> **addWriteOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:275

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteOutEdge`](PagNode.md#addwriteoutedge)

***

### getBasePt()

> **getBasePt**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:173

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getBasePt`](PagNode.md#getbasept)

***

### getCid()

> **getCid**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:181

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getCid`](PagNode.md#getcid)

***

### getClonedFrom()

> **getClonedFrom**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:323

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getClonedFrom`](PagNode.md#getclonedfrom)

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:331

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotAttr`](PagNode.md#getdotattr)

***

### getDotLabel()

> **getDotLabel**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:352

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotLabel`](PagNode.md#getdotlabel)

***

### getElementNode()

> **getElementNode**(): `undefined` \| `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:540

#### Returns

`undefined` \| `number`

***

### getID()

> **getID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:77

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getID`](PagNode.md#getid)

***

### getIncomingCopyEdges()

> **getIncomingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:208

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingCopyEdges`](PagNode.md#getincomingcopyedges)

***

### getIncomingEdge()

> **getIncomingEdge**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:121

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingEdge`](PagNode.md#getincomingedge)

***

### getIncomingThisEdges()

> **getIncomingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:228

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingThisEdges`](PagNode.md#getincomingthisedges)

***

### getIncomingWriteEdges()

> **getIncomingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:220

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingWriteEdges`](PagNode.md#getincomingwriteedges)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:81

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getKind`](PagNode.md#getkind)

***

### getOutEdges()

> **getOutEdges**(): `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:309

#### Returns

`object`

##### AddressEdge

> **AddressEdge**: `PagEdgeSet`

##### CopyEdge

> **CopyEdge**: `PagEdgeSet`

##### LoadEdge

> **LoadEdge**: `PagEdgeSet`

##### WriteEdge

> **WriteEdge**: `PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutEdges`](PagNode.md#getoutedges)

***

### getOutgoingCopyEdges()

> **getOutgoingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:204

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingCopyEdges`](PagNode.md#getoutgoingcopyedges)

***

### getOutgoingEdges()

> **getOutgoingEdges**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:125

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingEdges`](PagNode.md#getoutgoingedges)

***

### getOutgoingLoadEdges()

> **getOutgoingLoadEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:212

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingLoadEdges`](PagNode.md#getoutgoingloadedges)

***

### getOutgoingThisEdges()

> **getOutgoingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:224

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingThisEdges`](PagNode.md#getoutgoingthisedges)

***

### getOutgoingWriteEdges()

> **getOutgoingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:216

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingWriteEdges`](PagNode.md#getoutgoingwriteedges)

***

### getPointTo()

> **getPointTo**(): `IPtsCollection`\<`number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:297

#### Returns

`IPtsCollection`\<`number`\>

#### Inherited from

[`PagNode`](PagNode.md).[`getPointTo`](PagNode.md#getpointto)

***

### getStmt()

> **getStmt**(): `undefined` \| [`Stmt`](Stmt.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:196

#### Returns

`undefined` \| [`Stmt`](Stmt.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getStmt`](PagNode.md#getstmt)

***

### getValue()

> **getValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:293

#### Returns

[`Value`](../interfaces/Value.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getValue`](PagNode.md#getvalue)

***

### hasIncomingEdge()

> **hasIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:97

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdge`](PagNode.md#hasincomingedge)

***

### hasIncomingEdges()

> **hasIncomingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:89

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdges`](PagNode.md#hasincomingedges)

***

### hasOutgoingCopyEdge()

> **hasOutgoingCopyEdge**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:200

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingCopyEdge`](PagNode.md#hasoutgoingcopyedge)

***

### hasOutgoingEdge()

> **hasOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:101

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdge`](PagNode.md#hasoutgoingedge)

***

### hasOutgoingEdges()

> **hasOutgoingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:93

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdges`](PagNode.md#hasoutgoingedges)

***

### removeIncomingEdge()

> **removeIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:113

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeIncomingEdge`](PagNode.md#removeincomingedge)

***

### removeOutgoingEdge()

> **removeOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:117

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeOutgoingEdge`](PagNode.md#removeoutgoingedge)

***

### setBasePt()

> **setBasePt**(`pt`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:177

#### Parameters

##### pt

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setBasePt`](PagNode.md#setbasept)

***

### setCid()

> **setCid**(`cid`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:188

#### Parameters

##### cid

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setCid`](PagNode.md#setcid)

***

### setClonedFrom()

> **setClonedFrom**(`id`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:327

#### Parameters

##### id

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setClonedFrom`](PagNode.md#setclonedfrom)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:85

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setKind`](PagNode.md#setkind)

***

### setPointTo()

> **setPointTo**(`pts`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:305

#### Parameters

##### pts

`IPtsCollection`\<`number`\>

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setPointTo`](PagNode.md#setpointto)

***

### setStmt()

> **setStmt**(`s`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:192

#### Parameters

##### s

[`Stmt`](Stmt.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setStmt`](PagNode.md#setstmt)




============================================================
## FILE: `classes/PagNewExprNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagNewExprNode

# Class: PagNewExprNode

Defined in: src/callgraph/pointerAnalysis/Pag.ts:490

below is heapObj like Node

## Extends

- [`PagNode`](PagNode.md)

## Constructors

### Constructor

> **new PagNewExprNode**(`id`, `cid`, `expr`, `stmt?`): `PagNewExprNode`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:494

#### Parameters

##### id

`number`

##### cid

`undefined` | `number`

##### expr

[`AbstractExpr`](AbstractExpr.md)

##### stmt?

[`Stmt`](Stmt.md)

#### Returns

`PagNewExprNode`

#### Overrides

[`PagNode`](PagNode.md).[`constructor`](PagNode.md#constructor)

## Properties

### basePt

> `protected` **basePt**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:161

#### Inherited from

[`PagNode`](PagNode.md).[`basePt`](PagNode.md#basept)

***

### clonedFrom

> `protected` **clonedFrom**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:162

#### Inherited from

[`PagNode`](PagNode.md).[`clonedFrom`](PagNode.md#clonedfrom)

***

### fieldNodes

> **fieldNodes**: `Map`\<`string`, `number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:492

***

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:68

#### Inherited from

[`PagNode`](PagNode.md).[`kind`](PagNode.md#kind)

## Methods

### addAddressInEdge()

> **addAddressInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:232

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressInEdge`](PagNode.md#addaddressinedge)

***

### addAddressOutEdge()

> **addAddressOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:238

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressOutEdge`](PagNode.md#addaddressoutedge)

***

### addCopyInEdge()

> **addCopyInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:244

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyInEdge`](PagNode.md#addcopyinedge)

***

### addCopyOutEdge()

> **addCopyOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:250

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyOutEdge`](PagNode.md#addcopyoutedge)

***

### addFieldNode()

> **addFieldNode**(`fieldSignature`, `nodeID`): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:498

#### Parameters

##### fieldSignature

[`AbstractFieldRef`](AbstractFieldRef.md)

##### nodeID

`number`

#### Returns

`boolean`

***

### addIncomingEdge()

> **addIncomingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:105

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addIncomingEdge`](PagNode.md#addincomingedge)

***

### addLoadInEdge()

> **addLoadInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:257

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadInEdge`](PagNode.md#addloadinedge)

***

### addLoadOutEdge()

> **addLoadOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:263

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadOutEdge`](PagNode.md#addloadoutedge)

***

### addOutgoingEdge()

> **addOutgoingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:109

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addOutgoingEdge`](PagNode.md#addoutgoingedge)

***

### addPointToElement()

> **addPointToElement**(`node`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:301

#### Parameters

##### node

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addPointToElement`](PagNode.md#addpointtoelement)

***

### addThisInEdge()

> **addThisInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:281

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisInEdge`](PagNode.md#addthisinedge)

***

### addThisOutEdge()

> **addThisOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:287

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisOutEdge`](PagNode.md#addthisoutedge)

***

### addWriteInEdge()

> **addWriteInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:269

#### Parameters

##### e

[`WritePagEdge`](WritePagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteInEdge`](PagNode.md#addwriteinedge)

***

### addWriteOutEdge()

> **addWriteOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:275

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteOutEdge`](PagNode.md#addwriteoutedge)

***

### getBasePt()

> **getBasePt**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:173

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getBasePt`](PagNode.md#getbasept)

***

### getCid()

> **getCid**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:181

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getCid`](PagNode.md#getcid)

***

### getClonedFrom()

> **getClonedFrom**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:323

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getClonedFrom`](PagNode.md#getclonedfrom)

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:331

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotAttr`](PagNode.md#getdotattr)

***

### getDotLabel()

> **getDotLabel**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:352

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotLabel`](PagNode.md#getdotlabel)

***

### getFieldNode()

> **getFieldNode**(`fieldSignature`): `undefined` \| `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:509

#### Parameters

##### fieldSignature

[`AbstractFieldRef`](AbstractFieldRef.md)

#### Returns

`undefined` \| `number`

***

### getFieldNodes()

> **getFieldNodes**(): `undefined` \| `Map`\<`string`, `number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:516

#### Returns

`undefined` \| `Map`\<`string`, `number`\>

***

### getID()

> **getID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:77

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getID`](PagNode.md#getid)

***

### getIncomingCopyEdges()

> **getIncomingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:208

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingCopyEdges`](PagNode.md#getincomingcopyedges)

***

### getIncomingEdge()

> **getIncomingEdge**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:121

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingEdge`](PagNode.md#getincomingedge)

***

### getIncomingThisEdges()

> **getIncomingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:228

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingThisEdges`](PagNode.md#getincomingthisedges)

***

### getIncomingWriteEdges()

> **getIncomingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:220

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingWriteEdges`](PagNode.md#getincomingwriteedges)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:81

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getKind`](PagNode.md#getkind)

***

### getOutEdges()

> **getOutEdges**(): `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:309

#### Returns

`object`

##### AddressEdge

> **AddressEdge**: `PagEdgeSet`

##### CopyEdge

> **CopyEdge**: `PagEdgeSet`

##### LoadEdge

> **LoadEdge**: `PagEdgeSet`

##### WriteEdge

> **WriteEdge**: `PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutEdges`](PagNode.md#getoutedges)

***

### getOutgoingCopyEdges()

> **getOutgoingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:204

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingCopyEdges`](PagNode.md#getoutgoingcopyedges)

***

### getOutgoingEdges()

> **getOutgoingEdges**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:125

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingEdges`](PagNode.md#getoutgoingedges)

***

### getOutgoingLoadEdges()

> **getOutgoingLoadEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:212

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingLoadEdges`](PagNode.md#getoutgoingloadedges)

***

### getOutgoingThisEdges()

> **getOutgoingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:224

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingThisEdges`](PagNode.md#getoutgoingthisedges)

***

### getOutgoingWriteEdges()

> **getOutgoingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:216

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingWriteEdges`](PagNode.md#getoutgoingwriteedges)

***

### getPointTo()

> **getPointTo**(): `IPtsCollection`\<`number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:297

#### Returns

`IPtsCollection`\<`number`\>

#### Inherited from

[`PagNode`](PagNode.md).[`getPointTo`](PagNode.md#getpointto)

***

### getStmt()

> **getStmt**(): `undefined` \| [`Stmt`](Stmt.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:196

#### Returns

`undefined` \| [`Stmt`](Stmt.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getStmt`](PagNode.md#getstmt)

***

### getValue()

> **getValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:293

#### Returns

[`Value`](../interfaces/Value.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getValue`](PagNode.md#getvalue)

***

### hasIncomingEdge()

> **hasIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:97

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdge`](PagNode.md#hasincomingedge)

***

### hasIncomingEdges()

> **hasIncomingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:89

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdges`](PagNode.md#hasincomingedges)

***

### hasOutgoingCopyEdge()

> **hasOutgoingCopyEdge**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:200

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingCopyEdge`](PagNode.md#hasoutgoingcopyedge)

***

### hasOutgoingEdge()

> **hasOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:101

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdge`](PagNode.md#hasoutgoingedge)

***

### hasOutgoingEdges()

> **hasOutgoingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:93

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdges`](PagNode.md#hasoutgoingedges)

***

### removeIncomingEdge()

> **removeIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:113

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeIncomingEdge`](PagNode.md#removeincomingedge)

***

### removeOutgoingEdge()

> **removeOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:117

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeOutgoingEdge`](PagNode.md#removeoutgoingedge)

***

### setBasePt()

> **setBasePt**(`pt`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:177

#### Parameters

##### pt

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setBasePt`](PagNode.md#setbasept)

***

### setCid()

> **setCid**(`cid`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:188

#### Parameters

##### cid

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setCid`](PagNode.md#setcid)

***

### setClonedFrom()

> **setClonedFrom**(`id`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:327

#### Parameters

##### id

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setClonedFrom`](PagNode.md#setclonedfrom)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:85

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setKind`](PagNode.md#setkind)

***

### setPointTo()

> **setPointTo**(`pts`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:305

#### Parameters

##### pts

`IPtsCollection`\<`number`\>

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setPointTo`](PagNode.md#setpointto)

***

### setStmt()

> **setStmt**(`s`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:192

#### Parameters

##### s

[`Stmt`](Stmt.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setStmt`](PagNode.md#setstmt)




============================================================
## FILE: `classes/PagNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagNode

# Class: PagNode

Defined in: src/callgraph/pointerAnalysis/Pag.ts:141

## Extends

- [`BaseNode`](BaseNode.md)

## Extended by

- [`PagLocalNode`](PagLocalNode.md)
- [`PagInstanceFieldNode`](PagInstanceFieldNode.md)
- [`PagStaticFieldNode`](PagStaticFieldNode.md)
- [`PagThisRefNode`](PagThisRefNode.md)
- [`PagArrayNode`](PagArrayNode.md)
- [`PagNewExprNode`](PagNewExprNode.md)
- [`PagNewContainerExprNode`](PagNewContainerExprNode.md)
- [`PagParamNode`](PagParamNode.md)
- [`PagFuncNode`](PagFuncNode.md)
- [`PagGlobalThisNode`](PagGlobalThisNode.md)

## Constructors

### Constructor

> **new PagNode**(`id`, `cid`, `value`, `k`, `s?`): `PagNode`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:164

#### Parameters

##### id

`number`

##### cid

`undefined` | `number`

##### value

[`Value`](../interfaces/Value.md)

##### k

`number`

##### s?

[`Stmt`](Stmt.md)

#### Returns

`PagNode`

#### Overrides

[`BaseNode`](BaseNode.md).[`constructor`](BaseNode.md#constructor)

## Properties

### basePt

> `protected` **basePt**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:161

***

### clonedFrom

> `protected` **clonedFrom**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:162

***

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:68

#### Inherited from

[`BaseNode`](BaseNode.md).[`kind`](BaseNode.md#kind)

## Methods

### addAddressInEdge()

> **addAddressInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:232

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

***

### addAddressOutEdge()

> **addAddressOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:238

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

***

### addCopyInEdge()

> **addCopyInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:244

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

***

### addCopyOutEdge()

> **addCopyOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:250

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

***

### addIncomingEdge()

> **addIncomingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:105

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`BaseNode`](BaseNode.md).[`addIncomingEdge`](BaseNode.md#addincomingedge)

***

### addLoadInEdge()

> **addLoadInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:257

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

***

### addLoadOutEdge()

> **addLoadOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:263

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

***

### addOutgoingEdge()

> **addOutgoingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:109

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`BaseNode`](BaseNode.md).[`addOutgoingEdge`](BaseNode.md#addoutgoingedge)

***

### addPointToElement()

> **addPointToElement**(`node`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:301

#### Parameters

##### node

`number`

#### Returns

`void`

***

### addThisInEdge()

> **addThisInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:281

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

***

### addThisOutEdge()

> **addThisOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:287

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

***

### addWriteInEdge()

> **addWriteInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:269

#### Parameters

##### e

[`WritePagEdge`](WritePagEdge.md)

#### Returns

`void`

***

### addWriteOutEdge()

> **addWriteOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:275

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

***

### getBasePt()

> **getBasePt**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:173

#### Returns

`number`

***

### getCid()

> **getCid**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:181

#### Returns

`number`

***

### getClonedFrom()

> **getClonedFrom**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:323

#### Returns

`number`

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:331

#### Returns

`string`

#### Overrides

[`BaseNode`](BaseNode.md).[`getDotAttr`](BaseNode.md#getdotattr)

***

### getDotLabel()

> **getDotLabel**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:352

#### Returns

`string`

#### Overrides

[`BaseNode`](BaseNode.md).[`getDotLabel`](BaseNode.md#getdotlabel)

***

### getID()

> **getID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:77

#### Returns

`number`

#### Inherited from

[`BaseNode`](BaseNode.md).[`getID`](BaseNode.md#getid)

***

### getIncomingCopyEdges()

> **getIncomingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:208

#### Returns

`PagEdgeSet`

***

### getIncomingEdge()

> **getIncomingEdge**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:121

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`BaseNode`](BaseNode.md).[`getIncomingEdge`](BaseNode.md#getincomingedge)

***

### getIncomingThisEdges()

> **getIncomingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:228

#### Returns

`PagEdgeSet`

***

### getIncomingWriteEdges()

> **getIncomingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:220

#### Returns

`PagEdgeSet`

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:81

#### Returns

`number`

#### Inherited from

[`BaseNode`](BaseNode.md).[`getKind`](BaseNode.md#getkind)

***

### getOutEdges()

> **getOutEdges**(): `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:309

#### Returns

`object`

##### AddressEdge

> **AddressEdge**: `PagEdgeSet`

##### CopyEdge

> **CopyEdge**: `PagEdgeSet`

##### LoadEdge

> **LoadEdge**: `PagEdgeSet`

##### WriteEdge

> **WriteEdge**: `PagEdgeSet`

***

### getOutgoingCopyEdges()

> **getOutgoingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:204

#### Returns

`PagEdgeSet`

***

### getOutgoingEdges()

> **getOutgoingEdges**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:125

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`BaseNode`](BaseNode.md).[`getOutgoingEdges`](BaseNode.md#getoutgoingedges)

***

### getOutgoingLoadEdges()

> **getOutgoingLoadEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:212

#### Returns

`PagEdgeSet`

***

### getOutgoingThisEdges()

> **getOutgoingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:224

#### Returns

`PagEdgeSet`

***

### getOutgoingWriteEdges()

> **getOutgoingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:216

#### Returns

`PagEdgeSet`

***

### getPointTo()

> **getPointTo**(): `IPtsCollection`\<`number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:297

#### Returns

`IPtsCollection`\<`number`\>

***

### getStmt()

> **getStmt**(): `undefined` \| [`Stmt`](Stmt.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:196

#### Returns

`undefined` \| [`Stmt`](Stmt.md)

***

### getValue()

> **getValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:293

#### Returns

[`Value`](../interfaces/Value.md)

***

### hasIncomingEdge()

> **hasIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:97

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`BaseNode`](BaseNode.md).[`hasIncomingEdge`](BaseNode.md#hasincomingedge)

***

### hasIncomingEdges()

> **hasIncomingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:89

#### Returns

`boolean`

#### Inherited from

[`BaseNode`](BaseNode.md).[`hasIncomingEdges`](BaseNode.md#hasincomingedges)

***

### hasOutgoingCopyEdge()

> **hasOutgoingCopyEdge**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:200

#### Returns

`boolean`

***

### hasOutgoingEdge()

> **hasOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:101

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`BaseNode`](BaseNode.md).[`hasOutgoingEdge`](BaseNode.md#hasoutgoingedge)

***

### hasOutgoingEdges()

> **hasOutgoingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:93

#### Returns

`boolean`

#### Inherited from

[`BaseNode`](BaseNode.md).[`hasOutgoingEdges`](BaseNode.md#hasoutgoingedges)

***

### removeIncomingEdge()

> **removeIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:113

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`BaseNode`](BaseNode.md).[`removeIncomingEdge`](BaseNode.md#removeincomingedge)

***

### removeOutgoingEdge()

> **removeOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:117

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`BaseNode`](BaseNode.md).[`removeOutgoingEdge`](BaseNode.md#removeoutgoingedge)

***

### setBasePt()

> **setBasePt**(`pt`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:177

#### Parameters

##### pt

`number`

#### Returns

`void`

***

### setCid()

> **setCid**(`cid`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:188

#### Parameters

##### cid

`number`

#### Returns

`void`

***

### setClonedFrom()

> **setClonedFrom**(`id`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:327

#### Parameters

##### id

`number`

#### Returns

`void`

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:85

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`BaseNode`](BaseNode.md).[`setKind`](BaseNode.md#setkind)

***

### setPointTo()

> **setPointTo**(`pts`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:305

#### Parameters

##### pts

`IPtsCollection`\<`number`\>

#### Returns

`void`

***

### setStmt()

> **setStmt**(`s`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:192

#### Parameters

##### s

[`Stmt`](Stmt.md)

#### Returns

`void`




============================================================
## FILE: `classes/PagParamNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagParamNode

# Class: PagParamNode

Defined in: src/callgraph/pointerAnalysis/Pag.ts:548

## Extends

- [`PagNode`](PagNode.md)

## Constructors

### Constructor

> **new PagParamNode**(`id`, `cid`, `r`, `stmt?`): `PagParamNode`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:549

#### Parameters

##### id

`number`

##### cid

`undefined` | `number`

##### r

[`ArkParameterRef`](ArkParameterRef.md)

##### stmt?

[`Stmt`](Stmt.md)

#### Returns

`PagParamNode`

#### Overrides

[`PagNode`](PagNode.md).[`constructor`](PagNode.md#constructor)

## Properties

### basePt

> `protected` **basePt**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:161

#### Inherited from

[`PagNode`](PagNode.md).[`basePt`](PagNode.md#basept)

***

### clonedFrom

> `protected` **clonedFrom**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:162

#### Inherited from

[`PagNode`](PagNode.md).[`clonedFrom`](PagNode.md#clonedfrom)

***

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:68

#### Inherited from

[`PagNode`](PagNode.md).[`kind`](PagNode.md#kind)

## Methods

### addAddressInEdge()

> **addAddressInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:232

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressInEdge`](PagNode.md#addaddressinedge)

***

### addAddressOutEdge()

> **addAddressOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:238

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressOutEdge`](PagNode.md#addaddressoutedge)

***

### addCopyInEdge()

> **addCopyInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:244

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyInEdge`](PagNode.md#addcopyinedge)

***

### addCopyOutEdge()

> **addCopyOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:250

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyOutEdge`](PagNode.md#addcopyoutedge)

***

### addIncomingEdge()

> **addIncomingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:105

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addIncomingEdge`](PagNode.md#addincomingedge)

***

### addLoadInEdge()

> **addLoadInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:257

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadInEdge`](PagNode.md#addloadinedge)

***

### addLoadOutEdge()

> **addLoadOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:263

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadOutEdge`](PagNode.md#addloadoutedge)

***

### addOutgoingEdge()

> **addOutgoingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:109

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addOutgoingEdge`](PagNode.md#addoutgoingedge)

***

### addPointToElement()

> **addPointToElement**(`node`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:301

#### Parameters

##### node

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addPointToElement`](PagNode.md#addpointtoelement)

***

### addThisInEdge()

> **addThisInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:281

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisInEdge`](PagNode.md#addthisinedge)

***

### addThisOutEdge()

> **addThisOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:287

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisOutEdge`](PagNode.md#addthisoutedge)

***

### addWriteInEdge()

> **addWriteInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:269

#### Parameters

##### e

[`WritePagEdge`](WritePagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteInEdge`](PagNode.md#addwriteinedge)

***

### addWriteOutEdge()

> **addWriteOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:275

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteOutEdge`](PagNode.md#addwriteoutedge)

***

### getBasePt()

> **getBasePt**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:173

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getBasePt`](PagNode.md#getbasept)

***

### getCid()

> **getCid**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:181

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getCid`](PagNode.md#getcid)

***

### getClonedFrom()

> **getClonedFrom**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:323

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getClonedFrom`](PagNode.md#getclonedfrom)

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:331

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotAttr`](PagNode.md#getdotattr)

***

### getDotLabel()

> **getDotLabel**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:352

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotLabel`](PagNode.md#getdotlabel)

***

### getID()

> **getID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:77

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getID`](PagNode.md#getid)

***

### getIncomingCopyEdges()

> **getIncomingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:208

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingCopyEdges`](PagNode.md#getincomingcopyedges)

***

### getIncomingEdge()

> **getIncomingEdge**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:121

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingEdge`](PagNode.md#getincomingedge)

***

### getIncomingThisEdges()

> **getIncomingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:228

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingThisEdges`](PagNode.md#getincomingthisedges)

***

### getIncomingWriteEdges()

> **getIncomingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:220

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingWriteEdges`](PagNode.md#getincomingwriteedges)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:81

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getKind`](PagNode.md#getkind)

***

### getOutEdges()

> **getOutEdges**(): `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:309

#### Returns

`object`

##### AddressEdge

> **AddressEdge**: `PagEdgeSet`

##### CopyEdge

> **CopyEdge**: `PagEdgeSet`

##### LoadEdge

> **LoadEdge**: `PagEdgeSet`

##### WriteEdge

> **WriteEdge**: `PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutEdges`](PagNode.md#getoutedges)

***

### getOutgoingCopyEdges()

> **getOutgoingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:204

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingCopyEdges`](PagNode.md#getoutgoingcopyedges)

***

### getOutgoingEdges()

> **getOutgoingEdges**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:125

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingEdges`](PagNode.md#getoutgoingedges)

***

### getOutgoingLoadEdges()

> **getOutgoingLoadEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:212

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingLoadEdges`](PagNode.md#getoutgoingloadedges)

***

### getOutgoingThisEdges()

> **getOutgoingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:224

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingThisEdges`](PagNode.md#getoutgoingthisedges)

***

### getOutgoingWriteEdges()

> **getOutgoingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:216

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingWriteEdges`](PagNode.md#getoutgoingwriteedges)

***

### getPointTo()

> **getPointTo**(): `IPtsCollection`\<`number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:297

#### Returns

`IPtsCollection`\<`number`\>

#### Inherited from

[`PagNode`](PagNode.md).[`getPointTo`](PagNode.md#getpointto)

***

### getStmt()

> **getStmt**(): `undefined` \| [`Stmt`](Stmt.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:196

#### Returns

`undefined` \| [`Stmt`](Stmt.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getStmt`](PagNode.md#getstmt)

***

### getValue()

> **getValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:293

#### Returns

[`Value`](../interfaces/Value.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getValue`](PagNode.md#getvalue)

***

### hasIncomingEdge()

> **hasIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:97

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdge`](PagNode.md#hasincomingedge)

***

### hasIncomingEdges()

> **hasIncomingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:89

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdges`](PagNode.md#hasincomingedges)

***

### hasOutgoingCopyEdge()

> **hasOutgoingCopyEdge**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:200

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingCopyEdge`](PagNode.md#hasoutgoingcopyedge)

***

### hasOutgoingEdge()

> **hasOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:101

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdge`](PagNode.md#hasoutgoingedge)

***

### hasOutgoingEdges()

> **hasOutgoingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:93

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdges`](PagNode.md#hasoutgoingedges)

***

### removeIncomingEdge()

> **removeIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:113

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeIncomingEdge`](PagNode.md#removeincomingedge)

***

### removeOutgoingEdge()

> **removeOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:117

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeOutgoingEdge`](PagNode.md#removeoutgoingedge)

***

### setBasePt()

> **setBasePt**(`pt`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:177

#### Parameters

##### pt

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setBasePt`](PagNode.md#setbasept)

***

### setCid()

> **setCid**(`cid`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:188

#### Parameters

##### cid

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setCid`](PagNode.md#setcid)

***

### setClonedFrom()

> **setClonedFrom**(`id`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:327

#### Parameters

##### id

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setClonedFrom`](PagNode.md#setclonedfrom)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:85

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setKind`](PagNode.md#setkind)

***

### setPointTo()

> **setPointTo**(`pts`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:305

#### Parameters

##### pts

`IPtsCollection`\<`number`\>

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setPointTo`](PagNode.md#setpointto)

***

### setStmt()

> **setStmt**(`s`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:192

#### Parameters

##### s

[`Stmt`](Stmt.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setStmt`](PagNode.md#setstmt)




============================================================
## FILE: `classes/PagStaticFieldNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagStaticFieldNode

# Class: PagStaticFieldNode

Defined in: src/callgraph/pointerAnalysis/Pag.ts:456

## Extends

- [`PagNode`](PagNode.md)

## Constructors

### Constructor

> **new PagStaticFieldNode**(`id`, `cid`, `staticFieldRef`, `stmt?`): `PagStaticFieldNode`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:457

#### Parameters

##### id

`number`

##### cid

`undefined` | `number`

##### staticFieldRef

[`ArkStaticFieldRef`](ArkStaticFieldRef.md)

##### stmt?

[`Stmt`](Stmt.md)

#### Returns

`PagStaticFieldNode`

#### Overrides

[`PagNode`](PagNode.md).[`constructor`](PagNode.md#constructor)

## Properties

### basePt

> `protected` **basePt**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:161

#### Inherited from

[`PagNode`](PagNode.md).[`basePt`](PagNode.md#basept)

***

### clonedFrom

> `protected` **clonedFrom**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:162

#### Inherited from

[`PagNode`](PagNode.md).[`clonedFrom`](PagNode.md#clonedfrom)

***

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:68

#### Inherited from

[`PagNode`](PagNode.md).[`kind`](PagNode.md#kind)

## Methods

### addAddressInEdge()

> **addAddressInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:232

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressInEdge`](PagNode.md#addaddressinedge)

***

### addAddressOutEdge()

> **addAddressOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:238

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressOutEdge`](PagNode.md#addaddressoutedge)

***

### addCopyInEdge()

> **addCopyInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:244

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyInEdge`](PagNode.md#addcopyinedge)

***

### addCopyOutEdge()

> **addCopyOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:250

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyOutEdge`](PagNode.md#addcopyoutedge)

***

### addIncomingEdge()

> **addIncomingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:105

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addIncomingEdge`](PagNode.md#addincomingedge)

***

### addLoadInEdge()

> **addLoadInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:257

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadInEdge`](PagNode.md#addloadinedge)

***

### addLoadOutEdge()

> **addLoadOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:263

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadOutEdge`](PagNode.md#addloadoutedge)

***

### addOutgoingEdge()

> **addOutgoingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:109

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addOutgoingEdge`](PagNode.md#addoutgoingedge)

***

### addPointToElement()

> **addPointToElement**(`node`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:301

#### Parameters

##### node

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addPointToElement`](PagNode.md#addpointtoelement)

***

### addThisInEdge()

> **addThisInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:281

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisInEdge`](PagNode.md#addthisinedge)

***

### addThisOutEdge()

> **addThisOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:287

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisOutEdge`](PagNode.md#addthisoutedge)

***

### addWriteInEdge()

> **addWriteInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:269

#### Parameters

##### e

[`WritePagEdge`](WritePagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteInEdge`](PagNode.md#addwriteinedge)

***

### addWriteOutEdge()

> **addWriteOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:275

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteOutEdge`](PagNode.md#addwriteoutedge)

***

### getBasePt()

> **getBasePt**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:173

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getBasePt`](PagNode.md#getbasept)

***

### getCid()

> **getCid**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:181

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getCid`](PagNode.md#getcid)

***

### getClonedFrom()

> **getClonedFrom**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:323

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getClonedFrom`](PagNode.md#getclonedfrom)

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:331

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotAttr`](PagNode.md#getdotattr)

***

### getDotLabel()

> **getDotLabel**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:352

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotLabel`](PagNode.md#getdotlabel)

***

### getID()

> **getID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:77

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getID`](PagNode.md#getid)

***

### getIncomingCopyEdges()

> **getIncomingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:208

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingCopyEdges`](PagNode.md#getincomingcopyedges)

***

### getIncomingEdge()

> **getIncomingEdge**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:121

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingEdge`](PagNode.md#getincomingedge)

***

### getIncomingThisEdges()

> **getIncomingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:228

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingThisEdges`](PagNode.md#getincomingthisedges)

***

### getIncomingWriteEdges()

> **getIncomingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:220

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingWriteEdges`](PagNode.md#getincomingwriteedges)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:81

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getKind`](PagNode.md#getkind)

***

### getOutEdges()

> **getOutEdges**(): `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:309

#### Returns

`object`

##### AddressEdge

> **AddressEdge**: `PagEdgeSet`

##### CopyEdge

> **CopyEdge**: `PagEdgeSet`

##### LoadEdge

> **LoadEdge**: `PagEdgeSet`

##### WriteEdge

> **WriteEdge**: `PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutEdges`](PagNode.md#getoutedges)

***

### getOutgoingCopyEdges()

> **getOutgoingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:204

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingCopyEdges`](PagNode.md#getoutgoingcopyedges)

***

### getOutgoingEdges()

> **getOutgoingEdges**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:125

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingEdges`](PagNode.md#getoutgoingedges)

***

### getOutgoingLoadEdges()

> **getOutgoingLoadEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:212

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingLoadEdges`](PagNode.md#getoutgoingloadedges)

***

### getOutgoingThisEdges()

> **getOutgoingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:224

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingThisEdges`](PagNode.md#getoutgoingthisedges)

***

### getOutgoingWriteEdges()

> **getOutgoingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:216

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingWriteEdges`](PagNode.md#getoutgoingwriteedges)

***

### getPointTo()

> **getPointTo**(): `IPtsCollection`\<`number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:297

#### Returns

`IPtsCollection`\<`number`\>

#### Inherited from

[`PagNode`](PagNode.md).[`getPointTo`](PagNode.md#getpointto)

***

### getStmt()

> **getStmt**(): `undefined` \| [`Stmt`](Stmt.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:196

#### Returns

`undefined` \| [`Stmt`](Stmt.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getStmt`](PagNode.md#getstmt)

***

### getValue()

> **getValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:293

#### Returns

[`Value`](../interfaces/Value.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getValue`](PagNode.md#getvalue)

***

### hasIncomingEdge()

> **hasIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:97

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdge`](PagNode.md#hasincomingedge)

***

### hasIncomingEdges()

> **hasIncomingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:89

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdges`](PagNode.md#hasincomingedges)

***

### hasOutgoingCopyEdge()

> **hasOutgoingCopyEdge**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:200

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingCopyEdge`](PagNode.md#hasoutgoingcopyedge)

***

### hasOutgoingEdge()

> **hasOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:101

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdge`](PagNode.md#hasoutgoingedge)

***

### hasOutgoingEdges()

> **hasOutgoingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:93

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdges`](PagNode.md#hasoutgoingedges)

***

### removeIncomingEdge()

> **removeIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:113

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeIncomingEdge`](PagNode.md#removeincomingedge)

***

### removeOutgoingEdge()

> **removeOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:117

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeOutgoingEdge`](PagNode.md#removeoutgoingedge)

***

### setBasePt()

> **setBasePt**(`pt`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:177

#### Parameters

##### pt

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setBasePt`](PagNode.md#setbasept)

***

### setCid()

> **setCid**(`cid`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:188

#### Parameters

##### cid

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setCid`](PagNode.md#setcid)

***

### setClonedFrom()

> **setClonedFrom**(`id`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:327

#### Parameters

##### id

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setClonedFrom`](PagNode.md#setclonedfrom)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:85

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setKind`](PagNode.md#setkind)

***

### setPointTo()

> **setPointTo**(`pts`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:305

#### Parameters

##### pts

`IPtsCollection`\<`number`\>

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setPointTo`](PagNode.md#setpointto)

***

### setStmt()

> **setStmt**(`s`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:192

#### Parameters

##### s

[`Stmt`](Stmt.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setStmt`](PagNode.md#setstmt)




============================================================
## FILE: `classes/PagThisRefNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagThisRefNode

# Class: PagThisRefNode

Defined in: src/callgraph/pointerAnalysis/Pag.ts:462

## Extends

- [`PagNode`](PagNode.md)

## Constructors

### Constructor

> **new PagThisRefNode**(`id`, `thisRef`): `PagThisRefNode`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:464

#### Parameters

##### id

`number`

##### thisRef

[`ArkThisRef`](ArkThisRef.md)

#### Returns

`PagThisRefNode`

#### Overrides

[`PagNode`](PagNode.md).[`constructor`](PagNode.md#constructor)

## Properties

### basePt

> `protected` **basePt**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:161

#### Inherited from

[`PagNode`](PagNode.md).[`basePt`](PagNode.md#basept)

***

### clonedFrom

> `protected` **clonedFrom**: `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:162

#### Inherited from

[`PagNode`](PagNode.md).[`clonedFrom`](PagNode.md#clonedfrom)

***

### kind

> `protected` **kind**: `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:68

#### Inherited from

[`PagNode`](PagNode.md).[`kind`](PagNode.md#kind)

***

### pointToNode

> **pointToNode**: `number`[]

Defined in: src/callgraph/pointerAnalysis/Pag.ts:463

## Methods

### addAddressInEdge()

> **addAddressInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:232

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressInEdge`](PagNode.md#addaddressinedge)

***

### addAddressOutEdge()

> **addAddressOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:238

#### Parameters

##### e

[`AddrPagEdge`](AddrPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addAddressOutEdge`](PagNode.md#addaddressoutedge)

***

### addCopyInEdge()

> **addCopyInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:244

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyInEdge`](PagNode.md#addcopyinedge)

***

### addCopyOutEdge()

> **addCopyOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:250

#### Parameters

##### e

[`CopyPagEdge`](CopyPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addCopyOutEdge`](PagNode.md#addcopyoutedge)

***

### addIncomingEdge()

> **addIncomingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:105

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addIncomingEdge`](PagNode.md#addincomingedge)

***

### addLoadInEdge()

> **addLoadInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:257

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadInEdge`](PagNode.md#addloadinedge)

***

### addLoadOutEdge()

> **addLoadOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:263

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addLoadOutEdge`](PagNode.md#addloadoutedge)

***

### addOutgoingEdge()

> **addOutgoingEdge**(`e`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:109

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addOutgoingEdge`](PagNode.md#addoutgoingedge)

***

### addPointToElement()

> **addPointToElement**(`node`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:301

#### Parameters

##### node

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addPointToElement`](PagNode.md#addpointtoelement)

***

### addPTNode()

> **addPTNode**(`ptNode`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:473

#### Parameters

##### ptNode

`number`

#### Returns

`void`

***

### addThisInEdge()

> **addThisInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:281

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisInEdge`](PagNode.md#addthisinedge)

***

### addThisOutEdge()

> **addThisOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:287

#### Parameters

##### e

[`ThisPagEdge`](ThisPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addThisOutEdge`](PagNode.md#addthisoutedge)

***

### addWriteInEdge()

> **addWriteInEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:269

#### Parameters

##### e

[`WritePagEdge`](WritePagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteInEdge`](PagNode.md#addwriteinedge)

***

### addWriteOutEdge()

> **addWriteOutEdge**(`e`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:275

#### Parameters

##### e

[`LoadPagEdge`](LoadPagEdge.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`addWriteOutEdge`](PagNode.md#addwriteoutedge)

***

### getBasePt()

> **getBasePt**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:173

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getBasePt`](PagNode.md#getbasept)

***

### getCid()

> **getCid**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:181

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getCid`](PagNode.md#getcid)

***

### getClonedFrom()

> **getClonedFrom**(): `number`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:323

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getClonedFrom`](PagNode.md#getclonedfrom)

***

### getDotAttr()

> **getDotAttr**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:331

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotAttr`](PagNode.md#getdotattr)

***

### getDotLabel()

> **getDotLabel**(): `string`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:352

#### Returns

`string`

#### Inherited from

[`PagNode`](PagNode.md).[`getDotLabel`](PagNode.md#getdotlabel)

***

### getID()

> **getID**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:77

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getID`](PagNode.md#getid)

***

### getIncomingCopyEdges()

> **getIncomingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:208

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingCopyEdges`](PagNode.md#getincomingcopyedges)

***

### getIncomingEdge()

> **getIncomingEdge**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:121

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingEdge`](PagNode.md#getincomingedge)

***

### getIncomingThisEdges()

> **getIncomingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:228

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingThisEdges`](PagNode.md#getincomingthisedges)

***

### getIncomingWriteEdges()

> **getIncomingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:220

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getIncomingWriteEdges`](PagNode.md#getincomingwriteedges)

***

### getKind()

> **getKind**(): `number`

Defined in: src/core/graph/BaseExplicitGraph.ts:81

#### Returns

`number`

#### Inherited from

[`PagNode`](PagNode.md).[`getKind`](PagNode.md#getkind)

***

### getOutEdges()

> **getOutEdges**(): `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:309

#### Returns

`object`

##### AddressEdge

> **AddressEdge**: `PagEdgeSet`

##### CopyEdge

> **CopyEdge**: `PagEdgeSet`

##### LoadEdge

> **LoadEdge**: `PagEdgeSet`

##### WriteEdge

> **WriteEdge**: `PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutEdges`](PagNode.md#getoutedges)

***

### getOutgoingCopyEdges()

> **getOutgoingCopyEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:204

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingCopyEdges`](PagNode.md#getoutgoingcopyedges)

***

### getOutgoingEdges()

> **getOutgoingEdges**(): `Set`\<[`BaseEdge`](BaseEdge.md)\>

Defined in: src/core/graph/BaseExplicitGraph.ts:125

#### Returns

`Set`\<[`BaseEdge`](BaseEdge.md)\>

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingEdges`](PagNode.md#getoutgoingedges)

***

### getOutgoingLoadEdges()

> **getOutgoingLoadEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:212

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingLoadEdges`](PagNode.md#getoutgoingloadedges)

***

### getOutgoingThisEdges()

> **getOutgoingThisEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:224

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingThisEdges`](PagNode.md#getoutgoingthisedges)

***

### getOutgoingWriteEdges()

> **getOutgoingWriteEdges**(): `PagEdgeSet`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:216

#### Returns

`PagEdgeSet`

#### Inherited from

[`PagNode`](PagNode.md).[`getOutgoingWriteEdges`](PagNode.md#getoutgoingwriteedges)

***

### getPointTo()

> **getPointTo**(): `IPtsCollection`\<`number`\>

Defined in: src/callgraph/pointerAnalysis/Pag.ts:297

#### Returns

`IPtsCollection`\<`number`\>

#### Inherited from

[`PagNode`](PagNode.md).[`getPointTo`](PagNode.md#getpointto)

***

### getStmt()

> **getStmt**(): `undefined` \| [`Stmt`](Stmt.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:196

#### Returns

`undefined` \| [`Stmt`](Stmt.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getStmt`](PagNode.md#getstmt)

***

### getThisPTNode()

> **getThisPTNode**(): `number`[]

Defined in: src/callgraph/pointerAnalysis/Pag.ts:469

#### Returns

`number`[]

***

### getValue()

> **getValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:293

#### Returns

[`Value`](../interfaces/Value.md)

#### Inherited from

[`PagNode`](PagNode.md).[`getValue`](PagNode.md#getvalue)

***

### hasIncomingEdge()

> **hasIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:97

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdge`](PagNode.md#hasincomingedge)

***

### hasIncomingEdges()

> **hasIncomingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:89

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasIncomingEdges`](PagNode.md#hasincomingedges)

***

### hasOutgoingCopyEdge()

> **hasOutgoingCopyEdge**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:200

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingCopyEdge`](PagNode.md#hasoutgoingcopyedge)

***

### hasOutgoingEdge()

> **hasOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:101

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdge`](PagNode.md#hasoutgoingedge)

***

### hasOutgoingEdges()

> **hasOutgoingEdges**(): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:93

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`hasOutgoingEdges`](PagNode.md#hasoutgoingedges)

***

### removeIncomingEdge()

> **removeIncomingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:113

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeIncomingEdge`](PagNode.md#removeincomingedge)

***

### removeOutgoingEdge()

> **removeOutgoingEdge**(`e`): `boolean`

Defined in: src/core/graph/BaseExplicitGraph.ts:117

#### Parameters

##### e

[`BaseEdge`](BaseEdge.md)

#### Returns

`boolean`

#### Inherited from

[`PagNode`](PagNode.md).[`removeOutgoingEdge`](PagNode.md#removeoutgoingedge)

***

### setBasePt()

> **setBasePt**(`pt`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:177

#### Parameters

##### pt

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setBasePt`](PagNode.md#setbasept)

***

### setCid()

> **setCid**(`cid`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:188

#### Parameters

##### cid

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setCid`](PagNode.md#setcid)

***

### setClonedFrom()

> **setClonedFrom**(`id`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:327

#### Parameters

##### id

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setClonedFrom`](PagNode.md#setclonedfrom)

***

### setKind()

> **setKind**(`kind`): `void`

Defined in: src/core/graph/BaseExplicitGraph.ts:85

#### Parameters

##### kind

`number`

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setKind`](PagNode.md#setkind)

***

### setPointTo()

> **setPointTo**(`pts`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:305

#### Parameters

##### pts

`IPtsCollection`\<`number`\>

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setPointTo`](PagNode.md#setpointto)

***

### setStmt()

> **setStmt**(`s`): `void`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:192

#### Parameters

##### s

[`Stmt`](Stmt.md)

#### Returns

`void`

#### Inherited from

[`PagNode`](PagNode.md).[`setStmt`](PagNode.md#setstmt)




============================================================
## FILE: `classes/PathEdge.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PathEdge

# Class: PathEdge\<D\>

Defined in: src/core/dataflow/Edge.ts:28

## Type Parameters

### D

`D`

## Constructors

### Constructor

> **new PathEdge**\<`D`\>(`start`, `end`): `PathEdge`\<`D`\>

Defined in: src/core/dataflow/Edge.ts:32

#### Parameters

##### start

[`PathEdgePoint`](PathEdgePoint.md)\<`D`\>

##### end

[`PathEdgePoint`](PathEdgePoint.md)\<`D`\>

#### Returns

`PathEdge`\<`D`\>

## Properties

### edgeEnd

> **edgeEnd**: [`PathEdgePoint`](PathEdgePoint.md)\<`D`\>

Defined in: src/core/dataflow/Edge.ts:30

***

### edgeStart

> **edgeStart**: [`PathEdgePoint`](PathEdgePoint.md)\<`D`\>

Defined in: src/core/dataflow/Edge.ts:29




============================================================
## FILE: `classes/PathEdgePoint.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PathEdgePoint

# Class: PathEdgePoint\<D\>

Defined in: src/core/dataflow/Edge.ts:18

## Type Parameters

### D

`D`

## Constructors

### Constructor

> **new PathEdgePoint**\<`D`\>(`node`, `fact`): `PathEdgePoint`\<`D`\>

Defined in: src/core/dataflow/Edge.ts:22

#### Parameters

##### node

[`Stmt`](Stmt.md)

##### fact

`D`

#### Returns

`PathEdgePoint`\<`D`\>

## Properties

### fact

> **fact**: `D`

Defined in: src/core/dataflow/Edge.ts:20

***

### node

> **node**: [`Stmt`](Stmt.md)

Defined in: src/core/dataflow/Edge.ts:19



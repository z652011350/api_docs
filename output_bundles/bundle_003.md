

============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ConditionalTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ConditionalTypeNode

# Interface: ConditionalTypeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1000

## Extends

- [`TypeNode`](TypeNode.md)

## Properties

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`TypeNode`](TypeNode.md).[`_typeNodeBrand`](TypeNode.md#_typenodebrand)

***

### checkType

> `readonly` **checkType**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1002

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

### extendsType

> `readonly` **extendsType**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1003

***

### falseType

> `readonly` **falseType**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1005

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`TypeNode`](TypeNode.md).[`flags`](TypeNode.md#flags)

***

### kind

> `readonly` **kind**: [`ConditionalType`](../enumerations/SyntaxKind.md#conditionaltype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1001

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

### trueType

> `readonly` **trueType**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1004

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ConfigFileDiagnosticsReporter.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ConfigFileDiagnosticsReporter

# Interface: ConfigFileDiagnosticsReporter

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5263

Reports config file diagnostics

## Extended by

- [`ParseConfigFileHost`](ParseConfigFileHost.md)
- [`WatchCompilerHostOfConfigFile`](WatchCompilerHostOfConfigFile.md)

## Properties

### onUnRecoverableConfigFileDiagnostic

> **onUnRecoverableConfigFileDiagnostic**: [`DiagnosticReporter`](../type-aliases/DiagnosticReporter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5267

Reports unrecoverable error when parsing config file




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ConstructSignatureDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ConstructSignatureDeclaration

# Interface: ConstructSignatureDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:742

## Extends

- [`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`TypeElement`](TypeElement.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`TypeElement`](TypeElement.md).[`_declarationBrand`](TypeElement.md#_declarationbrand)

***

### \_typeElementBrand

> **\_typeElementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1637

#### Inherited from

[`TypeElement`](TypeElement.md).[`_typeElementBrand`](TypeElement.md#_typeelementbrand)

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

[`TypeElement`](TypeElement.md).[`decorators`](TypeElement.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`TypeElement`](TypeElement.md).[`end`](TypeElement.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`TypeElement`](TypeElement.md).[`flags`](TypeElement.md#flags)

***

### kind

> `readonly` **kind**: [`ConstructSignature`](../enumerations/SyntaxKind.md#constructsignature)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:743

#### Overrides

[`TypeElement`](TypeElement.md).[`kind`](TypeElement.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`TypeElement`](TypeElement.md).[`locals`](TypeElement.md#locals)

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

[`TypeElement`](TypeElement.md).[`modifiers`](TypeElement.md#modifiers)

***

### name?

> `readonly` `optional` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:733

#### Inherited from

[`TypeElement`](TypeElement.md).[`name`](TypeElement.md#name)

***

### parameters

> `readonly` **parameters**: [`NodeArray`](NodeArray.md)\<[`ParameterDeclaration`](ParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:735

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`parameters`](SignatureDeclarationBase.md#parameters)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`TypeElement`](TypeElement.md).[`parent`](TypeElement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`TypeElement`](TypeElement.md).[`pos`](TypeElement.md#pos)

***

### questionToken?

> `readonly` `optional` **questionToken**: [`QuestionToken`](../type-aliases/QuestionToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1639

#### Inherited from

[`TypeElement`](TypeElement.md).[`questionToken`](TypeElement.md#questiontoken)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`TypeElement`](TypeElement.md).[`skipCheck`](TypeElement.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`TypeElement`](TypeElement.md).[`symbol`](TypeElement.md#symbol)

***

### type?

> `readonly` `optional` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:736

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`type`](SignatureDeclarationBase.md#type)

***

### typeParameters?

> `readonly` `optional` **typeParameters**: [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:734

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`typeParameters`](SignatureDeclarationBase.md#typeparameters)

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

[`TypeElement`](TypeElement.md).[`forEachChild`](TypeElement.md#foreachchild)

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

[`TypeElement`](TypeElement.md).[`getChildAt`](TypeElement.md#getchildat)

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

[`TypeElement`](TypeElement.md).[`getChildCount`](TypeElement.md#getchildcount)

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

[`TypeElement`](TypeElement.md).[`getChildren`](TypeElement.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`TypeElement`](TypeElement.md).[`getEnd`](TypeElement.md#getend)

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

[`TypeElement`](TypeElement.md).[`getFirstToken`](TypeElement.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`TypeElement`](TypeElement.md).[`getFullStart`](TypeElement.md#getfullstart)

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

[`TypeElement`](TypeElement.md).[`getFullText`](TypeElement.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`TypeElement`](TypeElement.md).[`getFullWidth`](TypeElement.md#getfullwidth)

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

[`TypeElement`](TypeElement.md).[`getLastToken`](TypeElement.md#getlasttoken)

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

[`TypeElement`](TypeElement.md).[`getLeadingTriviaWidth`](TypeElement.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`TypeElement`](TypeElement.md).[`getSourceFile`](TypeElement.md#getsourcefile)

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

[`TypeElement`](TypeElement.md).[`getStart`](TypeElement.md#getstart)

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

[`TypeElement`](TypeElement.md).[`getText`](TypeElement.md#gettext)

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

[`TypeElement`](TypeElement.md).[`getWidth`](TypeElement.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ConstructorDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ConstructorDeclaration

# Interface: ConstructorDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:874

Several node kinds share function-like features such as a signature,
a name, and a body. These nodes should extend FunctionLikeDeclarationBase.
Examples:
- FunctionDeclaration
- MethodDeclaration
- AccessorDeclaration

## Extends

- [`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`ClassElement`](ClassElement.md).[`JSDocContainer`](JSDocContainer.md)

## Properties

### \_classElementBrand

> **\_classElementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1633

#### Inherited from

[`ClassElement`](ClassElement.md).[`_classElementBrand`](ClassElement.md#_classelementbrand)

***

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`ClassElement`](ClassElement.md).[`_declarationBrand`](ClassElement.md#_declarationbrand)

***

### \_functionLikeDeclarationBrand

> **\_functionLikeDeclarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:846

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`_functionLikeDeclarationBrand`](FunctionLikeDeclarationBase.md#_functionlikedeclarationbrand)

***

### asteriskToken?

> `readonly` `optional` **asteriskToken**: [`AsteriskToken`](../type-aliases/AsteriskToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:847

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`asteriskToken`](FunctionLikeDeclarationBase.md#asterisktoken)

***

### body?

> `readonly` `optional` **body**: [`Block`](Block.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:878

#### Overrides

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`body`](FunctionLikeDeclarationBase.md#body)

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

[`ClassElement`](ClassElement.md).[`decorators`](ClassElement.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`ClassElement`](ClassElement.md).[`end`](ClassElement.md#end)

***

### exclamationToken?

> `readonly` `optional` **exclamationToken**: [`ExclamationToken`](../type-aliases/ExclamationToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:849

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`exclamationToken`](FunctionLikeDeclarationBase.md#exclamationtoken)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`ClassElement`](ClassElement.md).[`flags`](ClassElement.md#flags)

***

### kind

> `readonly` **kind**: [`Constructor`](../enumerations/SyntaxKind.md#constructor)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:875

#### Overrides

[`ClassElement`](ClassElement.md).[`kind`](ClassElement.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`ClassElement`](ClassElement.md).[`locals`](ClassElement.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`Modifier`](../type-aliases/Modifier.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:877

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Overrides

[`ClassElement`](ClassElement.md).[`modifiers`](ClassElement.md#modifiers)

***

### name?

> `readonly` `optional` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:733

#### Inherited from

[`ClassElement`](ClassElement.md).[`name`](ClassElement.md#name)

***

### parameters

> `readonly` **parameters**: [`NodeArray`](NodeArray.md)\<[`ParameterDeclaration`](ParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:735

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`parameters`](FunctionLikeDeclarationBase.md#parameters)

***

### parent

> `readonly` **parent**: [`ClassLikeDeclaration`](../type-aliases/ClassLikeDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:876

#### Overrides

[`ClassElement`](ClassElement.md).[`parent`](ClassElement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`ClassElement`](ClassElement.md).[`pos`](ClassElement.md#pos)

***

### questionToken?

> `readonly` `optional` **questionToken**: [`QuestionToken`](../type-aliases/QuestionToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:848

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`questionToken`](FunctionLikeDeclarationBase.md#questiontoken)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`ClassElement`](ClassElement.md).[`skipCheck`](ClassElement.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`ClassElement`](ClassElement.md).[`symbol`](ClassElement.md#symbol)

***

### type?

> `readonly` `optional` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:736

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`type`](FunctionLikeDeclarationBase.md#type)

***

### typeParameters?

> `readonly` `optional` **typeParameters**: [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:734

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`typeParameters`](FunctionLikeDeclarationBase.md#typeparameters)

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

[`ClassElement`](ClassElement.md).[`forEachChild`](ClassElement.md#foreachchild)

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

[`ClassElement`](ClassElement.md).[`getChildAt`](ClassElement.md#getchildat)

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

[`ClassElement`](ClassElement.md).[`getChildCount`](ClassElement.md#getchildcount)

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

[`ClassElement`](ClassElement.md).[`getChildren`](ClassElement.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`ClassElement`](ClassElement.md).[`getEnd`](ClassElement.md#getend)

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

[`ClassElement`](ClassElement.md).[`getFirstToken`](ClassElement.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`ClassElement`](ClassElement.md).[`getFullStart`](ClassElement.md#getfullstart)

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

[`ClassElement`](ClassElement.md).[`getFullText`](ClassElement.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`ClassElement`](ClassElement.md).[`getFullWidth`](ClassElement.md#getfullwidth)

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

[`ClassElement`](ClassElement.md).[`getLastToken`](ClassElement.md#getlasttoken)

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

[`ClassElement`](ClassElement.md).[`getLeadingTriviaWidth`](ClassElement.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`ClassElement`](ClassElement.md).[`getSourceFile`](ClassElement.md#getsourcefile)

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

[`ClassElement`](ClassElement.md).[`getStart`](ClassElement.md#getstart)

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

[`ClassElement`](ClassElement.md).[`getText`](ClassElement.md#gettext)

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

[`ClassElement`](ClassElement.md).[`getWidth`](ClassElement.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ConstructorTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ConstructorTypeNode

# Interface: ConstructorTypeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:941

## Extends

- [`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`_declarationBrand`](FunctionOrConstructorTypeNodeBase.md#_declarationbrand)

***

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`_typeNodeBrand`](FunctionOrConstructorTypeNodeBase.md#_typenodebrand)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`decorators`](FunctionOrConstructorTypeNodeBase.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`end`](FunctionOrConstructorTypeNodeBase.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`flags`](FunctionOrConstructorTypeNodeBase.md#flags)

***

### kind

> `readonly` **kind**: [`ConstructorType`](../enumerations/SyntaxKind.md#constructortype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:942

#### Overrides

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`kind`](FunctionOrConstructorTypeNodeBase.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`locals`](FunctionOrConstructorTypeNodeBase.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`Modifier`](../type-aliases/Modifier.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:943

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Overrides

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`modifiers`](FunctionOrConstructorTypeNodeBase.md#modifiers)

***

### name?

> `readonly` `optional` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:733

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`name`](FunctionOrConstructorTypeNodeBase.md#name)

***

### parameters

> `readonly` **parameters**: [`NodeArray`](NodeArray.md)\<[`ParameterDeclaration`](ParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:735

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`parameters`](FunctionOrConstructorTypeNodeBase.md#parameters)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`parent`](FunctionOrConstructorTypeNodeBase.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`pos`](FunctionOrConstructorTypeNodeBase.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`skipCheck`](FunctionOrConstructorTypeNodeBase.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`symbol`](FunctionOrConstructorTypeNodeBase.md#symbol)

***

### type

> `readonly` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:936

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`type`](FunctionOrConstructorTypeNodeBase.md#type)

***

### typeParameters?

> `readonly` `optional` **typeParameters**: [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:734

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`typeParameters`](FunctionOrConstructorTypeNodeBase.md#typeparameters)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`forEachChild`](FunctionOrConstructorTypeNodeBase.md#foreachchild)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getChildAt`](FunctionOrConstructorTypeNodeBase.md#getchildat)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getChildCount`](FunctionOrConstructorTypeNodeBase.md#getchildcount)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getChildren`](FunctionOrConstructorTypeNodeBase.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getEnd`](FunctionOrConstructorTypeNodeBase.md#getend)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getFirstToken`](FunctionOrConstructorTypeNodeBase.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getFullStart`](FunctionOrConstructorTypeNodeBase.md#getfullstart)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getFullText`](FunctionOrConstructorTypeNodeBase.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getFullWidth`](FunctionOrConstructorTypeNodeBase.md#getfullwidth)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getLastToken`](FunctionOrConstructorTypeNodeBase.md#getlasttoken)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getLeadingTriviaWidth`](FunctionOrConstructorTypeNodeBase.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getSourceFile`](FunctionOrConstructorTypeNodeBase.md#getsourcefile)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getStart`](FunctionOrConstructorTypeNodeBase.md#getstart)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getText`](FunctionOrConstructorTypeNodeBase.md#gettext)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getWidth`](FunctionOrConstructorTypeNodeBase.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ContinueStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ContinueStatement

# Interface: ContinueStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1547

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

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Statement`](Statement.md).[`flags`](Statement.md#flags)

***

### kind

> `readonly` **kind**: [`ContinueStatement`](../enumerations/SyntaxKind.md#continuestatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1548

#### Overrides

[`Statement`](Statement.md).[`kind`](Statement.md#kind)

***

### label?

> `readonly` `optional` **label**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1549

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/CoreTransformationContext.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / CoreTransformationContext

# Interface: CoreTransformationContext

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4078

## Extended by

- [`TransformationContext`](TransformationContext.md)

## Properties

### factory

> `readonly` **factory**: [`NodeFactory`](NodeFactory.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4079

## Methods

### endLexicalEnvironment()

> **endLexicalEnvironment**(): `undefined` \| [`Statement`](Statement.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4089

Ends a lexical environment, returning any declarations.

#### Returns

`undefined` \| [`Statement`](Statement.md)[]

***

### getCompilerOptions()

> **getCompilerOptions**(): [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4081

Gets the compiler options supplied to the transformer.

#### Returns

[`CompilerOptions`](CompilerOptions.md)

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

***

### resumeLexicalEnvironment()

> **resumeLexicalEnvironment**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4087

Resumes a suspended lexical environment, usually before visiting a function body.

#### Returns

`void`

***

### startLexicalEnvironment()

> **startLexicalEnvironment**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4083

Starts a new lexical environment.

#### Returns

`void`

***

### suspendLexicalEnvironment()

> **suspendLexicalEnvironment**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4085

Suspends the current lexical environment, usually after visiting a parameter list.

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/CreateProgramOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / CreateProgramOptions

# Interface: CreateProgramOptions

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3331

## Properties

### configFileParsingDiagnostics?

> `optional` **configFileParsingDiagnostics**: readonly [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3337

***

### host?

> `optional` **host**: [`CompilerHost`](CompilerHost.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3335

***

### oldProgram?

> `optional` **oldProgram**: [`Program`](Program.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3336

***

### options

> **options**: [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3333

***

### projectReferences?

> `optional` **projectReferences**: readonly [`ProjectReference`](ProjectReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3334

***

### rootNames

> **rootNames**: readonly `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3332




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/CreateSourceFileOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / CreateSourceFileOptions

# Interface: CreateSourceFileOptions

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5230

## Properties

### impliedNodeFormat?

> `optional` **impliedNodeFormat**: [`CommonJS`](../enumerations/ModuleKind.md#commonjs) \| [`ESNext`](../enumerations/ModuleKind.md#esnext)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5237

Controls the format the file is detected as - this can be derived from only the path
and files on disk, but needs to be done with a module resolution cache in scope to be performant.
This is usually `undefined` for compilations that do not have `moduleResolution` values of `node16` or `nodenext`.

***

### languageVersion

> **languageVersion**: [`ScriptTarget`](../enumerations/ScriptTarget.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5231

***

### setExternalModuleIndicator()?

> `optional` **setExternalModuleIndicator**: (`file`) => `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5243

Controls how module-y-ness is set for the given file. Usually the result of calling
`getSetExternalModuleIndicator` on a valid `CompilerOptions` object. If not present, the default
check specified by `isFileProbablyExternalModule` will be used to set the field.

#### Parameters

##### file

[`SourceFile`](SourceFile.md)

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/CustomTransformer.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / CustomTransformer

# Interface: CustomTransformer

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2342

## Methods

### transformBundle()

> **transformBundle**(`node`): [`Bundle`](Bundle.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2344

#### Parameters

##### node

[`Bundle`](Bundle.md)

#### Returns

[`Bundle`](Bundle.md)

***

### transformSourceFile()

> **transformSourceFile**(`node`): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2343

#### Parameters

##### node

[`SourceFile`](SourceFile.md)

#### Returns

[`SourceFile`](SourceFile.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/CustomTransformers.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / CustomTransformers

# Interface: CustomTransformers

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2346

## Properties

### after?

> `optional` **after**: ([`CustomTransformerFactory`](../type-aliases/CustomTransformerFactory.md) \| [`TransformerFactory`](../type-aliases/TransformerFactory.md)\<[`SourceFile`](SourceFile.md)\>)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2350

Custom transformers to evaluate after built-in .js transformations.

***

### afterDeclarations?

> `optional` **afterDeclarations**: ([`CustomTransformerFactory`](../type-aliases/CustomTransformerFactory.md) \| [`TransformerFactory`](../type-aliases/TransformerFactory.md)\<[`SourceFile`](SourceFile.md) \| [`Bundle`](Bundle.md)\>)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2352

Custom transformers to evaluate after built-in .d.ts transformations.

***

### before?

> `optional` **before**: ([`CustomTransformerFactory`](../type-aliases/CustomTransformerFactory.md) \| [`TransformerFactory`](../type-aliases/TransformerFactory.md)\<[`SourceFile`](SourceFile.md)\>)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2348

Custom transformers to evaluate before built-in .js transformations.




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DebuggerStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DebuggerStatement

# Interface: DebuggerStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1486

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

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Statement`](Statement.md).[`flags`](Statement.md#flags)

***

### kind

> `readonly` **kind**: [`DebuggerStatement`](../enumerations/SyntaxKind.md#debuggerstatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1487

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Declaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Declaration

# Interface: Declaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:698

## Extends

- [`Node`](Node.md)

## Extended by

- [`Identifier`](Identifier.md)
- [`NamedDeclaration`](NamedDeclaration.md)
- [`TypeLiteralNode`](TypeLiteralNode.md)
- [`NamedTupleMember`](NamedTupleMember.md)
- [`MappedTypeNode`](MappedTypeNode.md)
- [`StringLiteral`](StringLiteral.md)
- [`BinaryExpression`](BinaryExpression.md)
- [`EtsComponentExpression`](EtsComponentExpression.md)
- [`NoSubstitutionTemplateLiteral`](NoSubstitutionTemplateLiteral.md)
- [`NumericLiteral`](NumericLiteral.md)
- [`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md)
- [`CallExpression`](CallExpression.md)
- [`NewExpression`](NewExpression.md)
- [`JSDocEnumTag`](JSDocEnumTag.md)
- [`JSDocSignature`](JSDocSignature.md)
- [`JSDocPropertyLikeTag`](JSDocPropertyLikeTag.md)
- [`SourceFile`](SourceFile.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DeclarationStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DeclarationStatement

# Interface: DeclarationStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:704

## Extends

- [`NamedDeclaration`](NamedDeclaration.md).[`Statement`](Statement.md)

## Extended by

- [`FunctionDeclaration`](FunctionDeclaration.md)
- [`MissingDeclaration`](MissingDeclaration.md)
- [`ClassDeclaration`](ClassDeclaration.md)
- [`StructDeclaration`](StructDeclaration.md)
- [`InterfaceDeclaration`](InterfaceDeclaration.md)
- [`TypeAliasDeclaration`](TypeAliasDeclaration.md)
- [`EnumDeclaration`](EnumDeclaration.md)
- [`ModuleDeclaration`](ModuleDeclaration.md)
- [`ImportEqualsDeclaration`](ImportEqualsDeclaration.md)
- [`NamespaceExportDeclaration`](NamespaceExportDeclaration.md)
- [`ExportDeclaration`](ExportDeclaration.md)
- [`ExportAssignment`](ExportAssignment.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`_declarationBrand`](NamedDeclaration.md#_declarationbrand)

***

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

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Statement`](Statement.md).[`flags`](Statement.md#flags)

***

### kind

> `readonly` **kind**: [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:598

#### Inherited from

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

### name?

> `readonly` `optional` **name**: [`Identifier`](Identifier.md) \| [`StringLiteral`](StringLiteral.md) \| [`NumericLiteral`](NumericLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:705

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`name`](NamedDeclaration.md#name)

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Decorator.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Decorator

# Interface: Decorator

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:716

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

> `readonly` **expression**: [`LeftHandSideExpression`](LeftHandSideExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:719

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Node`](Node.md).[`flags`](Node.md#flags)

***

### kind

> `readonly` **kind**: [`Decorator`](../enumerations/SyntaxKind.md#decorator)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:717

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

> `readonly` **parent**: [`NamedDeclaration`](NamedDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:718

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DefaultClause.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DefaultClause

# Interface: DefaultClause

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1578

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

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Node`](Node.md).[`flags`](Node.md#flags)

***

### kind

> `readonly` **kind**: [`DefaultClause`](../enumerations/SyntaxKind.md#defaultclause)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1579

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

> `readonly` **parent**: [`CaseBlock`](CaseBlock.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1580

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

### statements

> `readonly` **statements**: [`NodeArray`](NodeArray.md)\<[`Statement`](Statement.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1581

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DeferredTypeReference.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DeferredTypeReference

# Interface: DeferredTypeReference

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2848

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

> **target**: [`GenericType`](GenericType.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2845

#### Inherited from

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DefinitionInfo.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DefinitionInfo

# Interface: DefinitionInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6821

## Extends

- [`DocumentSpan`](DocumentSpan.md)

## Extended by

- [`ReferencedSymbolDefinitionInfo`](ReferencedSymbolDefinitionInfo.md)

## Properties

### containerKind

> **containerKind**: [`ScriptElementKind`](../enumerations/ScriptElementKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6824

***

### containerName

> **containerName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6825

***

### contextSpan?

> `optional` **contextSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6713

If DocumentSpan.textSpan is the span for name of the declaration,
then this is the span for relevant declaration

#### Inherited from

[`DocumentSpan`](DocumentSpan.md).[`contextSpan`](DocumentSpan.md#contextspan)

***

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6702

#### Inherited from

[`DocumentSpan`](DocumentSpan.md).[`fileName`](DocumentSpan.md#filename)

***

### kind

> **kind**: [`ScriptElementKind`](../enumerations/ScriptElementKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6822

***

### name

> **name**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6823

***

### originalContextSpan?

> `optional` **originalContextSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6714

#### Inherited from

[`DocumentSpan`](DocumentSpan.md).[`originalContextSpan`](DocumentSpan.md#originalcontextspan)

***

### originalFileName?

> `optional` **originalFileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6708

#### Inherited from

[`DocumentSpan`](DocumentSpan.md).[`originalFileName`](DocumentSpan.md#originalfilename)

***

### originalTextSpan?

> `optional` **originalTextSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6707

If the span represents a location that was remapped (e.g. via a .d.ts.map file),
then the original filename and span will be specified here

#### Inherited from

[`DocumentSpan`](DocumentSpan.md).[`originalTextSpan`](DocumentSpan.md#originaltextspan)

***

### textSpan

> **textSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6701

#### Inherited from

[`DocumentSpan`](DocumentSpan.md).[`textSpan`](DocumentSpan.md#textspan)

***

### unverified?

> `optional` **unverified**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6826




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DefinitionInfoAndBoundSpan.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DefinitionInfoAndBoundSpan

# Interface: DefinitionInfoAndBoundSpan

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6828

## Properties

### definitions?

> `optional` **definitions**: readonly [`DefinitionInfo`](DefinitionInfo.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6829

***

### textSpan

> **textSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6830




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DeleteExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DeleteExpression

# Interface: DeleteExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1113

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1115

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`flags`](UnaryExpression.md#flags)

***

### kind

> `readonly` **kind**: [`DeleteExpression`](../enumerations/SyntaxKind.md#deleteexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1114

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




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Diagnostic.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Diagnostic

# Interface: Diagnostic

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2994

## Extends

- [`DiagnosticRelatedInformation`](DiagnosticRelatedInformation.md)

## Extended by

- [`DiagnosticWithLocation`](DiagnosticWithLocation.md)

## Properties

### category

> **category**: [`DiagnosticCategory`](../enumerations/DiagnosticCategory.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3002

#### Inherited from

[`DiagnosticRelatedInformation`](DiagnosticRelatedInformation.md).[`category`](DiagnosticRelatedInformation.md#category)

***

### code

> **code**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3003

#### Inherited from

[`DiagnosticRelatedInformation`](DiagnosticRelatedInformation.md).[`code`](DiagnosticRelatedInformation.md#code)

***

### file

> **file**: `undefined` \| [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3004

#### Inherited from

[`DiagnosticRelatedInformation`](DiagnosticRelatedInformation.md).[`file`](DiagnosticRelatedInformation.md#file)

***

### length

> **length**: `undefined` \| `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3006

#### Inherited from

[`DiagnosticRelatedInformation`](DiagnosticRelatedInformation.md).[`length`](DiagnosticRelatedInformation.md#length)

***

### messageText

> **messageText**: `string` \| [`DiagnosticMessageChain`](DiagnosticMessageChain.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3007

#### Inherited from

[`DiagnosticRelatedInformation`](DiagnosticRelatedInformation.md).[`messageText`](DiagnosticRelatedInformation.md#messagetext)

***

### relatedInformation?

> `optional` **relatedInformation**: [`DiagnosticRelatedInformation`](DiagnosticRelatedInformation.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2999

***

### reportsDeprecated?

> `optional` **reportsDeprecated**: `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2997

***

### reportsUnnecessary?

> `optional` **reportsUnnecessary**: `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2996

May store more in future. For now, this will simply be `true` to indicate when a diagnostic is an unused-identifier diagnostic.

***

### source?

> `optional` **source**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2998

***

### start

> **start**: `undefined` \| `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3005

#### Inherited from

[`DiagnosticRelatedInformation`](DiagnosticRelatedInformation.md).[`start`](DiagnosticRelatedInformation.md#start)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DiagnosticMessage.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DiagnosticMessage

# Interface: DiagnosticMessage

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2974

## Properties

### category

> **category**: [`DiagnosticCategory`](../enumerations/DiagnosticCategory.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2976

***

### code

> **code**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2977

***

### key

> **key**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2975

***

### message

> **message**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2978

***

### reportsDeprecated?

> `optional` **reportsDeprecated**: `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2980

***

### reportsUnnecessary?

> `optional` **reportsUnnecessary**: `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2979




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DiagnosticMessageChain.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DiagnosticMessageChain

# Interface: DiagnosticMessageChain

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2988

A linked list of formatted diagnostic messages to be used as part of a multiline message.
It is built from the bottom up, leaving the head to be the "main" diagnostic.
While it seems that DiagnosticMessageChain is structurally similar to DiagnosticMessage,
the difference is that messages are all preformatted in DMC.

## Properties

### category

> **category**: [`DiagnosticCategory`](../enumerations/DiagnosticCategory.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2990

***

### code

> **code**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2991

***

### messageText

> **messageText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2989

***

### next?

> `optional` **next**: `DiagnosticMessageChain`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2992




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DiagnosticRelatedInformation.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DiagnosticRelatedInformation

# Interface: DiagnosticRelatedInformation

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3001

## Extended by

- [`Diagnostic`](Diagnostic.md)

## Properties

### category

> **category**: [`DiagnosticCategory`](../enumerations/DiagnosticCategory.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3002

***

### code

> **code**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3003

***

### file

> **file**: `undefined` \| [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3004

***

### length

> **length**: `undefined` \| `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3006

***

### messageText

> **messageText**: `string` \| [`DiagnosticMessageChain`](DiagnosticMessageChain.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3007

***

### start

> **start**: `undefined` \| `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3005




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DiagnosticWithLocation.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DiagnosticWithLocation

# Interface: DiagnosticWithLocation

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3009

## Extends

- [`Diagnostic`](Diagnostic.md)

## Properties

### category

> **category**: [`DiagnosticCategory`](../enumerations/DiagnosticCategory.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3002

#### Inherited from

[`Diagnostic`](Diagnostic.md).[`category`](Diagnostic.md#category)

***

### code

> **code**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3003

#### Inherited from

[`Diagnostic`](Diagnostic.md).[`code`](Diagnostic.md#code)

***

### file

> **file**: [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3010

#### Overrides

[`Diagnostic`](Diagnostic.md).[`file`](Diagnostic.md#file)

***

### length

> **length**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3012

#### Overrides

[`Diagnostic`](Diagnostic.md).[`length`](Diagnostic.md#length)

***

### messageText

> **messageText**: `string` \| [`DiagnosticMessageChain`](DiagnosticMessageChain.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3007

#### Inherited from

[`Diagnostic`](Diagnostic.md).[`messageText`](Diagnostic.md#messagetext)

***

### relatedInformation?

> `optional` **relatedInformation**: [`DiagnosticRelatedInformation`](DiagnosticRelatedInformation.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2999

#### Inherited from

[`Diagnostic`](Diagnostic.md).[`relatedInformation`](Diagnostic.md#relatedinformation)

***

### reportsDeprecated?

> `optional` **reportsDeprecated**: `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2997

#### Inherited from

[`Diagnostic`](Diagnostic.md).[`reportsDeprecated`](Diagnostic.md#reportsdeprecated)

***

### reportsUnnecessary?

> `optional` **reportsUnnecessary**: `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2996

May store more in future. For now, this will simply be `true` to indicate when a diagnostic is an unused-identifier diagnostic.

#### Inherited from

[`Diagnostic`](Diagnostic.md).[`reportsUnnecessary`](Diagnostic.md#reportsunnecessary)

***

### source?

> `optional` **source**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2998

#### Inherited from

[`Diagnostic`](Diagnostic.md).[`source`](Diagnostic.md#source)

***

### start

> **start**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3011

#### Overrides

[`Diagnostic`](Diagnostic.md).[`start`](Diagnostic.md#start)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DoStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DoStatement

# Interface: DoStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1516

## Extends

- [`IterationStatement`](IterationStatement.md)

## Properties

### \_statementBrand

> **\_statementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1471

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`_statementBrand`](IterationStatement.md#_statementbrand)

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

[`IterationStatement`](IterationStatement.md).[`decorators`](IterationStatement.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`end`](IterationStatement.md#end)

***

### expression

> `readonly` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1518

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`flags`](IterationStatement.md#flags)

***

### kind

> `readonly` **kind**: [`DoStatement`](../enumerations/SyntaxKind.md#dostatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1517

#### Overrides

[`IterationStatement`](IterationStatement.md).[`kind`](IterationStatement.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`locals`](IterationStatement.md#locals)

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

[`IterationStatement`](IterationStatement.md).[`modifiers`](IterationStatement.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`parent`](IterationStatement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`pos`](IterationStatement.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`skipCheck`](IterationStatement.md#skipcheck)

***

### statement

> `readonly` **statement**: [`Statement`](Statement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1514

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`statement`](IterationStatement.md#statement)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`symbol`](IterationStatement.md#symbol)

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

[`IterationStatement`](IterationStatement.md).[`forEachChild`](IterationStatement.md#foreachchild)

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

[`IterationStatement`](IterationStatement.md).[`getChildAt`](IterationStatement.md#getchildat)

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

[`IterationStatement`](IterationStatement.md).[`getChildCount`](IterationStatement.md#getchildcount)

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

[`IterationStatement`](IterationStatement.md).[`getChildren`](IterationStatement.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getEnd`](IterationStatement.md#getend)

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

[`IterationStatement`](IterationStatement.md).[`getFirstToken`](IterationStatement.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getFullStart`](IterationStatement.md#getfullstart)

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

[`IterationStatement`](IterationStatement.md).[`getFullText`](IterationStatement.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getFullWidth`](IterationStatement.md#getfullwidth)

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

[`IterationStatement`](IterationStatement.md).[`getLastToken`](IterationStatement.md#getlasttoken)

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

[`IterationStatement`](IterationStatement.md).[`getLeadingTriviaWidth`](IterationStatement.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getSourceFile`](IterationStatement.md#getsourcefile)

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

[`IterationStatement`](IterationStatement.md).[`getStart`](IterationStatement.md#getstart)

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

[`IterationStatement`](IterationStatement.md).[`getText`](IterationStatement.md#gettext)

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

[`IterationStatement`](IterationStatement.md).[`getWidth`](IterationStatement.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DocCommentTemplateOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DocCommentTemplateOptions

# Interface: DocCommentTemplateOptions

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6913

## Properties

### generateReturnInDocTemplate?

> `readonly` `optional` **generateReturnInDocTemplate**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6914




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DocumentHighlights.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DocumentHighlights

# Interface: DocumentHighlights

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7316

## Properties

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7317

***

### highlightSpans

> **highlightSpans**: [`HighlightSpan`](HighlightSpan.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7318




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DocumentRegistry.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DocumentRegistry

# Interface: DocumentRegistry

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7337

The document registry represents a store of SourceFile objects that can be shared between
multiple LanguageService instances. A LanguageService instance holds on the SourceFile (AST)
of files in the context.
SourceFile objects account for most of the memory usage by the language service. Sharing
the same DocumentRegistry instance between different instances of LanguageService allow
for more efficient memory utilization since all projects will share at least the library
file (lib.d.ts).

A more advanced use of the document registry is to serialize sourceFile objects to disk
and re-hydrate them when needed.

To create a default DocumentRegistry, use createDocumentRegistry to create one, and pass it
to all subsequent createLanguageService calls.

## Methods

### acquireDocument()

> **acquireDocument**(`fileName`, `compilationSettingsOrHost`, `scriptSnapshot`, `version`, `scriptKind?`, `sourceFileOptions?`): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7355

Request a stored SourceFile with a given fileName and compilationSettings.
The first call to acquire will call createLanguageServiceSourceFile to generate
the SourceFile if was not found in the registry.

#### Parameters

##### fileName

`string`

The name of the file requested

##### compilationSettingsOrHost

Some compilation settings like target affects the
shape of a the resulting SourceFile. This allows the DocumentRegistry to store
multiple copies of the same file for different compilation settings. A minimal
resolution cache is needed to fully define a source file's shape when
the compilation settings include `module: node16`+, so providing a cache host
object should be preferred. A common host is a language service `ConfiguredProject`.

[`CompilerOptions`](CompilerOptions.md) | [`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md)

##### scriptSnapshot

[`IScriptSnapshot`](IScriptSnapshot.md)

Text of the file. Only used if the file was not found
in the registry and a new one was created.

##### version

`string`

Current version of the file. Only used if the file was not found
in the registry and a new one was created.

##### scriptKind?

[`ScriptKind`](../enumerations/ScriptKind.md)

##### sourceFileOptions?

[`ScriptTarget`](../enumerations/ScriptTarget.md) | [`CreateSourceFileOptions`](CreateSourceFileOptions.md)

#### Returns

[`SourceFile`](SourceFile.md)

***

### acquireDocumentWithKey()

> **acquireDocumentWithKey**(`fileName`, `path`, `compilationSettingsOrHost`, `key`, `scriptSnapshot`, `version`, `scriptKind?`, `sourceFileOptions?`): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7356

#### Parameters

##### fileName

`string`

##### path

[`Path`](../type-aliases/Path.md)

##### compilationSettingsOrHost

[`CompilerOptions`](CompilerOptions.md) | [`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md)

##### key

[`DocumentRegistryBucketKey`](../type-aliases/DocumentRegistryBucketKey.md)

##### scriptSnapshot

[`IScriptSnapshot`](IScriptSnapshot.md)

##### version

`string`

##### scriptKind?

[`ScriptKind`](../enumerations/ScriptKind.md)

##### sourceFileOptions?

[`ScriptTarget`](../enumerations/ScriptTarget.md) | [`CreateSourceFileOptions`](CreateSourceFileOptions.md)

#### Returns

[`SourceFile`](SourceFile.md)

***

### getKeyForCompilationSettings()

> **getKeyForCompilationSettings**(`settings`): [`DocumentRegistryBucketKey`](../type-aliases/DocumentRegistryBucketKey.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7374

#### Parameters

##### settings

[`CompilerOptions`](CompilerOptions.md)

#### Returns

[`DocumentRegistryBucketKey`](../type-aliases/DocumentRegistryBucketKey.md)

***

### releaseDocument()

#### Call Signature

> **releaseDocument**(`fileName`, `compilationSettings`, `scriptKind?`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7386

##### Parameters

###### fileName

`string`

###### compilationSettings

[`CompilerOptions`](CompilerOptions.md)

###### scriptKind?

[`ScriptKind`](../enumerations/ScriptKind.md)

##### Returns

`void`

##### Deprecated

pass scriptKind and impliedNodeFormat for correctness

#### Call Signature

> **releaseDocument**(`fileName`, `compilationSettings`, `scriptKind`, `impliedNodeFormat`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7398

Informs the DocumentRegistry that a file is not needed any longer.

Note: It is not allowed to call release on a SourceFile that was not acquired from
this registry originally.

##### Parameters

###### fileName

`string`

The name of the file to be released

###### compilationSettings

[`CompilerOptions`](CompilerOptions.md)

The compilation settings used to acquire the file

###### scriptKind

[`ScriptKind`](../enumerations/ScriptKind.md)

The script kind of the file to be released

###### impliedNodeFormat

The implied source file format of the file to be released

`undefined` | [`CommonJS`](../enumerations/ModuleKind.md#commonjs) | [`ESNext`](../enumerations/ModuleKind.md#esnext)

##### Returns

`void`

***

### releaseDocumentWithKey()

#### Call Signature

> **releaseDocumentWithKey**(`path`, `key`, `scriptKind?`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7401

##### Parameters

###### path

[`Path`](../type-aliases/Path.md)

###### key

[`DocumentRegistryBucketKey`](../type-aliases/DocumentRegistryBucketKey.md)

###### scriptKind?

[`ScriptKind`](../enumerations/ScriptKind.md)

##### Returns

`void`

##### Deprecated

pass scriptKind for and impliedNodeFormat correctness

#### Call Signature

> **releaseDocumentWithKey**(`path`, `key`, `scriptKind`, `impliedNodeFormat`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7402

##### Parameters

###### path

[`Path`](../type-aliases/Path.md)

###### key

[`DocumentRegistryBucketKey`](../type-aliases/DocumentRegistryBucketKey.md)

###### scriptKind

[`ScriptKind`](../enumerations/ScriptKind.md)

###### impliedNodeFormat

`undefined` | [`CommonJS`](../enumerations/ModuleKind.md#commonjs) | [`ESNext`](../enumerations/ModuleKind.md#esnext)

##### Returns

`void`

***

### reportStats()

> **reportStats**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7403

#### Returns

`string`

***

### updateDocument()

> **updateDocument**(`fileName`, `compilationSettingsOrHost`, `scriptSnapshot`, `version`, `scriptKind?`, `sourceFileOptions?`): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7372

Request an updated version of an already existing SourceFile with a given fileName
and compilationSettings. The update will in-turn call updateLanguageServiceSourceFile
to get an updated SourceFile.

#### Parameters

##### fileName

`string`

The name of the file requested

##### compilationSettingsOrHost

Some compilation settings like target affects the
shape of a the resulting SourceFile. This allows the DocumentRegistry to store
multiple copies of the same file for different compilation settings. A minimal
resolution cache is needed to fully define a source file's shape when
the compilation settings include `module: node16`+, so providing a cache host
object should be preferred. A common host is a language service `ConfiguredProject`.

[`CompilerOptions`](CompilerOptions.md) | [`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md)

##### scriptSnapshot

[`IScriptSnapshot`](IScriptSnapshot.md)

Text of the file.

##### version

`string`

Current version of the file.

##### scriptKind?

[`ScriptKind`](../enumerations/ScriptKind.md)

##### sourceFileOptions?

[`ScriptTarget`](../enumerations/ScriptTarget.md) | [`CreateSourceFileOptions`](CreateSourceFileOptions.md)

#### Returns

[`SourceFile`](SourceFile.md)

***

### updateDocumentWithKey()

> **updateDocumentWithKey**(`fileName`, `path`, `compilationSettingsOrHost`, `key`, `scriptSnapshot`, `version`, `scriptKind?`, `sourceFileOptions?`): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7373

#### Parameters

##### fileName

`string`

##### path

[`Path`](../type-aliases/Path.md)

##### compilationSettingsOrHost

[`CompilerOptions`](CompilerOptions.md) | [`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md)

##### key

[`DocumentRegistryBucketKey`](../type-aliases/DocumentRegistryBucketKey.md)

##### scriptSnapshot

[`IScriptSnapshot`](IScriptSnapshot.md)

##### version

`string`

##### scriptKind?

[`ScriptKind`](../enumerations/ScriptKind.md)

##### sourceFileOptions?

[`ScriptTarget`](../enumerations/ScriptTarget.md) | [`CreateSourceFileOptions`](CreateSourceFileOptions.md)

#### Returns

[`SourceFile`](SourceFile.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/DocumentSpan.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / DocumentSpan

# Interface: DocumentSpan

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6700

## Extended by

- [`RenameLocation`](RenameLocation.md)
- [`ReferenceEntry`](ReferenceEntry.md)
- [`ImplementationLocation`](ImplementationLocation.md)
- [`DefinitionInfo`](DefinitionInfo.md)

## Properties

### contextSpan?

> `optional` **contextSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6713

If DocumentSpan.textSpan is the span for name of the declaration,
then this is the span for relevant declaration

***

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6702

***

### originalContextSpan?

> `optional` **originalContextSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6714

***

### originalFileName?

> `optional` **originalFileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6708

***

### originalTextSpan?

> `optional` **originalTextSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6707

If the span represents a location that was remapped (e.g. via a .d.ts.map file),
then the original filename and span will be specified here

***

### textSpan

> **textSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6701




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ESMap.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ESMap

# Interface: ESMap\<K, V\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:58

ES6 Map interface.

## Extends

- [`ReadonlyESMap`](ReadonlyESMap.md)\<`K`, `V`\>.[`Collection`](Collection.md)\<`K`\>

## Extended by

- [`Map`](Map.md)
- [`UnderscoreEscapedMap`](UnderscoreEscapedMap.md)

## Type Parameters

### K

`K`

### V

`V`

## Properties

### size

> `readonly` **size**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:36

#### Inherited from

[`Collection`](Collection.md).[`size`](Collection.md#size)

## Methods

### clear()

> **clear**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:43

#### Returns

`void`

#### Inherited from

[`Collection`](Collection.md).[`clear`](Collection.md#clear)

***

### delete()

> **delete**(`key`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:42

#### Parameters

##### key

`K`

#### Returns

`boolean`

#### Inherited from

[`Collection`](Collection.md).[`delete`](Collection.md#delete)

***

### entries()

> **entries**(): [`Iterator`](Iterator.md)\<\[`K`, `V`\]\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:49

#### Returns

[`Iterator`](Iterator.md)\<\[`K`, `V`\]\>

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`entries`](ReadonlyESMap.md#entries)

***

### forEach()

> **forEach**(`action`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:50

#### Parameters

##### action

(`value`, `key`) => `void`

#### Returns

`void`

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`forEach`](ReadonlyESMap.md#foreach)

***

### get()

> **get**(`key`): `undefined` \| `V`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:47

#### Parameters

##### key

`K`

#### Returns

`undefined` \| `V`

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`get`](ReadonlyESMap.md#get)

***

### has()

> **has**(`key`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:37

#### Parameters

##### key

`K`

#### Returns

`boolean`

#### Inherited from

[`Collection`](Collection.md).[`has`](Collection.md#has)

***

### keys()

> **keys**(): [`Iterator`](Iterator.md)\<`K`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:38

#### Returns

[`Iterator`](Iterator.md)\<`K`\>

#### Inherited from

[`Collection`](Collection.md).[`keys`](Collection.md#keys)

***

### set()

> **set**(`key`, `value`): `this`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:59

#### Parameters

##### key

`K`

##### value

`V`

#### Returns

`this`

***

### values()

> **values**(): [`Iterator`](Iterator.md)\<`V`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:48

#### Returns

[`Iterator`](Iterator.md)\<`V`\>

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`values`](ReadonlyESMap.md#values)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EditorOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EditorOptions

# Interface: ~~EditorOptions~~

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6763

## Deprecated

- consider using EditorSettings instead

## Extended by

- [`FormatCodeOptions`](FormatCodeOptions.md)

## Properties

### ~~BaseIndentSize?~~

> `optional` **BaseIndentSize**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6764

***

### ~~ConvertTabsToSpaces~~

> **ConvertTabsToSpaces**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6768

***

### ~~IndentSize~~

> **IndentSize**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6765

***

### ~~IndentStyle~~

> **IndentStyle**: [`IndentStyle`](../enumerations/IndentStyle.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6769

***

### ~~NewLineCharacter~~

> **NewLineCharacter**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6767

***

### ~~TabSize~~

> **TabSize**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6766




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EditorSettings.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EditorSettings

# Interface: EditorSettings

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6771

## Extended by

- [`FormatCodeSettings`](FormatCodeSettings.md)

## Properties

### baseIndentSize?

> `optional` **baseIndentSize**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6772

***

### convertTabsToSpaces?

> `optional` **convertTabsToSpaces**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6776

***

### indentSize?

> `optional` **indentSize**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6773

***

### indentStyle?

> `optional` **indentStyle**: [`IndentStyle`](../enumerations/IndentStyle.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6777

***

### newLineCharacter?

> `optional` **newLineCharacter**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6775

***

### tabSize?

> `optional` **tabSize**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6774

***

### trimTrailingWhitespace?

> `optional` **trimTrailingWhitespace**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6778




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ElementAccessChain.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ElementAccessChain

# Interface: ElementAccessChain

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1329

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

### \_optionalChainBrand

> **\_optionalChainBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1330

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

> `readonly` **expression**: [`LeftHandSideExpression`](LeftHandSideExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1325

#### Inherited from

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ElementAccessExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ElementAccessExpression

# Interface: ElementAccessExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1323

## Extends

- [`MemberExpression`](MemberExpression.md)

## Extended by

- [`ElementAccessChain`](ElementAccessChain.md)
- [`SuperElementAccessExpression`](SuperElementAccessExpression.md)

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

### argumentExpression

> `readonly` **argumentExpression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1327

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

### expression

> `readonly` **expression**: [`LeftHandSideExpression`](LeftHandSideExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1325

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`MemberExpression`](MemberExpression.md).[`flags`](MemberExpression.md#flags)

***

### kind

> `readonly` **kind**: [`ElementAccessExpression`](../enumerations/SyntaxKind.md#elementaccessexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1324

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

### questionDotToken?

> `readonly` `optional` **questionDotToken**: [`QuestionDotToken`](../type-aliases/QuestionDotToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1326

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EmitAndSemanticDiagnosticsBuilderProgram.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EmitAndSemanticDiagnosticsBuilderProgram

# Interface: EmitAndSemanticDiagnosticsBuilderProgram

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5747

The builder that can handle the changes in program and iterate through changed file to emit the files
The semantic diagnostics are cached per file and managed by clearing for the changed/affected files

## Extends

- [`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md)

## Properties

### builderProgramForLinter?

> `optional` **builderProgramForLinter**: `EmitAndSemanticDiagnosticsBuilderProgram`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5731

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`builderProgramForLinter`](SemanticDiagnosticsBuilderProgram.md#builderprogramforlinter)

## Methods

### emit()

> **emit**(`targetSourceFile?`, `writeFile?`, `cancellationToken?`, `emitOnlyDtsFiles?`, `customTransformers?`): [`EmitResult`](EmitResult.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5725

Emits the JavaScript and declaration files.
When targetSource file is specified, emits the files corresponding to that source file,
otherwise for the whole program.
In case of EmitAndSemanticDiagnosticsBuilderProgram, when targetSourceFile is specified,
it is assumed that that file is handled from affected file list. If targetSourceFile is not specified,
it will only emit all the affected files instead of whole program

The first of writeFile if provided, writeFile of BuilderProgramHost if provided, writeFile of compiler host
in that order would be used to write the files

#### Parameters

##### targetSourceFile?

[`SourceFile`](SourceFile.md)

##### writeFile?

[`WriteFileCallback`](../type-aliases/WriteFileCallback.md)

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

##### emitOnlyDtsFiles?

`boolean`

##### customTransformers?

[`CustomTransformers`](CustomTransformers.md)

#### Returns

[`EmitResult`](EmitResult.md)

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`emit`](SemanticDiagnosticsBuilderProgram.md#emit)

***

### emitNextAffectedFile()

> **emitNextAffectedFile**(`writeFile?`, `cancellationToken?`, `emitOnlyDtsFiles?`, `customTransformers?`): [`AffectedFileResult`](../type-aliases/AffectedFileResult.md)\<[`EmitResult`](EmitResult.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5753

Emits the next affected file's emit result (EmitResult and sourceFiles emitted) or returns undefined if iteration is complete
The first of writeFile if provided, writeFile of BuilderProgramHost if provided, writeFile of compiler host
in that order would be used to write the files

#### Parameters

##### writeFile?

[`WriteFileCallback`](../type-aliases/WriteFileCallback.md)

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

##### emitOnlyDtsFiles?

`boolean`

##### customTransformers?

[`CustomTransformers`](CustomTransformers.md)

#### Returns

[`AffectedFileResult`](../type-aliases/AffectedFileResult.md)\<[`EmitResult`](EmitResult.md)\>

***

### getAllDependencies()

> **getAllDependencies**(`sourceFile`): readonly `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5704

Get all the dependencies of the file

#### Parameters

##### sourceFile

[`SourceFile`](SourceFile.md)

#### Returns

readonly `string`[]

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`getAllDependencies`](SemanticDiagnosticsBuilderProgram.md#getalldependencies)

***

### getCompilerOptions()

> **getCompilerOptions**(): [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5672

Get compiler options of the program

#### Returns

[`CompilerOptions`](CompilerOptions.md)

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`getCompilerOptions`](SemanticDiagnosticsBuilderProgram.md#getcompileroptions)

***

### getConfigFileParsingDiagnostics()

> **getConfigFileParsingDiagnostics**(): readonly [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5692

Get the diagnostics from config file parsing

#### Returns

readonly [`Diagnostic`](Diagnostic.md)[]

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`getConfigFileParsingDiagnostics`](SemanticDiagnosticsBuilderProgram.md#getconfigfileparsingdiagnostics)

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5729

Get the current directory of the program

#### Returns

`string`

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`getCurrentDirectory`](SemanticDiagnosticsBuilderProgram.md#getcurrentdirectory)

***

### getDeclarationDiagnostics()

> **getDeclarationDiagnostics**(`sourceFile?`, `cancellationToken?`): readonly [`DiagnosticWithLocation`](DiagnosticWithLocation.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5700

Get the declaration diagnostics, for all source files if source file is not supplied

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

#### Returns

readonly [`DiagnosticWithLocation`](DiagnosticWithLocation.md)[]

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`getDeclarationDiagnostics`](SemanticDiagnosticsBuilderProgram.md#getdeclarationdiagnostics)

***

### getGlobalDiagnostics()

> **getGlobalDiagnostics**(`cancellationToken?`): readonly [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5688

Get the diagnostics that dont belong to any file

#### Parameters

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

#### Returns

readonly [`Diagnostic`](Diagnostic.md)[]

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`getGlobalDiagnostics`](SemanticDiagnosticsBuilderProgram.md#getglobaldiagnostics)

***

### getOptionsDiagnostics()

> **getOptionsDiagnostics**(`cancellationToken?`): readonly [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5684

Get the diagnostics for compiler options

#### Parameters

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

#### Returns

readonly [`Diagnostic`](Diagnostic.md)[]

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`getOptionsDiagnostics`](SemanticDiagnosticsBuilderProgram.md#getoptionsdiagnostics)

***

### getProgram()

> **getProgram**(): [`Program`](Program.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5668

Returns current program

#### Returns

[`Program`](Program.md)

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`getProgram`](SemanticDiagnosticsBuilderProgram.md#getprogram)

***

### getSemanticDiagnostics()

> **getSemanticDiagnostics**(`sourceFile?`, `cancellationToken?`): readonly [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5713

Gets the semantic diagnostics from the program corresponding to this state of file (if provided) or whole program
The semantic diagnostics are cached and managed here
Note that it is assumed that when asked about semantic diagnostics through this API,
the file has been taken out of affected files so it is safe to use cache or get from program and cache the diagnostics
In case of SemanticDiagnosticsBuilderProgram if the source file is not provided,
it will iterate through all the affected files, to ensure that cache stays valid and yet provide a way to get all semantic diagnostics

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

#### Returns

readonly [`Diagnostic`](Diagnostic.md)[]

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`getSemanticDiagnostics`](SemanticDiagnosticsBuilderProgram.md#getsemanticdiagnostics)

***

### getSemanticDiagnosticsOfNextAffectedFile()

> **getSemanticDiagnosticsOfNextAffectedFile**(`cancellationToken?`, `ignoreSourceFile?`): [`AffectedFileResult`](../type-aliases/AffectedFileResult.md)\<readonly [`Diagnostic`](Diagnostic.md)[]\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5741

Gets the semantic diagnostics from the program for the next affected file and caches it
Returns undefined if the iteration is complete

#### Parameters

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

##### ignoreSourceFile?

(`sourceFile`) => `boolean`

#### Returns

[`AffectedFileResult`](../type-aliases/AffectedFileResult.md)\<readonly [`Diagnostic`](Diagnostic.md)[]\>

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`getSemanticDiagnosticsOfNextAffectedFile`](SemanticDiagnosticsBuilderProgram.md#getsemanticdiagnosticsofnextaffectedfile)

***

### getSourceFile()

> **getSourceFile**(`fileName`): `undefined` \| [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5676

Get the source file in the program with file name

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| [`SourceFile`](SourceFile.md)

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`getSourceFile`](SemanticDiagnosticsBuilderProgram.md#getsourcefile)

***

### getSourceFiles()

> **getSourceFiles**(): readonly [`SourceFile`](SourceFile.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5680

Get a list of files in the program

#### Returns

readonly [`SourceFile`](SourceFile.md)[]

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`getSourceFiles`](SemanticDiagnosticsBuilderProgram.md#getsourcefiles)

***

### getSyntacticDiagnostics()

> **getSyntacticDiagnostics**(`sourceFile?`, `cancellationToken?`): readonly [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5696

Get the syntax diagnostics, for all source files if source file is not supplied

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

#### Returns

readonly [`Diagnostic`](Diagnostic.md)[]

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`getSyntacticDiagnostics`](SemanticDiagnosticsBuilderProgram.md#getsyntacticdiagnostics)

***

### isFileUpdateInConstEnumCache()?

> `optional` **isFileUpdateInConstEnumCache**(`sourceFile`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5730

#### Parameters

##### sourceFile

[`SourceFile`](SourceFile.md)

#### Returns

`boolean`

#### Inherited from

[`SemanticDiagnosticsBuilderProgram`](SemanticDiagnosticsBuilderProgram.md).[`isFileUpdateInConstEnumCache`](SemanticDiagnosticsBuilderProgram.md#isfileupdateinconstenumcache)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EmitHelperBase.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EmitHelperBase

# Interface: EmitHelperBase

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3553

## Extended by

- [`ScopedEmitHelper`](ScopedEmitHelper.md)
- [`UnscopedEmitHelper`](UnscopedEmitHelper.md)

## Properties

### dependencies?

> `readonly` `optional` **dependencies**: [`EmitHelper`](../type-aliases/EmitHelper.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3558

***

### name

> `readonly` **name**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3554

***

### priority?

> `readonly` `optional` **priority**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3557

***

### scoped

> `readonly` **scoped**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3555

***

### text

> `readonly` **text**: `string` \| (`node`) => `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3556




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EmitHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EmitHost

# Interface: EmitHost

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3584

## Extends

- [`ScriptReferenceHost`](ScriptReferenceHost.md).[`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md).[`SourceFileMayBeEmittedHost`](SourceFileMayBeEmittedHost.md)

## Properties

### getSourceFileFromReference()

> **getSourceFileFromReference**: (`referencingFile`, `ref`) => `undefined` \| [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3595

#### Parameters

##### referencingFile

[`SourceFile`](SourceFile.md) | [`UnparsedSource`](UnparsedSource.md)

##### ref

[`FileReference`](FileReference.md)

#### Returns

`undefined` \| [`SourceFile`](SourceFile.md)

***

### redirectTargetsMap

> `readonly` **redirectTargetsMap**: [`RedirectTargetsMap`](../type-aliases/RedirectTargetsMap.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3596

#### Overrides

[`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md).[`redirectTargetsMap`](ModuleSpecifierResolutionHost.md#redirecttargetsmap)

***

### writeFile

> **writeFile**: [`WriteFileCallback`](../type-aliases/WriteFileCallback.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3594

## Methods

### createHash()?

> `optional` **createHash**(`data`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3597

#### Parameters

##### data

`string`

#### Returns

`string`

***

### directoryExists()?

> `optional` **directoryExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4344

#### Parameters

##### path

`string`

#### Returns

`boolean`

#### Inherited from

[`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md).[`directoryExists`](ModuleSpecifierResolutionHost.md#directoryexists)

***

### fileExists()

> **fileExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4342

#### Parameters

##### path

`string`

#### Returns

`boolean`

#### Inherited from

[`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md).[`fileExists`](ModuleSpecifierResolutionHost.md#fileexists)

***

### getCanonicalFileName()

> **getCanonicalFileName**(`fileName`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3590

#### Parameters

##### fileName

`string`

#### Returns

`string`

***

### getCommonSourceDirectory()

> **getCommonSourceDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3589

#### Returns

`string`

***

### getCompilerOptions()

> **getCompilerOptions**(): [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2231

#### Returns

[`CompilerOptions`](CompilerOptions.md)

#### Inherited from

[`SourceFileMayBeEmittedHost`](SourceFileMayBeEmittedHost.md).[`getCompilerOptions`](SourceFileMayBeEmittedHost.md#getcompileroptions)

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3587

#### Returns

`string`

#### Overrides

[`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md).[`getCurrentDirectory`](ModuleSpecifierResolutionHost.md#getcurrentdirectory)

***

### getGlobalTypingsCacheLocation()?

> `optional` **getGlobalTypingsCacheLocation**(): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4349

#### Returns

`undefined` \| `string`

#### Inherited from

[`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md).[`getGlobalTypingsCacheLocation`](ModuleSpecifierResolutionHost.md#getglobaltypingscachelocation)

***

### getLibFileFromReference()

> **getLibFileFromReference**(`ref`): `undefined` \| [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3588

#### Parameters

##### ref

[`FileReference`](FileReference.md)

#### Returns

`undefined` \| [`SourceFile`](SourceFile.md)

***

### getModuleSpecifierCache()?

> `optional` **getModuleSpecifierCache**(): [`ModuleSpecifierCache`](ModuleSpecifierCache.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4347

#### Returns

[`ModuleSpecifierCache`](ModuleSpecifierCache.md)

#### Inherited from

[`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md).[`getModuleSpecifierCache`](ModuleSpecifierResolutionHost.md#getmodulespecifiercache)

***

### getNearestAncestorDirectoryWithPackageJson()?

> `optional` **getNearestAncestorDirectoryWithPackageJson**(`fileName`, `rootDir?`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4350

#### Parameters

##### fileName

`string`

##### rootDir?

`string`

#### Returns

`undefined` \| `string`

#### Inherited from

[`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md).[`getNearestAncestorDirectoryWithPackageJson`](ModuleSpecifierResolutionHost.md#getnearestancestordirectorywithpackagejson)

***

### getNewLine()

> **getNewLine**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3591

#### Returns

`string`

***

### getPackageJsonInfoCache()?

> `optional` **getPackageJsonInfoCache**(): `undefined` \| [`PackageJsonInfoCache`](PackageJsonInfoCache.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4348

#### Returns

`undefined` \| [`PackageJsonInfoCache`](PackageJsonInfoCache.md)

#### Inherited from

[`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md).[`getPackageJsonInfoCache`](ModuleSpecifierResolutionHost.md#getpackagejsoninfocache)

***

### getPrependNodes()

> **getPrependNodes**(): readonly ([`InputFiles`](InputFiles.md) \| [`UnparsedSource`](UnparsedSource.md))[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3593

#### Returns

readonly ([`InputFiles`](InputFiles.md) \| [`UnparsedSource`](UnparsedSource.md))[]

***

### getProjectReferenceRedirect()

> **getProjectReferenceRedirect**(`fileName`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4352

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| `string`

#### Inherited from

[`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md).[`getProjectReferenceRedirect`](ModuleSpecifierResolutionHost.md#getprojectreferenceredirect)

***

### getResolvedProjectReferenceToRedirect()

> **getResolvedProjectReferenceToRedirect**(`fileName`): `undefined` \| [`ResolvedProjectReference`](ResolvedProjectReference.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3581

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| [`ResolvedProjectReference`](ResolvedProjectReference.md)

#### Inherited from

[`SourceFileMayBeEmittedHost`](SourceFileMayBeEmittedHost.md).[`getResolvedProjectReferenceToRedirect`](SourceFileMayBeEmittedHost.md#getresolvedprojectreferencetoredirect)

***

### getSourceFile()

> **getSourceFile**(`fileName`): `undefined` \| [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2232

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| [`SourceFile`](SourceFile.md)

#### Inherited from

[`ScriptReferenceHost`](ScriptReferenceHost.md).[`getSourceFile`](ScriptReferenceHost.md#getsourcefile)

***

### getSourceFileByPath()

> **getSourceFileByPath**(`path`): `undefined` \| [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2233

#### Parameters

##### path

[`Path`](../type-aliases/Path.md)

#### Returns

`undefined` \| [`SourceFile`](SourceFile.md)

#### Inherited from

[`ScriptReferenceHost`](ScriptReferenceHost.md).[`getSourceFileByPath`](ScriptReferenceHost.md#getsourcefilebypath)

***

### getSourceFiles()

> **getSourceFiles**(): readonly [`SourceFile`](SourceFile.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3585

#### Returns

readonly [`SourceFile`](SourceFile.md)[]

***

### isEmitBlocked()

> **isEmitBlocked**(`emitFileName`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3592

#### Parameters

##### emitFileName

`string`

#### Returns

`boolean`

***

### isSourceFileFromExternalLibrary()

> **isSourceFileFromExternalLibrary**(`file`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3580

#### Parameters

##### file

[`SourceFile`](SourceFile.md)

#### Returns

`boolean`

#### Inherited from

[`SourceFileMayBeEmittedHost`](SourceFileMayBeEmittedHost.md).[`isSourceFileFromExternalLibrary`](SourceFileMayBeEmittedHost.md#issourcefilefromexternallibrary)

***

### isSourceOfProjectReferenceRedirect()

> **isSourceOfProjectReferenceRedirect**(`fileName`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4353

#### Parameters

##### fileName

`string`

#### Returns

`boolean`

#### Inherited from

[`SourceFileMayBeEmittedHost`](SourceFileMayBeEmittedHost.md).[`isSourceOfProjectReferenceRedirect`](SourceFileMayBeEmittedHost.md#issourceofprojectreferenceredirect)

***

### readFile()?

> `optional` **readFile**(`path`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4345

#### Parameters

##### path

`string`

#### Returns

`undefined` \| `string`

#### Inherited from

[`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md).[`readFile`](ModuleSpecifierResolutionHost.md#readfile)

***

### realpath()?

> `optional` **realpath**(`path`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4346

#### Parameters

##### path

`string`

#### Returns

`string`

#### Inherited from

[`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md).[`realpath`](ModuleSpecifierResolutionHost.md#realpath)

***

### useCaseSensitiveFileNames()

> **useCaseSensitiveFileNames**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3586

#### Returns

`boolean`

#### Overrides

[`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md).[`useCaseSensitiveFileNames`](ModuleSpecifierResolutionHost.md#usecasesensitivefilenames)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EmitOutput.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EmitOutput

# Interface: EmitOutput

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5631

## Properties

### emitSkipped

> **emitSkipped**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5633

***

### outputFiles

> **outputFiles**: [`OutputFile`](OutputFile.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5632




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EmitResult.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EmitResult

# Interface: EmitResult

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2378

## Properties

### diagnostics

> **diagnostics**: readonly [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2381

Contains declaration emit diagnostics

***

### emitSkipped

> **emitSkipped**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2379

***

### emittedFiles?

> `optional` **emittedFiles**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2382




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EmitTextWriter.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EmitTextWriter

# Interface: EmitTextWriter

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4319

## Extends

- `SymbolWriter`

## Properties

### moduleResolverHost?

> `optional` **moduleResolverHost**: [`ModuleSpecifierResolutionHost`](ModuleSpecifierResolutionHost.md) & `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4384

#### Type declaration

##### getCommonSourceDirectory()

> **getCommonSourceDirectory**(): `string`

###### Returns

`string`

#### Inherited from

`SymbolWriter.moduleResolverHost`

## Methods

### clear()

> **clear**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2569

#### Returns

`void`

#### Inherited from

`SymbolWriter.clear`

***

### decreaseIndent()

> **decreaseIndent**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2568

#### Returns

`void`

#### Inherited from

`SymbolWriter.decreaseIndent`

***

### getColumn()

> **getColumn**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4328

#### Returns

`number`

***

### getIndent()

> **getIndent**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4329

#### Returns

`number`

***

### getLine()

> **getLine**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4327

#### Returns

`number`

***

### getText()

> **getText**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4323

#### Returns

`string`

***

### getTextPos()

> **getTextPos**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4326

#### Returns

`number`

***

### getTextPosWithWriteLine()?

> `optional` **getTextPosWithWriteLine**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4333

#### Returns

`number`

***

### hasTrailingComment()

> **hasTrailingComment**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4331

#### Returns

`boolean`

***

### hasTrailingWhitespace()

> **hasTrailingWhitespace**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4332

#### Returns

`boolean`

***

### increaseIndent()

> **increaseIndent**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2567

#### Returns

`void`

#### Inherited from

`SymbolWriter.increaseIndent`

***

### isAtStartOfLine()

> **isAtStartOfLine**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4330

#### Returns

`boolean`

***

### nonEscapingWrite()?

> `optional` **nonEscapingWrite**(`text`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4334

#### Parameters

##### text

`string`

#### Returns

`void`

***

### rawWrite()

> **rawWrite**(`s`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4324

#### Parameters

##### s

`string`

#### Returns

`void`

***

### reportCyclicStructureError()?

> `optional` **reportCyclicStructureError**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4381

#### Returns

`void`

#### Inherited from

`SymbolWriter.reportCyclicStructureError`

***

### reportImportTypeNodeResolutionModeOverride()?

> `optional` **reportImportTypeNodeResolutionModeOverride**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4391

#### Returns

`void`

#### Inherited from

`SymbolWriter.reportImportTypeNodeResolutionModeOverride`

***

### reportInaccessibleThisError()?

> `optional` **reportInaccessibleThisError**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4378

#### Returns

`void`

#### Inherited from

`SymbolWriter.reportInaccessibleThisError`

***

### reportInaccessibleUniqueSymbolError()?

> `optional` **reportInaccessibleUniqueSymbolError**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4380

#### Returns

`void`

#### Inherited from

`SymbolWriter.reportInaccessibleUniqueSymbolError`

***

### reportLikelyUnsafeImportRequiredError()?

> `optional` **reportLikelyUnsafeImportRequiredError**(`specifier`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4382

#### Parameters

##### specifier

`string`

#### Returns

`void`

#### Inherited from

`SymbolWriter.reportLikelyUnsafeImportRequiredError`

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

#### Inherited from

`SymbolWriter.reportNonlocalAugmentation`

***

### reportNonSerializableProperty()?

> `optional` **reportNonSerializableProperty**(`propertyName`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4390

#### Parameters

##### propertyName

`string`

#### Returns

`void`

#### Inherited from

`SymbolWriter.reportNonSerializableProperty`

***

### reportPrivateInBaseOfClassExpression()?

> `optional` **reportPrivateInBaseOfClassExpression**(`propertyName`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4379

#### Parameters

##### propertyName

`string`

#### Returns

`void`

#### Inherited from

`SymbolWriter.reportPrivateInBaseOfClassExpression`

***

### reportTruncationError()?

> `optional` **reportTruncationError**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4383

#### Returns

`void`

#### Inherited from

`SymbolWriter.reportTruncationError`

***

### trackExternalModuleSymbolOfImportTypeNode()?

> `optional` **trackExternalModuleSymbolOfImportTypeNode**(`symbol`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4388

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

#### Returns

`void`

#### Inherited from

`SymbolWriter.trackExternalModuleSymbolOfImportTypeNode`

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

#### Inherited from

`SymbolWriter.trackReferencedAmbientModule`

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

#### Inherited from

`SymbolWriter.trackSymbol`

***

### write()

> **write**(`s`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4320

#### Parameters

##### s

`string`

#### Returns

`void`

***

### writeComment()

> **writeComment**(`text`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4322

#### Parameters

##### text

`string`

#### Returns

`void`

***

### writeKeyword()

> **writeKeyword**(`text`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2558

#### Parameters

##### text

`string`

#### Returns

`void`

#### Inherited from

`SymbolWriter.writeKeyword`

***

### writeLine()

> **writeLine**(`force?`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2566

#### Parameters

##### force?

`boolean`

#### Returns

`void`

#### Inherited from

`SymbolWriter.writeLine`

***

### writeLiteral()

> **writeLiteral**(`s`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4325

#### Parameters

##### s

`string`

#### Returns

`void`

***

### writeOperator()

> **writeOperator**(`text`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2559

#### Parameters

##### text

`string`

#### Returns

`void`

#### Inherited from

`SymbolWriter.writeOperator`

***

### writeParameter()

> **writeParameter**(`text`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2563

#### Parameters

##### text

`string`

#### Returns

`void`

#### Inherited from

`SymbolWriter.writeParameter`

***

### writeProperty()

> **writeProperty**(`text`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2564

#### Parameters

##### text

`string`

#### Returns

`void`

#### Inherited from

`SymbolWriter.writeProperty`

***

### writePunctuation()

> **writePunctuation**(`text`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2560

#### Parameters

##### text

`string`

#### Returns

`void`

#### Inherited from

`SymbolWriter.writePunctuation`

***

### writeSpace()

> **writeSpace**(`text`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2561

#### Parameters

##### text

`string`

#### Returns

`void`

#### Inherited from

`SymbolWriter.writeSpace`

***

### writeStringLiteral()

> **writeStringLiteral**(`text`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2562

#### Parameters

##### text

`string`

#### Returns

`void`

#### Inherited from

`SymbolWriter.writeStringLiteral`

***

### writeSymbol()

> **writeSymbol**(`text`, `symbol`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2565

#### Parameters

##### text

`string`

##### symbol

[`Symbol`](Symbol.md)

#### Returns

`void`

#### Inherited from

`SymbolWriter.writeSymbol`

***

### writeTrailingSemicolon()

> **writeTrailingSemicolon**(`text`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4321

#### Parameters

##### text

`string`

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EmptyStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EmptyStatement

# Interface: EmptyStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1483

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

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Statement`](Statement.md).[`flags`](Statement.md#flags)

***

### kind

> `readonly` **kind**: [`EmptyStatement`](../enumerations/SyntaxKind.md#emptystatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1484

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EnumDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EnumDeclaration

# Interface: EnumDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1668

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

> `readonly` **kind**: [`EnumDeclaration`](../enumerations/SyntaxKind.md#enumdeclaration)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1669

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

> `readonly` **members**: [`NodeArray`](NodeArray.md)\<[`EnumMember`](EnumMember.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1672

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`Modifier`](../type-aliases/Modifier.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1670

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1671

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EnumMember.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EnumMember

# Interface: EnumMember

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1662

## Extends

- [`NamedDeclaration`](NamedDeclaration.md).[`JSDocContainer`](JSDocContainer.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`_declarationBrand`](NamedDeclaration.md#_declarationbrand)

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

[`NamedDeclaration`](NamedDeclaration.md).[`decorators`](NamedDeclaration.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`end`](NamedDeclaration.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`flags`](NamedDeclaration.md#flags)

***

### initializer?

> `readonly` `optional` **initializer**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1666

***

### kind

> `readonly` **kind**: [`EnumMember`](../enumerations/SyntaxKind.md#enummember)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1663

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`kind`](NamedDeclaration.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`locals`](NamedDeclaration.md#locals)

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

[`NamedDeclaration`](NamedDeclaration.md).[`modifiers`](NamedDeclaration.md#modifiers)

***

### name

> `readonly` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1665

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`name`](NamedDeclaration.md#name)

***

### parent

> `readonly` **parent**: [`EnumDeclaration`](EnumDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1664

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`parent`](NamedDeclaration.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`pos`](NamedDeclaration.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`skipCheck`](NamedDeclaration.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`symbol`](NamedDeclaration.md#symbol)

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

[`NamedDeclaration`](NamedDeclaration.md).[`forEachChild`](NamedDeclaration.md#foreachchild)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getChildAt`](NamedDeclaration.md#getchildat)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getChildCount`](NamedDeclaration.md#getchildcount)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getChildren`](NamedDeclaration.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`getEnd`](NamedDeclaration.md#getend)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getFirstToken`](NamedDeclaration.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`getFullStart`](NamedDeclaration.md#getfullstart)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getFullText`](NamedDeclaration.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`getFullWidth`](NamedDeclaration.md#getfullwidth)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getLastToken`](NamedDeclaration.md#getlasttoken)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getLeadingTriviaWidth`](NamedDeclaration.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`getSourceFile`](NamedDeclaration.md#getsourcefile)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getStart`](NamedDeclaration.md#getstart)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getText`](NamedDeclaration.md#gettext)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getWidth`](NamedDeclaration.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EnumType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EnumType

# Interface: EnumType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2794

## Extends

- [`Type`](Type.md)

## Properties

### aliasSymbol?

> `optional` **aliasSymbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2773

#### Inherited from

[`Type`](Type.md).[`aliasSymbol`](Type.md#aliassymbol)

***

### aliasTypeArguments?

> `optional` **aliasTypeArguments**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2774

#### Inherited from

[`Type`](Type.md).[`aliasTypeArguments`](Type.md#aliastypearguments)

***

### flags

> **flags**: [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2770

#### Inherited from

[`Type`](Type.md).[`flags`](Type.md#flags)

***

### pattern?

> `optional` **pattern**: [`DestructuringPattern`](../type-aliases/DestructuringPattern.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2772

#### Inherited from

[`Type`](Type.md).[`pattern`](Type.md#pattern)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2771

#### Inherited from

[`Type`](Type.md).[`symbol`](Type.md#symbol)

## Methods

### getApparentProperties()

> **getApparentProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6124

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`Type`](Type.md).[`getApparentProperties`](Type.md#getapparentproperties)

***

### getBaseTypes()

> **getBaseTypes**(): `undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6129

#### Returns

`undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

#### Inherited from

[`Type`](Type.md).[`getBaseTypes`](Type.md#getbasetypes)

***

### getCallSignatures()

> **getCallSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6125

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`Type`](Type.md).[`getCallSignatures`](Type.md#getcallsignatures)

***

### getConstraint()

> **getConstraint**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6131

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`Type`](Type.md).[`getConstraint`](Type.md#getconstraint)

***

### getConstructSignatures()

> **getConstructSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6126

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`Type`](Type.md).[`getConstructSignatures`](Type.md#getconstructsignatures)

***

### getDefault()

> **getDefault**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6132

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`Type`](Type.md).[`getDefault`](Type.md#getdefault)

***

### getFlags()

> **getFlags**(): [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6120

#### Returns

[`TypeFlags`](../enumerations/TypeFlags.md)

#### Inherited from

[`Type`](Type.md).[`getFlags`](Type.md#getflags)

***

### getNonNullableType()

> **getNonNullableType**(): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6130

#### Returns

[`Type`](Type.md)

#### Inherited from

[`Type`](Type.md).[`getNonNullableType`](Type.md#getnonnullabletype)

***

### getNumberIndexType()

> **getNumberIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6128

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`Type`](Type.md).[`getNumberIndexType`](Type.md#getnumberindextype)

***

### getProperties()

> **getProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6122

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`Type`](Type.md).[`getProperties`](Type.md#getproperties)

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

[`Type`](Type.md).[`getProperty`](Type.md#getproperty)

***

### getStringIndexType()

> **getStringIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6127

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`Type`](Type.md).[`getStringIndexType`](Type.md#getstringindextype)

***

### getSymbol()

> **getSymbol**(): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6121

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`Type`](Type.md).[`getSymbol`](Type.md#getsymbol)

***

### isClass()

> **isClass**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6141

#### Returns

`this is InterfaceType`

#### Inherited from

[`Type`](Type.md).[`isClass`](Type.md#isclass)

***

### isClassOrInterface()

> **isClassOrInterface**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6140

#### Returns

`this is InterfaceType`

#### Inherited from

[`Type`](Type.md).[`isClassOrInterface`](Type.md#isclassorinterface)

***

### isIndexType()

> **isIndexType**(): `this is IndexType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6142

#### Returns

`this is IndexType`

#### Inherited from

[`Type`](Type.md).[`isIndexType`](Type.md#isindextype)

***

### isIntersection()

> **isIntersection**(): `this is IntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6134

#### Returns

`this is IntersectionType`

#### Inherited from

[`Type`](Type.md).[`isIntersection`](Type.md#isintersection)

***

### isLiteral()

> **isLiteral**(): `this is LiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6136

#### Returns

`this is LiteralType`

#### Inherited from

[`Type`](Type.md).[`isLiteral`](Type.md#isliteral)

***

### isNumberLiteral()

> **isNumberLiteral**(): `this is NumberLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6138

#### Returns

`this is NumberLiteralType`

#### Inherited from

[`Type`](Type.md).[`isNumberLiteral`](Type.md#isnumberliteral)

***

### isStringLiteral()

> **isStringLiteral**(): `this is StringLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6137

#### Returns

`this is StringLiteralType`

#### Inherited from

[`Type`](Type.md).[`isStringLiteral`](Type.md#isstringliteral)

***

### isTypeParameter()

> **isTypeParameter**(): `this is TypeParameter`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6139

#### Returns

`this is TypeParameter`

#### Inherited from

[`Type`](Type.md).[`isTypeParameter`](Type.md#istypeparameter)

***

### isUnion()

> **isUnion**(): `this is UnionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6133

#### Returns

`this is UnionType`

#### Inherited from

[`Type`](Type.md).[`isUnion`](Type.md#isunion)

***

### isUnionOrIntersection()

> **isUnionOrIntersection**(): `this is UnionOrIntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6135

#### Returns

`this is UnionOrIntersectionType`

#### Inherited from

[`Type`](Type.md).[`isUnionOrIntersection`](Type.md#isunionorintersection)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EtsComponentExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EtsComponentExpression

# Interface: EtsComponentExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1204

## Extends

- [`PrimaryExpression`](PrimaryExpression.md).[`Declaration`](Declaration.md)

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

### arguments

> `readonly` **arguments**: [`NodeArray`](NodeArray.md)\<[`Expression`](Expression.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1208

***

### body?

> `readonly` `optional` **body**: [`Block`](Block.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1209

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

### expression

> `readonly` **expression**: [`LeftHandSideExpression`](LeftHandSideExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1206

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Declaration`](Declaration.md).[`flags`](Declaration.md#flags)

***

### kind

> `readonly` **kind**: [`EtsComponentExpression`](../enumerations/SyntaxKind.md#etscomponentexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1205

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

### typeArguments?

> `readonly` `optional` **typeArguments**: [`NodeArray`](NodeArray.md)\<[`TypeNode`](TypeNode.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1207

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EtsOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EtsOptions

# Interface: EtsOptions

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3181

## Properties

### components

> **components**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3186

***

### concurrent

> **concurrent**: `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3205

#### decorator

> **decorator**: `string`

***

### customComponent?

> `optional` **customComponent**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3208

***

### emitDecorators

> **emitDecorators**: `object`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3213

#### emitParameters

> **emitParameters**: `boolean`

#### name

> **name**: `string`

***

### extend

> **extend**: `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3188

#### components

> **components**: `object`[]

#### decorator

> **decorator**: `string`[]

***

### libs

> **libs**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3187

***

### propertyDecorators

> **propertyDecorators**: `object`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3209

#### name

> **name**: `string`

#### needInitialization

> **needInitialization**: `boolean`

***

### render

> **render**: `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3182

#### decorator

> **decorator**: `string`[]

#### method

> **method**: `string`[]

***

### styles

> **styles**: `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3196

#### component

> **component**: `object`

##### component.instance

> **instance**: `string`

##### component.name

> **name**: `string`

##### component.type

> **type**: `string`

#### decorator

> **decorator**: `string`

#### property

> **property**: `string`

***

### syntaxComponents

> **syntaxComponents**: `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3217

#### attrUICallback

> **attrUICallback**: `object`[]

#### paramsUICallback

> **paramsUICallback**: `string`[]




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/EvolvingArrayType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / EvolvingArrayType

# Interface: EvolvingArrayType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2882

## Extends

- [`ObjectType`](ObjectType.md)

## Properties

### aliasSymbol?

> `optional` **aliasSymbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2773

#### Inherited from

[`ObjectType`](ObjectType.md).[`aliasSymbol`](ObjectType.md#aliassymbol)

***

### aliasTypeArguments?

> `optional` **aliasTypeArguments**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2774

#### Inherited from

[`ObjectType`](ObjectType.md).[`aliasTypeArguments`](ObjectType.md#aliastypearguments)

***

### elementType

> **elementType**: [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2883

***

### finalArrayType?

> `optional` **finalArrayType**: [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2884

***

### flags

> **flags**: [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2770

#### Inherited from

[`ObjectType`](ObjectType.md).[`flags`](ObjectType.md#flags)

***

### objectFlags

> **objectFlags**: [`ObjectFlags`](../enumerations/ObjectFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2818

#### Inherited from

[`ObjectType`](ObjectType.md).[`objectFlags`](ObjectType.md#objectflags)

***

### pattern?

> `optional` **pattern**: [`DestructuringPattern`](../type-aliases/DestructuringPattern.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2772

#### Inherited from

[`ObjectType`](ObjectType.md).[`pattern`](ObjectType.md#pattern)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2771

#### Inherited from

[`ObjectType`](ObjectType.md).[`symbol`](ObjectType.md#symbol)

## Methods

### getApparentProperties()

> **getApparentProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6124

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`ObjectType`](ObjectType.md).[`getApparentProperties`](ObjectType.md#getapparentproperties)

***

### getBaseTypes()

> **getBaseTypes**(): `undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6129

#### Returns

`undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

#### Inherited from

[`ObjectType`](ObjectType.md).[`getBaseTypes`](ObjectType.md#getbasetypes)

***

### getCallSignatures()

> **getCallSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6125

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`ObjectType`](ObjectType.md).[`getCallSignatures`](ObjectType.md#getcallsignatures)

***

### getConstraint()

> **getConstraint**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6131

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`ObjectType`](ObjectType.md).[`getConstraint`](ObjectType.md#getconstraint)

***

### getConstructSignatures()

> **getConstructSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6126

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`ObjectType`](ObjectType.md).[`getConstructSignatures`](ObjectType.md#getconstructsignatures)

***

### getDefault()

> **getDefault**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6132

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`ObjectType`](ObjectType.md).[`getDefault`](ObjectType.md#getdefault)

***

### getFlags()

> **getFlags**(): [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6120

#### Returns

[`TypeFlags`](../enumerations/TypeFlags.md)

#### Inherited from

[`ObjectType`](ObjectType.md).[`getFlags`](ObjectType.md#getflags)

***

### getNonNullableType()

> **getNonNullableType**(): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6130

#### Returns

[`Type`](Type.md)

#### Inherited from

[`ObjectType`](ObjectType.md).[`getNonNullableType`](ObjectType.md#getnonnullabletype)

***

### getNumberIndexType()

> **getNumberIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6128

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`ObjectType`](ObjectType.md).[`getNumberIndexType`](ObjectType.md#getnumberindextype)

***

### getProperties()

> **getProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6122

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`ObjectType`](ObjectType.md).[`getProperties`](ObjectType.md#getproperties)

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

[`ObjectType`](ObjectType.md).[`getProperty`](ObjectType.md#getproperty)

***

### getStringIndexType()

> **getStringIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6127

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`ObjectType`](ObjectType.md).[`getStringIndexType`](ObjectType.md#getstringindextype)

***

### getSymbol()

> **getSymbol**(): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6121

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`ObjectType`](ObjectType.md).[`getSymbol`](ObjectType.md#getsymbol)

***

### isClass()

> **isClass**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6141

#### Returns

`this is InterfaceType`

#### Inherited from

[`ObjectType`](ObjectType.md).[`isClass`](ObjectType.md#isclass)

***

### isClassOrInterface()

> **isClassOrInterface**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6140

#### Returns

`this is InterfaceType`

#### Inherited from

[`ObjectType`](ObjectType.md).[`isClassOrInterface`](ObjectType.md#isclassorinterface)

***

### isIndexType()

> **isIndexType**(): `this is IndexType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6142

#### Returns

`this is IndexType`

#### Inherited from

[`ObjectType`](ObjectType.md).[`isIndexType`](ObjectType.md#isindextype)

***

### isIntersection()

> **isIntersection**(): `this is IntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6134

#### Returns

`this is IntersectionType`

#### Inherited from

[`ObjectType`](ObjectType.md).[`isIntersection`](ObjectType.md#isintersection)

***

### isLiteral()

> **isLiteral**(): `this is LiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6136

#### Returns

`this is LiteralType`

#### Inherited from

[`ObjectType`](ObjectType.md).[`isLiteral`](ObjectType.md#isliteral)

***

### isNumberLiteral()

> **isNumberLiteral**(): `this is NumberLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6138

#### Returns

`this is NumberLiteralType`

#### Inherited from

[`ObjectType`](ObjectType.md).[`isNumberLiteral`](ObjectType.md#isnumberliteral)

***

### isStringLiteral()

> **isStringLiteral**(): `this is StringLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6137

#### Returns

`this is StringLiteralType`

#### Inherited from

[`ObjectType`](ObjectType.md).[`isStringLiteral`](ObjectType.md#isstringliteral)

***

### isTypeParameter()

> **isTypeParameter**(): `this is TypeParameter`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6139

#### Returns

`this is TypeParameter`

#### Inherited from

[`ObjectType`](ObjectType.md).[`isTypeParameter`](ObjectType.md#istypeparameter)

***

### isUnion()

> **isUnion**(): `this is UnionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6133

#### Returns

`this is UnionType`

#### Inherited from

[`ObjectType`](ObjectType.md).[`isUnion`](ObjectType.md#isunion)

***

### isUnionOrIntersection()

> **isUnionOrIntersection**(): `this is UnionOrIntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6135

#### Returns

`this is UnionOrIntersectionType`

#### Inherited from

[`ObjectType`](ObjectType.md).[`isUnionOrIntersection`](ObjectType.md#isunionorintersection)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ExportAssignment.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ExportAssignment

# Interface: ExportAssignment

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1831

This is either an `export =` or an `export default` declaration.
Unless `isExportEquals` is set, this node was parsed as an `export default`.

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

### expression

> `readonly` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1836

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`flags`](DeclarationStatement.md#flags)

***

### isExportEquals?

> `readonly` `optional` **isExportEquals**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1835

***

### kind

> `readonly` **kind**: [`ExportAssignment`](../enumerations/SyntaxKind.md#exportassignment)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1832

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1834

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

> `readonly` `optional` **name**: [`Identifier`](Identifier.md) \| [`StringLiteral`](StringLiteral.md) \| [`NumericLiteral`](NumericLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:705

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`name`](DeclarationStatement.md#name)

***

### parent

> `readonly` **parent**: [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1833

#### Overrides

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ExportDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ExportDeclaration

# Interface: ExportDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1763

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

### assertClause?

> `readonly` `optional` **assertClause**: [`AssertClause`](AssertClause.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1772

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

### exportClause?

> `readonly` `optional` **exportClause**: [`NamedExportBindings`](../type-aliases/NamedExportBindings.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1769

Will not be assigned in the case of `export * from "foo";`

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`flags`](DeclarationStatement.md#flags)

***

### isTypeOnly

> `readonly` **isTypeOnly**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1767

***

### kind

> `readonly` **kind**: [`ExportDeclaration`](../enumerations/SyntaxKind.md#exportdeclaration)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1764

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1766

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

### moduleSpecifier?

> `readonly` `optional` **moduleSpecifier**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1771

If this is not a StringLiteral it will be a grammar error.

***

### name?

> `readonly` `optional` **name**: [`Identifier`](Identifier.md) \| [`StringLiteral`](StringLiteral.md) \| [`NumericLiteral`](NumericLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:705

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`name`](DeclarationStatement.md#name)

***

### parent

> `readonly` **parent**: [`SourceFile`](SourceFile.md) \| [`ModuleBlock`](ModuleBlock.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1765

#### Overrides

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ExportSpecifier.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ExportSpecifier

# Interface: ExportSpecifier

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1792

## Extends

- [`NamedDeclaration`](NamedDeclaration.md).[`JSDocContainer`](JSDocContainer.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`_declarationBrand`](NamedDeclaration.md#_declarationbrand)

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

[`NamedDeclaration`](NamedDeclaration.md).[`decorators`](NamedDeclaration.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`end`](NamedDeclaration.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`flags`](NamedDeclaration.md#flags)

***

### isTypeOnly

> `readonly` **isTypeOnly**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1795

***

### kind

> `readonly` **kind**: [`ExportSpecifier`](../enumerations/SyntaxKind.md#exportspecifier)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1793

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`kind`](NamedDeclaration.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`locals`](NamedDeclaration.md#locals)

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

[`NamedDeclaration`](NamedDeclaration.md).[`modifiers`](NamedDeclaration.md#modifiers)

***

### name

> `readonly` **name**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1797

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`name`](NamedDeclaration.md#name)

***

### parent

> `readonly` **parent**: [`NamedExports`](NamedExports.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1794

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`parent`](NamedDeclaration.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`pos`](NamedDeclaration.md#pos)

***

### propertyName?

> `readonly` `optional` **propertyName**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1796

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`skipCheck`](NamedDeclaration.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`symbol`](NamedDeclaration.md#symbol)

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

[`NamedDeclaration`](NamedDeclaration.md).[`forEachChild`](NamedDeclaration.md#foreachchild)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getChildAt`](NamedDeclaration.md#getchildat)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getChildCount`](NamedDeclaration.md#getchildcount)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getChildren`](NamedDeclaration.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`getEnd`](NamedDeclaration.md#getend)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getFirstToken`](NamedDeclaration.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`getFullStart`](NamedDeclaration.md#getfullstart)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getFullText`](NamedDeclaration.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`getFullWidth`](NamedDeclaration.md#getfullwidth)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getLastToken`](NamedDeclaration.md#getlasttoken)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getLeadingTriviaWidth`](NamedDeclaration.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`getSourceFile`](NamedDeclaration.md#getsourcefile)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getStart`](NamedDeclaration.md#getstart)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getText`](NamedDeclaration.md#gettext)

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

[`NamedDeclaration`](NamedDeclaration.md).[`getWidth`](NamedDeclaration.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Expression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Expression

# Interface: Expression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1055

## Extends

- [`Node`](Node.md)

## Extended by

- [`OmittedExpression`](OmittedExpression.md)
- [`UnaryExpression`](UnaryExpression.md)
- [`YieldExpression`](YieldExpression.md)
- [`SyntheticExpression`](SyntheticExpression.md)
- [`BinaryExpression`](BinaryExpression.md)
- [`ConditionalExpression`](ConditionalExpression.md)
- [`ArrowFunction`](ArrowFunction.md)
- [`SpreadElement`](SpreadElement.md)
- [`AsExpression`](AsExpression.md)
- [`SatisfiesExpression`](SatisfiesExpression.md)
- [`JsxOpeningElement`](JsxOpeningElement.md)
- [`JsxOpeningFragment`](JsxOpeningFragment.md)
- [`JsxClosingFragment`](JsxClosingFragment.md)
- [`JsxExpression`](JsxExpression.md)
- [`CommaListExpression`](CommaListExpression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ExpressionStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ExpressionStatement

# Interface: ExpressionStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1503

## Extends

- [`Statement`](Statement.md)

## Extended by

- [`JsonObjectExpressionStatement`](JsonObjectExpressionStatement.md)

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1505

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Statement`](Statement.md).[`flags`](Statement.md#flags)

***

### kind

> `readonly` **kind**: [`ExpressionStatement`](../enumerations/SyntaxKind.md#expressionstatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1504

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ExpressionWithTypeArguments.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ExpressionWithTypeArguments

# Interface: ExpressionWithTypeArguments

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1353

## Extends

- [`MemberExpression`](MemberExpression.md).[`NodeWithTypeArguments`](NodeWithTypeArguments.md)

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

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`_typeNodeBrand`](NodeWithTypeArguments.md#_typenodebrand)

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

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`decorators`](NodeWithTypeArguments.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`end`](NodeWithTypeArguments.md#end)

***

### expression

> `readonly` **expression**: [`LeftHandSideExpression`](LeftHandSideExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1355

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`flags`](NodeWithTypeArguments.md#flags)

***

### kind

> `readonly` **kind**: [`ExpressionWithTypeArguments`](../enumerations/SyntaxKind.md#expressionwithtypearguments)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1354

#### Overrides

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`kind`](NodeWithTypeArguments.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`locals`](NodeWithTypeArguments.md#locals)

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

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`modifiers`](NodeWithTypeArguments.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`parent`](NodeWithTypeArguments.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`pos`](NodeWithTypeArguments.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`skipCheck`](NodeWithTypeArguments.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`symbol`](NodeWithTypeArguments.md#symbol)

***

### typeArguments?

> `readonly` `optional` **typeArguments**: [`NodeArray`](NodeArray.md)\<[`TypeNode`](TypeNode.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:946

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`typeArguments`](NodeWithTypeArguments.md#typearguments)

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

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`forEachChild`](NodeWithTypeArguments.md#foreachchild)

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

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getChildAt`](NodeWithTypeArguments.md#getchildat)

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

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getChildCount`](NodeWithTypeArguments.md#getchildcount)

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

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getChildren`](NodeWithTypeArguments.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getEnd`](NodeWithTypeArguments.md#getend)

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

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getFirstToken`](NodeWithTypeArguments.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getFullStart`](NodeWithTypeArguments.md#getfullstart)

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

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getFullText`](NodeWithTypeArguments.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getFullWidth`](NodeWithTypeArguments.md#getfullwidth)

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

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getLastToken`](NodeWithTypeArguments.md#getlasttoken)

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

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getLeadingTriviaWidth`](NodeWithTypeArguments.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getSourceFile`](NodeWithTypeArguments.md#getsourcefile)

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

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getStart`](NodeWithTypeArguments.md#getstart)

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

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getText`](NodeWithTypeArguments.md#gettext)

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

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`getWidth`](NodeWithTypeArguments.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ExtendedConfigCacheEntry.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ExtendedConfigCacheEntry

# Interface: ExtendedConfigCacheEntry

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5331

## Properties

### extendedConfig

> **extendedConfig**: `undefined` \| [`ParsedTsconfig`](ParsedTsconfig.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5333

***

### extendedResult

> **extendedResult**: [`TsConfigSourceFile`](TsConfigSourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5332




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ExternalModuleReference.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ExternalModuleReference

# Interface: ExternalModuleReference

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1712

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1715

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Node`](Node.md).[`flags`](Node.md#flags)

***

### kind

> `readonly` **kind**: [`ExternalModuleReference`](../enumerations/SyntaxKind.md#externalmodulereference)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1713

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

> `readonly` **parent**: [`ImportEqualsDeclaration`](ImportEqualsDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1714

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FalseLiteral.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FalseLiteral

# Interface: FalseLiteral

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1100

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

> `readonly` **kind**: [`FalseKeyword`](../enumerations/SyntaxKind.md#falsekeyword)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1101

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FileCheckModuleInfo.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FileCheckModuleInfo

# Interface: FileCheckModuleInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3439

## Properties

### checkPayload

> **checkPayload**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3441

***

### currentFileName

> **currentFileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3442

***

### fileNeedCheck

> **fileNeedCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3440




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FileExtensionInfo.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FileExtensionInfo

# Interface: FileExtensionInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2969

## Properties

### extension

> **extension**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2970

***

### isMixedContent

> **isMixedContent**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2971

***

### scriptKind?

> `optional` **scriptKind**: [`ScriptKind`](../enumerations/ScriptKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2972




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FileReference.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FileReference

# Interface: FileReference

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1838

## Extends

- [`TextRange`](TextRange.md)

## Properties

### end

> **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:99

#### Inherited from

[`TextRange`](TextRange.md).[`end`](TextRange.md#end)

***

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1839

***

### pos

> **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:98

#### Inherited from

[`TextRange`](TextRange.md).[`pos`](TextRange.md#pos)

***

### resolutionMode?

> `optional` **resolutionMode**: [`CommonJS`](../enumerations/ModuleKind.md#commonjs) \| [`ESNext`](../enumerations/ModuleKind.md#esnext)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1840




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FileTextChanges.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FileTextChanges

# Interface: FileTextChanges

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6603

## Properties

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6604

***

### isNewFile?

> `optional` **isNewFile**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6606

***

### textChanges

> **textChanges**: readonly [`TextChange`](TextChange.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6605




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FileWatcher.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FileWatcher

# Interface: FileWatcher

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4565

## Methods

### close()

> **close**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4566

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FlowArrayMutation.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FlowArrayMutation

# Interface: FlowArrayMutation

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2091

## Extends

- [`FlowNodeBase`](FlowNodeBase.md)

## Properties

### antecedent

> **antecedent**: [`FlowNode`](../type-aliases/FlowNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2093

***

### flags

> **flags**: [`FlowFlags`](../enumerations/FlowFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2064

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`flags`](FlowNodeBase.md#flags)

***

### id?

> `optional` **id**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2065

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`id`](FlowNodeBase.md#id)

***

### node

> **node**: [`BinaryExpression`](BinaryExpression.md) \| [`CallExpression`](CallExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2092




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FlowAssignment.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FlowAssignment

# Interface: FlowAssignment

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2073

## Extends

- [`FlowNodeBase`](FlowNodeBase.md)

## Properties

### antecedent

> **antecedent**: [`FlowNode`](../type-aliases/FlowNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2075

***

### flags

> **flags**: [`FlowFlags`](../enumerations/FlowFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2064

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`flags`](FlowNodeBase.md#flags)

***

### id?

> `optional` **id**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2065

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`id`](FlowNodeBase.md#id)

***

### node

> **node**: [`Expression`](Expression.md) \| [`VariableDeclaration`](VariableDeclaration.md) \| [`BindingElement`](BindingElement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2074




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FlowCall.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FlowCall

# Interface: FlowCall

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2077

## Extends

- [`FlowNodeBase`](FlowNodeBase.md)

## Properties

### antecedent

> **antecedent**: [`FlowNode`](../type-aliases/FlowNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2079

***

### flags

> **flags**: [`FlowFlags`](../enumerations/FlowFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2064

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`flags`](FlowNodeBase.md#flags)

***

### id?

> `optional` **id**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2065

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`id`](FlowNodeBase.md#id)

***

### node

> **node**: [`CallExpression`](CallExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2078




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FlowCondition.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FlowCondition

# Interface: FlowCondition

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2081

## Extends

- [`FlowNodeBase`](FlowNodeBase.md)

## Properties

### antecedent

> **antecedent**: [`FlowNode`](../type-aliases/FlowNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2083

***

### flags

> **flags**: [`FlowFlags`](../enumerations/FlowFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2064

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`flags`](FlowNodeBase.md#flags)

***

### id?

> `optional` **id**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2065

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`id`](FlowNodeBase.md#id)

***

### node

> **node**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2082




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FlowLabel.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FlowLabel

# Interface: FlowLabel

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2070

## Extends

- [`FlowNodeBase`](FlowNodeBase.md)

## Properties

### antecedents

> **antecedents**: `undefined` \| [`FlowNode`](../type-aliases/FlowNode.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2071

***

### flags

> **flags**: [`FlowFlags`](../enumerations/FlowFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2064

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`flags`](FlowNodeBase.md#flags)

***

### id?

> `optional` **id**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2065

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`id`](FlowNodeBase.md#id)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FlowNodeBase.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FlowNodeBase

# Interface: FlowNodeBase

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2063

## Extended by

- [`FlowStart`](FlowStart.md)
- [`FlowLabel`](FlowLabel.md)
- [`FlowAssignment`](FlowAssignment.md)
- [`FlowCall`](FlowCall.md)
- [`FlowCondition`](FlowCondition.md)
- [`FlowSwitchClause`](FlowSwitchClause.md)
- [`FlowArrayMutation`](FlowArrayMutation.md)
- [`FlowReduceLabel`](FlowReduceLabel.md)

## Properties

### flags

> **flags**: [`FlowFlags`](../enumerations/FlowFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2064

***

### id?

> `optional` **id**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2065




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FlowReduceLabel.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FlowReduceLabel

# Interface: FlowReduceLabel

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2095

## Extends

- [`FlowNodeBase`](FlowNodeBase.md)

## Properties

### antecedent

> **antecedent**: [`FlowNode`](../type-aliases/FlowNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2098

***

### antecedents

> **antecedents**: [`FlowNode`](../type-aliases/FlowNode.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2097

***

### flags

> **flags**: [`FlowFlags`](../enumerations/FlowFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2064

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`flags`](FlowNodeBase.md#flags)

***

### id?

> `optional` **id**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2065

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`id`](FlowNodeBase.md#id)

***

### target

> **target**: [`FlowLabel`](FlowLabel.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2096




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FlowStart.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FlowStart

# Interface: FlowStart

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2067

## Extends

- [`FlowNodeBase`](FlowNodeBase.md)

## Properties

### flags

> **flags**: [`FlowFlags`](../enumerations/FlowFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2064

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`flags`](FlowNodeBase.md#flags)

***

### id?

> `optional` **id**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2065

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`id`](FlowNodeBase.md#id)

***

### node?

> `optional` **node**: [`MethodDeclaration`](MethodDeclaration.md) \| [`GetAccessorDeclaration`](GetAccessorDeclaration.md) \| [`SetAccessorDeclaration`](SetAccessorDeclaration.md) \| [`FunctionExpression`](FunctionExpression.md) \| [`ArrowFunction`](ArrowFunction.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2068




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FlowSwitchClause.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FlowSwitchClause

# Interface: FlowSwitchClause

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2085

## Extends

- [`FlowNodeBase`](FlowNodeBase.md)

## Properties

### antecedent

> **antecedent**: [`FlowNode`](../type-aliases/FlowNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2089

***

### clauseEnd

> **clauseEnd**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2088

***

### clauseStart

> **clauseStart**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2087

***

### flags

> **flags**: [`FlowFlags`](../enumerations/FlowFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2064

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`flags`](FlowNodeBase.md#flags)

***

### id?

> `optional` **id**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2065

#### Inherited from

[`FlowNodeBase`](FlowNodeBase.md).[`id`](FlowNodeBase.md#id)

***

### switchStatement

> **switchStatement**: [`SwitchStatement`](SwitchStatement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2086




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ForInStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ForInStatement

# Interface: ForInStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1532

## Extends

- [`IterationStatement`](IterationStatement.md)

## Properties

### \_statementBrand

> **\_statementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1471

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`_statementBrand`](IterationStatement.md#_statementbrand)

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

[`IterationStatement`](IterationStatement.md).[`decorators`](IterationStatement.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`end`](IterationStatement.md#end)

***

### expression

> `readonly` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1535

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`flags`](IterationStatement.md#flags)

***

### initializer

> `readonly` **initializer**: [`ForInitializer`](../type-aliases/ForInitializer.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1534

***

### kind

> `readonly` **kind**: [`ForInStatement`](../enumerations/SyntaxKind.md#forinstatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1533

#### Overrides

[`IterationStatement`](IterationStatement.md).[`kind`](IterationStatement.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`locals`](IterationStatement.md#locals)

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

[`IterationStatement`](IterationStatement.md).[`modifiers`](IterationStatement.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`parent`](IterationStatement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`pos`](IterationStatement.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`skipCheck`](IterationStatement.md#skipcheck)

***

### statement

> `readonly` **statement**: [`Statement`](Statement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1514

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`statement`](IterationStatement.md#statement)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`symbol`](IterationStatement.md#symbol)

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

[`IterationStatement`](IterationStatement.md).[`forEachChild`](IterationStatement.md#foreachchild)

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

[`IterationStatement`](IterationStatement.md).[`getChildAt`](IterationStatement.md#getchildat)

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

[`IterationStatement`](IterationStatement.md).[`getChildCount`](IterationStatement.md#getchildcount)

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

[`IterationStatement`](IterationStatement.md).[`getChildren`](IterationStatement.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getEnd`](IterationStatement.md#getend)

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

[`IterationStatement`](IterationStatement.md).[`getFirstToken`](IterationStatement.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getFullStart`](IterationStatement.md#getfullstart)

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

[`IterationStatement`](IterationStatement.md).[`getFullText`](IterationStatement.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getFullWidth`](IterationStatement.md#getfullwidth)

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

[`IterationStatement`](IterationStatement.md).[`getLastToken`](IterationStatement.md#getlasttoken)

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

[`IterationStatement`](IterationStatement.md).[`getLeadingTriviaWidth`](IterationStatement.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getSourceFile`](IterationStatement.md#getsourcefile)

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

[`IterationStatement`](IterationStatement.md).[`getStart`](IterationStatement.md#getstart)

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

[`IterationStatement`](IterationStatement.md).[`getText`](IterationStatement.md#gettext)

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

[`IterationStatement`](IterationStatement.md).[`getWidth`](IterationStatement.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ForOfStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ForOfStatement

# Interface: ForOfStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1537

## Extends

- [`IterationStatement`](IterationStatement.md)

## Properties

### \_statementBrand

> **\_statementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1471

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`_statementBrand`](IterationStatement.md#_statementbrand)

***

### awaitModifier?

> `readonly` `optional` **awaitModifier**: [`AwaitKeyword`](../type-aliases/AwaitKeyword.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1539

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

[`IterationStatement`](IterationStatement.md).[`decorators`](IterationStatement.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`end`](IterationStatement.md#end)

***

### expression

> `readonly` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1541

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`flags`](IterationStatement.md#flags)

***

### initializer

> `readonly` **initializer**: [`ForInitializer`](../type-aliases/ForInitializer.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1540

***

### kind

> `readonly` **kind**: [`ForOfStatement`](../enumerations/SyntaxKind.md#forofstatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1538

#### Overrides

[`IterationStatement`](IterationStatement.md).[`kind`](IterationStatement.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`locals`](IterationStatement.md#locals)

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

[`IterationStatement`](IterationStatement.md).[`modifiers`](IterationStatement.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`parent`](IterationStatement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`pos`](IterationStatement.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`skipCheck`](IterationStatement.md#skipcheck)

***

### statement

> `readonly` **statement**: [`Statement`](Statement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1514

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`statement`](IterationStatement.md#statement)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`symbol`](IterationStatement.md#symbol)

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

[`IterationStatement`](IterationStatement.md).[`forEachChild`](IterationStatement.md#foreachchild)

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

[`IterationStatement`](IterationStatement.md).[`getChildAt`](IterationStatement.md#getchildat)

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

[`IterationStatement`](IterationStatement.md).[`getChildCount`](IterationStatement.md#getchildcount)

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

[`IterationStatement`](IterationStatement.md).[`getChildren`](IterationStatement.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getEnd`](IterationStatement.md#getend)

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

[`IterationStatement`](IterationStatement.md).[`getFirstToken`](IterationStatement.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getFullStart`](IterationStatement.md#getfullstart)

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

[`IterationStatement`](IterationStatement.md).[`getFullText`](IterationStatement.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getFullWidth`](IterationStatement.md#getfullwidth)

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

[`IterationStatement`](IterationStatement.md).[`getLastToken`](IterationStatement.md#getlasttoken)

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

[`IterationStatement`](IterationStatement.md).[`getLeadingTriviaWidth`](IterationStatement.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getSourceFile`](IterationStatement.md#getsourcefile)

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

[`IterationStatement`](IterationStatement.md).[`getStart`](IterationStatement.md#getstart)

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

[`IterationStatement`](IterationStatement.md).[`getText`](IterationStatement.md#gettext)

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

[`IterationStatement`](IterationStatement.md).[`getWidth`](IterationStatement.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ForStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ForStatement

# Interface: ForStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1525

## Extends

- [`IterationStatement`](IterationStatement.md)

## Properties

### \_statementBrand

> **\_statementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1471

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`_statementBrand`](IterationStatement.md#_statementbrand)

***

### condition?

> `readonly` `optional` **condition**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1528

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

[`IterationStatement`](IterationStatement.md).[`decorators`](IterationStatement.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`end`](IterationStatement.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`flags`](IterationStatement.md#flags)

***

### incrementor?

> `readonly` `optional` **incrementor**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1529

***

### initializer?

> `readonly` `optional` **initializer**: [`ForInitializer`](../type-aliases/ForInitializer.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1527

***

### kind

> `readonly` **kind**: [`ForStatement`](../enumerations/SyntaxKind.md#forstatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1526

#### Overrides

[`IterationStatement`](IterationStatement.md).[`kind`](IterationStatement.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`locals`](IterationStatement.md#locals)

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

[`IterationStatement`](IterationStatement.md).[`modifiers`](IterationStatement.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`parent`](IterationStatement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`pos`](IterationStatement.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`skipCheck`](IterationStatement.md#skipcheck)

***

### statement

> `readonly` **statement**: [`Statement`](Statement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1514

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`statement`](IterationStatement.md#statement)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`symbol`](IterationStatement.md#symbol)

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

[`IterationStatement`](IterationStatement.md).[`forEachChild`](IterationStatement.md#foreachchild)

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

[`IterationStatement`](IterationStatement.md).[`getChildAt`](IterationStatement.md#getchildat)

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

[`IterationStatement`](IterationStatement.md).[`getChildCount`](IterationStatement.md#getchildcount)

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

[`IterationStatement`](IterationStatement.md).[`getChildren`](IterationStatement.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getEnd`](IterationStatement.md#getend)

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

[`IterationStatement`](IterationStatement.md).[`getFirstToken`](IterationStatement.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getFullStart`](IterationStatement.md#getfullstart)

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

[`IterationStatement`](IterationStatement.md).[`getFullText`](IterationStatement.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getFullWidth`](IterationStatement.md#getfullwidth)

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

[`IterationStatement`](IterationStatement.md).[`getLastToken`](IterationStatement.md#getlasttoken)

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

[`IterationStatement`](IterationStatement.md).[`getLeadingTriviaWidth`](IterationStatement.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`getSourceFile`](IterationStatement.md#getsourcefile)

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

[`IterationStatement`](IterationStatement.md).[`getStart`](IterationStatement.md#getstart)

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

[`IterationStatement`](IterationStatement.md).[`getText`](IterationStatement.md#gettext)

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

[`IterationStatement`](IterationStatement.md).[`getWidth`](IterationStatement.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FormatCodeOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FormatCodeOptions

# Interface: ~~FormatCodeOptions~~

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6781

## Deprecated

- consider using FormatCodeSettings instead

## Extends

- [`EditorOptions`](EditorOptions.md)

## Properties

### ~~BaseIndentSize?~~

> `optional` **BaseIndentSize**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6764

#### Inherited from

[`EditorOptions`](EditorOptions.md).[`BaseIndentSize`](EditorOptions.md#baseindentsize)

***

### ~~ConvertTabsToSpaces~~

> **ConvertTabsToSpaces**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6768

#### Inherited from

[`EditorOptions`](EditorOptions.md).[`ConvertTabsToSpaces`](EditorOptions.md#converttabstospaces)

***

### ~~IndentSize~~

> **IndentSize**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6765

#### Inherited from

[`EditorOptions`](EditorOptions.md).[`IndentSize`](EditorOptions.md#indentsize)

***

### ~~IndentStyle~~

> **IndentStyle**: [`IndentStyle`](../enumerations/IndentStyle.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6769

#### Inherited from

[`EditorOptions`](EditorOptions.md).[`IndentStyle`](EditorOptions.md#indentstyle)

***

### ~~InsertSpaceAfterCommaDelimiter~~

> **InsertSpaceAfterCommaDelimiter**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6782

***

### ~~InsertSpaceAfterConstructor?~~

> `optional` **InsertSpaceAfterConstructor**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6785

***

### ~~InsertSpaceAfterFunctionKeywordForAnonymousFunctions~~

> **InsertSpaceAfterFunctionKeywordForAnonymousFunctions**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6787

***

### ~~InsertSpaceAfterKeywordsInControlFlowStatements~~

> **InsertSpaceAfterKeywordsInControlFlowStatements**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6786

***

### ~~InsertSpaceAfterOpeningAndBeforeClosingJsxExpressionBraces?~~

> `optional` **InsertSpaceAfterOpeningAndBeforeClosingJsxExpressionBraces**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6792

***

### ~~InsertSpaceAfterOpeningAndBeforeClosingNonemptyBraces?~~

> `optional` **InsertSpaceAfterOpeningAndBeforeClosingNonemptyBraces**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6790

***

### ~~InsertSpaceAfterOpeningAndBeforeClosingNonemptyBrackets~~

> **InsertSpaceAfterOpeningAndBeforeClosingNonemptyBrackets**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6789

***

### ~~InsertSpaceAfterOpeningAndBeforeClosingNonemptyParenthesis~~

> **InsertSpaceAfterOpeningAndBeforeClosingNonemptyParenthesis**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6788

***

### ~~InsertSpaceAfterOpeningAndBeforeClosingTemplateStringBraces~~

> **InsertSpaceAfterOpeningAndBeforeClosingTemplateStringBraces**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6791

***

### ~~InsertSpaceAfterSemicolonInForStatements~~

> **InsertSpaceAfterSemicolonInForStatements**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6783

***

### ~~InsertSpaceAfterTypeAssertion?~~

> `optional` **InsertSpaceAfterTypeAssertion**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6793

***

### ~~InsertSpaceBeforeAndAfterBinaryOperators~~

> **InsertSpaceBeforeAndAfterBinaryOperators**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6784

***

### ~~InsertSpaceBeforeFunctionParenthesis?~~

> `optional` **InsertSpaceBeforeFunctionParenthesis**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6794

***

### ~~insertSpaceBeforeTypeAnnotation?~~

> `optional` **insertSpaceBeforeTypeAnnotation**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6797

***

### ~~NewLineCharacter~~

> **NewLineCharacter**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6767

#### Inherited from

[`EditorOptions`](EditorOptions.md).[`NewLineCharacter`](EditorOptions.md#newlinecharacter)

***

### ~~PlaceOpenBraceOnNewLineForControlBlocks~~

> **PlaceOpenBraceOnNewLineForControlBlocks**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6796

***

### ~~PlaceOpenBraceOnNewLineForFunctions~~

> **PlaceOpenBraceOnNewLineForFunctions**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6795

***

### ~~TabSize~~

> **TabSize**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6766

#### Inherited from

[`EditorOptions`](EditorOptions.md).[`TabSize`](EditorOptions.md#tabsize)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FormatCodeSettings.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FormatCodeSettings

# Interface: FormatCodeSettings

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6799

## Extends

- [`EditorSettings`](EditorSettings.md)

## Properties

### baseIndentSize?

> `optional` **baseIndentSize**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6772

#### Inherited from

[`EditorSettings`](EditorSettings.md).[`baseIndentSize`](EditorSettings.md#baseindentsize)

***

### convertTabsToSpaces?

> `optional` **convertTabsToSpaces**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6776

#### Inherited from

[`EditorSettings`](EditorSettings.md).[`convertTabsToSpaces`](EditorSettings.md#converttabstospaces)

***

### indentMultiLineObjectLiteralBeginningOnBlankLine?

> `readonly` `optional` **indentMultiLineObjectLiteralBeginningOnBlankLine**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6817

***

### indentSize?

> `optional` **indentSize**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6773

#### Inherited from

[`EditorSettings`](EditorSettings.md).[`indentSize`](EditorSettings.md#indentsize)

***

### indentStyle?

> `optional` **indentStyle**: [`IndentStyle`](../enumerations/IndentStyle.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6777

#### Inherited from

[`EditorSettings`](EditorSettings.md).[`indentStyle`](EditorSettings.md#indentstyle)

***

### insertSpaceAfterCommaDelimiter?

> `readonly` `optional` **insertSpaceAfterCommaDelimiter**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6800

***

### insertSpaceAfterConstructor?

> `readonly` `optional` **insertSpaceAfterConstructor**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6803

***

### insertSpaceAfterFunctionKeywordForAnonymousFunctions?

> `readonly` `optional` **insertSpaceAfterFunctionKeywordForAnonymousFunctions**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6805

***

### insertSpaceAfterKeywordsInControlFlowStatements?

> `readonly` `optional` **insertSpaceAfterKeywordsInControlFlowStatements**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6804

***

### insertSpaceAfterOpeningAndBeforeClosingEmptyBraces?

> `readonly` `optional` **insertSpaceAfterOpeningAndBeforeClosingEmptyBraces**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6809

***

### insertSpaceAfterOpeningAndBeforeClosingJsxExpressionBraces?

> `readonly` `optional` **insertSpaceAfterOpeningAndBeforeClosingJsxExpressionBraces**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6811

***

### insertSpaceAfterOpeningAndBeforeClosingNonemptyBraces?

> `readonly` `optional` **insertSpaceAfterOpeningAndBeforeClosingNonemptyBraces**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6808

***

### insertSpaceAfterOpeningAndBeforeClosingNonemptyBrackets?

> `readonly` `optional` **insertSpaceAfterOpeningAndBeforeClosingNonemptyBrackets**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6807

***

### insertSpaceAfterOpeningAndBeforeClosingNonemptyParenthesis?

> `readonly` `optional` **insertSpaceAfterOpeningAndBeforeClosingNonemptyParenthesis**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6806

***

### insertSpaceAfterOpeningAndBeforeClosingTemplateStringBraces?

> `readonly` `optional` **insertSpaceAfterOpeningAndBeforeClosingTemplateStringBraces**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6810

***

### insertSpaceAfterSemicolonInForStatements?

> `readonly` `optional` **insertSpaceAfterSemicolonInForStatements**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6801

***

### insertSpaceAfterTypeAssertion?

> `readonly` `optional` **insertSpaceAfterTypeAssertion**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6812

***

### insertSpaceBeforeAndAfterBinaryOperators?

> `readonly` `optional` **insertSpaceBeforeAndAfterBinaryOperators**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6802

***

### insertSpaceBeforeFunctionParenthesis?

> `readonly` `optional` **insertSpaceBeforeFunctionParenthesis**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6813

***

### insertSpaceBeforeTypeAnnotation?

> `readonly` `optional` **insertSpaceBeforeTypeAnnotation**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6816

***

### newLineCharacter?

> `optional` **newLineCharacter**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6775

#### Inherited from

[`EditorSettings`](EditorSettings.md).[`newLineCharacter`](EditorSettings.md#newlinecharacter)

***

### placeOpenBraceOnNewLineForControlBlocks?

> `readonly` `optional` **placeOpenBraceOnNewLineForControlBlocks**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6815

***

### placeOpenBraceOnNewLineForFunctions?

> `readonly` `optional` **placeOpenBraceOnNewLineForFunctions**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6814

***

### semicolons?

> `readonly` `optional` **semicolons**: [`SemicolonPreference`](../enumerations/SemicolonPreference.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6818

***

### tabSize?

> `optional` **tabSize**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6774

#### Inherited from

[`EditorSettings`](EditorSettings.md).[`tabSize`](EditorSettings.md#tabsize)

***

### trimTrailingWhitespace?

> `optional` **trimTrailingWhitespace**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6778

#### Inherited from

[`EditorSettings`](EditorSettings.md).[`trimTrailingWhitespace`](EditorSettings.md#trimtrailingwhitespace)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FormatDiagnosticsHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FormatDiagnosticsHost

# Interface: FormatDiagnosticsHost

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5547

## Methods

### getCanonicalFileName()

> **getCanonicalFileName**(`fileName`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5549

#### Parameters

##### fileName

`string`

#### Returns

`string`

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5548

#### Returns

`string`

***

### getNewLine()

> **getNewLine**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5550

#### Returns

`string`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FunctionDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FunctionDeclaration

# Interface: FunctionDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:855

Several node kinds share function-like features such as a signature,
a name, and a body. These nodes should extend FunctionLikeDeclarationBase.
Examples:
- FunctionDeclaration
- MethodDeclaration
- AccessorDeclaration

## Extends

- [`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`DeclarationStatement`](DeclarationStatement.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`_declarationBrand`](DeclarationStatement.md#_declarationbrand)

***

### \_functionLikeDeclarationBrand

> **\_functionLikeDeclarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:846

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`_functionLikeDeclarationBrand`](FunctionLikeDeclarationBase.md#_functionlikedeclarationbrand)

***

### \_statementBrand

> **\_statementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1471

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`_statementBrand`](DeclarationStatement.md#_statementbrand)

***

### asteriskToken?

> `readonly` `optional` **asteriskToken**: [`AsteriskToken`](../type-aliases/AsteriskToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:847

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`asteriskToken`](FunctionLikeDeclarationBase.md#asterisktoken)

***

### body?

> `readonly` `optional` **body**: [`Block`](Block.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:859

#### Overrides

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`body`](FunctionLikeDeclarationBase.md#body)

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

### exclamationToken?

> `readonly` `optional` **exclamationToken**: [`ExclamationToken`](../type-aliases/ExclamationToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:849

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`exclamationToken`](FunctionLikeDeclarationBase.md#exclamationtoken)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`DeclarationStatement`](DeclarationStatement.md).[`flags`](DeclarationStatement.md#flags)

***

### kind

> `readonly` **kind**: [`FunctionDeclaration`](../enumerations/SyntaxKind.md#functiondeclaration)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:856

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:857

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:858

#### Overrides

[`DeclarationStatement`](DeclarationStatement.md).[`name`](DeclarationStatement.md#name)

***

### parameters

> `readonly` **parameters**: [`NodeArray`](NodeArray.md)\<[`ParameterDeclaration`](ParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:735

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`parameters`](FunctionLikeDeclarationBase.md#parameters)

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

### questionToken?

> `readonly` `optional` **questionToken**: [`QuestionToken`](../type-aliases/QuestionToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:848

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`questionToken`](FunctionLikeDeclarationBase.md#questiontoken)

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

### type?

> `readonly` `optional` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:736

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`type`](FunctionLikeDeclarationBase.md#type)

***

### typeParameters?

> `readonly` `optional` **typeParameters**: [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:734

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`typeParameters`](FunctionLikeDeclarationBase.md#typeparameters)

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FunctionExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FunctionExpression

# Interface: FunctionExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1198

Several node kinds share function-like features such as a signature,
a name, and a body. These nodes should extend FunctionLikeDeclarationBase.
Examples:
- FunctionDeclaration
- MethodDeclaration
- AccessorDeclaration

## Extends

- [`PrimaryExpression`](PrimaryExpression.md).[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`JSDocContainer`](JSDocContainer.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`_declarationBrand`](FunctionLikeDeclarationBase.md#_declarationbrand)

***

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`_expressionBrand`](PrimaryExpression.md#_expressionbrand)

***

### \_functionLikeDeclarationBrand

> **\_functionLikeDeclarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:846

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`_functionLikeDeclarationBrand`](FunctionLikeDeclarationBase.md#_functionlikedeclarationbrand)

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

### asteriskToken?

> `readonly` `optional` **asteriskToken**: [`AsteriskToken`](../type-aliases/AsteriskToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:847

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`asteriskToken`](FunctionLikeDeclarationBase.md#asterisktoken)

***

### body

> `readonly` **body**: [`Block`](Block.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1202

#### Overrides

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`body`](FunctionLikeDeclarationBase.md#body)

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

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`decorators`](FunctionLikeDeclarationBase.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`end`](FunctionLikeDeclarationBase.md#end)

***

### exclamationToken?

> `readonly` `optional` **exclamationToken**: [`ExclamationToken`](../type-aliases/ExclamationToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:849

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`exclamationToken`](FunctionLikeDeclarationBase.md#exclamationtoken)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`flags`](FunctionLikeDeclarationBase.md#flags)

***

### kind

> `readonly` **kind**: [`FunctionExpression`](../enumerations/SyntaxKind.md#functionexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1199

#### Overrides

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`kind`](FunctionLikeDeclarationBase.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`locals`](FunctionLikeDeclarationBase.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`Modifier`](../type-aliases/Modifier.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1200

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Overrides

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`modifiers`](FunctionLikeDeclarationBase.md#modifiers)

***

### name?

> `readonly` `optional` **name**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1201

#### Overrides

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`name`](FunctionLikeDeclarationBase.md#name)

***

### parameters

> `readonly` **parameters**: [`NodeArray`](NodeArray.md)\<[`ParameterDeclaration`](ParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:735

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`parameters`](FunctionLikeDeclarationBase.md#parameters)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`parent`](FunctionLikeDeclarationBase.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`pos`](FunctionLikeDeclarationBase.md#pos)

***

### questionToken?

> `readonly` `optional` **questionToken**: [`QuestionToken`](../type-aliases/QuestionToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:848

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`questionToken`](FunctionLikeDeclarationBase.md#questiontoken)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`skipCheck`](FunctionLikeDeclarationBase.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`symbol`](FunctionLikeDeclarationBase.md#symbol)

***

### type?

> `readonly` `optional` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:736

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`type`](FunctionLikeDeclarationBase.md#type)

***

### typeParameters?

> `readonly` `optional` **typeParameters**: [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:734

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`typeParameters`](FunctionLikeDeclarationBase.md#typeparameters)

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

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`forEachChild`](FunctionLikeDeclarationBase.md#foreachchild)

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

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getChildAt`](FunctionLikeDeclarationBase.md#getchildat)

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

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getChildCount`](FunctionLikeDeclarationBase.md#getchildcount)

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

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getChildren`](FunctionLikeDeclarationBase.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getEnd`](FunctionLikeDeclarationBase.md#getend)

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

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getFirstToken`](FunctionLikeDeclarationBase.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getFullStart`](FunctionLikeDeclarationBase.md#getfullstart)

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

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getFullText`](FunctionLikeDeclarationBase.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getFullWidth`](FunctionLikeDeclarationBase.md#getfullwidth)

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

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getLastToken`](FunctionLikeDeclarationBase.md#getlasttoken)

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

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getLeadingTriviaWidth`](FunctionLikeDeclarationBase.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getSourceFile`](FunctionLikeDeclarationBase.md#getsourcefile)

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

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getStart`](FunctionLikeDeclarationBase.md#getstart)

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

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getText`](FunctionLikeDeclarationBase.md#gettext)

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

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`getWidth`](FunctionLikeDeclarationBase.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FunctionLikeDeclarationBase.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FunctionLikeDeclarationBase

# Interface: FunctionLikeDeclarationBase

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:845

Several node kinds share function-like features such as a signature,
a name, and a body. These nodes should extend FunctionLikeDeclarationBase.
Examples:
- FunctionDeclaration
- MethodDeclaration
- AccessorDeclaration

## Extends

- [`SignatureDeclarationBase`](SignatureDeclarationBase.md)

## Extended by

- [`FunctionDeclaration`](FunctionDeclaration.md)
- [`MethodDeclaration`](MethodDeclaration.md)
- [`ConstructorDeclaration`](ConstructorDeclaration.md)
- [`GetAccessorDeclaration`](GetAccessorDeclaration.md)
- [`SetAccessorDeclaration`](SetAccessorDeclaration.md)
- [`FunctionExpression`](FunctionExpression.md)
- [`ArrowFunction`](ArrowFunction.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`_declarationBrand`](SignatureDeclarationBase.md#_declarationbrand)

***

### \_functionLikeDeclarationBrand

> **\_functionLikeDeclarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:846

***

### asteriskToken?

> `readonly` `optional` **asteriskToken**: [`AsteriskToken`](../type-aliases/AsteriskToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:847

***

### body?

> `readonly` `optional` **body**: [`Expression`](Expression.md) \| [`Block`](Block.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:850

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`decorators`](SignatureDeclarationBase.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`end`](SignatureDeclarationBase.md#end)

***

### exclamationToken?

> `readonly` `optional` **exclamationToken**: [`ExclamationToken`](../type-aliases/ExclamationToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:849

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`flags`](SignatureDeclarationBase.md#flags)

***

### kind

> `readonly` **kind**: [`MethodSignature`](../enumerations/SyntaxKind.md#methodsignature) \| [`MethodDeclaration`](../enumerations/SyntaxKind.md#methoddeclaration) \| [`Constructor`](../enumerations/SyntaxKind.md#constructor) \| [`GetAccessor`](../enumerations/SyntaxKind.md#getaccessor) \| [`SetAccessor`](../enumerations/SyntaxKind.md#setaccessor) \| [`CallSignature`](../enumerations/SyntaxKind.md#callsignature) \| [`ConstructSignature`](../enumerations/SyntaxKind.md#constructsignature) \| [`IndexSignature`](../enumerations/SyntaxKind.md#indexsignature) \| [`FunctionType`](../enumerations/SyntaxKind.md#functiontype) \| [`ConstructorType`](../enumerations/SyntaxKind.md#constructortype) \| [`FunctionExpression`](../enumerations/SyntaxKind.md#functionexpression) \| [`ArrowFunction`](../enumerations/SyntaxKind.md#arrowfunction) \| [`FunctionDeclaration`](../enumerations/SyntaxKind.md#functiondeclaration) \| [`JSDocFunctionType`](../enumerations/SyntaxKind.md#jsdocfunctiontype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:732

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`kind`](SignatureDeclarationBase.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`locals`](SignatureDeclarationBase.md#locals)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`modifiers`](SignatureDeclarationBase.md#modifiers)

***

### name?

> `readonly` `optional` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:733

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`name`](SignatureDeclarationBase.md#name)

***

### parameters

> `readonly` **parameters**: [`NodeArray`](NodeArray.md)\<[`ParameterDeclaration`](ParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:735

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`parameters`](SignatureDeclarationBase.md#parameters)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`parent`](SignatureDeclarationBase.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`pos`](SignatureDeclarationBase.md#pos)

***

### questionToken?

> `readonly` `optional` **questionToken**: [`QuestionToken`](../type-aliases/QuestionToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:848

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`skipCheck`](SignatureDeclarationBase.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`symbol`](SignatureDeclarationBase.md#symbol)

***

### type?

> `readonly` `optional` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:736

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`type`](SignatureDeclarationBase.md#type)

***

### typeParameters?

> `readonly` `optional` **typeParameters**: [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:734

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`typeParameters`](SignatureDeclarationBase.md#typeparameters)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`forEachChild`](SignatureDeclarationBase.md#foreachchild)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getChildAt`](SignatureDeclarationBase.md#getchildat)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getChildCount`](SignatureDeclarationBase.md#getchildcount)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getChildren`](SignatureDeclarationBase.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getEnd`](SignatureDeclarationBase.md#getend)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getFirstToken`](SignatureDeclarationBase.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getFullStart`](SignatureDeclarationBase.md#getfullstart)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getFullText`](SignatureDeclarationBase.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getFullWidth`](SignatureDeclarationBase.md#getfullwidth)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getLastToken`](SignatureDeclarationBase.md#getlasttoken)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getLeadingTriviaWidth`](SignatureDeclarationBase.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getSourceFile`](SignatureDeclarationBase.md#getsourcefile)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getStart`](SignatureDeclarationBase.md#getstart)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getText`](SignatureDeclarationBase.md#gettext)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getWidth`](SignatureDeclarationBase.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FunctionOrConstructorTypeNodeBase.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FunctionOrConstructorTypeNodeBase

# Interface: FunctionOrConstructorTypeNodeBase

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:934

## Extends

- [`TypeNode`](TypeNode.md).[`SignatureDeclarationBase`](SignatureDeclarationBase.md)

## Extended by

- [`FunctionTypeNode`](FunctionTypeNode.md)
- [`ConstructorTypeNode`](ConstructorTypeNode.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`_declarationBrand`](SignatureDeclarationBase.md#_declarationbrand)

***

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`decorators`](SignatureDeclarationBase.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`end`](SignatureDeclarationBase.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`flags`](SignatureDeclarationBase.md#flags)

***

### kind

> `readonly` **kind**: [`FunctionType`](../enumerations/SyntaxKind.md#functiontype) \| [`ConstructorType`](../enumerations/SyntaxKind.md#constructortype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:935

#### Overrides

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`kind`](SignatureDeclarationBase.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`locals`](SignatureDeclarationBase.md#locals)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`modifiers`](SignatureDeclarationBase.md#modifiers)

***

### name?

> `readonly` `optional` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:733

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`name`](SignatureDeclarationBase.md#name)

***

### parameters

> `readonly` **parameters**: [`NodeArray`](NodeArray.md)\<[`ParameterDeclaration`](ParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:735

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`parameters`](SignatureDeclarationBase.md#parameters)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`parent`](SignatureDeclarationBase.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`pos`](SignatureDeclarationBase.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`skipCheck`](SignatureDeclarationBase.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`symbol`](SignatureDeclarationBase.md#symbol)

***

### type

> `readonly` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:936

#### Overrides

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`type`](SignatureDeclarationBase.md#type)

***

### typeParameters?

> `readonly` `optional` **typeParameters**: [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:734

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`typeParameters`](SignatureDeclarationBase.md#typeparameters)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`forEachChild`](SignatureDeclarationBase.md#foreachchild)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getChildAt`](SignatureDeclarationBase.md#getchildat)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getChildCount`](SignatureDeclarationBase.md#getchildcount)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getChildren`](SignatureDeclarationBase.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getEnd`](SignatureDeclarationBase.md#getend)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getFirstToken`](SignatureDeclarationBase.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getFullStart`](SignatureDeclarationBase.md#getfullstart)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getFullText`](SignatureDeclarationBase.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getFullWidth`](SignatureDeclarationBase.md#getfullwidth)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getLastToken`](SignatureDeclarationBase.md#getlasttoken)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getLeadingTriviaWidth`](SignatureDeclarationBase.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getSourceFile`](SignatureDeclarationBase.md#getsourcefile)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getStart`](SignatureDeclarationBase.md#getstart)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getText`](SignatureDeclarationBase.md#gettext)

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

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`getWidth`](SignatureDeclarationBase.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/FunctionTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / FunctionTypeNode

# Interface: FunctionTypeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:938

## Extends

- [`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`_declarationBrand`](FunctionOrConstructorTypeNodeBase.md#_declarationbrand)

***

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`_typeNodeBrand`](FunctionOrConstructorTypeNodeBase.md#_typenodebrand)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`decorators`](FunctionOrConstructorTypeNodeBase.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`end`](FunctionOrConstructorTypeNodeBase.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`flags`](FunctionOrConstructorTypeNodeBase.md#flags)

***

### kind

> `readonly` **kind**: [`FunctionType`](../enumerations/SyntaxKind.md#functiontype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:939

#### Overrides

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`kind`](FunctionOrConstructorTypeNodeBase.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`locals`](FunctionOrConstructorTypeNodeBase.md#locals)

***

### ~~modifiers?~~

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`Modifier`](../type-aliases/Modifier.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8408

#### Deprecated

A function type cannot have modifiers

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`modifiers`](FunctionOrConstructorTypeNodeBase.md#modifiers)

***

### name?

> `readonly` `optional` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:733

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`name`](FunctionOrConstructorTypeNodeBase.md#name)

***

### parameters

> `readonly` **parameters**: [`NodeArray`](NodeArray.md)\<[`ParameterDeclaration`](ParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:735

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`parameters`](FunctionOrConstructorTypeNodeBase.md#parameters)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`parent`](FunctionOrConstructorTypeNodeBase.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`pos`](FunctionOrConstructorTypeNodeBase.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`skipCheck`](FunctionOrConstructorTypeNodeBase.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`symbol`](FunctionOrConstructorTypeNodeBase.md#symbol)

***

### type

> `readonly` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:936

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`type`](FunctionOrConstructorTypeNodeBase.md#type)

***

### typeParameters?

> `readonly` `optional` **typeParameters**: [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:734

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`typeParameters`](FunctionOrConstructorTypeNodeBase.md#typeparameters)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`forEachChild`](FunctionOrConstructorTypeNodeBase.md#foreachchild)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getChildAt`](FunctionOrConstructorTypeNodeBase.md#getchildat)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getChildCount`](FunctionOrConstructorTypeNodeBase.md#getchildcount)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getChildren`](FunctionOrConstructorTypeNodeBase.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getEnd`](FunctionOrConstructorTypeNodeBase.md#getend)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getFirstToken`](FunctionOrConstructorTypeNodeBase.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getFullStart`](FunctionOrConstructorTypeNodeBase.md#getfullstart)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getFullText`](FunctionOrConstructorTypeNodeBase.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getFullWidth`](FunctionOrConstructorTypeNodeBase.md#getfullwidth)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getLastToken`](FunctionOrConstructorTypeNodeBase.md#getlasttoken)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getLeadingTriviaWidth`](FunctionOrConstructorTypeNodeBase.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getSourceFile`](FunctionOrConstructorTypeNodeBase.md#getsourcefile)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getStart`](FunctionOrConstructorTypeNodeBase.md#getstart)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getText`](FunctionOrConstructorTypeNodeBase.md#gettext)

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

[`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md).[`getWidth`](FunctionOrConstructorTypeNodeBase.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/GenericType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / GenericType

# Interface: GenericType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2850

Class and interface types (ObjectFlags.Class and ObjectFlags.Interface).

## Extends

- [`InterfaceType`](InterfaceType.md).[`TypeReference`](TypeReference.md)

## Extended by

- [`TupleType`](TupleType.md)

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

### localTypeParameters

> **localTypeParameters**: `undefined` \| [`TypeParameter`](TypeParameter.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2824

#### Inherited from

[`InterfaceType`](InterfaceType.md).[`localTypeParameters`](InterfaceType.md#localtypeparameters)

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

### outerTypeParameters

> **outerTypeParameters**: `undefined` \| [`TypeParameter`](TypeParameter.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2823

#### Inherited from

[`InterfaceType`](InterfaceType.md).[`outerTypeParameters`](InterfaceType.md#outertypeparameters)

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

> **target**: `GenericType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2845

#### Inherited from

[`TypeReference`](TypeReference.md).[`target`](TypeReference.md#target)

***

### thisType

> **thisType**: `undefined` \| [`TypeParameter`](TypeParameter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2825

#### Inherited from

[`InterfaceType`](InterfaceType.md).[`thisType`](InterfaceType.md#thistype)

***

### typeArguments?

> `optional` **typeArguments**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6145

#### Inherited from

[`TypeReference`](TypeReference.md).[`typeArguments`](TypeReference.md#typearguments)

***

### typeParameters

> **typeParameters**: `undefined` \| [`TypeParameter`](TypeParameter.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2822

#### Inherited from

[`InterfaceType`](InterfaceType.md).[`typeParameters`](InterfaceType.md#typeparameters)

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/GetAccessorDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / GetAccessorDeclaration

# Interface: GetAccessorDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:885

Several node kinds share function-like features such as a signature,
a name, and a body. These nodes should extend FunctionLikeDeclarationBase.
Examples:
- FunctionDeclaration
- MethodDeclaration
- AccessorDeclaration

## Extends

- [`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`ClassElement`](ClassElement.md).[`TypeElement`](TypeElement.md).[`ObjectLiteralElement`](ObjectLiteralElement.md).[`JSDocContainer`](JSDocContainer.md)

## Properties

### \_classElementBrand

> **\_classElementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1633

#### Inherited from

[`ClassElement`](ClassElement.md).[`_classElementBrand`](ClassElement.md#_classelementbrand)

***

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`_declarationBrand`](ObjectLiteralElement.md#_declarationbrand)

***

### \_functionLikeDeclarationBrand

> **\_functionLikeDeclarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:846

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`_functionLikeDeclarationBrand`](FunctionLikeDeclarationBase.md#_functionlikedeclarationbrand)

***

### \_objectLiteralBrand

> **\_objectLiteralBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:798

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`_objectLiteralBrand`](ObjectLiteralElement.md#_objectliteralbrand)

***

### \_typeElementBrand

> **\_typeElementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1637

#### Inherited from

[`TypeElement`](TypeElement.md).[`_typeElementBrand`](TypeElement.md#_typeelementbrand)

***

### asteriskToken?

> `readonly` `optional` **asteriskToken**: [`AsteriskToken`](../type-aliases/AsteriskToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:847

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`asteriskToken`](FunctionLikeDeclarationBase.md#asterisktoken)

***

### body?

> `readonly` `optional` **body**: [`Block`](Block.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:890

#### Overrides

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`body`](FunctionLikeDeclarationBase.md#body)

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

### exclamationToken?

> `readonly` `optional` **exclamationToken**: [`ExclamationToken`](../type-aliases/ExclamationToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:849

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`exclamationToken`](FunctionLikeDeclarationBase.md#exclamationtoken)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`flags`](ObjectLiteralElement.md#flags)

***

### kind

> `readonly` **kind**: [`GetAccessor`](../enumerations/SyntaxKind.md#getaccessor)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:886

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:888

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Overrides

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`modifiers`](ObjectLiteralElement.md#modifiers)

***

### name

> `readonly` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:889

#### Overrides

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`name`](ObjectLiteralElement.md#name)

***

### parameters

> `readonly` **parameters**: [`NodeArray`](NodeArray.md)\<[`ParameterDeclaration`](ParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:735

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`parameters`](FunctionLikeDeclarationBase.md#parameters)

***

### parent

> `readonly` **parent**: [`ClassLikeDeclaration`](../type-aliases/ClassLikeDeclaration.md) \| [`ObjectLiteralExpression`](ObjectLiteralExpression.md) \| [`InterfaceDeclaration`](InterfaceDeclaration.md) \| [`TypeLiteralNode`](TypeLiteralNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:887

#### Overrides

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`parent`](ObjectLiteralElement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`pos`](ObjectLiteralElement.md#pos)

***

### questionToken?

> `readonly` `optional` **questionToken**: [`QuestionToken`](../type-aliases/QuestionToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:848

#### Inherited from

[`TypeElement`](TypeElement.md).[`questionToken`](TypeElement.md#questiontoken)

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

***

### type?

> `readonly` `optional` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:736

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`type`](FunctionLikeDeclarationBase.md#type)

***

### typeParameters?

> `readonly` `optional` **typeParameters**: [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:734

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`typeParameters`](FunctionLikeDeclarationBase.md#typeparameters)

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



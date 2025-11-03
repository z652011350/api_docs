

============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ObjectBindingPattern.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ObjectBindingPattern

# Interface: ObjectBindingPattern

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:825

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

### elements

> `readonly` **elements**: [`NodeArray`](NodeArray.md)\<[`BindingElement`](BindingElement.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:828

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

> `readonly` **kind**: [`ObjectBindingPattern`](../enumerations/SyntaxKind.md#objectbindingpattern)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:826

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

> `readonly` **parent**: [`ParameterDeclaration`](ParameterDeclaration.md) \| [`VariableDeclaration`](VariableDeclaration.md) \| [`BindingElement`](BindingElement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:827

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ObjectDestructuringAssignment.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ObjectDestructuringAssignment

# Interface: ObjectDestructuringAssignment

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1172

## Extends

- [`AssignmentExpression`](AssignmentExpression.md)\<[`EqualsToken`](../type-aliases/EqualsToken.md)\>

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`_declarationBrand`](AssignmentExpression.md#_declarationbrand)

***

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`_expressionBrand`](AssignmentExpression.md#_expressionbrand)

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

[`AssignmentExpression`](AssignmentExpression.md).[`decorators`](AssignmentExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`end`](AssignmentExpression.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`flags`](AssignmentExpression.md#flags)

***

### kind

> `readonly` **kind**: [`BinaryExpression`](../enumerations/SyntaxKind.md#binaryexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1162

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`kind`](AssignmentExpression.md#kind)

***

### left

> `readonly` **left**: [`ObjectLiteralExpression`](ObjectLiteralExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1173

#### Overrides

[`AssignmentExpression`](AssignmentExpression.md).[`left`](AssignmentExpression.md#left)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`locals`](AssignmentExpression.md#locals)

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

[`AssignmentExpression`](AssignmentExpression.md).[`modifiers`](AssignmentExpression.md#modifiers)

***

### operatorToken

> `readonly` **operatorToken**: [`EqualsToken`](../type-aliases/EqualsToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1170

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`operatorToken`](AssignmentExpression.md#operatortoken)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`parent`](AssignmentExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`pos`](AssignmentExpression.md#pos)

***

### right

> `readonly` **right**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1165

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`right`](AssignmentExpression.md#right)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`skipCheck`](AssignmentExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`symbol`](AssignmentExpression.md#symbol)

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

[`AssignmentExpression`](AssignmentExpression.md).[`forEachChild`](AssignmentExpression.md#foreachchild)

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

[`AssignmentExpression`](AssignmentExpression.md).[`getChildAt`](AssignmentExpression.md#getchildat)

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

[`AssignmentExpression`](AssignmentExpression.md).[`getChildCount`](AssignmentExpression.md#getchildcount)

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

[`AssignmentExpression`](AssignmentExpression.md).[`getChildren`](AssignmentExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`getEnd`](AssignmentExpression.md#getend)

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

[`AssignmentExpression`](AssignmentExpression.md).[`getFirstToken`](AssignmentExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`getFullStart`](AssignmentExpression.md#getfullstart)

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

[`AssignmentExpression`](AssignmentExpression.md).[`getFullText`](AssignmentExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`getFullWidth`](AssignmentExpression.md#getfullwidth)

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

[`AssignmentExpression`](AssignmentExpression.md).[`getLastToken`](AssignmentExpression.md#getlasttoken)

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

[`AssignmentExpression`](AssignmentExpression.md).[`getLeadingTriviaWidth`](AssignmentExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`AssignmentExpression`](AssignmentExpression.md).[`getSourceFile`](AssignmentExpression.md#getsourcefile)

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

[`AssignmentExpression`](AssignmentExpression.md).[`getStart`](AssignmentExpression.md#getstart)

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

[`AssignmentExpression`](AssignmentExpression.md).[`getText`](AssignmentExpression.md#gettext)

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

[`AssignmentExpression`](AssignmentExpression.md).[`getWidth`](AssignmentExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ObjectLiteralElement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ObjectLiteralElement

# Interface: ObjectLiteralElement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:797

## Extends

- [`NamedDeclaration`](NamedDeclaration.md)

## Extended by

- [`PropertyAssignment`](PropertyAssignment.md)
- [`ShorthandPropertyAssignment`](ShorthandPropertyAssignment.md)
- [`SpreadAssignment`](SpreadAssignment.md)
- [`MethodDeclaration`](MethodDeclaration.md)
- [`GetAccessorDeclaration`](GetAccessorDeclaration.md)
- [`SetAccessorDeclaration`](SetAccessorDeclaration.md)
- [`JsxAttribute`](JsxAttribute.md)
- [`JsxSpreadAttribute`](JsxSpreadAttribute.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`_declarationBrand`](NamedDeclaration.md#_declarationbrand)

***

### \_objectLiteralBrand

> **\_objectLiteralBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:798

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

### kind

> `readonly` **kind**: [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:598

#### Inherited from

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

### name?

> `readonly` `optional` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:799

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`name`](NamedDeclaration.md#name)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ObjectLiteralExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ObjectLiteralExpression

# Interface: ObjectLiteralExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1298

This interface is a base interface for ObjectLiteralExpression and JSXAttributes to extend from. JSXAttributes is similar to
ObjectLiteralExpression in that it contains array of properties; however, JSXAttributes' properties can only be
JSXAttribute or JSXSpreadAttribute. ObjectLiteralExpression, on the other hand, can only have properties of type
ObjectLiteralElement (e.g. PropertyAssignment, ShorthandPropertyAssignment etc.)

## Extends

- [`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md)\<[`ObjectLiteralElementLike`](../type-aliases/ObjectLiteralElementLike.md)\>

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`_declarationBrand`](ObjectLiteralExpressionBase.md#_declarationbrand)

***

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`_expressionBrand`](ObjectLiteralExpressionBase.md#_expressionbrand)

***

### \_leftHandSideExpressionBrand

> **\_leftHandSideExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1086

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`_leftHandSideExpressionBrand`](ObjectLiteralExpressionBase.md#_lefthandsideexpressionbrand)

***

### \_memberExpressionBrand

> **\_memberExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1089

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`_memberExpressionBrand`](ObjectLiteralExpressionBase.md#_memberexpressionbrand)

***

### \_primaryExpressionBrand

> **\_primaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1092

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`_primaryExpressionBrand`](ObjectLiteralExpressionBase.md#_primaryexpressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`_unaryExpressionBrand`](ObjectLiteralExpressionBase.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`_updateExpressionBrand`](ObjectLiteralExpressionBase.md#_updateexpressionbrand)

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

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`decorators`](ObjectLiteralExpressionBase.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`end`](ObjectLiteralExpressionBase.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`flags`](ObjectLiteralExpressionBase.md#flags)

***

### kind

> `readonly` **kind**: [`ObjectLiteralExpression`](../enumerations/SyntaxKind.md#objectliteralexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1299

#### Overrides

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`kind`](ObjectLiteralExpressionBase.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`locals`](ObjectLiteralExpressionBase.md#locals)

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

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`modifiers`](ObjectLiteralExpressionBase.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`parent`](ObjectLiteralExpressionBase.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`pos`](ObjectLiteralExpressionBase.md#pos)

***

### properties

> `readonly` **properties**: [`NodeArray`](NodeArray.md)\<[`ObjectLiteralElementLike`](../type-aliases/ObjectLiteralElementLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1296

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`properties`](ObjectLiteralExpressionBase.md#properties)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`skipCheck`](ObjectLiteralExpressionBase.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`symbol`](ObjectLiteralExpressionBase.md#symbol)

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

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`forEachChild`](ObjectLiteralExpressionBase.md#foreachchild)

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

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getChildAt`](ObjectLiteralExpressionBase.md#getchildat)

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

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getChildCount`](ObjectLiteralExpressionBase.md#getchildcount)

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

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getChildren`](ObjectLiteralExpressionBase.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getEnd`](ObjectLiteralExpressionBase.md#getend)

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

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getFirstToken`](ObjectLiteralExpressionBase.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getFullStart`](ObjectLiteralExpressionBase.md#getfullstart)

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

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getFullText`](ObjectLiteralExpressionBase.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getFullWidth`](ObjectLiteralExpressionBase.md#getfullwidth)

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

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getLastToken`](ObjectLiteralExpressionBase.md#getlasttoken)

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

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getLeadingTriviaWidth`](ObjectLiteralExpressionBase.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getSourceFile`](ObjectLiteralExpressionBase.md#getsourcefile)

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

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getStart`](ObjectLiteralExpressionBase.md#getstart)

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

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getText`](ObjectLiteralExpressionBase.md#gettext)

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

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`getWidth`](ObjectLiteralExpressionBase.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ObjectLiteralExpressionBase.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ObjectLiteralExpressionBase

# Interface: ObjectLiteralExpressionBase\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1295

This interface is a base interface for ObjectLiteralExpression and JSXAttributes to extend from. JSXAttributes is similar to
ObjectLiteralExpression in that it contains array of properties; however, JSXAttributes' properties can only be
JSXAttribute or JSXSpreadAttribute. ObjectLiteralExpression, on the other hand, can only have properties of type
ObjectLiteralElement (e.g. PropertyAssignment, ShorthandPropertyAssignment etc.)

## Extends

- [`PrimaryExpression`](PrimaryExpression.md).[`Declaration`](Declaration.md)

## Extended by

- [`ObjectLiteralExpression`](ObjectLiteralExpression.md)
- [`JsxAttributes`](JsxAttributes.md)

## Type Parameters

### T

`T` *extends* [`ObjectLiteralElement`](ObjectLiteralElement.md)

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

### kind

> `readonly` **kind**: [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:598

#### Inherited from

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

### properties

> `readonly` **properties**: [`NodeArray`](NodeArray.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1296

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ObjectType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ObjectType

# Interface: ObjectType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2817

## Extends

- [`Type`](Type.md)

## Extended by

- [`InterfaceType`](InterfaceType.md)
- [`TypeReference`](TypeReference.md)
- [`EvolvingArrayType`](EvolvingArrayType.md)

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

### objectFlags

> **objectFlags**: [`ObjectFlags`](../enumerations/ObjectFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2818

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/OmittedExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / OmittedExpression

# Interface: OmittedExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1058

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

### kind

> `readonly` **kind**: [`OmittedExpression`](../enumerations/SyntaxKind.md#omittedexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1059

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/OptionalTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / OptionalTypeNode

# Interface: OptionalTypeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:983

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

> `readonly` **kind**: [`OptionalType`](../enumerations/SyntaxKind.md#optionaltype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:984

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

### type

> `readonly` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:985

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/OrganizeImportsArgs.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / OrganizeImportsArgs

# Interface: OrganizeImportsArgs

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6447

## Extends

- [`CombinedCodeFixScope`](CombinedCodeFixScope.md)

## Properties

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6440

#### Inherited from

[`CombinedCodeFixScope`](CombinedCodeFixScope.md).[`fileName`](CombinedCodeFixScope.md#filename)

***

### mode?

> `optional` **mode**: [`OrganizeImportsMode`](../enumerations/OrganizeImportsMode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6450

***

### ~~skipDestructiveCodeActions?~~

> `optional` **skipDestructiveCodeActions**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6449

#### Deprecated

Use `mode` instead

***

### type

> **type**: `"file"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6439

#### Inherited from

[`CombinedCodeFixScope`](CombinedCodeFixScope.md).[`type`](CombinedCodeFixScope.md#type)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/OutliningSpan.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / OutliningSpan

# Interface: OutliningSpan

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7055

## Properties

### autoCollapse

> **autoCollapse**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7066

Whether or not this region should be automatically collapsed when
the 'Collapse to Definitions' command is invoked.

***

### bannerText

> **bannerText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7061

The text to display in the editor for the collapsed region.

***

### hintSpan

> **hintSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7059

The span of the document to display when the user hovers over the collapsed span.

***

### kind

> **kind**: [`OutliningSpanKind`](../enumerations/OutliningSpanKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7070

Classification of the contents of the span

***

### textSpan

> **textSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:7057

The span of the document to actually collapse.




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/OutputFile.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / OutputFile

# Interface: OutputFile

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5635

## Properties

### name

> **name**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5636

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5638

***

### writeByteOrderMark

> **writeByteOrderMark**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5637




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PackageId.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PackageId

# Interface: PackageId

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3393

Unique identifier with a package name and version.
If changing this, remember to change `packageIdIsEqual`.

## Properties

### name

> **name**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3399

Name of the package.
Should not include `@types`.
If accessing a non-index file, this should include its name e.g. "foo/bar".

***

### subModuleName

> **subModuleName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3404

Name of a submodule within this package.
May be "".

***

### version

> **version**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3406

Version of the package, e.g. "1.2.3"




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PackageJsonInfoCache.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PackageJsonInfoCache

# Interface: PackageJsonInfoCache

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5395

## Extended by

- [`TypeReferenceDirectiveResolutionCache`](TypeReferenceDirectiveResolutionCache.md)
- [`ModuleResolutionCache`](ModuleResolutionCache.md)
- [`NonRelativeModuleNameResolutionCache`](NonRelativeModuleNameResolutionCache.md)

## Methods

### clear()

> **clear**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5396

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ParameterDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ParameterDeclaration

# Interface: ParameterDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:759

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

### dotDotDotToken?

> `readonly` `optional` **dotDotDotToken**: [`DotDotDotToken`](../type-aliases/DotDotDotToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:763

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:767

***

### kind

> `readonly` **kind**: [`Parameter`](../enumerations/SyntaxKind.md#parameter)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:760

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:762

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`modifiers`](NamedDeclaration.md#modifiers)

***

### name

> `readonly` **name**: [`BindingName`](../type-aliases/BindingName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:764

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`name`](NamedDeclaration.md#name)

***

### parent

> `readonly` **parent**: [`SignatureDeclaration`](../type-aliases/SignatureDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:761

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`parent`](NamedDeclaration.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`pos`](NamedDeclaration.md#pos)

***

### questionToken?

> `readonly` `optional` **questionToken**: [`QuestionToken`](../type-aliases/QuestionToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:765

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

***

### type?

> `readonly` `optional` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:766

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ParenthesizedExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ParenthesizedExpression

# Interface: ParenthesizedExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1276

## Extends

- [`PrimaryExpression`](PrimaryExpression.md).[`JSDocContainer`](JSDocContainer.md)

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

### expression

> `readonly` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1278

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`flags`](PrimaryExpression.md#flags)

***

### kind

> `readonly` **kind**: [`ParenthesizedExpression`](../enumerations/SyntaxKind.md#parenthesizedexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1277

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ParenthesizedTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ParenthesizedTypeNode

# Interface: ParenthesizedTypeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1011

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

> `readonly` **kind**: [`ParenthesizedType`](../enumerations/SyntaxKind.md#parenthesizedtype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1012

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

### type

> `readonly` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1013

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ParseConfigFileHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ParseConfigFileHost

# Interface: ParseConfigFileHost

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5272

Interface extending ParseConfigHost to support ParseConfigFile that reads config file and reports errors

## Extends

- [`ParseConfigHost`](ParseConfigHost.md).[`ConfigFileDiagnosticsReporter`](ConfigFileDiagnosticsReporter.md)

## Properties

### onUnRecoverableConfigFileDiagnostic

> **onUnRecoverableConfigFileDiagnostic**: [`DiagnosticReporter`](../type-aliases/DiagnosticReporter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5267

Reports unrecoverable error when parsing config file

#### Inherited from

[`ConfigFileDiagnosticsReporter`](ConfigFileDiagnosticsReporter.md).[`onUnRecoverableConfigFileDiagnostic`](ConfigFileDiagnosticsReporter.md#onunrecoverableconfigfilediagnostic)

***

### useCaseSensitiveFileNames

> **useCaseSensitiveFileNames**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2237

#### Inherited from

[`ParseConfigHost`](ParseConfigHost.md).[`useCaseSensitiveFileNames`](ParseConfigHost.md#usecasesensitivefilenames)

## Methods

### fileExists()

> **fileExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2243

Gets a value indicating whether the specified path exists and is a file.

#### Parameters

##### path

`string`

The path to test.

#### Returns

`boolean`

#### Inherited from

[`ParseConfigHost`](ParseConfigHost.md).[`fileExists`](ParseConfigHost.md#fileexists)

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5273

#### Returns

`string`

***

### readDirectory()

> **readDirectory**(`rootDir`, `extensions`, `excludes`, `includes`, `depth?`): readonly `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2238

#### Parameters

##### rootDir

`string`

##### extensions

readonly `string`[]

##### excludes

`undefined` | readonly `string`[]

##### includes

readonly `string`[]

##### depth?

`number`

#### Returns

readonly `string`[]

#### Inherited from

[`ParseConfigHost`](ParseConfigHost.md).[`readDirectory`](ParseConfigHost.md#readdirectory)

***

### readFile()

> **readFile**(`path`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2244

#### Parameters

##### path

`string`

#### Returns

`undefined` \| `string`

#### Inherited from

[`ParseConfigHost`](ParseConfigHost.md).[`readFile`](ParseConfigHost.md#readfile)

***

### trace()?

> `optional` **trace**(`s`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2245

#### Parameters

##### s

`string`

#### Returns

`void`

#### Inherited from

[`ParseConfigHost`](ParseConfigHost.md).[`trace`](ParseConfigHost.md#trace)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ParseConfigHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ParseConfigHost

# Interface: ParseConfigHost

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2236

## Extended by

- [`ParseConfigFileHost`](ParseConfigFileHost.md)

## Properties

### useCaseSensitiveFileNames

> **useCaseSensitiveFileNames**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2237

## Methods

### fileExists()

> **fileExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2243

Gets a value indicating whether the specified path exists and is a file.

#### Parameters

##### path

`string`

The path to test.

#### Returns

`boolean`

***

### readDirectory()

> **readDirectory**(`rootDir`, `extensions`, `excludes`, `includes`, `depth?`): readonly `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2238

#### Parameters

##### rootDir

`string`

##### extensions

readonly `string`[]

##### excludes

`undefined` | readonly `string`[]

##### includes

readonly `string`[]

##### depth?

`number`

#### Returns

readonly `string`[]

***

### readFile()

> **readFile**(`path`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2244

#### Parameters

##### path

`string`

#### Returns

`undefined` \| `string`

***

### trace()?

> `optional` **trace**(`s`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2245

#### Parameters

##### s

`string`

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ParsedCommandLine.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ParsedCommandLine

# Interface: ParsedCommandLine

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3316

Either a parsed command line or a parsed tsconfig.json

## Properties

### compileOnSave?

> `optional` **compileOnSave**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3325

***

### errors

> **errors**: [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3323

***

### fileNames

> **fileNames**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3319

***

### options

> **options**: [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3317

***

### projectReferences?

> `optional` **projectReferences**: readonly [`ProjectReference`](ProjectReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3320

***

### raw?

> `optional` **raw**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3322

***

### typeAcquisition?

> `optional` **typeAcquisition**: [`TypeAcquisition`](TypeAcquisition.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3318

***

### watchOptions?

> `optional` **watchOptions**: [`WatchOptions`](WatchOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3321

***

### wildcardDirectories?

> `optional` **wildcardDirectories**: [`MapLike`](MapLike.md)\<[`WatchDirectoryFlags`](../enumerations/WatchDirectoryFlags.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3324




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ParsedTsconfig.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ParsedTsconfig

# Interface: ParsedTsconfig

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5321

## Properties

### extendedConfigPath?

> `optional` **extendedConfigPath**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5329

Note that the case of the config path has not yet been normalized, as no files have been imported into the project yet

***

### options?

> `optional` **options**: [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5323

***

### raw

> **raw**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5322

***

### typeAcquisition?

> `optional` **typeAcquisition**: [`TypeAcquisition`](TypeAcquisition.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5325

***

### watchOptions?

> `optional` **watchOptions**: [`WatchOptions`](WatchOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5324




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PartiallyEmittedExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PartiallyEmittedExpression

# Interface: PartiallyEmittedExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1061

## Extends

- [`LeftHandSideExpression`](LeftHandSideExpression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`_expressionBrand`](LeftHandSideExpression.md#_expressionbrand)

***

### \_leftHandSideExpressionBrand

> **\_leftHandSideExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1086

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`_leftHandSideExpressionBrand`](LeftHandSideExpression.md#_lefthandsideexpressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`_unaryExpressionBrand`](LeftHandSideExpression.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`_updateExpressionBrand`](LeftHandSideExpression.md#_updateexpressionbrand)

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

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`decorators`](LeftHandSideExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`end`](LeftHandSideExpression.md#end)

***

### expression

> `readonly` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1063

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`flags`](LeftHandSideExpression.md#flags)

***

### kind

> `readonly` **kind**: [`PartiallyEmittedExpression`](../enumerations/SyntaxKind.md#partiallyemittedexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1062

#### Overrides

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`kind`](LeftHandSideExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`locals`](LeftHandSideExpression.md#locals)

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

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`modifiers`](LeftHandSideExpression.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`parent`](LeftHandSideExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`pos`](LeftHandSideExpression.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`skipCheck`](LeftHandSideExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`symbol`](LeftHandSideExpression.md#symbol)

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

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`forEachChild`](LeftHandSideExpression.md#foreachchild)

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

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getChildAt`](LeftHandSideExpression.md#getchildat)

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

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getChildCount`](LeftHandSideExpression.md#getchildcount)

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

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getChildren`](LeftHandSideExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getEnd`](LeftHandSideExpression.md#getend)

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

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getFirstToken`](LeftHandSideExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getFullStart`](LeftHandSideExpression.md#getfullstart)

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

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getFullText`](LeftHandSideExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getFullWidth`](LeftHandSideExpression.md#getfullwidth)

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

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getLastToken`](LeftHandSideExpression.md#getlasttoken)

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

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getLeadingTriviaWidth`](LeftHandSideExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getSourceFile`](LeftHandSideExpression.md#getsourcefile)

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

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getStart`](LeftHandSideExpression.md#getstart)

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

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getText`](LeftHandSideExpression.md#gettext)

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

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`getWidth`](LeftHandSideExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PerDirectoryResolutionCache.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PerDirectoryResolutionCache

# Interface: PerDirectoryResolutionCache\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5376

Cached resolutions per containing directory.
This assumes that any module id will have the same resolution for sibling files located in the same folder.

## Extended by

- [`TypeReferenceDirectiveResolutionCache`](TypeReferenceDirectiveResolutionCache.md)
- [`ModuleResolutionCache`](ModuleResolutionCache.md)

## Type Parameters

### T

`T`

## Methods

### clear()

> **clear**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5378

#### Returns

`void`

***

### getOrCreateCacheForDirectory()

> **getOrCreateCacheForDirectory**(`directoryName`, `redirectedReference?`): [`ModeAwareCache`](ModeAwareCache.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5377

#### Parameters

##### directoryName

`string`

##### redirectedReference?

[`ResolvedProjectReference`](ResolvedProjectReference.md)

#### Returns

[`ModeAwareCache`](ModeAwareCache.md)\<`T`\>

***

### update()

> **update**(`options`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5383

Updates with the current compilerOptions the cache will operate with.
 This updates the redirects map as well if needed so module resolutions are cached if they can across the projects

#### Parameters

##### options

[`CompilerOptions`](CompilerOptions.md)

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PerModuleNameCache.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PerModuleNameCache

# Interface: PerModuleNameCache

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5398

## Methods

### get()

> **get**(`directory`): `undefined` \| [`ResolvedModuleWithFailedLookupLocations`](ResolvedModuleWithFailedLookupLocations.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5399

#### Parameters

##### directory

`string`

#### Returns

`undefined` \| [`ResolvedModuleWithFailedLookupLocations`](ResolvedModuleWithFailedLookupLocations.md)

***

### set()

> **set**(`directory`, `result`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5400

#### Parameters

##### directory

`string`

##### result

[`ResolvedModuleWithFailedLookupLocations`](ResolvedModuleWithFailedLookupLocations.md)

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PerformanceEvent.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PerformanceEvent

# Interface: PerformanceEvent

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6208

## Properties

### durationMs

> **durationMs**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6210

***

### kind

> **kind**: `"UpdateGraph"` \| `"CreatePackageJsonAutoImportProvider"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6209




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PluginImport.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PluginImport

# Interface: PluginImport

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3040

## Properties

### name

> **name**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3041




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PostfixUnaryExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PostfixUnaryExpression

# Interface: PostfixUnaryExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1080

## Extends

- [`UpdateExpression`](UpdateExpression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`_expressionBrand`](UpdateExpression.md#_expressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`_unaryExpressionBrand`](UpdateExpression.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`_updateExpressionBrand`](UpdateExpression.md#_updateexpressionbrand)

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

[`UpdateExpression`](UpdateExpression.md).[`decorators`](UpdateExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`end`](UpdateExpression.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`flags`](UpdateExpression.md#flags)

***

### kind

> `readonly` **kind**: [`PostfixUnaryExpression`](../enumerations/SyntaxKind.md#postfixunaryexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1081

#### Overrides

[`UpdateExpression`](UpdateExpression.md).[`kind`](UpdateExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`locals`](UpdateExpression.md#locals)

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

[`UpdateExpression`](UpdateExpression.md).[`modifiers`](UpdateExpression.md#modifiers)

***

### operand

> `readonly` **operand**: [`LeftHandSideExpression`](LeftHandSideExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1082

***

### operator

> `readonly` **operator**: [`PostfixUnaryOperator`](../type-aliases/PostfixUnaryOperator.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1083

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`parent`](UpdateExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`pos`](UpdateExpression.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`skipCheck`](UpdateExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`symbol`](UpdateExpression.md#symbol)

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

[`UpdateExpression`](UpdateExpression.md).[`forEachChild`](UpdateExpression.md#foreachchild)

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

[`UpdateExpression`](UpdateExpression.md).[`getChildAt`](UpdateExpression.md#getchildat)

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

[`UpdateExpression`](UpdateExpression.md).[`getChildCount`](UpdateExpression.md#getchildcount)

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

[`UpdateExpression`](UpdateExpression.md).[`getChildren`](UpdateExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`getEnd`](UpdateExpression.md#getend)

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

[`UpdateExpression`](UpdateExpression.md).[`getFirstToken`](UpdateExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`getFullStart`](UpdateExpression.md#getfullstart)

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

[`UpdateExpression`](UpdateExpression.md).[`getFullText`](UpdateExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`getFullWidth`](UpdateExpression.md#getfullwidth)

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

[`UpdateExpression`](UpdateExpression.md).[`getLastToken`](UpdateExpression.md#getlasttoken)

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

[`UpdateExpression`](UpdateExpression.md).[`getLeadingTriviaWidth`](UpdateExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`getSourceFile`](UpdateExpression.md#getsourcefile)

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

[`UpdateExpression`](UpdateExpression.md).[`getStart`](UpdateExpression.md#getstart)

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

[`UpdateExpression`](UpdateExpression.md).[`getText`](UpdateExpression.md#gettext)

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

[`UpdateExpression`](UpdateExpression.md).[`getWidth`](UpdateExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PreProcessedFileInfo.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PreProcessedFileInfo

# Interface: PreProcessedFileInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6193

## Properties

### ambientExternalModules?

> `optional` **ambientExternalModules**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6198

***

### importedFiles

> **importedFiles**: [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6197

***

### isLibFile

> **isLibFile**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6199

***

### libReferenceDirectives

> **libReferenceDirectives**: [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6196

***

### referencedFiles

> **referencedFiles**: [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6194

***

### typeReferenceDirectives

> **typeReferenceDirectives**: [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6195




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PrefixUnaryExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PrefixUnaryExpression

# Interface: PrefixUnaryExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1074

## Extends

- [`UpdateExpression`](UpdateExpression.md)

## Extended by

- [`JsonMinusNumericLiteral`](JsonMinusNumericLiteral.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`_expressionBrand`](UpdateExpression.md#_expressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`_unaryExpressionBrand`](UpdateExpression.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`_updateExpressionBrand`](UpdateExpression.md#_updateexpressionbrand)

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

[`UpdateExpression`](UpdateExpression.md).[`decorators`](UpdateExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`end`](UpdateExpression.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`flags`](UpdateExpression.md#flags)

***

### kind

> `readonly` **kind**: [`PrefixUnaryExpression`](../enumerations/SyntaxKind.md#prefixunaryexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1075

#### Overrides

[`UpdateExpression`](UpdateExpression.md).[`kind`](UpdateExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`locals`](UpdateExpression.md#locals)

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

[`UpdateExpression`](UpdateExpression.md).[`modifiers`](UpdateExpression.md#modifiers)

***

### operand

> `readonly` **operand**: [`UnaryExpression`](UnaryExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1077

***

### operator

> `readonly` **operator**: [`PrefixUnaryOperator`](../type-aliases/PrefixUnaryOperator.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1076

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`parent`](UpdateExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`pos`](UpdateExpression.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`skipCheck`](UpdateExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`symbol`](UpdateExpression.md#symbol)

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

[`UpdateExpression`](UpdateExpression.md).[`forEachChild`](UpdateExpression.md#foreachchild)

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

[`UpdateExpression`](UpdateExpression.md).[`getChildAt`](UpdateExpression.md#getchildat)

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

[`UpdateExpression`](UpdateExpression.md).[`getChildCount`](UpdateExpression.md#getchildcount)

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

[`UpdateExpression`](UpdateExpression.md).[`getChildren`](UpdateExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`getEnd`](UpdateExpression.md#getend)

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

[`UpdateExpression`](UpdateExpression.md).[`getFirstToken`](UpdateExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`getFullStart`](UpdateExpression.md#getfullstart)

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

[`UpdateExpression`](UpdateExpression.md).[`getFullText`](UpdateExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`getFullWidth`](UpdateExpression.md#getfullwidth)

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

[`UpdateExpression`](UpdateExpression.md).[`getLastToken`](UpdateExpression.md#getlasttoken)

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

[`UpdateExpression`](UpdateExpression.md).[`getLeadingTriviaWidth`](UpdateExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`getSourceFile`](UpdateExpression.md#getsourcefile)

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

[`UpdateExpression`](UpdateExpression.md).[`getStart`](UpdateExpression.md#getstart)

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

[`UpdateExpression`](UpdateExpression.md).[`getText`](UpdateExpression.md#gettext)

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

[`UpdateExpression`](UpdateExpression.md).[`getWidth`](UpdateExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PrimaryExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PrimaryExpression

# Interface: PrimaryExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1091

## Extends

- [`MemberExpression`](MemberExpression.md)

## Extended by

- [`Identifier`](Identifier.md)
- [`PrivateIdentifier`](PrivateIdentifier.md)
- [`NullLiteral`](NullLiteral.md)
- [`TrueLiteral`](TrueLiteral.md)
- [`FalseLiteral`](FalseLiteral.md)
- [`ThisExpression`](ThisExpression.md)
- [`SuperExpression`](SuperExpression.md)
- [`ImportExpression`](ImportExpression.md)
- [`FunctionExpression`](FunctionExpression.md)
- [`EtsComponentExpression`](EtsComponentExpression.md)
- [`LiteralExpression`](LiteralExpression.md)
- [`TemplateExpression`](TemplateExpression.md)
- [`ParenthesizedExpression`](ParenthesizedExpression.md)
- [`ArrayLiteralExpression`](ArrayLiteralExpression.md)
- [`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md)
- [`NewExpression`](NewExpression.md)
- [`MetaProperty`](MetaProperty.md)
- [`JsxElement`](JsxElement.md)
- [`JsxSelfClosingElement`](JsxSelfClosingElement.md)
- [`JsxFragment`](JsxFragment.md)
- [`ClassExpression`](ClassExpression.md)

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

### \_primaryExpressionBrand

> **\_primaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1092

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

> `readonly` **kind**: [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:598

#### Inherited from

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PrintHandlers.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PrintHandlers

# Interface: PrintHandlers

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4215

## Methods

### hasGlobalName()?

> `optional` **hasGlobalName**(`name`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4220

A hook used by the Printer when generating unique names to avoid collisions with
globally defined names that exist outside of the current source file.

#### Parameters

##### name

`string`

#### Returns

`boolean`

***

### isEmitNotificationEnabled()?

> `optional` **isEmitNotificationEnabled**(`node`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4244

A hook used to check if an emit notification is required for a node.

#### Parameters

##### node

[`Node`](Node.md)

The node to emit.

#### Returns

`boolean`

***

### onEmitNode()?

> `optional` **onEmitNode**(`hint`, `node`, `emitCallback`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4239

A hook used by the Printer to provide notifications prior to emitting a node. A
compatible implementation **must** invoke `emitCallback` with the provided `hint` and
`node` values.

#### Parameters

##### hint

[`EmitHint`](../enumerations/EmitHint.md)

A hint indicating the intended purpose of the node.

##### node

[`Node`](Node.md)

The node to emit.

##### emitCallback

(`hint`, `node`) => `void`

A callback that, when invoked, will emit the node.

#### Returns

`void`

#### Example

```ts
var printer = createPrinter(printerOptions, {
  onEmitNode(hint, node, emitCallback) {
    // set up or track state prior to emitting the node...
    emitCallback(hint, node);
    // restore state after emitting the node...
  }
});
```

***

### substituteNode()?

> `optional` **substituteNode**(`hint`, `node`): [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4261

A hook used by the Printer to perform just-in-time substitution of a node. This is
primarily used by node transformations that need to substitute one node for another,
such as replacing `myExportedVar` with `exports.myExportedVar`.

#### Parameters

##### hint

[`EmitHint`](../enumerations/EmitHint.md)

A hint indicating the intended purpose of the node.

##### node

[`Node`](Node.md)

The node to emit.

#### Returns

[`Node`](Node.md)

#### Example

```ts
var printer = createPrinter(printerOptions, {
  substituteNode(hint, node) {
    // perform substitution if necessary...
    return node;
  }
});
```




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Printer.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Printer

# Interface: Printer

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4186

## Methods

### printBundle()

> **printBundle**(`bundle`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4212

Prints a bundle of source files as-is, without any emit transformations.

#### Parameters

##### bundle

[`Bundle`](Bundle.md)

#### Returns

`string`

***

### printFile()

> **printFile**(`sourceFile`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4208

Prints a source file as-is, without any emit transformations.

#### Parameters

##### sourceFile

[`SourceFile`](SourceFile.md)

#### Returns

`string`

***

### printList()

> **printList**\<`T`\>(`format`, `list`, `sourceFile`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4204

Prints a list of nodes using the given format flags

#### Type Parameters

##### T

`T` *extends* [`Node`](Node.md)

#### Parameters

##### format

[`ListFormat`](../enumerations/ListFormat.md)

##### list

[`NodeArray`](NodeArray.md)\<`T`\>

##### sourceFile

[`SourceFile`](SourceFile.md)

#### Returns

`string`

***

### printNode()

> **printNode**(`hint`, `node`, `sourceFile`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4200

Print a node and its subtree as-is, without any emit transformations.

#### Parameters

##### hint

[`EmitHint`](../enumerations/EmitHint.md)

A value indicating the purpose of a node. This is primarily used to
distinguish between an `Identifier` used in an expression position, versus an
`Identifier` used as an `IdentifierName` as part of a declaration. For most nodes you
should just pass `Unspecified`.

##### node

[`Node`](Node.md)

The node to print. The node and its subtree are printed as-is, without any
emit transformations.

##### sourceFile

[`SourceFile`](SourceFile.md)

A source file that provides context for the node. The source text of
the file is used to emit the original source content for literals and identifiers, while
the identifiers of the source file are used when generating unique names to avoid
collisions.

#### Returns

`string`

***

### writeFile()

> **writeFile**(`sourceFile`, `writer`, `sourceMapGenerator`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4213

#### Parameters

##### sourceFile

[`SourceFile`](SourceFile.md)

##### writer

[`EmitTextWriter`](EmitTextWriter.md)

##### sourceMapGenerator

`undefined` | [`SourceMapGenerator`](SourceMapGenerator.md)

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PrinterOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PrinterOptions

# Interface: PrinterOptions

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4263

## Properties

### inlineSourceMap?

> `optional` **inlineSourceMap**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4269

***

### inlineSources?

> `optional` **inlineSources**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4270

***

### newLine?

> `optional` **newLine**: [`NewLineKind`](../enumerations/NewLineKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4265

***

### noEmitHelpers?

> `optional` **noEmitHelpers**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4267

***

### omitTrailingSemicolon?

> `optional` **omitTrailingSemicolon**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4266

***

### removeComments?

> `optional` **removeComments**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4264

***

### sourceMap?

> `optional` **sourceMap**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4268




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PrivateIdentifier.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PrivateIdentifier

# Interface: PrivateIdentifier

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:712

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

### escapedText

> `readonly` **escapedText**: [`__String`](../type-aliases/String.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:714

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`PrimaryExpression`](PrimaryExpression.md).[`flags`](PrimaryExpression.md#flags)

***

### kind

> `readonly` **kind**: [`PrivateIdentifier`](../enumerations/SyntaxKind.md#privateidentifier)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:713

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

### text

> `readonly` **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6108

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Program.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Program

# Interface: Program

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2273

## Extends

- [`ScriptReferenceHost`](ScriptReferenceHost.md)

## Methods

### emit()

> **emit**(`targetSourceFile?`, `writeFile?`, `cancellationToken?`, `emitOnlyDtsFiles?`, `customTransformers?`): [`EmitResult`](EmitResult.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2293

Emits the JavaScript and declaration files.  If targetSourceFile is not specified, then
the JavaScript and declaration files will be produced for all the files in this program.
If targetSourceFile is specified, then only the JavaScript and declaration for that
specific file will be generated.

If writeFile is not specified then the writeFile callback from the compiler host will be
used for writing the JavaScript and declaration files.  Otherwise, the writeFile parameter
will be invoked when writing the JavaScript and declaration files.

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

***

### getCompilerOptions()

> **getCompilerOptions**(): [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2231

#### Returns

[`CompilerOptions`](CompilerOptions.md)

#### Inherited from

[`ScriptReferenceHost`](ScriptReferenceHost.md).[`getCompilerOptions`](ScriptReferenceHost.md#getcompileroptions)

***

### getConfigFileParsingDiagnostics()

> **getConfigFileParsingDiagnostics**(): readonly [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2301

#### Returns

readonly [`Diagnostic`](Diagnostic.md)[]

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2274

#### Returns

`string`

#### Overrides

[`ScriptReferenceHost`](ScriptReferenceHost.md).[`getCurrentDirectory`](ScriptReferenceHost.md#getcurrentdirectory)

***

### getDeclarationDiagnostics()

> **getDeclarationDiagnostics**(`sourceFile?`, `cancellationToken?`): readonly [`DiagnosticWithLocation`](DiagnosticWithLocation.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2300

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

#### Returns

readonly [`DiagnosticWithLocation`](DiagnosticWithLocation.md)[]

***

### getEtsLibSFromProgram()

> **getEtsLibSFromProgram**(): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2302

#### Returns

`string`[]

***

### getFileCheckedModuleInfo()?

> `optional` **getFileCheckedModuleInfo**(`containFilePath`): [`FileCheckModuleInfo`](FileCheckModuleInfo.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2329

#### Parameters

##### containFilePath

`string`

#### Returns

[`FileCheckModuleInfo`](FileCheckModuleInfo.md)

***

### getGlobalDiagnostics()

> **getGlobalDiagnostics**(`cancellationToken?`): readonly [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2295

#### Parameters

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

#### Returns

readonly [`Diagnostic`](Diagnostic.md)[]

***

### getIdentifierCount()

> **getIdentifierCount**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2312

#### Returns

`number`

***

### getInstantiationCount()

> **getInstantiationCount**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2315

#### Returns

`number`

***

### getJsDocNodeCheckedConfig()?

> `optional` **getJsDocNodeCheckedConfig**(`jsDocFileCheckInfo`, `symbolSourceFilePath`): [`JsDocNodeCheckConfig`](JsDocNodeCheckConfig.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2327

#### Parameters

##### jsDocFileCheckInfo

[`FileCheckModuleInfo`](FileCheckModuleInfo.md)

##### symbolSourceFilePath

`string`

#### Returns

[`JsDocNodeCheckConfig`](JsDocNodeCheckConfig.md)

***

### getJsDocNodeConditionCheckedResult()?

> `optional` **getJsDocNodeConditionCheckedResult**(`jsDocFileCheckedInfo`, `jsDocs`): [`ConditionCheckResult`](ConditionCheckResult.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2328

#### Parameters

##### jsDocFileCheckedInfo

[`FileCheckModuleInfo`](FileCheckModuleInfo.md)

##### jsDocs

[`JsDocTagInfo`](JsDocTagInfo.md)[]

#### Returns

[`ConditionCheckResult`](ConditionCheckResult.md)

***

### getLinterTypeChecker()

> **getLinterTypeChecker**(): [`TypeChecker`](TypeChecker.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2310

Gets a type checker that can be used to semantically analyze source files in the program for arkts linter.

#### Returns

[`TypeChecker`](TypeChecker.md)

***

### getNodeCount()

> **getNodeCount**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2311

#### Returns

`number`

***

### getOptionsDiagnostics()

> **getOptionsDiagnostics**(`cancellationToken?`): readonly [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2294

#### Parameters

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

#### Returns

readonly [`Diagnostic`](Diagnostic.md)[]

***

### getProjectReferences()

> **getProjectReferences**(): `undefined` \| readonly [`ProjectReference`](ProjectReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2325

#### Returns

`undefined` \| readonly [`ProjectReference`](ProjectReference.md)[]

***

### getRelationCacheSizes()

> **getRelationCacheSizes**(): `object`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2316

#### Returns

`object`

##### assignable

> **assignable**: `number`

##### identity

> **identity**: `number`

##### strictSubtype

> **strictSubtype**: `number`

##### subtype

> **subtype**: `number`

***

### getResolvedProjectReferences()

> **getResolvedProjectReferences**(): `undefined` \| readonly (`undefined` \| [`ResolvedProjectReference`](ResolvedProjectReference.md))[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2326

#### Returns

`undefined` \| readonly (`undefined` \| [`ResolvedProjectReference`](ResolvedProjectReference.md))[]

***

### getRootFileNames()

> **getRootFileNames**(): readonly `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2278

Get a list of root file names that were passed to a 'createProgram'

#### Returns

readonly `string`[]

***

### getSemanticDiagnostics()

> **getSemanticDiagnostics**(`sourceFile?`, `cancellationToken?`): readonly [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2298

The first time this is called, it will return global diagnostics (no location).

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

#### Returns

readonly [`Diagnostic`](Diagnostic.md)[]

***

### getSemanticDiagnosticsForLinter()

> **getSemanticDiagnosticsForLinter**(`sourceFile?`, `cancellationToken?`): readonly [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2299

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

#### Returns

readonly [`Diagnostic`](Diagnostic.md)[]

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

### getSourceFileFromReference()

> **getSourceFileFromReference**(`referencingFile`, `ref`): `undefined` \| [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2324

#### Parameters

##### referencingFile

[`SourceFile`](SourceFile.md) | [`UnparsedSource`](UnparsedSource.md)

##### ref

[`FileReference`](FileReference.md)

#### Returns

`undefined` \| [`SourceFile`](SourceFile.md)

***

### getSourceFiles()

> **getSourceFiles**(): readonly [`SourceFile`](SourceFile.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2282

Get a list of files in the program

#### Returns

readonly [`SourceFile`](SourceFile.md)[]

***

### getSymbolCount()

> **getSymbolCount**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2313

#### Returns

`number`

***

### getSyntacticDiagnostics()

> **getSyntacticDiagnostics**(`sourceFile?`, `cancellationToken?`): readonly [`DiagnosticWithLocation`](DiagnosticWithLocation.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2296

#### Parameters

##### sourceFile?

[`SourceFile`](SourceFile.md)

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

#### Returns

readonly [`DiagnosticWithLocation`](DiagnosticWithLocation.md)[]

***

### getTypeChecker()

> **getTypeChecker**(): [`TypeChecker`](TypeChecker.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2306

Gets a type checker that can be used to semantically analyze source files in the program.

#### Returns

[`TypeChecker`](TypeChecker.md)

***

### getTypeCount()

> **getTypeCount**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2314

#### Returns

`number`

***

### isSourceFileDefaultLibrary()

> **isSourceFileDefaultLibrary**(`file`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2323

#### Parameters

##### file

[`SourceFile`](SourceFile.md)

#### Returns

`boolean`

***

### isSourceFileFromExternalLibrary()

> **isSourceFileFromExternalLibrary**(`file`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2322

#### Parameters

##### file

[`SourceFile`](SourceFile.md)

#### Returns

`boolean`

***

### releaseTypeChecker()

> **releaseTypeChecker**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2333

Release typeChecker & linterTypeChecker

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ProgramHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ProgramHost

# Interface: ProgramHost\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5808

## Extended by

- [`WatchCompilerHost`](WatchCompilerHost.md)
- [`SolutionBuilderHostBase`](SolutionBuilderHostBase.md)

## Type Parameters

### T

`T` *extends* [`BuilderProgram`](BuilderProgram.md)

## Properties

### createProgram

> **createProgram**: [`CreateProgram`](../type-aliases/CreateProgram.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5812

Used to create the program when need for program creation or recreation detected

## Methods

### createHash()?

> `optional` **createHash**(`data`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5818

#### Parameters

##### data

`string`

#### Returns

`string`

***

### directoryExists()?

> `optional` **directoryExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5830

If provided, used for module resolution as well as to handle directory structure

#### Parameters

##### path

`string`

#### Returns

`boolean`

***

### fileExists()

> **fileExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5823

Use to check file presence for source files and
if resolveModuleNames is not provided (complier is in charge of module resolution) then module files as well

#### Parameters

##### path

`string`

#### Returns

`boolean`

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5815

#### Returns

`string`

***

### getDefaultLibFileName()

> **getDefaultLibFileName**(`options`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5816

#### Parameters

##### options

[`CompilerOptions`](CompilerOptions.md)

#### Returns

`string`

***

### getDefaultLibLocation()?

> `optional` **getDefaultLibLocation**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5817

#### Returns

`string`

***

### getDirectories()?

> `optional` **getDirectories**(`path`): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5832

If provided, used in resolutions as well as handling directory structure

#### Parameters

##### path

`string`

#### Returns

`string`[]

***

### getEnvironmentVariable()?

> `optional` **getEnvironmentVariable**(`name`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5840

If provided is used to get the environment variable

#### Parameters

##### name

`string`

#### Returns

`undefined` \| `string`

***

### getModuleResolutionCache()?

> `optional` **getModuleResolutionCache**(): `undefined` \| [`ModuleResolutionCache`](ModuleResolutionCache.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5850

Returns the module resolution cache used by a provided `resolveModuleNames` implementation so that any non-name module resolution operations (eg, package.json lookup) can reuse it

#### Returns

`undefined` \| [`ModuleResolutionCache`](ModuleResolutionCache.md)

***

### getNewLine()

> **getNewLine**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5814

#### Returns

`string`

***

### hasInvalidatedResolutions()?

> `optional` **hasInvalidatedResolutions**(`filePath`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5846

If provided along with custom resolveModuleNames or resolveTypeReferenceDirectives, used to determine if unchanged file path needs to re-resolve modules/type reference directives

#### Parameters

##### filePath

[`Path`](../type-aliases/Path.md)

#### Returns

`boolean`

***

### readDirectory()?

> `optional` **readDirectory**(`path`, `extensions?`, `exclude?`, `include?`, `depth?`): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5834

If provided, used to cache and handle directory structure modifications

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5828

Use to read file text for source files and
if resolveModuleNames is not provided (complier is in charge of module resolution) then module files as well

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5836

Symbol links resolution

#### Parameters

##### path

`string`

#### Returns

`string`

***

### resolveModuleNames()?

> `optional` **resolveModuleNames**(`moduleNames`, `containingFile`, `reusedNames`, `redirectedReference`, `options`, `containingSourceFile?`): (`undefined` \| [`ResolvedModule`](ResolvedModule.md))[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5842

If provided, used to resolve the module names, otherwise typescript's default module resolution

#### Parameters

##### moduleNames

`string`[]

##### containingFile

`string`

##### reusedNames

`undefined` | `string`[]

##### redirectedReference

`undefined` | [`ResolvedProjectReference`](ResolvedProjectReference.md)

##### options

[`CompilerOptions`](CompilerOptions.md)

##### containingSourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

(`undefined` \| [`ResolvedModule`](ResolvedModule.md))[]

***

### resolveTypeReferenceDirectives()?

> `optional` **resolveTypeReferenceDirectives**(`typeReferenceDirectiveNames`, `containingFile`, `redirectedReference`, `options`, `containingFileMode?`): (`undefined` \| [`ResolvedTypeReferenceDirective`](ResolvedTypeReferenceDirective.md))[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5844

If provided, used to resolve type reference directives, otherwise typescript's default resolution

#### Parameters

##### typeReferenceDirectiveNames

`string`[] | readonly [`FileReference`](FileReference.md)[]

##### containingFile

`string`

##### redirectedReference

`undefined` | [`ResolvedProjectReference`](ResolvedProjectReference.md)

##### options

[`CompilerOptions`](CompilerOptions.md)

##### containingFileMode?

[`CommonJS`](../enumerations/ModuleKind.md#commonjs) | [`ESNext`](../enumerations/ModuleKind.md#esnext)

#### Returns

(`undefined` \| [`ResolvedTypeReferenceDirective`](ResolvedTypeReferenceDirective.md))[]

***

### trace()?

> `optional` **trace**(`s`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5838

If provided would be used to write log about compilation

#### Parameters

##### s

`string`

#### Returns

`void`

***

### useCaseSensitiveFileNames()

> **useCaseSensitiveFileNames**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5813

#### Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ProjectReference.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ProjectReference

# Interface: ProjectReference

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3043

## Properties

### circular?

> `optional` **circular**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3051

True if it is intended that this reference form a circularity

***

### originalPath?

> `optional` **originalPath**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3047

The path as the user originally wrote it

***

### path

> **path**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3045

A normalized path on disk

***

### prepend?

> `optional` **prepend**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3049

True if the output of this reference should be prepended to the output of this project. Only valid for --outFile compilations




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PropertyAccessChain.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PropertyAccessChain

# Interface: PropertyAccessChain

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1310

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

### \_optionalChainBrand

> **\_optionalChainBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1311

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

> `readonly` **expression**: [`LeftHandSideExpression`](LeftHandSideExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1306

#### Inherited from

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1312

#### Overrides

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PropertyAccessEntityNameExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PropertyAccessEntityNameExpression

# Interface: PropertyAccessEntityNameExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1318

Brand for a PropertyAccessExpression which, like a QualifiedName, consists of a sequence of identifiers separated by dots.

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

### \_propertyAccessExpressionLikeQualifiedNameBrand?

> `optional` **\_propertyAccessExpressionLikeQualifiedNameBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1319

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

> `readonly` **expression**: [`EntityNameExpression`](../type-aliases/EntityNameExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1320

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

> `readonly` **name**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1321

#### Overrides

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PropertyAccessExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PropertyAccessExpression

# Interface: PropertyAccessExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1304

## Extends

- [`MemberExpression`](MemberExpression.md).[`NamedDeclaration`](NamedDeclaration.md)

## Extended by

- [`PropertyAccessChain`](PropertyAccessChain.md)
- [`SuperPropertyAccessExpression`](SuperPropertyAccessExpression.md)
- [`PropertyAccessEntityNameExpression`](PropertyAccessEntityNameExpression.md)
- [`JsxTagNamePropertyAccess`](JsxTagNamePropertyAccess.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`_declarationBrand`](NamedDeclaration.md#_declarationbrand)

***

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

[`NamedDeclaration`](NamedDeclaration.md).[`decorators`](NamedDeclaration.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`end`](NamedDeclaration.md#end)

***

### expression

> `readonly` **expression**: [`LeftHandSideExpression`](LeftHandSideExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1306

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`flags`](NamedDeclaration.md#flags)

***

### kind

> `readonly` **kind**: [`PropertyAccessExpression`](../enumerations/SyntaxKind.md#propertyaccessexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1305

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

> `readonly` **name**: [`MemberName`](../type-aliases/MemberName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1308

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`name`](NamedDeclaration.md#name)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`parent`](NamedDeclaration.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`pos`](NamedDeclaration.md#pos)

***

### questionDotToken?

> `readonly` `optional` **questionDotToken**: [`QuestionDotToken`](../type-aliases/QuestionDotToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1307

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PropertyAssignment.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PropertyAssignment

# Interface: PropertyAssignment

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:803

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

### ~~exclamationToken?~~

> `readonly` `optional` **exclamationToken**: [`ExclamationToken`](../type-aliases/ExclamationToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8396

#### Deprecated

A property assignment cannot have an exclamation token

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`flags`](ObjectLiteralElement.md#flags)

***

### initializer

> `readonly` **initializer**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:807

***

### kind

> `readonly` **kind**: [`PropertyAssignment`](../enumerations/SyntaxKind.md#propertyassignment)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:804

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

### name

> `readonly` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:806

#### Overrides

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`name`](ObjectLiteralElement.md#name)

***

### parent

> `readonly` **parent**: [`ObjectLiteralExpression`](ObjectLiteralExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:805

#### Overrides

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`parent`](ObjectLiteralElement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`pos`](ObjectLiteralElement.md#pos)

***

### ~~questionToken?~~

> `readonly` `optional` **questionToken**: [`QuestionToken`](../type-aliases/QuestionToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8394

#### Deprecated

A property assignment cannot have a question token

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PropertyDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PropertyDeclaration

# Interface: PropertyDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:784

## Extends

- [`ClassElement`](ClassElement.md).[`JSDocContainer`](JSDocContainer.md)

## Extended by

- [`AutoAccessorPropertyDeclaration`](AutoAccessorPropertyDeclaration.md)

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:790

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`ClassElement`](ClassElement.md).[`flags`](ClassElement.md#flags)

***

### initializer?

> `readonly` `optional` **initializer**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:792

***

### kind

> `readonly` **kind**: [`PropertyDeclaration`](../enumerations/SyntaxKind.md#propertydeclaration)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:785

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

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`ModifierLike`](../type-aliases/ModifierLike.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:787

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

### name

> `readonly` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:788

#### Overrides

[`ClassElement`](ClassElement.md).[`name`](ClassElement.md#name)

***

### parent

> `readonly` **parent**: [`ClassLikeDeclaration`](../type-aliases/ClassLikeDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:786

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:789

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:791

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PropertyLikeDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PropertyLikeDeclaration

# Interface: PropertyLikeDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:822

## Extends

- [`NamedDeclaration`](NamedDeclaration.md)

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

### kind

> `readonly` **kind**: [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:598

#### Inherited from

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:823

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`name`](NamedDeclaration.md#name)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PropertySignature.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PropertySignature

# Interface: PropertySignature

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:777

## Extends

- [`TypeElement`](TypeElement.md).[`JSDocContainer`](JSDocContainer.md)

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

### ~~initializer?~~

> `readonly` `optional` **initializer**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8390

#### Deprecated

A property signature cannot have an initializer

***

### kind

> `readonly` **kind**: [`PropertySignature`](../enumerations/SyntaxKind.md#propertysignature)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:778

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

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`Modifier`](../type-aliases/Modifier.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:779

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Overrides

[`TypeElement`](TypeElement.md).[`modifiers`](TypeElement.md#modifiers)

***

### name

> `readonly` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:780

#### Overrides

[`TypeElement`](TypeElement.md).[`name`](TypeElement.md#name)

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:781

#### Overrides

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:782

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PseudoBigInt.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PseudoBigInt

# Interface: PseudoBigInt

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4507

Represents a bigint literal value without requiring bigint support

## Properties

### base10Value

> **base10Value**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4509

***

### negative

> **negative**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4508




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/PunctuationToken.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / PunctuationToken

# Interface: PunctuationToken\<TKind\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:622

## Extends

- [`Token`](Token.md)\<`TKind`\>

## Type Parameters

### TKind

`TKind` *extends* [`PunctuationSyntaxKind`](../type-aliases/PunctuationSyntaxKind.md)

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

[`Token`](Token.md).[`decorators`](Token.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Token`](Token.md).[`end`](Token.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Token`](Token.md).[`flags`](Token.md#flags)

***

### kind

> `readonly` **kind**: `TKind`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:619

#### Inherited from

[`Token`](Token.md).[`kind`](Token.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Token`](Token.md).[`locals`](Token.md#locals)

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

[`Token`](Token.md).[`modifiers`](Token.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`Token`](Token.md).[`parent`](Token.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`Token`](Token.md).[`pos`](Token.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Token`](Token.md).[`skipCheck`](Token.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Token`](Token.md).[`symbol`](Token.md#symbol)

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

[`Token`](Token.md).[`forEachChild`](Token.md#foreachchild)

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

[`Token`](Token.md).[`getChildAt`](Token.md#getchildat)

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

[`Token`](Token.md).[`getChildCount`](Token.md#getchildcount)

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

[`Token`](Token.md).[`getChildren`](Token.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`Token`](Token.md).[`getEnd`](Token.md#getend)

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

[`Token`](Token.md).[`getFirstToken`](Token.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`Token`](Token.md).[`getFullStart`](Token.md#getfullstart)

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

[`Token`](Token.md).[`getFullText`](Token.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`Token`](Token.md).[`getFullWidth`](Token.md#getfullwidth)

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

[`Token`](Token.md).[`getLastToken`](Token.md#getlasttoken)

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

[`Token`](Token.md).[`getLeadingTriviaWidth`](Token.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`Token`](Token.md).[`getSourceFile`](Token.md#getsourcefile)

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

[`Token`](Token.md).[`getStart`](Token.md#getstart)

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

[`Token`](Token.md).[`getText`](Token.md#gettext)

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

[`Token`](Token.md).[`getWidth`](Token.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Push.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Push

# Interface: Push\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:89

Array that is only intended to be pushed to, never read.

## Type Parameters

### T

`T`

## Methods

### push()

> **push**(...`values`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:90

#### Parameters

##### values

...`T`[]

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/QualifiedName.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / QualifiedName

# Interface: QualifiedName

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:689

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

> `readonly` **kind**: [`QualifiedName`](../enumerations/SyntaxKind.md#qualifiedname)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:690

#### Overrides

[`Node`](Node.md).[`kind`](Node.md#kind)

***

### left

> `readonly` **left**: [`EntityName`](../type-aliases/EntityName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:691

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

### right

> `readonly` **right**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:692

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/QuickInfo.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / QuickInfo

# Interface: QuickInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6881

## Properties

### displayParts?

> `optional` **displayParts**: [`SymbolDisplayPart`](SymbolDisplayPart.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6885

***

### documentation?

> `optional` **documentation**: [`SymbolDisplayPart`](SymbolDisplayPart.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6886

***

### kind

> **kind**: [`ScriptElementKind`](../enumerations/ScriptElementKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6882

***

### kindModifiers

> **kindModifiers**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6883

***

### tags?

> `optional` **tags**: [`JSDocTagInfo`](JSDocTagInfo-1.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6887

***

### textSpan

> **textSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6884




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/RawSourceMap.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / RawSourceMap

# Interface: RawSourceMap

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4272

## Properties

### file

> **file**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4274

***

### mappings

> **mappings**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4278

***

### names?

> `optional` **names**: `null` \| `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4279

***

### sourceRoot?

> `optional` **sourceRoot**: `null` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4275

***

### sources

> **sources**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4276

***

### sourcesContent?

> `optional` **sourcesContent**: `null` \| (`null` \| `string`)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4277

***

### version

> **version**: `3`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4273




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ReadBuildProgramHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ReadBuildProgramHost

# Interface: ReadBuildProgramHost

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5774

## Methods

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5776

#### Returns

`string`

***

### getLastCompiledProgram()?

> `optional` **getLastCompiledProgram**(): [`Program`](Program.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5778

#### Returns

[`Program`](Program.md)

***

### readFile()

> **readFile**(`fileName`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5777

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| `string`

***

### useCaseSensitiveFileNames()

> **useCaseSensitiveFileNames**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5775

#### Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ReadonlyCollection.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ReadonlyCollection

# Interface: ReadonlyCollection\<K\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:35

Common read methods for ES6 Map/Set.

## Extended by

- [`Collection`](Collection.md)
- [`ReadonlyESMap`](ReadonlyESMap.md)
- [`ReadonlySet`](ReadonlySet.md)

## Type Parameters

### K

`K`

## Properties

### size

> `readonly` **size**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:36

## Methods

### has()

> **has**(`key`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:37

#### Parameters

##### key

`K`

#### Returns

`boolean`

***

### keys()

> **keys**(): [`Iterator`](Iterator.md)\<`K`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:38

#### Returns

[`Iterator`](Iterator.md)\<`K`\>




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ReadonlyESMap.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ReadonlyESMap

# Interface: ReadonlyESMap\<K, V\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:46

ES6 Map interface, only read methods included.

## Extends

- [`ReadonlyCollection`](ReadonlyCollection.md)\<`K`\>

## Extended by

- [`ReadonlyMap`](ReadonlyMap.md)
- [`ESMap`](ESMap.md)
- [`ReadonlyUnderscoreEscapedMap`](ReadonlyUnderscoreEscapedMap.md)

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

[`ReadonlyCollection`](ReadonlyCollection.md).[`size`](ReadonlyCollection.md#size)

## Methods

### entries()

> **entries**(): [`Iterator`](Iterator.md)\<\[`K`, `V`\]\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:49

#### Returns

[`Iterator`](Iterator.md)\<\[`K`, `V`\]\>

***

### forEach()

> **forEach**(`action`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:50

#### Parameters

##### action

(`value`, `key`) => `void`

#### Returns

`void`

***

### get()

> **get**(`key`): `undefined` \| `V`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:47

#### Parameters

##### key

`K`

#### Returns

`undefined` \| `V`

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

[`ReadonlyCollection`](ReadonlyCollection.md).[`has`](ReadonlyCollection.md#has)

***

### keys()

> **keys**(): [`Iterator`](Iterator.md)\<`K`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:38

#### Returns

[`Iterator`](Iterator.md)\<`K`\>

#### Inherited from

[`ReadonlyCollection`](ReadonlyCollection.md).[`keys`](ReadonlyCollection.md#keys)

***

### values()

> **values**(): [`Iterator`](Iterator.md)\<`V`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:48

#### Returns

[`Iterator`](Iterator.md)\<`V`\>




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ReadonlyMap.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ReadonlyMap

# Interface: ReadonlyMap\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:55

ES6 Map interface, only read methods included.

## Extends

- [`ReadonlyESMap`](ReadonlyESMap.md)\<`string`, `T`\>

## Type Parameters

### T

`T`

## Properties

### size

> `readonly` **size**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:36

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`size`](ReadonlyESMap.md#size)

## Methods

### entries()

> **entries**(): [`Iterator`](Iterator.md)\<\[`string`, `T`\]\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:49

#### Returns

[`Iterator`](Iterator.md)\<\[`string`, `T`\]\>

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

> **get**(`key`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:47

#### Parameters

##### key

`string`

#### Returns

`undefined` \| `T`

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`get`](ReadonlyESMap.md#get)

***

### has()

> **has**(`key`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:37

#### Parameters

##### key

`string`

#### Returns

`boolean`

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`has`](ReadonlyESMap.md#has)

***

### keys()

> **keys**(): [`Iterator`](Iterator.md)\<`string`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:38

#### Returns

[`Iterator`](Iterator.md)\<`string`\>

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`keys`](ReadonlyESMap.md#keys)

***

### values()

> **values**(): [`Iterator`](Iterator.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:48

#### Returns

[`Iterator`](Iterator.md)\<`T`\>

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`values`](ReadonlyESMap.md#values)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ReadonlySet.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ReadonlySet

# Interface: ReadonlySet\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:67

ES6 Set interface, only read methods included.

## Extends

- [`ReadonlyCollection`](ReadonlyCollection.md)\<`T`\>

## Extended by

- [`Set`](Set.md)

## Type Parameters

### T

`T`

## Properties

### size

> `readonly` **size**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:36

#### Inherited from

[`ReadonlyCollection`](ReadonlyCollection.md).[`size`](ReadonlyCollection.md#size)

## Methods

### entries()

> **entries**(): [`Iterator`](Iterator.md)\<\[`T`, `T`\]\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:70

#### Returns

[`Iterator`](Iterator.md)\<\[`T`, `T`\]\>

***

### forEach()

> **forEach**(`action`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:71

#### Parameters

##### action

(`value`, `key`) => `void`

#### Returns

`void`

***

### has()

> **has**(`value`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:68

#### Parameters

##### value

`T`

#### Returns

`boolean`

#### Overrides

[`ReadonlyCollection`](ReadonlyCollection.md).[`has`](ReadonlyCollection.md#has)

***

### keys()

> **keys**(): [`Iterator`](Iterator.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:38

#### Returns

[`Iterator`](Iterator.md)\<`T`\>

#### Inherited from

[`ReadonlyCollection`](ReadonlyCollection.md).[`keys`](ReadonlyCollection.md#keys)

***

### values()

> **values**(): [`Iterator`](Iterator.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:69

#### Returns

[`Iterator`](Iterator.md)\<`T`\>




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ReadonlyTextRange.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ReadonlyTextRange

# Interface: ReadonlyTextRange

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:101

## Extended by

- [`Node`](Node.md)
- [`NodeArray`](NodeArray.md)

## Properties

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ReadonlyUnderscoreEscapedMap.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ReadonlyUnderscoreEscapedMap

# Interface: ReadonlyUnderscoreEscapedMap\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2711

ReadonlyMap where keys are `__String`s.

## Extends

- [`ReadonlyESMap`](ReadonlyESMap.md)\<[`__String`](../type-aliases/String.md), `T`\>

## Extended by

- [`UnderscoreEscapedMap`](UnderscoreEscapedMap.md)

## Type Parameters

### T

`T`

## Properties

### size

> `readonly` **size**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:36

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`size`](ReadonlyESMap.md#size)

## Methods

### entries()

> **entries**(): [`Iterator`](Iterator.md)\<\[[`__String`](../type-aliases/String.md), `T`\]\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:49

#### Returns

[`Iterator`](Iterator.md)\<\[[`__String`](../type-aliases/String.md), `T`\]\>

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

> **get**(`key`): `undefined` \| `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:47

#### Parameters

##### key

[`__String`](../type-aliases/String.md)

#### Returns

`undefined` \| `T`

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`get`](ReadonlyESMap.md#get)

***

### has()

> **has**(`key`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:37

#### Parameters

##### key

[`__String`](../type-aliases/String.md)

#### Returns

`boolean`

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`has`](ReadonlyESMap.md#has)

***

### keys()

> **keys**(): [`Iterator`](Iterator.md)\<[`__String`](../type-aliases/String.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:38

#### Returns

[`Iterator`](Iterator.md)\<[`__String`](../type-aliases/String.md)\>

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`keys`](ReadonlyESMap.md#keys)

***

### values()

> **values**(): [`Iterator`](Iterator.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:48

#### Returns

[`Iterator`](Iterator.md)\<`T`\>

#### Inherited from

[`ReadonlyESMap`](ReadonlyESMap.md).[`values`](ReadonlyESMap.md#values)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/RefactorActionInfo.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / RefactorActionInfo

# Interface: RefactorActionInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6663

Represents a single refactoring action - for example, the "Extract Method..." refactor might
offer several actions, each corresponding to a surround class or closure to extract into.

## Properties

### description

> **description**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6673

A description of this refactoring action to show to the user.
If the parent refactoring is inlined away, this will be the only text shown,
so this description should make sense by itself if the parent is inlineable=true

***

### kind?

> `optional` **kind**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6682

The hierarchical dotted name of the refactor action.

***

### name

> **name**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6667

The programmatic name of the refactoring action

***

### notApplicableReason?

> `optional` **notApplicableReason**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6678

A message to show to the user if the refactoring cannot be applied in
the current context.




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/RefactorEditInfo.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / RefactorEditInfo

# Interface: RefactorEditInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6688

A set of edits to make in response to a refactor action, plus an optional
location where renaming should be invoked from

## Properties

### commands?

> `optional` **commands**: [`InstallPackageAction`](InstallPackageAction.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6692

***

### edits

> **edits**: [`FileTextChanges`](FileTextChanges.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6689

***

### renameFilename?

> `optional` **renameFilename**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6690

***

### renameLocation?

> `optional` **renameLocation**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6691




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ReferenceEntry.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ReferenceEntry

# Interface: ReferenceEntry

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6720

## Extends

- [`DocumentSpan`](DocumentSpan.md)

## Extended by

- [`ReferencedSymbolEntry`](ReferencedSymbolEntry.md)

## Properties

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

### isInString?

> `optional` **isInString**: `true`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6722

***

### isWriteAccess

> **isWriteAccess**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6721

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




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ReferencedSymbol.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ReferencedSymbol

# Interface: ReferencedSymbol

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6835

## Properties

### definition

> **definition**: [`ReferencedSymbolDefinitionInfo`](ReferencedSymbolDefinitionInfo.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6836

***

### references

> **references**: [`ReferencedSymbolEntry`](ReferencedSymbolEntry.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6837




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ReferencedSymbolDefinitionInfo.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ReferencedSymbolDefinitionInfo

# Interface: ReferencedSymbolDefinitionInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6832

## Extends

- [`DefinitionInfo`](DefinitionInfo.md)

## Properties

### containerKind

> **containerKind**: [`ScriptElementKind`](../enumerations/ScriptElementKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6824

#### Inherited from

[`DefinitionInfo`](DefinitionInfo.md).[`containerKind`](DefinitionInfo.md#containerkind)

***

### containerName

> **containerName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6825

#### Inherited from

[`DefinitionInfo`](DefinitionInfo.md).[`containerName`](DefinitionInfo.md#containername)

***

### contextSpan?

> `optional` **contextSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6713

If DocumentSpan.textSpan is the span for name of the declaration,
then this is the span for relevant declaration

#### Inherited from

[`DefinitionInfo`](DefinitionInfo.md).[`contextSpan`](DefinitionInfo.md#contextspan)

***

### displayParts

> **displayParts**: [`SymbolDisplayPart`](SymbolDisplayPart.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6833

***

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6702

#### Inherited from

[`DefinitionInfo`](DefinitionInfo.md).[`fileName`](DefinitionInfo.md#filename)

***

### kind

> **kind**: [`ScriptElementKind`](../enumerations/ScriptElementKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6822

#### Inherited from

[`DefinitionInfo`](DefinitionInfo.md).[`kind`](DefinitionInfo.md#kind)

***

### name

> **name**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6823

#### Inherited from

[`DefinitionInfo`](DefinitionInfo.md).[`name`](DefinitionInfo.md#name)

***

### originalContextSpan?

> `optional` **originalContextSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6714

#### Inherited from

[`DefinitionInfo`](DefinitionInfo.md).[`originalContextSpan`](DefinitionInfo.md#originalcontextspan)

***

### originalFileName?

> `optional` **originalFileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6708

#### Inherited from

[`DefinitionInfo`](DefinitionInfo.md).[`originalFileName`](DefinitionInfo.md#originalfilename)

***

### originalTextSpan?

> `optional` **originalTextSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6707

If the span represents a location that was remapped (e.g. via a .d.ts.map file),
then the original filename and span will be specified here

#### Inherited from

[`DefinitionInfo`](DefinitionInfo.md).[`originalTextSpan`](DefinitionInfo.md#originaltextspan)

***

### textSpan

> **textSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6701

#### Inherited from

[`DefinitionInfo`](DefinitionInfo.md).[`textSpan`](DefinitionInfo.md#textspan)

***

### unverified?

> `optional` **unverified**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6826

#### Inherited from

[`DefinitionInfo`](DefinitionInfo.md).[`unverified`](DefinitionInfo.md#unverified)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ReferencedSymbolEntry.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ReferencedSymbolEntry

# Interface: ReferencedSymbolEntry

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6839

## Extends

- [`ReferenceEntry`](ReferenceEntry.md)

## Properties

### contextSpan?

> `optional` **contextSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6713

If DocumentSpan.textSpan is the span for name of the declaration,
then this is the span for relevant declaration

#### Inherited from

[`ReferenceEntry`](ReferenceEntry.md).[`contextSpan`](ReferenceEntry.md#contextspan)

***

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6702

#### Inherited from

[`ReferenceEntry`](ReferenceEntry.md).[`fileName`](ReferenceEntry.md#filename)

***

### isDefinition?

> `optional` **isDefinition**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6840

***

### isInString?

> `optional` **isInString**: `true`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6722

#### Inherited from

[`ReferenceEntry`](ReferenceEntry.md).[`isInString`](ReferenceEntry.md#isinstring)

***

### isWriteAccess

> **isWriteAccess**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6721

#### Inherited from

[`ReferenceEntry`](ReferenceEntry.md).[`isWriteAccess`](ReferenceEntry.md#iswriteaccess)

***

### originalContextSpan?

> `optional` **originalContextSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6714

#### Inherited from

[`ReferenceEntry`](ReferenceEntry.md).[`originalContextSpan`](ReferenceEntry.md#originalcontextspan)

***

### originalFileName?

> `optional` **originalFileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6708

#### Inherited from

[`ReferenceEntry`](ReferenceEntry.md).[`originalFileName`](ReferenceEntry.md#originalfilename)

***

### originalTextSpan?

> `optional` **originalTextSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6707

If the span represents a location that was remapped (e.g. via a .d.ts.map file),
then the original filename and span will be specified here

#### Inherited from

[`ReferenceEntry`](ReferenceEntry.md).[`originalTextSpan`](ReferenceEntry.md#originaltextspan)

***

### textSpan

> **textSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6701

#### Inherited from

[`ReferenceEntry`](ReferenceEntry.md).[`textSpan`](ReferenceEntry.md#textspan)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/RegularExpressionLiteral.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / RegularExpressionLiteral

# Interface: RegularExpressionLiteral

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1229

## Extends

- [`LiteralExpression`](LiteralExpression.md)

## Properties

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

[`LiteralExpression`](LiteralExpression.md).[`decorators`](LiteralExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`end`](LiteralExpression.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`flags`](LiteralExpression.md#flags)

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

> `readonly` **kind**: [`RegularExpressionLiteral`](../enumerations/SyntaxKind.md#regularexpressionliteral)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1230

#### Overrides

[`LiteralExpression`](LiteralExpression.md).[`kind`](LiteralExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`locals`](LiteralExpression.md#locals)

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

[`LiteralExpression`](LiteralExpression.md).[`modifiers`](LiteralExpression.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`parent`](LiteralExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`pos`](LiteralExpression.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`skipCheck`](LiteralExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`symbol`](LiteralExpression.md#symbol)

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

[`LiteralExpression`](LiteralExpression.md).[`forEachChild`](LiteralExpression.md#foreachchild)

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

[`LiteralExpression`](LiteralExpression.md).[`getChildAt`](LiteralExpression.md#getchildat)

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

[`LiteralExpression`](LiteralExpression.md).[`getChildCount`](LiteralExpression.md#getchildcount)

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

[`LiteralExpression`](LiteralExpression.md).[`getChildren`](LiteralExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`getEnd`](LiteralExpression.md#getend)

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

[`LiteralExpression`](LiteralExpression.md).[`getFirstToken`](LiteralExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`getFullStart`](LiteralExpression.md#getfullstart)

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

[`LiteralExpression`](LiteralExpression.md).[`getFullText`](LiteralExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`getFullWidth`](LiteralExpression.md#getfullwidth)

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

[`LiteralExpression`](LiteralExpression.md).[`getLastToken`](LiteralExpression.md#getlasttoken)

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

[`LiteralExpression`](LiteralExpression.md).[`getLeadingTriviaWidth`](LiteralExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`LiteralExpression`](LiteralExpression.md).[`getSourceFile`](LiteralExpression.md#getsourcefile)

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

[`LiteralExpression`](LiteralExpression.md).[`getStart`](LiteralExpression.md#getstart)

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

[`LiteralExpression`](LiteralExpression.md).[`getText`](LiteralExpression.md#gettext)

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

[`LiteralExpression`](LiteralExpression.md).[`getWidth`](LiteralExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/RenameInfoFailure.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / RenameInfoFailure

# Interface: RenameInfoFailure

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6903

## Properties

### canRename

> **canRename**: `false`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6904

***

### localizedErrorMessage

> **localizedErrorMessage**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6905




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/RenameInfoOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / RenameInfoOptions

# Interface: ~~RenameInfoOptions~~

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6910

## Deprecated

Use `UserPreferences` instead.

## Properties

### ~~allowRenameOfImportPath?~~

> `readonly` `optional` **allowRenameOfImportPath**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6911




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/RenameInfoSuccess.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / RenameInfoSuccess

# Interface: RenameInfoSuccess

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6890

## Properties

### canRename

> **canRename**: `true`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6891

***

### displayName

> **displayName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6897

***

### fileToRename?

> `optional` **fileToRename**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6896

File or directory to rename.
If set, `getEditsForFileRename` should be called instead of `findRenameLocations`.

***

### fullDisplayName

> **fullDisplayName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6898

***

### kind

> **kind**: [`ScriptElementKind`](../enumerations/ScriptElementKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6899

***

### kindModifiers

> **kindModifiers**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6900

***

### triggerSpan

> **triggerSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6901




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/RenameLocation.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / RenameLocation

# Interface: RenameLocation

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6716

## Extends

- [`DocumentSpan`](DocumentSpan.md)

## Properties

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

### prefixText?

> `readonly` `optional` **prefixText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6717

***

### suffixText?

> `readonly` `optional` **suffixText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6718

***

### textSpan

> **textSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6701

#### Inherited from

[`DocumentSpan`](DocumentSpan.md).[`textSpan`](DocumentSpan.md#textspan)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ReportFileInError.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ReportFileInError

# Interface: ReportFileInError

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5931

## Properties

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5932

***

### line

> **line**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5933




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ResolveProjectReferencePathHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ResolveProjectReferencePathHost

# Interface: ~~ResolveProjectReferencePathHost~~

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5619

## Deprecated

## Methods

### ~~fileExists()~~

> **fileExists**(`fileName`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5620

#### Parameters

##### fileName

`string`

#### Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ResolvedModule.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ResolvedModule

# Interface: ResolvedModule

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3370

Represents the result of module resolution.
Module resolution will pick up tsx/jsx/js files even if '--jsx' and '--allowJs' are turned off.
The Program will then filter results based on these flags.

Prefer to return a `ResolvedModuleFull` so that the file type does not have to be inferred.

## Extended by

- [`ResolvedModuleFull`](ResolvedModuleFull.md)

## Properties

### isExternalLibraryImport?

> `optional` **isExternalLibraryImport**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3374

True if `resolvedFileName` comes from `node_modules`.

***

### resolvedFileName

> **resolvedFileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3372

Path of the file the module was resolved to.




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ResolvedModuleFull.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ResolvedModuleFull

# Interface: ResolvedModuleFull

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3381

ResolvedModule with an explicitly provided `extension` property.
Prefer this over `ResolvedModule`.
If changing this, remember to change `moduleResolutionIsEqualTo`.

## Extends

- [`ResolvedModule`](ResolvedModule.md)

## Properties

### extension

> **extension**: [`Extension`](../enumerations/Extension.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3386

Extension of resolvedFileName. This must match what's at the end of resolvedFileName.
This is optional for backwards-compatibility, but will be added if not provided.

***

### isExternalLibraryImport?

> `optional` **isExternalLibraryImport**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3374

True if `resolvedFileName` comes from `node_modules`.

#### Inherited from

[`ResolvedModule`](ResolvedModule.md).[`isExternalLibraryImport`](ResolvedModule.md#isexternallibraryimport)

***

### packageId?

> `optional` **packageId**: [`PackageId`](PackageId.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3387

***

### resolvedFileName

> **resolvedFileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3372

Path of the file the module was resolved to.

#### Inherited from

[`ResolvedModule`](ResolvedModule.md).[`resolvedFileName`](ResolvedModule.md#resolvedfilename)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ResolvedModuleSpecifierInfo.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ResolvedModuleSpecifierInfo

# Interface: ResolvedModuleSpecifierInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4360

## Properties

### isBlockedByPackageJsonDependencies

> **isBlockedByPackageJsonDependencies**: `undefined` \| `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4363

***

### modulePaths

> **modulePaths**: `undefined` \| readonly [`ModulePath`](ModulePath.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4361

***

### moduleSpecifiers

> **moduleSpecifiers**: `undefined` \| readonly `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4362




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ResolvedModuleWithFailedLookupLocations.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ResolvedModuleWithFailedLookupLocations

# Interface: ResolvedModuleWithFailedLookupLocations

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3425

## Properties

### resolvedModule

> `readonly` **resolvedModule**: `undefined` \| [`ResolvedModuleFull`](ResolvedModuleFull.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3426




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ResolvedProjectReference.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ResolvedProjectReference

# Interface: ResolvedProjectReference

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2336

## Properties

### commandLine

> **commandLine**: [`ParsedCommandLine`](ParsedCommandLine.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2337

***

### references?

> `optional` **references**: readonly (`undefined` \| `ResolvedProjectReference`)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2339

***

### sourceFile

> **sourceFile**: [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2338




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ResolvedTypeReferenceDirective.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ResolvedTypeReferenceDirective

# Interface: ResolvedTypeReferenceDirective

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3428

## Properties

### isExternalLibraryImport?

> `optional` **isExternalLibraryImport**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3433

True if `resolvedFileName` comes from `node_modules` or `oh_modules`.

***

### packageId?

> `optional` **packageId**: [`PackageId`](PackageId.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3431

***

### primary

> **primary**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3429

***

### resolvedFileName

> **resolvedFileName**: `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3430




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ResolvedTypeReferenceDirectiveWithFailedLookupLocations.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ResolvedTypeReferenceDirectiveWithFailedLookupLocations

# Interface: ResolvedTypeReferenceDirectiveWithFailedLookupLocations

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3435

## Properties

### failedLookupLocations

> `readonly` **failedLookupLocations**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3437

***

### resolvedTypeReferenceDirective

> `readonly` **resolvedTypeReferenceDirective**: `undefined` \| [`ResolvedTypeReferenceDirective`](ResolvedTypeReferenceDirective.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3436




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/RestTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / RestTypeNode

# Interface: RestTypeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:987

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

> `readonly` **kind**: [`RestType`](../enumerations/SyntaxKind.md#resttype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:988

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

### type

> `readonly` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:989

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ReturnStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ReturnStatement

# Interface: ReturnStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1552

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

### expression?

> `readonly` `optional` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1554

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Statement`](Statement.md).[`flags`](Statement.md#flags)

***

### kind

> `readonly` **kind**: [`ReturnStatement`](../enumerations/SyntaxKind.md#returnstatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1553

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SatisfiesExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SatisfiesExpression

# Interface: SatisfiesExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1380

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1382

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Expression`](Expression.md).[`flags`](Expression.md#flags)

***

### kind

> `readonly` **kind**: [`SatisfiesExpression`](../enumerations/SyntaxKind.md#satisfiesexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1381

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

### type

> `readonly` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1383

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Scanner.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Scanner

# Interface: Scanner

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4574

## Methods

### getStartPos()

> **getStartPos**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4575

#### Returns

`number`

***

### getText()

> **getText**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4603

#### Returns

`string`

***

### getTextPos()

> **getTextPos**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4577

#### Returns

`number`

***

### getToken()

> **getToken**(): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4576

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### getTokenPos()

> **getTokenPos**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4578

#### Returns

`number`

***

### getTokenText()

> **getTokenText**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4579

#### Returns

`string`

***

### getTokenValue()

> **getTokenValue**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4580

#### Returns

`string`

***

### hasExtendedUnicodeEscape()

> **hasExtendedUnicodeEscape**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4582

#### Returns

`boolean`

***

### hasPrecedingLineBreak()

> **hasPrecedingLineBreak**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4583

#### Returns

`boolean`

***

### hasUnicodeEscape()

> **hasUnicodeEscape**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4581

#### Returns

`boolean`

***

### isIdentifier()

> **isIdentifier**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4584

#### Returns

`boolean`

***

### isReservedWord()

> **isReservedWord**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4585

#### Returns

`boolean`

***

### isUnterminated()

> **isUnterminated**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4586

#### Returns

`boolean`

***

### lookAhead()

> **lookAhead**\<`T`\>(`callback`): `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4609

#### Type Parameters

##### T

`T`

#### Parameters

##### callback

() => `T`

#### Returns

`T`

***

### reScanAsteriskEqualsToken()

> **reScanAsteriskEqualsToken**(): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4589

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### reScanGreaterToken()

> **reScanGreaterToken**(): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4587

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### reScanHashToken()

> **reScanHashToken**(): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4597

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### reScanInvalidIdentifier()

> **reScanInvalidIdentifier**(): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4599

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### reScanJsxAttributeValue()

> **reScanJsxAttributeValue**(): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4594

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### reScanJsxToken()

> **reScanJsxToken**(`allowMultilineJsxText?`): [`JsxTokenSyntaxKind`](../type-aliases/JsxTokenSyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4595

#### Parameters

##### allowMultilineJsxText?

`boolean`

#### Returns

[`JsxTokenSyntaxKind`](../type-aliases/JsxTokenSyntaxKind.md)

***

### reScanLessThanToken()

> **reScanLessThanToken**(): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4596

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### reScanQuestionToken()

> **reScanQuestionToken**(): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4598

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### reScanSlashToken()

> **reScanSlashToken**(): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4588

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### reScanTemplateHeadOrNoSubstitutionTemplate()

> **reScanTemplateHeadOrNoSubstitutionTemplate**(): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4591

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### reScanTemplateToken()

> **reScanTemplateToken**(`isTaggedTemplate`): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4590

#### Parameters

##### isTaggedTemplate

`boolean`

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### scan()

> **scan**(): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4602

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### scanJsDocToken()

> **scanJsDocToken**(): [`JSDocSyntaxKind`](../type-aliases/JSDocSyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4601

#### Returns

[`JSDocSyntaxKind`](../type-aliases/JSDocSyntaxKind.md)

***

### scanJsxAttributeValue()

> **scanJsxAttributeValue**(): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4593

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### scanJsxIdentifier()

> **scanJsxIdentifier**(): [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4592

#### Returns

[`SyntaxKind`](../enumerations/SyntaxKind.md)

***

### scanJsxToken()

> **scanJsxToken**(): [`JsxTokenSyntaxKind`](../type-aliases/JsxTokenSyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4600

#### Returns

[`JsxTokenSyntaxKind`](../type-aliases/JsxTokenSyntaxKind.md)

***

### scanRange()

> **scanRange**\<`T`\>(`start`, `length`, `callback`): `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4610

#### Type Parameters

##### T

`T`

#### Parameters

##### start

`number`

##### length

`number`

##### callback

() => `T`

#### Returns

`T`

***

### setEtsContext()

> **setEtsContext**(`isEtsContext`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4612

#### Parameters

##### isEtsContext

`boolean`

#### Returns

`void`

***

### setLanguageVariant()

> **setLanguageVariant**(`variant`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4607

#### Parameters

##### variant

[`LanguageVariant`](../enumerations/LanguageVariant.md)

#### Returns

`void`

***

### setOnError()

> **setOnError**(`onError`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4605

#### Parameters

##### onError

`undefined` | [`ErrorCallback`](../type-aliases/ErrorCallback.md)

#### Returns

`void`

***

### setScriptTarget()

> **setScriptTarget**(`scriptTarget`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4606

#### Parameters

##### scriptTarget

[`ScriptTarget`](../enumerations/ScriptTarget.md)

#### Returns

`void`

***

### setText()

> **setText**(`text`, `start?`, `length?`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4604

#### Parameters

##### text

`undefined` | `string`

##### start?

`number`

##### length?

`number`

#### Returns

`void`

***

### setTextPos()

> **setTextPos**(`textPos`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4608

#### Parameters

##### textPos

`number`

#### Returns

`void`

***

### tryScan()

> **tryScan**\<`T`\>(`callback`): `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4611

#### Type Parameters

##### T

`T`

#### Parameters

##### callback

() => `T`

#### Returns

`T`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ScopedEmitHelper.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ScopedEmitHelper

# Interface: ScopedEmitHelper

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3560

## Extends

- [`EmitHelperBase`](EmitHelperBase.md)

## Properties

### dependencies?

> `readonly` `optional` **dependencies**: [`EmitHelper`](../type-aliases/EmitHelper.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3558

#### Inherited from

[`EmitHelperBase`](EmitHelperBase.md).[`dependencies`](EmitHelperBase.md#dependencies)

***

### name

> `readonly` **name**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3554

#### Inherited from

[`EmitHelperBase`](EmitHelperBase.md).[`name`](EmitHelperBase.md#name)

***

### priority?

> `readonly` `optional` **priority**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3557

#### Inherited from

[`EmitHelperBase`](EmitHelperBase.md).[`priority`](EmitHelperBase.md#priority)

***

### scoped

> `readonly` **scoped**: `true`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3561

#### Overrides

[`EmitHelperBase`](EmitHelperBase.md).[`scoped`](EmitHelperBase.md#scoped)

***

### text

> `readonly` **text**: `string` \| (`node`) => `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3556

#### Inherited from

[`EmitHelperBase`](EmitHelperBase.md).[`text`](EmitHelperBase.md#text)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ScriptReferenceHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ScriptReferenceHost

# Interface: ScriptReferenceHost

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2230

## Extended by

- [`Program`](Program.md)
- [`EmitHost`](EmitHost.md)

## Methods

### getCompilerOptions()

> **getCompilerOptions**(): [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2231

#### Returns

[`CompilerOptions`](CompilerOptions.md)

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2234

#### Returns

`string`

***

### getSourceFile()

> **getSourceFile**(`fileName`): `undefined` \| [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2232

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| [`SourceFile`](SourceFile.md)

***

### getSourceFileByPath()

> **getSourceFileByPath**(`path`): `undefined` \| [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2233

#### Parameters

##### path

[`Path`](../type-aliases/Path.md)

#### Returns

`undefined` \| [`SourceFile`](SourceFile.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SelectionRange.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SelectionRange

# Interface: SelectionRange

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6923

## Properties

### parent?

> `optional` **parent**: `SelectionRange`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6925

***

### textSpan

> **textSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6924




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SemanticDiagnosticsBuilderProgram.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SemanticDiagnosticsBuilderProgram

# Interface: SemanticDiagnosticsBuilderProgram

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5736

The builder that caches the semantic diagnostics for the program and handles the changed files and affected files

## Extends

- [`BuilderProgram`](BuilderProgram.md)

## Extended by

- [`EmitAndSemanticDiagnosticsBuilderProgram`](EmitAndSemanticDiagnosticsBuilderProgram.md)

## Properties

### builderProgramForLinter?

> `optional` **builderProgramForLinter**: [`EmitAndSemanticDiagnosticsBuilderProgram`](EmitAndSemanticDiagnosticsBuilderProgram.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5731

#### Inherited from

[`BuilderProgram`](BuilderProgram.md).[`builderProgramForLinter`](BuilderProgram.md#builderprogramforlinter)

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

[`BuilderProgram`](BuilderProgram.md).[`emit`](BuilderProgram.md#emit)

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

[`BuilderProgram`](BuilderProgram.md).[`getAllDependencies`](BuilderProgram.md#getalldependencies)

***

### getCompilerOptions()

> **getCompilerOptions**(): [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5672

Get compiler options of the program

#### Returns

[`CompilerOptions`](CompilerOptions.md)

#### Inherited from

[`BuilderProgram`](BuilderProgram.md).[`getCompilerOptions`](BuilderProgram.md#getcompileroptions)

***

### getConfigFileParsingDiagnostics()

> **getConfigFileParsingDiagnostics**(): readonly [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5692

Get the diagnostics from config file parsing

#### Returns

readonly [`Diagnostic`](Diagnostic.md)[]

#### Inherited from

[`BuilderProgram`](BuilderProgram.md).[`getConfigFileParsingDiagnostics`](BuilderProgram.md#getconfigfileparsingdiagnostics)

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5729

Get the current directory of the program

#### Returns

`string`

#### Inherited from

[`BuilderProgram`](BuilderProgram.md).[`getCurrentDirectory`](BuilderProgram.md#getcurrentdirectory)

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

[`BuilderProgram`](BuilderProgram.md).[`getDeclarationDiagnostics`](BuilderProgram.md#getdeclarationdiagnostics)

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

[`BuilderProgram`](BuilderProgram.md).[`getGlobalDiagnostics`](BuilderProgram.md#getglobaldiagnostics)

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

[`BuilderProgram`](BuilderProgram.md).[`getOptionsDiagnostics`](BuilderProgram.md#getoptionsdiagnostics)

***

### getProgram()

> **getProgram**(): [`Program`](Program.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5668

Returns current program

#### Returns

[`Program`](Program.md)

#### Inherited from

[`BuilderProgram`](BuilderProgram.md).[`getProgram`](BuilderProgram.md#getprogram)

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

[`BuilderProgram`](BuilderProgram.md).[`getSemanticDiagnostics`](BuilderProgram.md#getsemanticdiagnostics)

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

[`BuilderProgram`](BuilderProgram.md).[`getSourceFile`](BuilderProgram.md#getsourcefile)

***

### getSourceFiles()

> **getSourceFiles**(): readonly [`SourceFile`](SourceFile.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5680

Get a list of files in the program

#### Returns

readonly [`SourceFile`](SourceFile.md)[]

#### Inherited from

[`BuilderProgram`](BuilderProgram.md).[`getSourceFiles`](BuilderProgram.md#getsourcefiles)

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

[`BuilderProgram`](BuilderProgram.md).[`getSyntacticDiagnostics`](BuilderProgram.md#getsyntacticdiagnostics)

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

[`BuilderProgram`](BuilderProgram.md).[`isFileUpdateInConstEnumCache`](BuilderProgram.md#isfileupdateinconstenumcache)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SemicolonClassElement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SemicolonClassElement

# Interface: SemicolonClassElement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:881

For when we encounter a semicolon in a class declaration. ES6 allows these as class elements.

## Extends

- [`ClassElement`](ClassElement.md)

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

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`ClassElement`](ClassElement.md).[`flags`](ClassElement.md#flags)

***

### kind

> `readonly` **kind**: [`SemicolonClassElement`](../enumerations/SyntaxKind.md#semicolonclasselement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:882

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

[`ClassElement`](ClassElement.md).[`modifiers`](ClassElement.md#modifiers)

***

### name?

> `readonly` `optional` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1634

#### Inherited from

[`ClassElement`](ClassElement.md).[`name`](ClassElement.md#name)

***

### parent

> `readonly` **parent**: [`ClassLikeDeclaration`](../type-aliases/ClassLikeDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:883

#### Overrides

[`ClassElement`](ClassElement.md).[`parent`](ClassElement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`ClassElement`](ClassElement.md).[`pos`](ClassElement.md#pos)

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Set.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Set

# Interface: Set\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:74

ES6 Set interface.

## Extends

- [`ReadonlySet`](ReadonlySet.md)\<`T`\>.[`Collection`](Collection.md)\<`T`\>

## Type Parameters

### T

`T`

## Properties

### size

> `readonly` **size**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:36

#### Inherited from

[`Collection`](Collection.md).[`size`](Collection.md#size)

## Methods

### add()

> **add**(`value`): `this`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:75

#### Parameters

##### value

`T`

#### Returns

`this`

***

### clear()

> **clear**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:43

#### Returns

`void`

#### Inherited from

[`Collection`](Collection.md).[`clear`](Collection.md#clear)

***

### delete()

> **delete**(`value`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:76

#### Parameters

##### value

`T`

#### Returns

`boolean`

#### Overrides

[`Collection`](Collection.md).[`delete`](Collection.md#delete)

***

### entries()

> **entries**(): [`Iterator`](Iterator.md)\<\[`T`, `T`\]\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:70

#### Returns

[`Iterator`](Iterator.md)\<\[`T`, `T`\]\>

#### Inherited from

[`ReadonlySet`](ReadonlySet.md).[`entries`](ReadonlySet.md#entries)

***

### forEach()

> **forEach**(`action`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:71

#### Parameters

##### action

(`value`, `key`) => `void`

#### Returns

`void`

#### Inherited from

[`ReadonlySet`](ReadonlySet.md).[`forEach`](ReadonlySet.md#foreach)

***

### has()

> **has**(`value`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:68

#### Parameters

##### value

`T`

#### Returns

`boolean`

#### Inherited from

[`Collection`](Collection.md).[`has`](Collection.md#has)

***

### keys()

> **keys**(): [`Iterator`](Iterator.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:38

#### Returns

[`Iterator`](Iterator.md)\<`T`\>

#### Inherited from

[`Collection`](Collection.md).[`keys`](Collection.md#keys)

***

### values()

> **values**(): [`Iterator`](Iterator.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:69

#### Returns

[`Iterator`](Iterator.md)\<`T`\>

#### Inherited from

[`ReadonlySet`](ReadonlySet.md).[`values`](ReadonlySet.md#values)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SetAccessorDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SetAccessorDeclaration

# Interface: SetAccessorDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:892

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:897

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

> `readonly` **kind**: [`SetAccessor`](../enumerations/SyntaxKind.md#setaccessor)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:893

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:895

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:896

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:894

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




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/ShorthandPropertyAssignment.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / ShorthandPropertyAssignment

# Interface: ShorthandPropertyAssignment

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:809

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

### equalsToken?

> `readonly` `optional` **equalsToken**: [`EqualsToken`](../type-aliases/EqualsToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:813

***

### ~~exclamationToken?~~

> `readonly` `optional` **exclamationToken**: [`ExclamationToken`](../type-aliases/ExclamationToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8404

#### Deprecated

A shorthand property assignment cannot have an exclamation token

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`flags`](ObjectLiteralElement.md#flags)

***

### kind

> `readonly` **kind**: [`ShorthandPropertyAssignment`](../enumerations/SyntaxKind.md#shorthandpropertyassignment)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:810

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

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`Modifier`](../type-aliases/Modifier.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8400

#### Deprecated

A shorthand property assignment cannot have modifiers

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`modifiers`](ObjectLiteralElement.md#modifiers)

***

### name

> `readonly` **name**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:812

#### Overrides

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`name`](ObjectLiteralElement.md#name)

***

### objectAssignmentInitializer?

> `readonly` `optional` **objectAssignmentInitializer**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:814

***

### parent

> `readonly` **parent**: [`ObjectLiteralExpression`](ObjectLiteralExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:811

#### Overrides

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`parent`](ObjectLiteralElement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`pos`](ObjectLiteralElement.md#pos)

***

### ~~questionToken?~~

> `readonly` `optional` **questionToken**: [`QuestionToken`](../type-aliases/QuestionToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8402

#### Deprecated

A shorthand property assignment cannot have a question token

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Signature.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Signature

# Interface: Signature

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2936

## Properties

### declaration?

> `optional` **declaration**: [`SignatureDeclaration`](../type-aliases/SignatureDeclaration.md) \| [`JSDocSignature`](JSDocSignature.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2937

***

### parameters

> **parameters**: readonly [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2939

***

### typeParameters?

> `optional` **typeParameters**: readonly [`TypeParameter`](TypeParameter.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2938

## Methods

### getDeclaration()

> **getDeclaration**(): [`SignatureDeclaration`](../type-aliases/SignatureDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6148

#### Returns

[`SignatureDeclaration`](../type-aliases/SignatureDeclaration.md)

***

### getDocumentationComment()

> **getDocumentationComment**(`typeChecker`): [`SymbolDisplayPart`](SymbolDisplayPart.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6153

#### Parameters

##### typeChecker

`undefined` | [`TypeChecker`](TypeChecker.md)

#### Returns

[`SymbolDisplayPart`](SymbolDisplayPart.md)[]

***

### getJsDocTags()

> **getJsDocTags**(): [`JSDocTagInfo`](JSDocTagInfo-1.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6154

#### Returns

[`JSDocTagInfo`](JSDocTagInfo-1.md)[]

***

### getParameters()

> **getParameters**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6150

#### Returns

[`Symbol`](Symbol.md)[]

***

### getReturnType()

> **getReturnType**(): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6152

#### Returns

[`Type`](Type.md)

***

### getTypeParameterAtPosition()

> **getTypeParameterAtPosition**(`pos`): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6151

#### Parameters

##### pos

`number`

#### Returns

[`Type`](Type.md)

***

### getTypeParameters()

> **getTypeParameters**(): `undefined` \| [`TypeParameter`](TypeParameter.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6149

#### Returns

`undefined` \| [`TypeParameter`](TypeParameter.md)[]




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SignatureDeclarationBase.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SignatureDeclarationBase

# Interface: SignatureDeclarationBase

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:731

## Extends

- [`NamedDeclaration`](NamedDeclaration.md).[`JSDocContainer`](JSDocContainer.md)

## Extended by

- [`CallSignatureDeclaration`](CallSignatureDeclaration.md)
- [`ConstructSignatureDeclaration`](ConstructSignatureDeclaration.md)
- [`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md)
- [`MethodSignature`](MethodSignature.md)
- [`IndexSignatureDeclaration`](IndexSignatureDeclaration.md)
- [`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md)
- [`JSDocFunctionType`](JSDocFunctionType.md)

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

### kind

> `readonly` **kind**: [`MethodSignature`](../enumerations/SyntaxKind.md#methodsignature) \| [`MethodDeclaration`](../enumerations/SyntaxKind.md#methoddeclaration) \| [`Constructor`](../enumerations/SyntaxKind.md#constructor) \| [`GetAccessor`](../enumerations/SyntaxKind.md#getaccessor) \| [`SetAccessor`](../enumerations/SyntaxKind.md#setaccessor) \| [`CallSignature`](../enumerations/SyntaxKind.md#callsignature) \| [`ConstructSignature`](../enumerations/SyntaxKind.md#constructsignature) \| [`IndexSignature`](../enumerations/SyntaxKind.md#indexsignature) \| [`FunctionType`](../enumerations/SyntaxKind.md#functiontype) \| [`ConstructorType`](../enumerations/SyntaxKind.md#constructortype) \| [`FunctionExpression`](../enumerations/SyntaxKind.md#functionexpression) \| [`ArrowFunction`](../enumerations/SyntaxKind.md#arrowfunction) \| [`FunctionDeclaration`](../enumerations/SyntaxKind.md#functiondeclaration) \| [`JSDocFunctionType`](../enumerations/SyntaxKind.md#jsdocfunctiontype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:732

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

### name?

> `readonly` `optional` **name**: [`PropertyName`](../type-aliases/PropertyName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:733

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`name`](NamedDeclaration.md#name)

***

### parameters

> `readonly` **parameters**: [`NodeArray`](NodeArray.md)\<[`ParameterDeclaration`](ParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:735

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

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

***

### type?

> `readonly` `optional` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:736

***

### typeParameters?

> `readonly` `optional` **typeParameters**: [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:734

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SignatureHelpCharacterTypedReason.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SignatureHelpCharacterTypedReason

# Interface: SignatureHelpCharacterTypedReason

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6491

Signals that the signature help request came from a user typing a character.
Depending on the character and the syntactic context, the request may or may not be served a result.

## Properties

### kind

> **kind**: `"characterTyped"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6492

***

### triggerCharacter

> **triggerCharacter**: [`SignatureHelpTriggerCharacter`](../type-aliases/SignatureHelpTriggerCharacter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6496

Character that was responsible for triggering signature help.




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SignatureHelpInvokedReason.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SignatureHelpInvokedReason

# Interface: SignatureHelpInvokedReason

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6483

Signals that the user manually requested signature help.
The language service will unconditionally attempt to provide a result.

## Properties

### kind

> **kind**: `"invoked"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6484

***

### triggerCharacter?

> `optional` **triggerCharacter**: `undefined`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6485




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SignatureHelpItem.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SignatureHelpItem

# Interface: SignatureHelpItem

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6934

Represents a single signature to show in signature help.
The id is used for subsequent calls into the language service to ask questions about the
signature help item in the context of any documents that have been updated.  i.e. after
an edit has happened, while signature help is still active, the host can ask important
questions like 'what parameter is the user currently contained within?'.

## Properties

### documentation

> **documentation**: [`SymbolDisplayPart`](SymbolDisplayPart.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6940

***

### isVariadic

> **isVariadic**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6935

***

### parameters

> **parameters**: [`SignatureHelpParameter`](SignatureHelpParameter.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6939

***

### prefixDisplayParts

> **prefixDisplayParts**: [`SymbolDisplayPart`](SymbolDisplayPart.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6936

***

### separatorDisplayParts

> **separatorDisplayParts**: [`SymbolDisplayPart`](SymbolDisplayPart.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6938

***

### suffixDisplayParts

> **suffixDisplayParts**: [`SymbolDisplayPart`](SymbolDisplayPart.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6937

***

### tags

> **tags**: [`JSDocTagInfo`](JSDocTagInfo-1.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6941




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SignatureHelpItems.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SignatureHelpItems

# Interface: SignatureHelpItems

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6946

Represents a set of signature help items, and the preferred item that should be selected.

## Properties

### applicableSpan

> **applicableSpan**: [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6948

***

### argumentCount

> **argumentCount**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6951

***

### argumentIndex

> **argumentIndex**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6950

***

### items

> **items**: [`SignatureHelpItem`](SignatureHelpItem.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6947

***

### selectedItemIndex

> **selectedItemIndex**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6949




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SignatureHelpItemsOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SignatureHelpItemsOptions

# Interface: SignatureHelpItemsOptions

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6475

## Properties

### triggerReason?

> `optional` **triggerReason**: [`SignatureHelpTriggerReason`](../type-aliases/SignatureHelpTriggerReason.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6476




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SignatureHelpParameter.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SignatureHelpParameter

# Interface: SignatureHelpParameter

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6916

## Properties

### displayParts

> **displayParts**: [`SymbolDisplayPart`](SymbolDisplayPart.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6919

***

### documentation

> **documentation**: [`SymbolDisplayPart`](SymbolDisplayPart.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6918

***

### isOptional

> **isOptional**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6920

***

### isRest?

> `optional` **isRest**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6921

***

### name

> **name**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6917




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SignatureHelpRetriggeredReason.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SignatureHelpRetriggeredReason

# Interface: SignatureHelpRetriggeredReason

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6504

Signals that this signature help request came from typing a character or moving the cursor.
This should only occur if a signature help session was already active and the editor needs to see if it should adjust.
The language service will unconditionally attempt to provide a result.
`triggerCharacter` can be `undefined` for a retrigger caused by a cursor move.

## Properties

### kind

> **kind**: `"retrigger"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6505

***

### triggerCharacter?

> `optional` **triggerCharacter**: [`SignatureHelpRetriggerCharacter`](../type-aliases/SignatureHelpRetriggerCharacter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6509

Character that was responsible for triggering signature help.




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SolutionBuilder.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SolutionBuilder

# Interface: SolutionBuilder\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5956

## Type Parameters

### T

`T` *extends* [`BuilderProgram`](BuilderProgram.md)

## Methods

### build()

> **build**(`project?`, `cancellationToken?`, `writeFile?`, `getCustomTransformers?`): [`ExitStatus`](../enumerations/ExitStatus.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5957

#### Parameters

##### project?

`string`

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

##### writeFile?

[`WriteFileCallback`](../type-aliases/WriteFileCallback.md)

##### getCustomTransformers?

(`project`) => [`CustomTransformers`](CustomTransformers.md)

#### Returns

[`ExitStatus`](../enumerations/ExitStatus.md)

***

### buildReferences()

> **buildReferences**(`project`, `cancellationToken?`, `writeFile?`, `getCustomTransformers?`): [`ExitStatus`](../enumerations/ExitStatus.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5959

#### Parameters

##### project

`string`

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

##### writeFile?

[`WriteFileCallback`](../type-aliases/WriteFileCallback.md)

##### getCustomTransformers?

(`project`) => [`CustomTransformers`](CustomTransformers.md)

#### Returns

[`ExitStatus`](../enumerations/ExitStatus.md)

***

### clean()

> **clean**(`project?`): [`ExitStatus`](../enumerations/ExitStatus.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5958

#### Parameters

##### project?

`string`

#### Returns

[`ExitStatus`](../enumerations/ExitStatus.md)

***

### cleanReferences()

> **cleanReferences**(`project?`): [`ExitStatus`](../enumerations/ExitStatus.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5960

#### Parameters

##### project?

`string`

#### Returns

[`ExitStatus`](../enumerations/ExitStatus.md)

***

### getNextInvalidatedProject()

> **getNextInvalidatedProject**(`cancellationToken?`): `undefined` \| [`InvalidatedProject`](../type-aliases/InvalidatedProject.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5961

#### Parameters

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

#### Returns

`undefined` \| [`InvalidatedProject`](../type-aliases/InvalidatedProject.md)\<`T`\>




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SolutionBuilderHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SolutionBuilderHost

# Interface: SolutionBuilderHost\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5951

## Extends

- [`SolutionBuilderHostBase`](SolutionBuilderHostBase.md)\<`T`\>

## Type Parameters

### T

`T` *extends* [`BuilderProgram`](BuilderProgram.md)

## Properties

### createProgram

> **createProgram**: [`CreateProgram`](../type-aliases/CreateProgram.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5812

Used to create the program when need for program creation or recreation detected

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`createProgram`](SolutionBuilderHostBase.md#createprogram)

***

### getCustomTransformers()?

> `optional` **getCustomTransformers**: (`project`) => `undefined` \| [`CustomTransformers`](CustomTransformers.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5942

#### Parameters

##### project

`string`

#### Returns

`undefined` \| [`CustomTransformers`](CustomTransformers.md)

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getCustomTransformers`](SolutionBuilderHostBase.md#getcustomtransformers)

***

### reportDiagnostic

> **reportDiagnostic**: [`DiagnosticReporter`](../type-aliases/DiagnosticReporter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5947

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`reportDiagnostic`](SolutionBuilderHostBase.md#reportdiagnostic)

***

### reportErrorSummary?

> `optional` **reportErrorSummary**: [`ReportEmitErrorSummary`](../type-aliases/ReportEmitErrorSummary.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5952

***

### reportSolutionBuilderStatus

> **reportSolutionBuilderStatus**: [`DiagnosticReporter`](../type-aliases/DiagnosticReporter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5948

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`reportSolutionBuilderStatus`](SolutionBuilderHostBase.md#reportsolutionbuilderstatus)

## Methods

### afterProgramEmitAndDiagnostics()?

> `optional` **afterProgramEmitAndDiagnostics**(`program`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5949

#### Parameters

##### program

`T`

#### Returns

`void`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`afterProgramEmitAndDiagnostics`](SolutionBuilderHostBase.md#afterprogramemitanddiagnostics)

***

### createDirectory()?

> `optional` **createDirectory**(`path`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5936

#### Parameters

##### path

`string`

#### Returns

`void`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`createDirectory`](SolutionBuilderHostBase.md#createdirectory)

***

### createHash()?

> `optional` **createHash**(`data`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5818

#### Parameters

##### data

`string`

#### Returns

`string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`createHash`](SolutionBuilderHostBase.md#createhash)

***

### deleteFile()

> **deleteFile**(`fileName`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5945

#### Parameters

##### fileName

`string`

#### Returns

`void`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`deleteFile`](SolutionBuilderHostBase.md#deletefile)

***

### directoryExists()?

> `optional` **directoryExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5830

If provided, used for module resolution as well as to handle directory structure

#### Parameters

##### path

`string`

#### Returns

`boolean`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`directoryExists`](SolutionBuilderHostBase.md#directoryexists)

***

### fileExists()

> **fileExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5823

Use to check file presence for source files and
if resolveModuleNames is not provided (complier is in charge of module resolution) then module files as well

#### Parameters

##### path

`string`

#### Returns

`boolean`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`fileExists`](SolutionBuilderHostBase.md#fileexists)

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5815

#### Returns

`string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getCurrentDirectory`](SolutionBuilderHostBase.md#getcurrentdirectory)

***

### getDefaultLibFileName()

> **getDefaultLibFileName**(`options`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5816

#### Parameters

##### options

[`CompilerOptions`](CompilerOptions.md)

#### Returns

`string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getDefaultLibFileName`](SolutionBuilderHostBase.md#getdefaultlibfilename)

***

### getDefaultLibLocation()?

> `optional` **getDefaultLibLocation**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5817

#### Returns

`string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getDefaultLibLocation`](SolutionBuilderHostBase.md#getdefaultliblocation)

***

### getDirectories()?

> `optional` **getDirectories**(`path`): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5832

If provided, used in resolutions as well as handling directory structure

#### Parameters

##### path

`string`

#### Returns

`string`[]

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getDirectories`](SolutionBuilderHostBase.md#getdirectories)

***

### getEnvironmentVariable()?

> `optional` **getEnvironmentVariable**(`name`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5840

If provided is used to get the environment variable

#### Parameters

##### name

`string`

#### Returns

`undefined` \| `string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getEnvironmentVariable`](SolutionBuilderHostBase.md#getenvironmentvariable)

***

### getModifiedTime()

> **getModifiedTime**(`fileName`): `undefined` \| `Date`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5943

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| `Date`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getModifiedTime`](SolutionBuilderHostBase.md#getmodifiedtime)

***

### getModuleResolutionCache()?

> `optional` **getModuleResolutionCache**(): `undefined` \| [`ModuleResolutionCache`](ModuleResolutionCache.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5850

Returns the module resolution cache used by a provided `resolveModuleNames` implementation so that any non-name module resolution operations (eg, package.json lookup) can reuse it

#### Returns

`undefined` \| [`ModuleResolutionCache`](ModuleResolutionCache.md)

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getModuleResolutionCache`](SolutionBuilderHostBase.md#getmoduleresolutioncache)

***

### getNewLine()

> **getNewLine**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5814

#### Returns

`string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getNewLine`](SolutionBuilderHostBase.md#getnewline)

***

### getParsedCommandLine()?

> `optional` **getParsedCommandLine**(`fileName`): `undefined` \| [`ParsedCommandLine`](ParsedCommandLine.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5946

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| [`ParsedCommandLine`](ParsedCommandLine.md)

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getParsedCommandLine`](SolutionBuilderHostBase.md#getparsedcommandline)

***

### hasInvalidatedResolutions()?

> `optional` **hasInvalidatedResolutions**(`filePath`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5846

If provided along with custom resolveModuleNames or resolveTypeReferenceDirectives, used to determine if unchanged file path needs to re-resolve modules/type reference directives

#### Parameters

##### filePath

[`Path`](../type-aliases/Path.md)

#### Returns

`boolean`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`hasInvalidatedResolutions`](SolutionBuilderHostBase.md#hasinvalidatedresolutions)

***

### readDirectory()?

> `optional` **readDirectory**(`path`, `extensions?`, `exclude?`, `include?`, `depth?`): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5834

If provided, used to cache and handle directory structure modifications

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

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`readDirectory`](SolutionBuilderHostBase.md#readdirectory)

***

### readFile()

> **readFile**(`path`, `encoding?`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5828

Use to read file text for source files and
if resolveModuleNames is not provided (complier is in charge of module resolution) then module files as well

#### Parameters

##### path

`string`

##### encoding?

`string`

#### Returns

`undefined` \| `string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`readFile`](SolutionBuilderHostBase.md#readfile)

***

### realpath()?

> `optional` **realpath**(`path`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5836

Symbol links resolution

#### Parameters

##### path

`string`

#### Returns

`string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`realpath`](SolutionBuilderHostBase.md#realpath)

***

### resolveModuleNames()?

> `optional` **resolveModuleNames**(`moduleNames`, `containingFile`, `reusedNames`, `redirectedReference`, `options`, `containingSourceFile?`): (`undefined` \| [`ResolvedModule`](ResolvedModule.md))[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5842

If provided, used to resolve the module names, otherwise typescript's default module resolution

#### Parameters

##### moduleNames

`string`[]

##### containingFile

`string`

##### reusedNames

`undefined` | `string`[]

##### redirectedReference

`undefined` | [`ResolvedProjectReference`](ResolvedProjectReference.md)

##### options

[`CompilerOptions`](CompilerOptions.md)

##### containingSourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

(`undefined` \| [`ResolvedModule`](ResolvedModule.md))[]

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`resolveModuleNames`](SolutionBuilderHostBase.md#resolvemodulenames)

***

### resolveTypeReferenceDirectives()?

> `optional` **resolveTypeReferenceDirectives**(`typeReferenceDirectiveNames`, `containingFile`, `redirectedReference`, `options`, `containingFileMode?`): (`undefined` \| [`ResolvedTypeReferenceDirective`](ResolvedTypeReferenceDirective.md))[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5844

If provided, used to resolve type reference directives, otherwise typescript's default resolution

#### Parameters

##### typeReferenceDirectiveNames

`string`[] | readonly [`FileReference`](FileReference.md)[]

##### containingFile

`string`

##### redirectedReference

`undefined` | [`ResolvedProjectReference`](ResolvedProjectReference.md)

##### options

[`CompilerOptions`](CompilerOptions.md)

##### containingFileMode?

[`CommonJS`](../enumerations/ModuleKind.md#commonjs) | [`ESNext`](../enumerations/ModuleKind.md#esnext)

#### Returns

(`undefined` \| [`ResolvedTypeReferenceDirective`](ResolvedTypeReferenceDirective.md))[]

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`resolveTypeReferenceDirectives`](SolutionBuilderHostBase.md#resolvetypereferencedirectives)

***

### setModifiedTime()

> **setModifiedTime**(`fileName`, `date`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5944

#### Parameters

##### fileName

`string`

##### date

`Date`

#### Returns

`void`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`setModifiedTime`](SolutionBuilderHostBase.md#setmodifiedtime)

***

### trace()?

> `optional` **trace**(`s`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5838

If provided would be used to write log about compilation

#### Parameters

##### s

`string`

#### Returns

`void`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`trace`](SolutionBuilderHostBase.md#trace)

***

### useCaseSensitiveFileNames()

> **useCaseSensitiveFileNames**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5813

#### Returns

`boolean`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`useCaseSensitiveFileNames`](SolutionBuilderHostBase.md#usecasesensitivefilenames)

***

### writeFile()?

> `optional` **writeFile**(`path`, `data`, `writeByteOrderMark?`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5941

Should provide create directory and writeFile if done of invalidatedProjects is not invoked with
writeFileCallback

#### Parameters

##### path

`string`

##### data

`string`

##### writeByteOrderMark?

`boolean`

#### Returns

`void`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`writeFile`](SolutionBuilderHostBase.md#writefile)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SolutionBuilderHostBase.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SolutionBuilderHostBase

# Interface: SolutionBuilderHostBase\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5935

## Extends

- [`ProgramHost`](ProgramHost.md)\<`T`\>

## Extended by

- [`SolutionBuilderHost`](SolutionBuilderHost.md)
- [`SolutionBuilderWithWatchHost`](SolutionBuilderWithWatchHost.md)

## Type Parameters

### T

`T` *extends* [`BuilderProgram`](BuilderProgram.md)

## Properties

### createProgram

> **createProgram**: [`CreateProgram`](../type-aliases/CreateProgram.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5812

Used to create the program when need for program creation or recreation detected

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`createProgram`](ProgramHost.md#createprogram)

***

### getCustomTransformers()?

> `optional` **getCustomTransformers**: (`project`) => `undefined` \| [`CustomTransformers`](CustomTransformers.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5942

#### Parameters

##### project

`string`

#### Returns

`undefined` \| [`CustomTransformers`](CustomTransformers.md)

***

### reportDiagnostic

> **reportDiagnostic**: [`DiagnosticReporter`](../type-aliases/DiagnosticReporter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5947

***

### reportSolutionBuilderStatus

> **reportSolutionBuilderStatus**: [`DiagnosticReporter`](../type-aliases/DiagnosticReporter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5948

## Methods

### afterProgramEmitAndDiagnostics()?

> `optional` **afterProgramEmitAndDiagnostics**(`program`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5949

#### Parameters

##### program

`T`

#### Returns

`void`

***

### createDirectory()?

> `optional` **createDirectory**(`path`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5936

#### Parameters

##### path

`string`

#### Returns

`void`

***

### createHash()?

> `optional` **createHash**(`data`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5818

#### Parameters

##### data

`string`

#### Returns

`string`

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`createHash`](ProgramHost.md#createhash)

***

### deleteFile()

> **deleteFile**(`fileName`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5945

#### Parameters

##### fileName

`string`

#### Returns

`void`

***

### directoryExists()?

> `optional` **directoryExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5830

If provided, used for module resolution as well as to handle directory structure

#### Parameters

##### path

`string`

#### Returns

`boolean`

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`directoryExists`](ProgramHost.md#directoryexists)

***

### fileExists()

> **fileExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5823

Use to check file presence for source files and
if resolveModuleNames is not provided (complier is in charge of module resolution) then module files as well

#### Parameters

##### path

`string`

#### Returns

`boolean`

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`fileExists`](ProgramHost.md#fileexists)

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5815

#### Returns

`string`

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`getCurrentDirectory`](ProgramHost.md#getcurrentdirectory)

***

### getDefaultLibFileName()

> **getDefaultLibFileName**(`options`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5816

#### Parameters

##### options

[`CompilerOptions`](CompilerOptions.md)

#### Returns

`string`

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`getDefaultLibFileName`](ProgramHost.md#getdefaultlibfilename)

***

### getDefaultLibLocation()?

> `optional` **getDefaultLibLocation**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5817

#### Returns

`string`

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`getDefaultLibLocation`](ProgramHost.md#getdefaultliblocation)

***

### getDirectories()?

> `optional` **getDirectories**(`path`): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5832

If provided, used in resolutions as well as handling directory structure

#### Parameters

##### path

`string`

#### Returns

`string`[]

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`getDirectories`](ProgramHost.md#getdirectories)

***

### getEnvironmentVariable()?

> `optional` **getEnvironmentVariable**(`name`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5840

If provided is used to get the environment variable

#### Parameters

##### name

`string`

#### Returns

`undefined` \| `string`

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`getEnvironmentVariable`](ProgramHost.md#getenvironmentvariable)

***

### getModifiedTime()

> **getModifiedTime**(`fileName`): `undefined` \| `Date`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5943

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| `Date`

***

### getModuleResolutionCache()?

> `optional` **getModuleResolutionCache**(): `undefined` \| [`ModuleResolutionCache`](ModuleResolutionCache.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5850

Returns the module resolution cache used by a provided `resolveModuleNames` implementation so that any non-name module resolution operations (eg, package.json lookup) can reuse it

#### Returns

`undefined` \| [`ModuleResolutionCache`](ModuleResolutionCache.md)

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`getModuleResolutionCache`](ProgramHost.md#getmoduleresolutioncache)

***

### getNewLine()

> **getNewLine**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5814

#### Returns

`string`

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`getNewLine`](ProgramHost.md#getnewline)

***

### getParsedCommandLine()?

> `optional` **getParsedCommandLine**(`fileName`): `undefined` \| [`ParsedCommandLine`](ParsedCommandLine.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5946

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| [`ParsedCommandLine`](ParsedCommandLine.md)

***

### hasInvalidatedResolutions()?

> `optional` **hasInvalidatedResolutions**(`filePath`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5846

If provided along with custom resolveModuleNames or resolveTypeReferenceDirectives, used to determine if unchanged file path needs to re-resolve modules/type reference directives

#### Parameters

##### filePath

[`Path`](../type-aliases/Path.md)

#### Returns

`boolean`

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`hasInvalidatedResolutions`](ProgramHost.md#hasinvalidatedresolutions)

***

### readDirectory()?

> `optional` **readDirectory**(`path`, `extensions?`, `exclude?`, `include?`, `depth?`): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5834

If provided, used to cache and handle directory structure modifications

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

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`readDirectory`](ProgramHost.md#readdirectory)

***

### readFile()

> **readFile**(`path`, `encoding?`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5828

Use to read file text for source files and
if resolveModuleNames is not provided (complier is in charge of module resolution) then module files as well

#### Parameters

##### path

`string`

##### encoding?

`string`

#### Returns

`undefined` \| `string`

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`readFile`](ProgramHost.md#readfile)

***

### realpath()?

> `optional` **realpath**(`path`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5836

Symbol links resolution

#### Parameters

##### path

`string`

#### Returns

`string`

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`realpath`](ProgramHost.md#realpath)

***

### resolveModuleNames()?

> `optional` **resolveModuleNames**(`moduleNames`, `containingFile`, `reusedNames`, `redirectedReference`, `options`, `containingSourceFile?`): (`undefined` \| [`ResolvedModule`](ResolvedModule.md))[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5842

If provided, used to resolve the module names, otherwise typescript's default module resolution

#### Parameters

##### moduleNames

`string`[]

##### containingFile

`string`

##### reusedNames

`undefined` | `string`[]

##### redirectedReference

`undefined` | [`ResolvedProjectReference`](ResolvedProjectReference.md)

##### options

[`CompilerOptions`](CompilerOptions.md)

##### containingSourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

(`undefined` \| [`ResolvedModule`](ResolvedModule.md))[]

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`resolveModuleNames`](ProgramHost.md#resolvemodulenames)

***

### resolveTypeReferenceDirectives()?

> `optional` **resolveTypeReferenceDirectives**(`typeReferenceDirectiveNames`, `containingFile`, `redirectedReference`, `options`, `containingFileMode?`): (`undefined` \| [`ResolvedTypeReferenceDirective`](ResolvedTypeReferenceDirective.md))[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5844

If provided, used to resolve type reference directives, otherwise typescript's default resolution

#### Parameters

##### typeReferenceDirectiveNames

`string`[] | readonly [`FileReference`](FileReference.md)[]

##### containingFile

`string`

##### redirectedReference

`undefined` | [`ResolvedProjectReference`](ResolvedProjectReference.md)

##### options

[`CompilerOptions`](CompilerOptions.md)

##### containingFileMode?

[`CommonJS`](../enumerations/ModuleKind.md#commonjs) | [`ESNext`](../enumerations/ModuleKind.md#esnext)

#### Returns

(`undefined` \| [`ResolvedTypeReferenceDirective`](ResolvedTypeReferenceDirective.md))[]

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`resolveTypeReferenceDirectives`](ProgramHost.md#resolvetypereferencedirectives)

***

### setModifiedTime()

> **setModifiedTime**(`fileName`, `date`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5944

#### Parameters

##### fileName

`string`

##### date

`Date`

#### Returns

`void`

***

### trace()?

> `optional` **trace**(`s`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5838

If provided would be used to write log about compilation

#### Parameters

##### s

`string`

#### Returns

`void`

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`trace`](ProgramHost.md#trace)

***

### useCaseSensitiveFileNames()

> **useCaseSensitiveFileNames**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5813

#### Returns

`boolean`

#### Inherited from

[`ProgramHost`](ProgramHost.md).[`useCaseSensitiveFileNames`](ProgramHost.md#usecasesensitivefilenames)

***

### writeFile()?

> `optional` **writeFile**(`path`, `data`, `writeByteOrderMark?`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5941

Should provide create directory and writeFile if done of invalidatedProjects is not invoked with
writeFileCallback

#### Parameters

##### path

`string`

##### data

`string`

##### writeByteOrderMark?

`boolean`

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/SolutionBuilderWithWatchHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / SolutionBuilderWithWatchHost

# Interface: SolutionBuilderWithWatchHost\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5954

Host that has watch functionality used in --watch mode

## Extends

- [`SolutionBuilderHostBase`](SolutionBuilderHostBase.md)\<`T`\>.[`WatchHost`](WatchHost.md)

## Type Parameters

### T

`T` *extends* [`BuilderProgram`](BuilderProgram.md)

## Properties

### createProgram

> **createProgram**: [`CreateProgram`](../type-aliases/CreateProgram.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5812

Used to create the program when need for program creation or recreation detected

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`createProgram`](SolutionBuilderHostBase.md#createprogram)

***

### getCustomTransformers()?

> `optional` **getCustomTransformers**: (`project`) => `undefined` \| [`CustomTransformers`](CustomTransformers.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5942

#### Parameters

##### project

`string`

#### Returns

`undefined` \| [`CustomTransformers`](CustomTransformers.md)

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getCustomTransformers`](SolutionBuilderHostBase.md#getcustomtransformers)

***

### reportDiagnostic

> **reportDiagnostic**: [`DiagnosticReporter`](../type-aliases/DiagnosticReporter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5947

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`reportDiagnostic`](SolutionBuilderHostBase.md#reportdiagnostic)

***

### reportSolutionBuilderStatus

> **reportSolutionBuilderStatus**: [`DiagnosticReporter`](../type-aliases/DiagnosticReporter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5948

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`reportSolutionBuilderStatus`](SolutionBuilderHostBase.md#reportsolutionbuilderstatus)

## Methods

### afterProgramEmitAndDiagnostics()?

> `optional` **afterProgramEmitAndDiagnostics**(`program`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5949

#### Parameters

##### program

`T`

#### Returns

`void`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`afterProgramEmitAndDiagnostics`](SolutionBuilderHostBase.md#afterprogramemitanddiagnostics)

***

### clearTimeout()?

> `optional` **clearTimeout**(`timeoutId`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5806

If provided, will be used to reset existing delayed compilation

#### Parameters

##### timeoutId

`any`

#### Returns

`void`

#### Inherited from

[`WatchHost`](WatchHost.md).[`clearTimeout`](WatchHost.md#cleartimeout)

***

### createDirectory()?

> `optional` **createDirectory**(`path`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5936

#### Parameters

##### path

`string`

#### Returns

`void`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`createDirectory`](SolutionBuilderHostBase.md#createdirectory)

***

### createHash()?

> `optional` **createHash**(`data`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5818

#### Parameters

##### data

`string`

#### Returns

`string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`createHash`](SolutionBuilderHostBase.md#createhash)

***

### deleteFile()

> **deleteFile**(`fileName`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5945

#### Parameters

##### fileName

`string`

#### Returns

`void`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`deleteFile`](SolutionBuilderHostBase.md#deletefile)

***

### directoryExists()?

> `optional` **directoryExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5830

If provided, used for module resolution as well as to handle directory structure

#### Parameters

##### path

`string`

#### Returns

`boolean`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`directoryExists`](SolutionBuilderHostBase.md#directoryexists)

***

### fileExists()

> **fileExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5823

Use to check file presence for source files and
if resolveModuleNames is not provided (complier is in charge of module resolution) then module files as well

#### Parameters

##### path

`string`

#### Returns

`boolean`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`fileExists`](SolutionBuilderHostBase.md#fileexists)

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5815

#### Returns

`string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getCurrentDirectory`](SolutionBuilderHostBase.md#getcurrentdirectory)

***

### getDefaultLibFileName()

> **getDefaultLibFileName**(`options`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5816

#### Parameters

##### options

[`CompilerOptions`](CompilerOptions.md)

#### Returns

`string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getDefaultLibFileName`](SolutionBuilderHostBase.md#getdefaultlibfilename)

***

### getDefaultLibLocation()?

> `optional` **getDefaultLibLocation**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5817

#### Returns

`string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getDefaultLibLocation`](SolutionBuilderHostBase.md#getdefaultliblocation)

***

### getDirectories()?

> `optional` **getDirectories**(`path`): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5832

If provided, used in resolutions as well as handling directory structure

#### Parameters

##### path

`string`

#### Returns

`string`[]

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getDirectories`](SolutionBuilderHostBase.md#getdirectories)

***

### getEnvironmentVariable()?

> `optional` **getEnvironmentVariable**(`name`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5840

If provided is used to get the environment variable

#### Parameters

##### name

`string`

#### Returns

`undefined` \| `string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getEnvironmentVariable`](SolutionBuilderHostBase.md#getenvironmentvariable)

***

### getModifiedTime()

> **getModifiedTime**(`fileName`): `undefined` \| `Date`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5943

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| `Date`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getModifiedTime`](SolutionBuilderHostBase.md#getmodifiedtime)

***

### getModuleResolutionCache()?

> `optional` **getModuleResolutionCache**(): `undefined` \| [`ModuleResolutionCache`](ModuleResolutionCache.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5850

Returns the module resolution cache used by a provided `resolveModuleNames` implementation so that any non-name module resolution operations (eg, package.json lookup) can reuse it

#### Returns

`undefined` \| [`ModuleResolutionCache`](ModuleResolutionCache.md)

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getModuleResolutionCache`](SolutionBuilderHostBase.md#getmoduleresolutioncache)

***

### getNewLine()

> **getNewLine**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5814

#### Returns

`string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getNewLine`](SolutionBuilderHostBase.md#getnewline)

***

### getParsedCommandLine()?

> `optional` **getParsedCommandLine**(`fileName`): `undefined` \| [`ParsedCommandLine`](ParsedCommandLine.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5946

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| [`ParsedCommandLine`](ParsedCommandLine.md)

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`getParsedCommandLine`](SolutionBuilderHostBase.md#getparsedcommandline)

***

### hasInvalidatedResolutions()?

> `optional` **hasInvalidatedResolutions**(`filePath`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5846

If provided along with custom resolveModuleNames or resolveTypeReferenceDirectives, used to determine if unchanged file path needs to re-resolve modules/type reference directives

#### Parameters

##### filePath

[`Path`](../type-aliases/Path.md)

#### Returns

`boolean`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`hasInvalidatedResolutions`](SolutionBuilderHostBase.md#hasinvalidatedresolutions)

***

### onWatchStatusChange()?

> `optional` **onWatchStatusChange**(`diagnostic`, `newLine`, `options`, `errorCount?`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5798

If provided, called with Diagnostic message that informs about change in watch status

#### Parameters

##### diagnostic

[`Diagnostic`](Diagnostic.md)

##### newLine

`string`

##### options

[`CompilerOptions`](CompilerOptions.md)

##### errorCount?

`number`

#### Returns

`void`

#### Inherited from

[`WatchHost`](WatchHost.md).[`onWatchStatusChange`](WatchHost.md#onwatchstatuschange)

***

### readDirectory()?

> `optional` **readDirectory**(`path`, `extensions?`, `exclude?`, `include?`, `depth?`): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5834

If provided, used to cache and handle directory structure modifications

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

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`readDirectory`](SolutionBuilderHostBase.md#readdirectory)

***

### readFile()

> **readFile**(`path`, `encoding?`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5828

Use to read file text for source files and
if resolveModuleNames is not provided (complier is in charge of module resolution) then module files as well

#### Parameters

##### path

`string`

##### encoding?

`string`

#### Returns

`undefined` \| `string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`readFile`](SolutionBuilderHostBase.md#readfile)

***

### realpath()?

> `optional` **realpath**(`path`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5836

Symbol links resolution

#### Parameters

##### path

`string`

#### Returns

`string`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`realpath`](SolutionBuilderHostBase.md#realpath)

***

### resolveModuleNames()?

> `optional` **resolveModuleNames**(`moduleNames`, `containingFile`, `reusedNames`, `redirectedReference`, `options`, `containingSourceFile?`): (`undefined` \| [`ResolvedModule`](ResolvedModule.md))[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5842

If provided, used to resolve the module names, otherwise typescript's default module resolution

#### Parameters

##### moduleNames

`string`[]

##### containingFile

`string`

##### reusedNames

`undefined` | `string`[]

##### redirectedReference

`undefined` | [`ResolvedProjectReference`](ResolvedProjectReference.md)

##### options

[`CompilerOptions`](CompilerOptions.md)

##### containingSourceFile?

[`SourceFile`](SourceFile.md)

#### Returns

(`undefined` \| [`ResolvedModule`](ResolvedModule.md))[]

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`resolveModuleNames`](SolutionBuilderHostBase.md#resolvemodulenames)

***

### resolveTypeReferenceDirectives()?

> `optional` **resolveTypeReferenceDirectives**(`typeReferenceDirectiveNames`, `containingFile`, `redirectedReference`, `options`, `containingFileMode?`): (`undefined` \| [`ResolvedTypeReferenceDirective`](ResolvedTypeReferenceDirective.md))[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5844

If provided, used to resolve type reference directives, otherwise typescript's default resolution

#### Parameters

##### typeReferenceDirectiveNames

`string`[] | readonly [`FileReference`](FileReference.md)[]

##### containingFile

`string`

##### redirectedReference

`undefined` | [`ResolvedProjectReference`](ResolvedProjectReference.md)

##### options

[`CompilerOptions`](CompilerOptions.md)

##### containingFileMode?

[`CommonJS`](../enumerations/ModuleKind.md#commonjs) | [`ESNext`](../enumerations/ModuleKind.md#esnext)

#### Returns

(`undefined` \| [`ResolvedTypeReferenceDirective`](ResolvedTypeReferenceDirective.md))[]

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`resolveTypeReferenceDirectives`](SolutionBuilderHostBase.md#resolvetypereferencedirectives)

***

### setModifiedTime()

> **setModifiedTime**(`fileName`, `date`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5944

#### Parameters

##### fileName

`string`

##### date

`Date`

#### Returns

`void`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`setModifiedTime`](SolutionBuilderHostBase.md#setmodifiedtime)

***

### setTimeout()?

> `optional` **setTimeout**(`callback`, `ms`, ...`args`): `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5804

If provided, will be used to set delayed compilation, so that multiple changes in short span are compiled together

#### Parameters

##### callback

(...`args`) => `void`

##### ms

`number`

##### args

...`any`[]

#### Returns

`any`

#### Inherited from

[`WatchHost`](WatchHost.md).[`setTimeout`](WatchHost.md#settimeout)

***

### trace()?

> `optional` **trace**(`s`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5838

If provided would be used to write log about compilation

#### Parameters

##### s

`string`

#### Returns

`void`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`trace`](SolutionBuilderHostBase.md#trace)

***

### useCaseSensitiveFileNames()

> **useCaseSensitiveFileNames**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5813

#### Returns

`boolean`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`useCaseSensitiveFileNames`](SolutionBuilderHostBase.md#usecasesensitivefilenames)

***

### watchDirectory()

> **watchDirectory**(`path`, `callback`, `recursive?`, `options?`): [`FileWatcher`](FileWatcher.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5802

Used to watch resolved module's failed lookup locations, config file specs, type roots where auto type reference directives are added

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

#### Inherited from

[`WatchHost`](WatchHost.md).[`watchDirectory`](WatchHost.md#watchdirectory)

***

### watchFile()

> **watchFile**(`path`, `callback`, `pollingInterval?`, `options?`): [`FileWatcher`](FileWatcher.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5800

Used to watch changes in source files, missing files needed to update the program or config file

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

#### Inherited from

[`WatchHost`](WatchHost.md).[`watchFile`](WatchHost.md#watchfile)

***

### writeFile()?

> `optional` **writeFile**(`path`, `data`, `writeByteOrderMark?`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5941

Should provide create directory and writeFile if done of invalidatedProjects is not invoked with
writeFileCallback

#### Parameters

##### path

`string`

##### data

`string`

##### writeByteOrderMark?

`boolean`

#### Returns

`void`

#### Inherited from

[`SolutionBuilderHostBase`](SolutionBuilderHostBase.md).[`writeFile`](SolutionBuilderHostBase.md#writefile)



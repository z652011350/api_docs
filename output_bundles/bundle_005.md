

============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocPublicTag.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocPublicTag

# Interface: JSDocPublicTag

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1964

## Extends

- [`JSDocTag`](JSDocTag.md)

## Properties

### comment?

> `readonly` `optional` **comment**: `string` \| [`NodeArray`](NodeArray.md)\<[`JSDocComment`](../type-aliases/JSDocComment.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1914

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`comment`](JSDocTag.md#comment)

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

[`JSDocTag`](JSDocTag.md).[`decorators`](JSDocTag.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`end`](JSDocTag.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`flags`](JSDocTag.md#flags)

***

### kind

> `readonly` **kind**: [`JSDocPublicTag`](../enumerations/SyntaxKind.md#jsdocpublictag)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1965

#### Overrides

[`JSDocTag`](JSDocTag.md).[`kind`](JSDocTag.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`locals`](JSDocTag.md#locals)

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

[`JSDocTag`](JSDocTag.md).[`modifiers`](JSDocTag.md#modifiers)

***

### parent

> `readonly` **parent**: [`JSDoc`](JSDoc.md) \| [`JSDocTypeLiteral`](JSDocTypeLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1912

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`parent`](JSDocTag.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`pos`](JSDocTag.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`skipCheck`](JSDocTag.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`symbol`](JSDocTag.md#symbol)

***

### tagName

> `readonly` **tagName**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1913

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`tagName`](JSDocTag.md#tagname)

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

[`JSDocTag`](JSDocTag.md).[`forEachChild`](JSDocTag.md#foreachchild)

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

[`JSDocTag`](JSDocTag.md).[`getChildAt`](JSDocTag.md#getchildat)

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

[`JSDocTag`](JSDocTag.md).[`getChildCount`](JSDocTag.md#getchildcount)

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

[`JSDocTag`](JSDocTag.md).[`getChildren`](JSDocTag.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getEnd`](JSDocTag.md#getend)

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

[`JSDocTag`](JSDocTag.md).[`getFirstToken`](JSDocTag.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullStart`](JSDocTag.md#getfullstart)

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

[`JSDocTag`](JSDocTag.md).[`getFullText`](JSDocTag.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullWidth`](JSDocTag.md#getfullwidth)

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

[`JSDocTag`](JSDocTag.md).[`getLastToken`](JSDocTag.md#getlasttoken)

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

[`JSDocTag`](JSDocTag.md).[`getLeadingTriviaWidth`](JSDocTag.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getSourceFile`](JSDocTag.md#getsourcefile)

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

[`JSDocTag`](JSDocTag.md).[`getStart`](JSDocTag.md#getstart)

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

[`JSDocTag`](JSDocTag.md).[`getText`](JSDocTag.md#gettext)

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

[`JSDocTag`](JSDocTag.md).[`getWidth`](JSDocTag.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocReadonlyTag.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocReadonlyTag

# Interface: JSDocReadonlyTag

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1973

## Extends

- [`JSDocTag`](JSDocTag.md)

## Properties

### comment?

> `readonly` `optional` **comment**: `string` \| [`NodeArray`](NodeArray.md)\<[`JSDocComment`](../type-aliases/JSDocComment.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1914

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`comment`](JSDocTag.md#comment)

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

[`JSDocTag`](JSDocTag.md).[`decorators`](JSDocTag.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`end`](JSDocTag.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`flags`](JSDocTag.md#flags)

***

### kind

> `readonly` **kind**: [`JSDocReadonlyTag`](../enumerations/SyntaxKind.md#jsdocreadonlytag)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1974

#### Overrides

[`JSDocTag`](JSDocTag.md).[`kind`](JSDocTag.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`locals`](JSDocTag.md#locals)

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

[`JSDocTag`](JSDocTag.md).[`modifiers`](JSDocTag.md#modifiers)

***

### parent

> `readonly` **parent**: [`JSDoc`](JSDoc.md) \| [`JSDocTypeLiteral`](JSDocTypeLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1912

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`parent`](JSDocTag.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`pos`](JSDocTag.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`skipCheck`](JSDocTag.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`symbol`](JSDocTag.md#symbol)

***

### tagName

> `readonly` **tagName**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1913

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`tagName`](JSDocTag.md#tagname)

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

[`JSDocTag`](JSDocTag.md).[`forEachChild`](JSDocTag.md#foreachchild)

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

[`JSDocTag`](JSDocTag.md).[`getChildAt`](JSDocTag.md#getchildat)

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

[`JSDocTag`](JSDocTag.md).[`getChildCount`](JSDocTag.md#getchildcount)

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

[`JSDocTag`](JSDocTag.md).[`getChildren`](JSDocTag.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getEnd`](JSDocTag.md#getend)

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

[`JSDocTag`](JSDocTag.md).[`getFirstToken`](JSDocTag.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullStart`](JSDocTag.md#getfullstart)

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

[`JSDocTag`](JSDocTag.md).[`getFullText`](JSDocTag.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullWidth`](JSDocTag.md#getfullwidth)

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

[`JSDocTag`](JSDocTag.md).[`getLastToken`](JSDocTag.md#getlasttoken)

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

[`JSDocTag`](JSDocTag.md).[`getLeadingTriviaWidth`](JSDocTag.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getSourceFile`](JSDocTag.md#getsourcefile)

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

[`JSDocTag`](JSDocTag.md).[`getStart`](JSDocTag.md#getstart)

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

[`JSDocTag`](JSDocTag.md).[`getText`](JSDocTag.md#gettext)

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

[`JSDocTag`](JSDocTag.md).[`getWidth`](JSDocTag.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocReturnTag.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocReturnTag

# Interface: JSDocReturnTag

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1997

## Extends

- [`JSDocTag`](JSDocTag.md)

## Properties

### comment?

> `readonly` `optional` **comment**: `string` \| [`NodeArray`](NodeArray.md)\<[`JSDocComment`](../type-aliases/JSDocComment.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1914

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`comment`](JSDocTag.md#comment)

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

[`JSDocTag`](JSDocTag.md).[`decorators`](JSDocTag.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`end`](JSDocTag.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`flags`](JSDocTag.md#flags)

***

### kind

> `readonly` **kind**: [`JSDocReturnTag`](../enumerations/SyntaxKind.md#jsdocreturntag)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1998

#### Overrides

[`JSDocTag`](JSDocTag.md).[`kind`](JSDocTag.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`locals`](JSDocTag.md#locals)

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

[`JSDocTag`](JSDocTag.md).[`modifiers`](JSDocTag.md#modifiers)

***

### parent

> `readonly` **parent**: [`JSDoc`](JSDoc.md) \| [`JSDocTypeLiteral`](JSDocTypeLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1912

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`parent`](JSDocTag.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`pos`](JSDocTag.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`skipCheck`](JSDocTag.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`symbol`](JSDocTag.md#symbol)

***

### tagName

> `readonly` **tagName**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1913

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`tagName`](JSDocTag.md#tagname)

***

### typeExpression?

> `readonly` `optional` **typeExpression**: [`JSDocTypeExpression`](JSDocTypeExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1999

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

[`JSDocTag`](JSDocTag.md).[`forEachChild`](JSDocTag.md#foreachchild)

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

[`JSDocTag`](JSDocTag.md).[`getChildAt`](JSDocTag.md#getchildat)

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

[`JSDocTag`](JSDocTag.md).[`getChildCount`](JSDocTag.md#getchildcount)

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

[`JSDocTag`](JSDocTag.md).[`getChildren`](JSDocTag.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getEnd`](JSDocTag.md#getend)

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

[`JSDocTag`](JSDocTag.md).[`getFirstToken`](JSDocTag.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullStart`](JSDocTag.md#getfullstart)

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

[`JSDocTag`](JSDocTag.md).[`getFullText`](JSDocTag.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullWidth`](JSDocTag.md#getfullwidth)

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

[`JSDocTag`](JSDocTag.md).[`getLastToken`](JSDocTag.md#getlasttoken)

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

[`JSDocTag`](JSDocTag.md).[`getLeadingTriviaWidth`](JSDocTag.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getSourceFile`](JSDocTag.md#getsourcefile)

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

[`JSDocTag`](JSDocTag.md).[`getStart`](JSDocTag.md#getstart)

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

[`JSDocTag`](JSDocTag.md).[`getText`](JSDocTag.md#gettext)

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

[`JSDocTag`](JSDocTag.md).[`getWidth`](JSDocTag.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocSeeTag.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocSeeTag

# Interface: JSDocSeeTag

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1993

## Extends

- [`JSDocTag`](JSDocTag.md)

## Properties

### comment?

> `readonly` `optional` **comment**: `string` \| [`NodeArray`](NodeArray.md)\<[`JSDocComment`](../type-aliases/JSDocComment.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1914

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`comment`](JSDocTag.md#comment)

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

[`JSDocTag`](JSDocTag.md).[`decorators`](JSDocTag.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`end`](JSDocTag.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`flags`](JSDocTag.md#flags)

***

### kind

> `readonly` **kind**: [`JSDocSeeTag`](../enumerations/SyntaxKind.md#jsdocseetag)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1994

#### Overrides

[`JSDocTag`](JSDocTag.md).[`kind`](JSDocTag.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`locals`](JSDocTag.md#locals)

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

[`JSDocTag`](JSDocTag.md).[`modifiers`](JSDocTag.md#modifiers)

***

### name?

> `readonly` `optional` **name**: [`JSDocNameReference`](JSDocNameReference.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1995

***

### parent

> `readonly` **parent**: [`JSDoc`](JSDoc.md) \| [`JSDocTypeLiteral`](JSDocTypeLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1912

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`parent`](JSDocTag.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`pos`](JSDocTag.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`skipCheck`](JSDocTag.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`symbol`](JSDocTag.md#symbol)

***

### tagName

> `readonly` **tagName**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1913

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`tagName`](JSDocTag.md#tagname)

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

[`JSDocTag`](JSDocTag.md).[`forEachChild`](JSDocTag.md#foreachchild)

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

[`JSDocTag`](JSDocTag.md).[`getChildAt`](JSDocTag.md#getchildat)

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

[`JSDocTag`](JSDocTag.md).[`getChildCount`](JSDocTag.md#getchildcount)

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

[`JSDocTag`](JSDocTag.md).[`getChildren`](JSDocTag.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getEnd`](JSDocTag.md#getend)

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

[`JSDocTag`](JSDocTag.md).[`getFirstToken`](JSDocTag.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullStart`](JSDocTag.md#getfullstart)

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

[`JSDocTag`](JSDocTag.md).[`getFullText`](JSDocTag.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullWidth`](JSDocTag.md#getfullwidth)

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

[`JSDocTag`](JSDocTag.md).[`getLastToken`](JSDocTag.md#getlasttoken)

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

[`JSDocTag`](JSDocTag.md).[`getLeadingTriviaWidth`](JSDocTag.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getSourceFile`](JSDocTag.md#getsourcefile)

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

[`JSDocTag`](JSDocTag.md).[`getStart`](JSDocTag.md#getstart)

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

[`JSDocTag`](JSDocTag.md).[`getText`](JSDocTag.md#gettext)

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

[`JSDocTag`](JSDocTag.md).[`getWidth`](JSDocTag.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocSignature.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocSignature

# Interface: JSDocSignature

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2019

## Extends

- [`JSDocType`](JSDocType.md).[`Declaration`](Declaration.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`Declaration`](Declaration.md).[`_declarationBrand`](Declaration.md#_declarationbrand)

***

### \_jsDocTypeBrand

> **\_jsDocTypeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1871

#### Inherited from

[`JSDocType`](JSDocType.md).[`_jsDocTypeBrand`](JSDocType.md#_jsdoctypebrand)

***

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`JSDocType`](JSDocType.md).[`_typeNodeBrand`](JSDocType.md#_typenodebrand)

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

> `readonly` **kind**: [`JSDocSignature`](../enumerations/SyntaxKind.md#jsdocsignature)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2020

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

### parameters

> `readonly` **parameters**: readonly [`JSDocParameterTag`](JSDocParameterTag.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2022

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

### type

> `readonly` **type**: `undefined` \| [`JSDocReturnTag`](JSDocReturnTag.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2023

***

### typeParameters?

> `readonly` `optional` **typeParameters**: readonly [`JSDocTemplateTag`](JSDocTemplateTag.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2021

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocTag.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocTag

# Interface: JSDocTag

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1911

## Extends

- [`Node`](Node.md)

## Extended by

- [`JSDocUnknownTag`](JSDocUnknownTag.md)
- [`JSDocAugmentsTag`](JSDocAugmentsTag.md)
- [`JSDocImplementsTag`](JSDocImplementsTag.md)
- [`JSDocAuthorTag`](JSDocAuthorTag.md)
- [`JSDocDeprecatedTag`](JSDocDeprecatedTag.md)
- [`JSDocClassTag`](JSDocClassTag.md)
- [`JSDocPublicTag`](JSDocPublicTag.md)
- [`JSDocPrivateTag`](JSDocPrivateTag.md)
- [`JSDocProtectedTag`](JSDocProtectedTag.md)
- [`JSDocReadonlyTag`](JSDocReadonlyTag.md)
- [`JSDocOverrideTag`](JSDocOverrideTag.md)
- [`JSDocEnumTag`](JSDocEnumTag.md)
- [`JSDocThisTag`](JSDocThisTag.md)
- [`JSDocTemplateTag`](JSDocTemplateTag.md)
- [`JSDocSeeTag`](JSDocSeeTag.md)
- [`JSDocReturnTag`](JSDocReturnTag.md)
- [`JSDocTypeTag`](JSDocTypeTag.md)
- [`JSDocTypedefTag`](JSDocTypedefTag.md)
- [`JSDocCallbackTag`](JSDocCallbackTag.md)
- [`JSDocPropertyLikeTag`](JSDocPropertyLikeTag.md)

## Properties

### comment?

> `readonly` `optional` **comment**: `string` \| [`NodeArray`](NodeArray.md)\<[`JSDocComment`](../type-aliases/JSDocComment.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1914

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

> `readonly` **parent**: [`JSDoc`](JSDoc.md) \| [`JSDocTypeLiteral`](JSDocTypeLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1912

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

***

### tagName

> `readonly` **tagName**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1913

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocTagInfo-1.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocTagInfo

# Interface: JSDocTagInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6876

## Properties

### index?

> `optional` **index**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6879

***

### name

> **name**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6877

***

### text?

> `optional` **text**: `string` \| [`SymbolDisplayPart`](SymbolDisplayPart.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6878




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocTemplateTag.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocTemplateTag

# Interface: JSDocTemplateTag

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1988

## Extends

- [`JSDocTag`](JSDocTag.md)

## Properties

### comment?

> `readonly` `optional` **comment**: `string` \| [`NodeArray`](NodeArray.md)\<[`JSDocComment`](../type-aliases/JSDocComment.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1914

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`comment`](JSDocTag.md#comment)

***

### constraint

> `readonly` **constraint**: `undefined` \| [`JSDocTypeExpression`](JSDocTypeExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1990

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

[`JSDocTag`](JSDocTag.md).[`decorators`](JSDocTag.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`end`](JSDocTag.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`flags`](JSDocTag.md#flags)

***

### kind

> `readonly` **kind**: [`JSDocTemplateTag`](../enumerations/SyntaxKind.md#jsdoctemplatetag)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1989

#### Overrides

[`JSDocTag`](JSDocTag.md).[`kind`](JSDocTag.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`locals`](JSDocTag.md#locals)

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

[`JSDocTag`](JSDocTag.md).[`modifiers`](JSDocTag.md#modifiers)

***

### parent

> `readonly` **parent**: [`JSDoc`](JSDoc.md) \| [`JSDocTypeLiteral`](JSDocTypeLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1912

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`parent`](JSDocTag.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`pos`](JSDocTag.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`skipCheck`](JSDocTag.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`symbol`](JSDocTag.md#symbol)

***

### tagName

> `readonly` **tagName**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1913

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`tagName`](JSDocTag.md#tagname)

***

### typeParameters

> `readonly` **typeParameters**: [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1991

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

[`JSDocTag`](JSDocTag.md).[`forEachChild`](JSDocTag.md#foreachchild)

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

[`JSDocTag`](JSDocTag.md).[`getChildAt`](JSDocTag.md#getchildat)

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

[`JSDocTag`](JSDocTag.md).[`getChildCount`](JSDocTag.md#getchildcount)

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

[`JSDocTag`](JSDocTag.md).[`getChildren`](JSDocTag.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getEnd`](JSDocTag.md#getend)

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

[`JSDocTag`](JSDocTag.md).[`getFirstToken`](JSDocTag.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullStart`](JSDocTag.md#getfullstart)

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

[`JSDocTag`](JSDocTag.md).[`getFullText`](JSDocTag.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullWidth`](JSDocTag.md#getfullwidth)

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

[`JSDocTag`](JSDocTag.md).[`getLastToken`](JSDocTag.md#getlasttoken)

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

[`JSDocTag`](JSDocTag.md).[`getLeadingTriviaWidth`](JSDocTag.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getSourceFile`](JSDocTag.md#getsourcefile)

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

[`JSDocTag`](JSDocTag.md).[`getStart`](JSDocTag.md#getstart)

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

[`JSDocTag`](JSDocTag.md).[`getText`](JSDocTag.md#gettext)

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

[`JSDocTag`](JSDocTag.md).[`getWidth`](JSDocTag.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocText.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocText

# Interface: JSDocText

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1932

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

> `readonly` **kind**: [`JSDocText`](../enumerations/SyntaxKind.md#jsdoctext)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1933

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

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1934

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocThisTag.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocThisTag

# Interface: JSDocThisTag

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1984

## Extends

- [`JSDocTag`](JSDocTag.md)

## Properties

### comment?

> `readonly` `optional` **comment**: `string` \| [`NodeArray`](NodeArray.md)\<[`JSDocComment`](../type-aliases/JSDocComment.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1914

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`comment`](JSDocTag.md#comment)

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

[`JSDocTag`](JSDocTag.md).[`decorators`](JSDocTag.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`end`](JSDocTag.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`flags`](JSDocTag.md#flags)

***

### kind

> `readonly` **kind**: [`JSDocThisTag`](../enumerations/SyntaxKind.md#jsdocthistag)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1985

#### Overrides

[`JSDocTag`](JSDocTag.md).[`kind`](JSDocTag.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`locals`](JSDocTag.md#locals)

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

[`JSDocTag`](JSDocTag.md).[`modifiers`](JSDocTag.md#modifiers)

***

### parent

> `readonly` **parent**: [`JSDoc`](JSDoc.md) \| [`JSDocTypeLiteral`](JSDocTypeLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1912

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`parent`](JSDocTag.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`pos`](JSDocTag.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`skipCheck`](JSDocTag.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`symbol`](JSDocTag.md#symbol)

***

### tagName

> `readonly` **tagName**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1913

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`tagName`](JSDocTag.md#tagname)

***

### typeExpression

> `readonly` **typeExpression**: [`JSDocTypeExpression`](JSDocTypeExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1986

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

[`JSDocTag`](JSDocTag.md).[`forEachChild`](JSDocTag.md#foreachchild)

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

[`JSDocTag`](JSDocTag.md).[`getChildAt`](JSDocTag.md#getchildat)

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

[`JSDocTag`](JSDocTag.md).[`getChildCount`](JSDocTag.md#getchildcount)

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

[`JSDocTag`](JSDocTag.md).[`getChildren`](JSDocTag.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getEnd`](JSDocTag.md#getend)

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

[`JSDocTag`](JSDocTag.md).[`getFirstToken`](JSDocTag.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullStart`](JSDocTag.md#getfullstart)

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

[`JSDocTag`](JSDocTag.md).[`getFullText`](JSDocTag.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullWidth`](JSDocTag.md#getfullwidth)

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

[`JSDocTag`](JSDocTag.md).[`getLastToken`](JSDocTag.md#getlasttoken)

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

[`JSDocTag`](JSDocTag.md).[`getLeadingTriviaWidth`](JSDocTag.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getSourceFile`](JSDocTag.md#getsourcefile)

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

[`JSDocTag`](JSDocTag.md).[`getStart`](JSDocTag.md#getstart)

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

[`JSDocTag`](JSDocTag.md).[`getText`](JSDocTag.md#gettext)

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

[`JSDocTag`](JSDocTag.md).[`getWidth`](JSDocTag.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocType

# Interface: JSDocType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1870

## Extends

- [`TypeNode`](TypeNode.md)

## Extended by

- [`JSDocAllType`](JSDocAllType.md)
- [`JSDocUnknownType`](JSDocUnknownType.md)
- [`JSDocNonNullableType`](JSDocNonNullableType.md)
- [`JSDocNullableType`](JSDocNullableType.md)
- [`JSDocOptionalType`](JSDocOptionalType.md)
- [`JSDocFunctionType`](JSDocFunctionType.md)
- [`JSDocVariadicType`](JSDocVariadicType.md)
- [`JSDocNamepathType`](JSDocNamepathType.md)
- [`JSDocSignature`](JSDocSignature.md)
- [`JSDocTypeLiteral`](JSDocTypeLiteral.md)

## Properties

### \_jsDocTypeBrand

> **\_jsDocTypeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1871

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

> `readonly` **kind**: [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:598

#### Inherited from

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocTypeExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocTypeExpression

# Interface: JSDocTypeExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1856

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

> `readonly` **kind**: [`JSDocTypeExpression`](../enumerations/SyntaxKind.md#jsdoctypeexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1857

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1858

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocTypeLiteral.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocTypeLiteral

# Interface: JSDocTypeLiteral

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2039

## Extends

- [`JSDocType`](JSDocType.md)

## Properties

### \_jsDocTypeBrand

> **\_jsDocTypeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1871

#### Inherited from

[`JSDocType`](JSDocType.md).[`_jsDocTypeBrand`](JSDocType.md#_jsdoctypebrand)

***

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`JSDocType`](JSDocType.md).[`_typeNodeBrand`](JSDocType.md#_typenodebrand)

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

[`JSDocType`](JSDocType.md).[`decorators`](JSDocType.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`JSDocType`](JSDocType.md).[`end`](JSDocType.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`JSDocType`](JSDocType.md).[`flags`](JSDocType.md#flags)

***

### isArrayType

> `readonly` **isArrayType**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2043

If true, then this type literal represents an *array* of its type.

***

### jsDocPropertyTags?

> `readonly` `optional` **jsDocPropertyTags**: readonly [`JSDocPropertyLikeTag`](JSDocPropertyLikeTag.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2041

***

### kind

> `readonly` **kind**: [`JSDocTypeLiteral`](../enumerations/SyntaxKind.md#jsdoctypeliteral)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2040

#### Overrides

[`JSDocType`](JSDocType.md).[`kind`](JSDocType.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`JSDocType`](JSDocType.md).[`locals`](JSDocType.md#locals)

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

[`JSDocType`](JSDocType.md).[`modifiers`](JSDocType.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`JSDocType`](JSDocType.md).[`parent`](JSDocType.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`JSDocType`](JSDocType.md).[`pos`](JSDocType.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`JSDocType`](JSDocType.md).[`skipCheck`](JSDocType.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`JSDocType`](JSDocType.md).[`symbol`](JSDocType.md#symbol)

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

[`JSDocType`](JSDocType.md).[`forEachChild`](JSDocType.md#foreachchild)

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

[`JSDocType`](JSDocType.md).[`getChildAt`](JSDocType.md#getchildat)

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

[`JSDocType`](JSDocType.md).[`getChildCount`](JSDocType.md#getchildcount)

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

[`JSDocType`](JSDocType.md).[`getChildren`](JSDocType.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`JSDocType`](JSDocType.md).[`getEnd`](JSDocType.md#getend)

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

[`JSDocType`](JSDocType.md).[`getFirstToken`](JSDocType.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`JSDocType`](JSDocType.md).[`getFullStart`](JSDocType.md#getfullstart)

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

[`JSDocType`](JSDocType.md).[`getFullText`](JSDocType.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`JSDocType`](JSDocType.md).[`getFullWidth`](JSDocType.md#getfullwidth)

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

[`JSDocType`](JSDocType.md).[`getLastToken`](JSDocType.md#getlasttoken)

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

[`JSDocType`](JSDocType.md).[`getLeadingTriviaWidth`](JSDocType.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`JSDocType`](JSDocType.md).[`getSourceFile`](JSDocType.md#getsourcefile)

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

[`JSDocType`](JSDocType.md).[`getStart`](JSDocType.md#getstart)

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

[`JSDocType`](JSDocType.md).[`getText`](JSDocType.md#gettext)

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

[`JSDocType`](JSDocType.md).[`getWidth`](JSDocType.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocTypeTag.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocTypeTag

# Interface: JSDocTypeTag

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2001

## Extends

- [`JSDocTag`](JSDocTag.md)

## Properties

### comment?

> `readonly` `optional` **comment**: `string` \| [`NodeArray`](NodeArray.md)\<[`JSDocComment`](../type-aliases/JSDocComment.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1914

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`comment`](JSDocTag.md#comment)

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

[`JSDocTag`](JSDocTag.md).[`decorators`](JSDocTag.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`end`](JSDocTag.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`flags`](JSDocTag.md#flags)

***

### kind

> `readonly` **kind**: [`JSDocTypeTag`](../enumerations/SyntaxKind.md#jsdoctypetag)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2002

#### Overrides

[`JSDocTag`](JSDocTag.md).[`kind`](JSDocTag.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`locals`](JSDocTag.md#locals)

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

[`JSDocTag`](JSDocTag.md).[`modifiers`](JSDocTag.md#modifiers)

***

### parent

> `readonly` **parent**: [`JSDoc`](JSDoc.md) \| [`JSDocTypeLiteral`](JSDocTypeLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1912

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`parent`](JSDocTag.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`pos`](JSDocTag.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`skipCheck`](JSDocTag.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`symbol`](JSDocTag.md#symbol)

***

### tagName

> `readonly` **tagName**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1913

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`tagName`](JSDocTag.md#tagname)

***

### typeExpression

> `readonly` **typeExpression**: [`JSDocTypeExpression`](JSDocTypeExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2003

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

[`JSDocTag`](JSDocTag.md).[`forEachChild`](JSDocTag.md#foreachchild)

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

[`JSDocTag`](JSDocTag.md).[`getChildAt`](JSDocTag.md#getchildat)

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

[`JSDocTag`](JSDocTag.md).[`getChildCount`](JSDocTag.md#getchildcount)

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

[`JSDocTag`](JSDocTag.md).[`getChildren`](JSDocTag.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getEnd`](JSDocTag.md#getend)

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

[`JSDocTag`](JSDocTag.md).[`getFirstToken`](JSDocTag.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullStart`](JSDocTag.md#getfullstart)

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

[`JSDocTag`](JSDocTag.md).[`getFullText`](JSDocTag.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullWidth`](JSDocTag.md#getfullwidth)

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

[`JSDocTag`](JSDocTag.md).[`getLastToken`](JSDocTag.md#getlasttoken)

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

[`JSDocTag`](JSDocTag.md).[`getLeadingTriviaWidth`](JSDocTag.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getSourceFile`](JSDocTag.md#getsourcefile)

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

[`JSDocTag`](JSDocTag.md).[`getStart`](JSDocTag.md#getstart)

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

[`JSDocTag`](JSDocTag.md).[`getText`](JSDocTag.md#gettext)

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

[`JSDocTag`](JSDocTag.md).[`getWidth`](JSDocTag.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocTypedefTag.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocTypedefTag

# Interface: JSDocTypedefTag

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2005

## Extends

- [`JSDocTag`](JSDocTag.md).[`NamedDeclaration`](NamedDeclaration.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`_declarationBrand`](NamedDeclaration.md#_declarationbrand)

***

### comment?

> `readonly` `optional` **comment**: `string` \| [`NodeArray`](NodeArray.md)\<[`JSDocComment`](../type-aliases/JSDocComment.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1914

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`comment`](JSDocTag.md#comment)

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

### fullName?

> `readonly` `optional` **fullName**: [`Identifier`](Identifier.md) \| [`JSDocNamespaceDeclaration`](JSDocNamespaceDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2008

***

### kind

> `readonly` **kind**: [`JSDocTypedefTag`](../enumerations/SyntaxKind.md#jsdoctypedeftag)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2006

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

> `readonly` `optional` **name**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2009

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`name`](NamedDeclaration.md#name)

***

### parent

> `readonly` **parent**: [`JSDoc`](JSDoc.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2007

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

***

### tagName

> `readonly` **tagName**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1913

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`tagName`](JSDocTag.md#tagname)

***

### typeExpression?

> `readonly` `optional` **typeExpression**: [`JSDocTypeLiteral`](JSDocTypeLiteral.md) \| [`JSDocTypeExpression`](JSDocTypeExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2010

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocUnknownTag.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocUnknownTag

# Interface: JSDocUnknownTag

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1936

## Extends

- [`JSDocTag`](JSDocTag.md)

## Properties

### comment?

> `readonly` `optional` **comment**: `string` \| [`NodeArray`](NodeArray.md)\<[`JSDocComment`](../type-aliases/JSDocComment.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1914

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`comment`](JSDocTag.md#comment)

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

[`JSDocTag`](JSDocTag.md).[`decorators`](JSDocTag.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`end`](JSDocTag.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`flags`](JSDocTag.md#flags)

***

### kind

> `readonly` **kind**: [`JSDocTag`](../enumerations/SyntaxKind.md#jsdoctag)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1937

#### Overrides

[`JSDocTag`](JSDocTag.md).[`kind`](JSDocTag.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`locals`](JSDocTag.md#locals)

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

[`JSDocTag`](JSDocTag.md).[`modifiers`](JSDocTag.md#modifiers)

***

### parent

> `readonly` **parent**: [`JSDoc`](JSDoc.md) \| [`JSDocTypeLiteral`](JSDocTypeLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1912

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`parent`](JSDocTag.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`pos`](JSDocTag.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`skipCheck`](JSDocTag.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`symbol`](JSDocTag.md#symbol)

***

### tagName

> `readonly` **tagName**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1913

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`tagName`](JSDocTag.md#tagname)

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

[`JSDocTag`](JSDocTag.md).[`forEachChild`](JSDocTag.md#foreachchild)

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

[`JSDocTag`](JSDocTag.md).[`getChildAt`](JSDocTag.md#getchildat)

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

[`JSDocTag`](JSDocTag.md).[`getChildCount`](JSDocTag.md#getchildcount)

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

[`JSDocTag`](JSDocTag.md).[`getChildren`](JSDocTag.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getEnd`](JSDocTag.md#getend)

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

[`JSDocTag`](JSDocTag.md).[`getFirstToken`](JSDocTag.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullStart`](JSDocTag.md#getfullstart)

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

[`JSDocTag`](JSDocTag.md).[`getFullText`](JSDocTag.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getFullWidth`](JSDocTag.md#getfullwidth)

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

[`JSDocTag`](JSDocTag.md).[`getLastToken`](JSDocTag.md#getlasttoken)

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

[`JSDocTag`](JSDocTag.md).[`getLeadingTriviaWidth`](JSDocTag.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`JSDocTag`](JSDocTag.md).[`getSourceFile`](JSDocTag.md#getsourcefile)

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

[`JSDocTag`](JSDocTag.md).[`getStart`](JSDocTag.md#getstart)

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

[`JSDocTag`](JSDocTag.md).[`getText`](JSDocTag.md#gettext)

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

[`JSDocTag`](JSDocTag.md).[`getWidth`](JSDocTag.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocUnknownType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocUnknownType

# Interface: JSDocUnknownType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1876

## Extends

- [`JSDocType`](JSDocType.md)

## Properties

### \_jsDocTypeBrand

> **\_jsDocTypeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1871

#### Inherited from

[`JSDocType`](JSDocType.md).[`_jsDocTypeBrand`](JSDocType.md#_jsdoctypebrand)

***

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`JSDocType`](JSDocType.md).[`_typeNodeBrand`](JSDocType.md#_typenodebrand)

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

[`JSDocType`](JSDocType.md).[`decorators`](JSDocType.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`JSDocType`](JSDocType.md).[`end`](JSDocType.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`JSDocType`](JSDocType.md).[`flags`](JSDocType.md#flags)

***

### kind

> `readonly` **kind**: [`JSDocUnknownType`](../enumerations/SyntaxKind.md#jsdocunknowntype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1877

#### Overrides

[`JSDocType`](JSDocType.md).[`kind`](JSDocType.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`JSDocType`](JSDocType.md).[`locals`](JSDocType.md#locals)

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

[`JSDocType`](JSDocType.md).[`modifiers`](JSDocType.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`JSDocType`](JSDocType.md).[`parent`](JSDocType.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`JSDocType`](JSDocType.md).[`pos`](JSDocType.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`JSDocType`](JSDocType.md).[`skipCheck`](JSDocType.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`JSDocType`](JSDocType.md).[`symbol`](JSDocType.md#symbol)

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

[`JSDocType`](JSDocType.md).[`forEachChild`](JSDocType.md#foreachchild)

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

[`JSDocType`](JSDocType.md).[`getChildAt`](JSDocType.md#getchildat)

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

[`JSDocType`](JSDocType.md).[`getChildCount`](JSDocType.md#getchildcount)

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

[`JSDocType`](JSDocType.md).[`getChildren`](JSDocType.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`JSDocType`](JSDocType.md).[`getEnd`](JSDocType.md#getend)

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

[`JSDocType`](JSDocType.md).[`getFirstToken`](JSDocType.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`JSDocType`](JSDocType.md).[`getFullStart`](JSDocType.md#getfullstart)

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

[`JSDocType`](JSDocType.md).[`getFullText`](JSDocType.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`JSDocType`](JSDocType.md).[`getFullWidth`](JSDocType.md#getfullwidth)

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

[`JSDocType`](JSDocType.md).[`getLastToken`](JSDocType.md#getlasttoken)

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

[`JSDocType`](JSDocType.md).[`getLeadingTriviaWidth`](JSDocType.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`JSDocType`](JSDocType.md).[`getSourceFile`](JSDocType.md#getsourcefile)

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

[`JSDocType`](JSDocType.md).[`getStart`](JSDocType.md#getstart)

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

[`JSDocType`](JSDocType.md).[`getText`](JSDocType.md#gettext)

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

[`JSDocType`](JSDocType.md).[`getWidth`](JSDocType.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JSDocVariadicType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JSDocVariadicType

# Interface: JSDocVariadicType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1896

## Extends

- [`JSDocType`](JSDocType.md)

## Properties

### \_jsDocTypeBrand

> **\_jsDocTypeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1871

#### Inherited from

[`JSDocType`](JSDocType.md).[`_jsDocTypeBrand`](JSDocType.md#_jsdoctypebrand)

***

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`JSDocType`](JSDocType.md).[`_typeNodeBrand`](JSDocType.md#_typenodebrand)

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

[`JSDocType`](JSDocType.md).[`decorators`](JSDocType.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`JSDocType`](JSDocType.md).[`end`](JSDocType.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`JSDocType`](JSDocType.md).[`flags`](JSDocType.md#flags)

***

### kind

> `readonly` **kind**: [`JSDocVariadicType`](../enumerations/SyntaxKind.md#jsdocvariadictype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1897

#### Overrides

[`JSDocType`](JSDocType.md).[`kind`](JSDocType.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`JSDocType`](JSDocType.md).[`locals`](JSDocType.md#locals)

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

[`JSDocType`](JSDocType.md).[`modifiers`](JSDocType.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`JSDocType`](JSDocType.md).[`parent`](JSDocType.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`JSDocType`](JSDocType.md).[`pos`](JSDocType.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`JSDocType`](JSDocType.md).[`skipCheck`](JSDocType.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`JSDocType`](JSDocType.md).[`symbol`](JSDocType.md#symbol)

***

### type

> `readonly` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1898

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

[`JSDocType`](JSDocType.md).[`forEachChild`](JSDocType.md#foreachchild)

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

[`JSDocType`](JSDocType.md).[`getChildAt`](JSDocType.md#getchildat)

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

[`JSDocType`](JSDocType.md).[`getChildCount`](JSDocType.md#getchildcount)

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

[`JSDocType`](JSDocType.md).[`getChildren`](JSDocType.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`JSDocType`](JSDocType.md).[`getEnd`](JSDocType.md#getend)

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

[`JSDocType`](JSDocType.md).[`getFirstToken`](JSDocType.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`JSDocType`](JSDocType.md).[`getFullStart`](JSDocType.md#getfullstart)

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

[`JSDocType`](JSDocType.md).[`getFullText`](JSDocType.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`JSDocType`](JSDocType.md).[`getFullWidth`](JSDocType.md#getfullwidth)

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

[`JSDocType`](JSDocType.md).[`getLastToken`](JSDocType.md#getlasttoken)

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

[`JSDocType`](JSDocType.md).[`getLeadingTriviaWidth`](JSDocType.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`JSDocType`](JSDocType.md).[`getSourceFile`](JSDocType.md#getsourcefile)

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

[`JSDocType`](JSDocType.md).[`getStart`](JSDocType.md#getstart)

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

[`JSDocType`](JSDocType.md).[`getText`](JSDocType.md#gettext)

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

[`JSDocType`](JSDocType.md).[`getWidth`](JSDocType.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsDocNodeCheckConfig.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsDocNodeCheckConfig

# Interface: JsDocNodeCheckConfig

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3444

## Properties

### checkConfig

> **checkConfig**: [`JsDocNodeCheckConfigItem`](JsDocNodeCheckConfigItem.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3446

***

### nodeNeedCheck

> **nodeNeedCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3445




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsDocNodeCheckConfigItem.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsDocNodeCheckConfigItem

# Interface: JsDocNodeCheckConfigItem

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3448

## Properties

### checkJsDocSpecialValidCallback()?

> `optional` **checkJsDocSpecialValidCallback**: (`jsDocTags`, `config`) => `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3456

#### Parameters

##### jsDocTags

readonly [`JSDocTag`](JSDocTag.md)[]

##### config

`JsDocNodeCheckConfigItem`

#### Returns

`boolean`

***

### checkValidCallback()?

> `optional` **checkValidCallback**: (`jsDocTag`, `config`) => `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3455

#### Parameters

##### jsDocTag

[`JSDocTag`](JSDocTag.md)

##### config

`JsDocNodeCheckConfigItem`

#### Returns

`boolean`

***

### message

> **message**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3450

***

### needConditionCheck

> **needConditionCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3451

***

### specifyCheckConditionFuncName

> **specifyCheckConditionFuncName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3453

***

### tagName

> **tagName**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3449

***

### tagNameShouldExisted

> **tagNameShouldExisted**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3454

***

### type

> **type**: [`DiagnosticCategory`](../enumerations/DiagnosticCategory.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3452




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsDocTagInfo.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsDocTagInfo

# Interface: JsDocTagInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2269

## Properties

### name

> **name**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2270

***

### text?

> `optional` **text**: `string` \| [`SymbolDisplayPart`](SymbolDisplayPart.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2271




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsonMinusNumericLiteral.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsonMinusNumericLiteral

# Interface: JsonMinusNumericLiteral

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2221

## Extends

- [`PrefixUnaryExpression`](PrefixUnaryExpression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`_expressionBrand`](PrefixUnaryExpression.md#_expressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`_unaryExpressionBrand`](PrefixUnaryExpression.md#_unaryexpressionbrand)

***

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`_updateExpressionBrand`](PrefixUnaryExpression.md#_updateexpressionbrand)

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

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`decorators`](PrefixUnaryExpression.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`end`](PrefixUnaryExpression.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`flags`](PrefixUnaryExpression.md#flags)

***

### kind

> `readonly` **kind**: [`PrefixUnaryExpression`](../enumerations/SyntaxKind.md#prefixunaryexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2222

#### Overrides

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`kind`](PrefixUnaryExpression.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`locals`](PrefixUnaryExpression.md#locals)

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

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`modifiers`](PrefixUnaryExpression.md#modifiers)

***

### operand

> `readonly` **operand**: [`NumericLiteral`](NumericLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2224

#### Overrides

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`operand`](PrefixUnaryExpression.md#operand)

***

### operator

> `readonly` **operator**: [`MinusToken`](../enumerations/SyntaxKind.md#minustoken)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2223

#### Overrides

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`operator`](PrefixUnaryExpression.md#operator)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`parent`](PrefixUnaryExpression.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`pos`](PrefixUnaryExpression.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`skipCheck`](PrefixUnaryExpression.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`symbol`](PrefixUnaryExpression.md#symbol)

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

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`forEachChild`](PrefixUnaryExpression.md#foreachchild)

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

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getChildAt`](PrefixUnaryExpression.md#getchildat)

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

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getChildCount`](PrefixUnaryExpression.md#getchildcount)

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

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getChildren`](PrefixUnaryExpression.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getEnd`](PrefixUnaryExpression.md#getend)

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

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getFirstToken`](PrefixUnaryExpression.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getFullStart`](PrefixUnaryExpression.md#getfullstart)

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

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getFullText`](PrefixUnaryExpression.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getFullWidth`](PrefixUnaryExpression.md#getfullwidth)

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

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getLastToken`](PrefixUnaryExpression.md#getlasttoken)

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

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getLeadingTriviaWidth`](PrefixUnaryExpression.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getSourceFile`](PrefixUnaryExpression.md#getsourcefile)

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

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getStart`](PrefixUnaryExpression.md#getstart)

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

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getText`](PrefixUnaryExpression.md#gettext)

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

[`PrefixUnaryExpression`](PrefixUnaryExpression.md).[`getWidth`](PrefixUnaryExpression.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsonObjectExpressionStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsonObjectExpressionStatement

# Interface: JsonObjectExpressionStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2227

## Extends

- [`ExpressionStatement`](ExpressionStatement.md)

## Properties

### \_statementBrand

> **\_statementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1471

#### Inherited from

[`ExpressionStatement`](ExpressionStatement.md).[`_statementBrand`](ExpressionStatement.md#_statementbrand)

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

[`ExpressionStatement`](ExpressionStatement.md).[`decorators`](ExpressionStatement.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`ExpressionStatement`](ExpressionStatement.md).[`end`](ExpressionStatement.md#end)

***

### expression

> `readonly` **expression**: [`JsonObjectExpression`](../type-aliases/JsonObjectExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2228

#### Overrides

[`ExpressionStatement`](ExpressionStatement.md).[`expression`](ExpressionStatement.md#expression)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`ExpressionStatement`](ExpressionStatement.md).[`flags`](ExpressionStatement.md#flags)

***

### kind

> `readonly` **kind**: [`ExpressionStatement`](../enumerations/SyntaxKind.md#expressionstatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1504

#### Inherited from

[`ExpressionStatement`](ExpressionStatement.md).[`kind`](ExpressionStatement.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`ExpressionStatement`](ExpressionStatement.md).[`locals`](ExpressionStatement.md#locals)

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

[`ExpressionStatement`](ExpressionStatement.md).[`modifiers`](ExpressionStatement.md#modifiers)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`ExpressionStatement`](ExpressionStatement.md).[`parent`](ExpressionStatement.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`ExpressionStatement`](ExpressionStatement.md).[`pos`](ExpressionStatement.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`ExpressionStatement`](ExpressionStatement.md).[`skipCheck`](ExpressionStatement.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`ExpressionStatement`](ExpressionStatement.md).[`symbol`](ExpressionStatement.md#symbol)

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

[`ExpressionStatement`](ExpressionStatement.md).[`forEachChild`](ExpressionStatement.md#foreachchild)

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

[`ExpressionStatement`](ExpressionStatement.md).[`getChildAt`](ExpressionStatement.md#getchildat)

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

[`ExpressionStatement`](ExpressionStatement.md).[`getChildCount`](ExpressionStatement.md#getchildcount)

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

[`ExpressionStatement`](ExpressionStatement.md).[`getChildren`](ExpressionStatement.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`ExpressionStatement`](ExpressionStatement.md).[`getEnd`](ExpressionStatement.md#getend)

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

[`ExpressionStatement`](ExpressionStatement.md).[`getFirstToken`](ExpressionStatement.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`ExpressionStatement`](ExpressionStatement.md).[`getFullStart`](ExpressionStatement.md#getfullstart)

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

[`ExpressionStatement`](ExpressionStatement.md).[`getFullText`](ExpressionStatement.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`ExpressionStatement`](ExpressionStatement.md).[`getFullWidth`](ExpressionStatement.md#getfullwidth)

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

[`ExpressionStatement`](ExpressionStatement.md).[`getLastToken`](ExpressionStatement.md#getlasttoken)

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

[`ExpressionStatement`](ExpressionStatement.md).[`getLeadingTriviaWidth`](ExpressionStatement.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`ExpressionStatement`](ExpressionStatement.md).[`getSourceFile`](ExpressionStatement.md#getsourcefile)

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

[`ExpressionStatement`](ExpressionStatement.md).[`getStart`](ExpressionStatement.md#getstart)

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

[`ExpressionStatement`](ExpressionStatement.md).[`getText`](ExpressionStatement.md#gettext)

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

[`ExpressionStatement`](ExpressionStatement.md).[`getWidth`](ExpressionStatement.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsonSourceFile.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsonSourceFile

# Interface: JsonSourceFile

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2215

## Extends

- [`SourceFile`](SourceFile.md)

## Extended by

- [`TsConfigSourceFile`](TsConfigSourceFile.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`SourceFile`](SourceFile.md).[`_declarationBrand`](SourceFile.md#_declarationbrand)

***

### amdDependencies

> **amdDependencies**: readonly [`AmdDependency`](AmdDependency.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2122

#### Inherited from

[`SourceFile`](SourceFile.md).[`amdDependencies`](SourceFile.md#amddependencies)

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

[`SourceFile`](SourceFile.md).[`decorators`](SourceFile.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`SourceFile`](SourceFile.md).[`end`](SourceFile.md#end)

***

### endOfFileToken

> `readonly` **endOfFileToken**: [`Token`](Token.md)\<[`EndOfFileToken`](../enumerations/SyntaxKind.md#endoffiletoken)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2119

#### Inherited from

[`SourceFile`](SourceFile.md).[`endOfFileToken`](SourceFile.md#endoffiletoken)

***

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2120

#### Inherited from

[`SourceFile`](SourceFile.md).[`fileName`](SourceFile.md#filename)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`SourceFile`](SourceFile.md).[`flags`](SourceFile.md#flags)

***

### hasNoDefaultLib

> **hasNoDefaultLib**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2137

lib.d.ts should have a reference comment like

 /// <reference no-default-lib="true"/>

If any other file has this comment, it signals not to include lib.d.ts
because this containing file is intended to act as a default library.

#### Inherited from

[`SourceFile`](SourceFile.md).[`hasNoDefaultLib`](SourceFile.md#hasnodefaultlib)

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

[`SourceFile`](SourceFile.md).[`impliedNodeFormat`](SourceFile.md#impliednodeformat)

***

### isDeclarationFile

> **isDeclarationFile**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2128

#### Inherited from

[`SourceFile`](SourceFile.md).[`isDeclarationFile`](SourceFile.md#isdeclarationfile)

***

### kind

> `readonly` **kind**: [`SourceFile`](../enumerations/SyntaxKind.md#sourcefile)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2117

#### Inherited from

[`SourceFile`](SourceFile.md).[`kind`](SourceFile.md#kind)

***

### languageVariant

> **languageVariant**: [`LanguageVariant`](../enumerations/LanguageVariant.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2127

#### Inherited from

[`SourceFile`](SourceFile.md).[`languageVariant`](SourceFile.md#languagevariant)

***

### languageVersion

> **languageVersion**: [`ScriptTarget`](../enumerations/ScriptTarget.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2138

#### Inherited from

[`SourceFile`](SourceFile.md).[`languageVersion`](SourceFile.md#languageversion)

***

### libReferenceDirectives

> **libReferenceDirectives**: readonly [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2126

#### Inherited from

[`SourceFile`](SourceFile.md).[`libReferenceDirectives`](SourceFile.md#libreferencedirectives)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`SourceFile`](SourceFile.md).[`locals`](SourceFile.md#locals)

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

[`SourceFile`](SourceFile.md).[`modifiers`](SourceFile.md#modifiers)

***

### moduleName?

> `optional` **moduleName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2123

#### Inherited from

[`SourceFile`](SourceFile.md).[`moduleName`](SourceFile.md#modulename)

***

### parent

> `readonly` **parent**: [`Node`](Node.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:600

#### Inherited from

[`SourceFile`](SourceFile.md).[`parent`](SourceFile.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`SourceFile`](SourceFile.md).[`pos`](SourceFile.md#pos)

***

### referencedFiles

> **referencedFiles**: readonly [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2124

#### Inherited from

[`SourceFile`](SourceFile.md).[`referencedFiles`](SourceFile.md#referencedfiles)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`SourceFile`](SourceFile.md).[`skipCheck`](SourceFile.md#skipcheck)

***

### statements

> `readonly` **statements**: [`NodeArray`](NodeArray.md)\<[`JsonObjectExpressionStatement`](JsonObjectExpressionStatement.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2216

#### Overrides

[`SourceFile`](SourceFile.md).[`statements`](SourceFile.md#statements)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`SourceFile`](SourceFile.md).[`symbol`](SourceFile.md#symbol)

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2121

#### Inherited from

[`SourceFile`](SourceFile.md).[`text`](SourceFile.md#text)

***

### typeReferenceDirectives

> **typeReferenceDirectives**: readonly [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2125

#### Inherited from

[`SourceFile`](SourceFile.md).[`typeReferenceDirectives`](SourceFile.md#typereferencedirectives)

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

[`SourceFile`](SourceFile.md).[`forEachChild`](SourceFile.md#foreachchild)

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

[`SourceFile`](SourceFile.md).[`getChildAt`](SourceFile.md#getchildat)

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

[`SourceFile`](SourceFile.md).[`getChildCount`](SourceFile.md#getchildcount)

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

[`SourceFile`](SourceFile.md).[`getChildren`](SourceFile.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`SourceFile`](SourceFile.md).[`getEnd`](SourceFile.md#getend)

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

[`SourceFile`](SourceFile.md).[`getFirstToken`](SourceFile.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`SourceFile`](SourceFile.md).[`getFullStart`](SourceFile.md#getfullstart)

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

[`SourceFile`](SourceFile.md).[`getFullText`](SourceFile.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`SourceFile`](SourceFile.md).[`getFullWidth`](SourceFile.md#getfullwidth)

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

[`SourceFile`](SourceFile.md).[`getLastToken`](SourceFile.md#getlasttoken)

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

[`SourceFile`](SourceFile.md).[`getLeadingTriviaWidth`](SourceFile.md#getleadingtriviawidth)

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

[`SourceFile`](SourceFile.md).[`getLineAndCharacterOfPosition`](SourceFile.md#getlineandcharacterofposition)

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

[`SourceFile`](SourceFile.md).[`getLineEndOfPosition`](SourceFile.md#getlineendofposition)

***

### getLineStarts()

> **getLineStarts**(): readonly `number`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6159

#### Returns

readonly `number`[]

#### Inherited from

[`SourceFile`](SourceFile.md).[`getLineStarts`](SourceFile.md#getlinestarts)

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

[`SourceFile`](SourceFile.md).[`getPositionOfLineAndCharacter`](SourceFile.md#getpositionoflineandcharacter)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`SourceFile`](SourceFile.md).[`getSourceFile`](SourceFile.md#getsourcefile)

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

[`SourceFile`](SourceFile.md).[`getStart`](SourceFile.md#getstart)

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

[`SourceFile`](SourceFile.md).[`getText`](SourceFile.md#gettext)

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

[`SourceFile`](SourceFile.md).[`getWidth`](SourceFile.md#getwidth)

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

[`SourceFile`](SourceFile.md).[`update`](SourceFile.md#update)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxAttribute.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxAttribute

# Interface: JsxAttribute

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1441

## Extends

- [`ObjectLiteralElement`](ObjectLiteralElement.md)

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

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`flags`](ObjectLiteralElement.md#flags)

***

### initializer?

> `readonly` `optional` **initializer**: [`JsxAttributeValue`](../type-aliases/JsxAttributeValue.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1445

***

### kind

> `readonly` **kind**: [`JsxAttribute`](../enumerations/SyntaxKind.md#jsxattribute)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1442

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

> `readonly` **name**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1444

#### Overrides

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`name`](ObjectLiteralElement.md#name)

***

### parent

> `readonly` **parent**: [`JsxAttributes`](JsxAttributes.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1443

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxAttributes.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxAttributes

# Interface: JsxAttributes

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1410

This interface is a base interface for ObjectLiteralExpression and JSXAttributes to extend from. JSXAttributes is similar to
ObjectLiteralExpression in that it contains array of properties; however, JSXAttributes' properties can only be
JSXAttribute or JSXSpreadAttribute. ObjectLiteralExpression, on the other hand, can only have properties of type
ObjectLiteralElement (e.g. PropertyAssignment, ShorthandPropertyAssignment etc.)

## Extends

- [`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md)\<[`JsxAttributeLike`](../type-aliases/JsxAttributeLike.md)\>

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

> `readonly` **kind**: [`JsxAttributes`](../enumerations/SyntaxKind.md#jsxattributes)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1411

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

> `readonly` **parent**: [`JsxOpeningLikeElement`](../type-aliases/JsxOpeningLikeElement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1412

#### Overrides

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`parent`](ObjectLiteralExpressionBase.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`ObjectLiteralExpressionBase`](ObjectLiteralExpressionBase.md).[`pos`](ObjectLiteralExpressionBase.md#pos)

***

### properties

> `readonly` **properties**: [`NodeArray`](NodeArray.md)\<[`JsxAttributeLike`](../type-aliases/JsxAttributeLike.md)\>

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxClosingElement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxClosingElement

# Interface: JsxClosingElement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1453

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

> `readonly` **kind**: [`JsxClosingElement`](../enumerations/SyntaxKind.md#jsxclosingelement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1454

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

> `readonly` **parent**: [`JsxElement`](JsxElement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1455

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

***

### tagName

> `readonly` **tagName**: [`JsxTagNameExpression`](../type-aliases/JsxTagNameExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1456

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxClosingFragment.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxClosingFragment

# Interface: JsxClosingFragment

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1437

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

> `readonly` **kind**: [`JsxClosingFragment`](../enumerations/SyntaxKind.md#jsxclosingfragment)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1438

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

> `readonly` **parent**: [`JsxFragment`](JsxFragment.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1439

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxClosingTagInfo.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxClosingTagInfo

# Interface: JsxClosingTagInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6435

## Properties

### newText

> `readonly` **newText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6436




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxElement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxElement

# Interface: JsxElement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1398

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

### children

> `readonly` **children**: [`NodeArray`](NodeArray.md)\<[`JsxChild`](../type-aliases/JsxChild.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1401

***

### closingElement

> `readonly` **closingElement**: [`JsxClosingElement`](JsxClosingElement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1402

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

> `readonly` **kind**: [`JsxElement`](../enumerations/SyntaxKind.md#jsxelement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1399

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

### openingElement

> `readonly` **openingElement**: [`JsxOpeningElement`](JsxOpeningElement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1400

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxExpression

# Interface: JsxExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1458

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

### dotDotDotToken?

> `readonly` `optional` **dotDotDotToken**: [`Token`](Token.md)\<[`DotDotDotToken`](../enumerations/SyntaxKind.md#dotdotdottoken)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1461

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`Expression`](Expression.md).[`end`](Expression.md#end)

***

### expression?

> `readonly` `optional` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1462

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Expression`](Expression.md).[`flags`](Expression.md#flags)

***

### kind

> `readonly` **kind**: [`JsxExpression`](../enumerations/SyntaxKind.md#jsxexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1459

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

> `readonly` **parent**: [`JsxElement`](JsxElement.md) \| [`JsxFragment`](JsxFragment.md) \| [`JsxAttributeLike`](../type-aliases/JsxAttributeLike.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1460

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxFragment.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxFragment

# Interface: JsxFragment

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1427

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

### children

> `readonly` **children**: [`NodeArray`](NodeArray.md)\<[`JsxChild`](../type-aliases/JsxChild.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1430

***

### closingFragment

> `readonly` **closingFragment**: [`JsxClosingFragment`](JsxClosingFragment.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1431

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

> `readonly` **kind**: [`JsxFragment`](../enumerations/SyntaxKind.md#jsxfragment)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1428

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

### openingFragment

> `readonly` **openingFragment**: [`JsxOpeningFragment`](JsxOpeningFragment.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1429

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxOpeningElement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxOpeningElement

# Interface: JsxOpeningElement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1414

## Extends

- [`Expression`](Expression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`Expression`](Expression.md).[`_expressionBrand`](Expression.md#_expressionbrand)

***

### attributes

> `readonly` **attributes**: [`JsxAttributes`](JsxAttributes.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1419

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

> `readonly` **kind**: [`JsxOpeningElement`](../enumerations/SyntaxKind.md#jsxopeningelement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1415

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

> `readonly` **parent**: [`JsxElement`](JsxElement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1416

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

***

### tagName

> `readonly` **tagName**: [`JsxTagNameExpression`](../type-aliases/JsxTagNameExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1417

***

### typeArguments?

> `readonly` `optional` **typeArguments**: [`NodeArray`](NodeArray.md)\<[`TypeNode`](TypeNode.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1418

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxOpeningFragment.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxOpeningFragment

# Interface: JsxOpeningFragment

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1433

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

> `readonly` **kind**: [`JsxOpeningFragment`](../enumerations/SyntaxKind.md#jsxopeningfragment)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1434

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

> `readonly` **parent**: [`JsxFragment`](JsxFragment.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1435

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxSelfClosingElement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxSelfClosingElement

# Interface: JsxSelfClosingElement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1421

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

### attributes

> `readonly` **attributes**: [`JsxAttributes`](JsxAttributes.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1425

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

> `readonly` **kind**: [`JsxSelfClosingElement`](../enumerations/SyntaxKind.md#jsxselfclosingelement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1422

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

### tagName

> `readonly` **tagName**: [`JsxTagNameExpression`](../type-aliases/JsxTagNameExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1423

***

### typeArguments?

> `readonly` `optional` **typeArguments**: [`NodeArray`](NodeArray.md)\<[`TypeNode`](TypeNode.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1424

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxSpreadAttribute.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxSpreadAttribute

# Interface: JsxSpreadAttribute

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1448

## Extends

- [`ObjectLiteralElement`](ObjectLiteralElement.md)

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1451

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`ObjectLiteralElement`](ObjectLiteralElement.md).[`flags`](ObjectLiteralElement.md#flags)

***

### kind

> `readonly` **kind**: [`JsxSpreadAttribute`](../enumerations/SyntaxKind.md#jsxspreadattribute)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1449

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

> `readonly` **parent**: [`JsxAttributes`](JsxAttributes.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1450

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxTagNamePropertyAccess.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxTagNamePropertyAccess

# Interface: JsxTagNamePropertyAccess

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1407

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

> `readonly` **expression**: [`JsxTagNameExpression`](../type-aliases/JsxTagNameExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1408

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/JsxText.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / JsxText

# Interface: JsxText

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1464

## Extends

- [`LiteralLikeNode`](LiteralLikeNode.md)

## Properties

### containsOnlyTriviaWhiteSpaces

> `readonly` **containsOnlyTriviaWhiteSpaces**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1467

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

> `readonly` **kind**: [`JsxText`](../enumerations/SyntaxKind.md#jsxtext)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1465

#### Overrides

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

> `readonly` **parent**: [`JsxElement`](JsxElement.md) \| [`JsxFragment`](JsxFragment.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1466

#### Overrides

[`LiteralLikeNode`](LiteralLikeNode.md).[`parent`](LiteralLikeNode.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`LiteralLikeNode`](LiteralLikeNode.md).[`pos`](LiteralLikeNode.md#pos)

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/KeywordToken.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / KeywordToken

# Interface: KeywordToken\<TKind\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:635

## Extends

- [`Token`](Token.md)\<`TKind`\>

## Extended by

- [`ModifierToken`](ModifierToken.md)
- [`KeywordTypeNode`](KeywordTypeNode.md)

## Type Parameters

### TKind

`TKind` *extends* [`KeywordSyntaxKind`](../type-aliases/KeywordSyntaxKind.md)

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/KeywordTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / KeywordTypeNode

# Interface: KeywordTypeNode\<TKind\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:914

## Extends

- [`KeywordToken`](KeywordToken.md)\<`TKind`\>.[`TypeNode`](TypeNode.md)

## Type Parameters

### TKind

`TKind` *extends* [`KeywordTypeSyntaxKind`](../type-aliases/KeywordTypeSyntaxKind.md) = [`KeywordTypeSyntaxKind`](../type-aliases/KeywordTypeSyntaxKind.md)

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

> `readonly` **kind**: `TKind`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:915

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/LabeledStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / LabeledStatement

# Interface: LabeledStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1584

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

> `readonly` **kind**: [`LabeledStatement`](../enumerations/SyntaxKind.md#labeledstatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1585

#### Overrides

[`Statement`](Statement.md).[`kind`](Statement.md#kind)

***

### label

> `readonly` **label**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1586

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

### statement

> `readonly` **statement**: [`Statement`](Statement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1587

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/LanguageService.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / LanguageService

# Interface: LanguageService

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6270

## Methods

### applyCodeActionCommand()

#### Call Signature

> **applyCodeActionCommand**(`action`, `formatSettings?`): `Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6411

##### Parameters

###### action

[`InstallPackageAction`](InstallPackageAction.md)

###### formatSettings?

[`FormatCodeSettings`](FormatCodeSettings.md)

##### Returns

`Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)\>

#### Call Signature

> **applyCodeActionCommand**(`action`, `formatSettings?`): `Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)[]\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6412

##### Parameters

###### action

[`InstallPackageAction`](InstallPackageAction.md)[]

###### formatSettings?

[`FormatCodeSettings`](FormatCodeSettings.md)

##### Returns

`Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)[]\>

#### Call Signature

> **applyCodeActionCommand**(`action`, `formatSettings?`): `Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md) \| [`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)[]\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6413

##### Parameters

###### action

[`InstallPackageAction`](InstallPackageAction.md) | [`InstallPackageAction`](InstallPackageAction.md)[]

###### formatSettings?

[`FormatCodeSettings`](FormatCodeSettings.md)

##### Returns

`Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md) \| [`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)[]\>

#### Call Signature

> **applyCodeActionCommand**(`fileName`, `action`): `Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6415

##### Parameters

###### fileName

`string`

###### action

[`InstallPackageAction`](InstallPackageAction.md)

##### Returns

`Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)\>

##### Deprecated

`fileName` will be ignored

#### Call Signature

> **applyCodeActionCommand**(`fileName`, `action`): `Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)[]\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6417

##### Parameters

###### fileName

`string`

###### action

[`InstallPackageAction`](InstallPackageAction.md)[]

##### Returns

`Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)[]\>

##### Deprecated

`fileName` will be ignored

#### Call Signature

> **applyCodeActionCommand**(`fileName`, `action`): `Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md) \| [`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)[]\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6419

##### Parameters

###### fileName

`string`

###### action

[`InstallPackageAction`](InstallPackageAction.md) | [`InstallPackageAction`](InstallPackageAction.md)[]

##### Returns

`Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md) \| [`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)[]\>

##### Deprecated

`fileName` will be ignored

***

### cleanupSemanticCache()

> **cleanupSemanticCache**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6272

This is used as a part of restarting the language service.

#### Returns

`void`

***

### commentSelection()

> **commentSelection**(`fileName`, `textRange`): [`TextChange`](TextChange.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6429

#### Parameters

##### fileName

`string`

##### textRange

[`TextRange`](TextRange.md)

#### Returns

[`TextChange`](TextChange.md)[]

***

### dispose()

> **dispose**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6431

#### Returns

`void`

***

### findReferences()

> **findReferences**(`fileName`, `position`): `undefined` \| [`ReferencedSymbol`](ReferencedSymbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6381

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

`undefined` \| [`ReferencedSymbol`](ReferencedSymbol.md)[]

***

### findRenameLocations()

> **findRenameLocations**(`fileName`, `position`, `findInStrings`, `findInComments`, `providePrefixAndSuffixTextForRename?`): `undefined` \| readonly [`RenameLocation`](RenameLocation.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6374

#### Parameters

##### fileName

`string`

##### position

`number`

##### findInStrings

`boolean`

##### findInComments

`boolean`

##### providePrefixAndSuffixTextForRename?

`boolean`

#### Returns

`undefined` \| readonly [`RenameLocation`](RenameLocation.md)[]

***

### getApplicableRefactors()

> **getApplicableRefactors**(`fileName`, `positionOrRange`, `preferences`, `triggerReason?`, `kind?`): [`ApplicableRefactorInfo`](ApplicableRefactorInfo.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6420

#### Parameters

##### fileName

`string`

##### positionOrRange

`number` | [`TextRange`](TextRange.md)

##### preferences

`undefined` | [`UserPreferences`](UserPreferences.md)

##### triggerReason?

[`RefactorTriggerReason`](../type-aliases/RefactorTriggerReason.md)

##### kind?

`string`

#### Returns

[`ApplicableRefactorInfo`](ApplicableRefactorInfo.md)[]

***

### getBraceMatchingAtPosition()

> **getBraceMatchingAtPosition**(`fileName`, `position`): [`TextSpan`](TextSpan.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6395

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

[`TextSpan`](TextSpan.md)[]

***

### getBreakpointStatementAtPosition()

> **getBreakpointStatementAtPosition**(`fileName`, `position`): `undefined` \| [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6369

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

`undefined` \| [`TextSpan`](TextSpan.md)

***

### getBuilderProgram()

> **getBuilderProgram**(): `undefined` \| [`BuilderProgram`](BuilderProgram.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6426

#### Returns

`undefined` \| [`BuilderProgram`](BuilderProgram.md)

***

### getCodeFixesAtPosition()

> **getCodeFixesAtPosition**(`fileName`, `start`, `end`, `errorCodes`, `formatOptions`, `preferences`): readonly [`CodeFixAction`](CodeFixAction.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6409

#### Parameters

##### fileName

`string`

##### start

`number`

##### end

`number`

##### errorCodes

readonly `number`[]

##### formatOptions

[`FormatCodeSettings`](FormatCodeSettings.md)

##### preferences

[`UserPreferences`](UserPreferences.md)

#### Returns

readonly [`CodeFixAction`](CodeFixAction.md)[]

***

### getCombinedCodeFix()

> **getCombinedCodeFix**(`scope`, `fixId`, `formatOptions`, `preferences`): [`CombinedCodeActions`](CombinedCodeActions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6410

#### Parameters

##### scope

[`CombinedCodeFixScope`](CombinedCodeFixScope.md)

##### fixId

##### formatOptions

[`FormatCodeSettings`](FormatCodeSettings.md)

##### preferences

[`UserPreferences`](UserPreferences.md)

#### Returns

[`CombinedCodeActions`](CombinedCodeActions.md)

***

### getCompilerOptionsDiagnostics()

> **getCompilerOptionsDiagnostics**(): [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6318

Gets global diagnostics related to the program configuration and compiler options.

#### Returns

[`Diagnostic`](Diagnostic.md)[]

***

### getCompletionEntryDetails()

> **getCompletionEntryDetails**(`fileName`, `position`, `entryName`, `formatOptions`, `source`, `preferences`, `data`): `undefined` \| [`CompletionEntryDetails`](CompletionEntryDetails.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6358

Gets the extended details for a completion entry retrieved from `getCompletionsAtPosition`.

#### Parameters

##### fileName

`string`

The path to the file

##### position

`number`

A zero based index of the character where you want the entries

##### entryName

`string`

The `name` from an existing completion which came from `getCompletionsAtPosition`

##### formatOptions

How should code samples in the completions be formatted, can be undefined for backwards compatibility

`undefined` | [`FormatCodeSettings`](FormatCodeSettings.md) | [`FormatCodeOptions`](FormatCodeOptions.md)

##### source

`source` property from the completion entry

`undefined` | `string`

##### preferences

User settings, can be undefined for backwards compatibility

`undefined` | [`UserPreferences`](UserPreferences.md)

##### data

`data` property from the completion entry

`undefined` | [`CompletionEntryData`](../type-aliases/CompletionEntryData.md)

#### Returns

`undefined` \| [`CompletionEntryDetails`](CompletionEntryDetails.md)

***

### getCompletionEntrySymbol()

> **getCompletionEntrySymbol**(`fileName`, `position`, `name`, `source`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6359

#### Parameters

##### fileName

`string`

##### position

`number`

##### name

`string`

##### source

`undefined` | `string`

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

***

### getCompletionsAtPosition()

> **getCompletionsAtPosition**(`fileName`, `position`, `options`, `formattingSettings?`): `undefined` \| [`WithMetadata`](../type-aliases/WithMetadata.md)\<[`CompletionInfo`](CompletionInfo.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6346

Gets completion entries at a particular position in a file.

#### Parameters

##### fileName

`string`

The path to the file

##### position

`number`

A zero-based index of the character where you want the entries

##### options

An object describing how the request was triggered and what kinds
of code actions can be returned with the completions.

`undefined` | [`GetCompletionsAtPositionOptions`](GetCompletionsAtPositionOptions.md)

##### formattingSettings?

[`FormatCodeSettings`](FormatCodeSettings.md)

settings needed for calling formatting functions.

#### Returns

`undefined` \| [`WithMetadata`](../type-aliases/WithMetadata.md)\<[`CompletionInfo`](CompletionInfo.md)\>

***

### getDefinitionAndBoundSpan()

> **getDefinitionAndBoundSpan**(`fileName`, `position`): `undefined` \| [`DefinitionInfoAndBoundSpan`](DefinitionInfoAndBoundSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6377

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

`undefined` \| [`DefinitionInfoAndBoundSpan`](DefinitionInfoAndBoundSpan.md)

***

### getDefinitionAtPosition()

> **getDefinitionAtPosition**(`fileName`, `position`): `undefined` \| readonly [`DefinitionInfo`](DefinitionInfo.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6376

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

`undefined` \| readonly [`DefinitionInfo`](DefinitionInfo.md)[]

***

### getDocCommentTemplateAtPosition()

> **getDocCommentTemplateAtPosition**(`fileName`, `position`, `options?`): `undefined` \| [`TextInsertion`](TextInsertion.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6400

#### Parameters

##### fileName

`string`

##### position

`number`

##### options?

[`DocCommentTemplateOptions`](DocCommentTemplateOptions.md)

#### Returns

`undefined` \| [`TextInsertion`](TextInsertion.md)

***

### getDocumentHighlights()

> **getDocumentHighlights**(`fileName`, `position`, `filesToSearch`): `undefined` \| [`DocumentHighlights`](DocumentHighlights.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6382

#### Parameters

##### fileName

`string`

##### position

`number`

##### filesToSearch

`string`[]

#### Returns

`undefined` \| [`DocumentHighlights`](DocumentHighlights.md)[]

***

### getEditsForFileRename()

> **getEditsForFileRename**(`oldFilePath`, `newFilePath`, `formatOptions`, `preferences`): readonly [`FileTextChanges`](FileTextChanges.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6423

#### Parameters

##### oldFilePath

`string`

##### newFilePath

`string`

##### formatOptions

[`FormatCodeSettings`](FormatCodeSettings.md)

##### preferences

`undefined` | [`UserPreferences`](UserPreferences.md)

#### Returns

readonly [`FileTextChanges`](FileTextChanges.md)[]

***

### getEditsForRefactor()

> **getEditsForRefactor**(`fileName`, `formatOptions`, `positionOrRange`, `refactorName`, `actionName`, `preferences`): `undefined` \| [`RefactorEditInfo`](RefactorEditInfo.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6421

#### Parameters

##### fileName

`string`

##### formatOptions

[`FormatCodeSettings`](FormatCodeSettings.md)

##### positionOrRange

`number` | [`TextRange`](TextRange.md)

##### refactorName

`string`

##### actionName

`string`

##### preferences

`undefined` | [`UserPreferences`](UserPreferences.md)

#### Returns

`undefined` \| [`RefactorEditInfo`](RefactorEditInfo.md)

***

### getEmitOutput()

> **getEmitOutput**(`fileName`, `emitOnlyDtsFiles?`, `forceDtsEmit?`): [`EmitOutput`](EmitOutput.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6424

#### Parameters

##### fileName

`string`

##### emitOnlyDtsFiles?

`boolean`

##### forceDtsEmit?

`boolean`

#### Returns

[`EmitOutput`](EmitOutput.md)

***

### getEncodedSemanticClassifications()

> **getEncodedSemanticClassifications**(`fileName`, `span`, `format?`): [`Classifications`](Classifications.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6336

Gets semantic highlights information for a particular file. Has two formats, an older
version used by VS and a format used by VS Code.

#### Parameters

##### fileName

`string`

The path to the file

##### span

[`TextSpan`](TextSpan.md)

##### format?

[`SemanticClassificationFormat`](../enumerations/SemanticClassificationFormat.md)

Which format to use, defaults to "original"

#### Returns

[`Classifications`](Classifications.md)

a number array encoded as triples of [start, length, ClassificationType, ...].

***

### getEncodedSyntacticClassifications()

> **getEncodedSyntacticClassifications**(`fileName`, `span`): [`Classifications`](Classifications.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6326

Encoded as triples of [start, length, ClassificationType].

#### Parameters

##### fileName

`string`

##### span

[`TextSpan`](TextSpan.md)

#### Returns

[`Classifications`](Classifications.md)

***

### getFileReferences()

> **getFileReferences**(`fileName`): [`ReferenceEntry`](ReferenceEntry.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6383

#### Parameters

##### fileName

`string`

#### Returns

[`ReferenceEntry`](ReferenceEntry.md)[]

***

### getFormattingEditsAfterKeystroke()

> **getFormattingEditsAfterKeystroke**(`fileName`, `position`, `key`, `options`): [`TextChange`](TextChange.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6399

#### Parameters

##### fileName

`string`

##### position

`number`

##### key

`string`

##### options

[`FormatCodeSettings`](FormatCodeSettings.md) | [`FormatCodeOptions`](FormatCodeOptions.md)

#### Returns

[`TextChange`](TextChange.md)[]

***

### getFormattingEditsForDocument()

> **getFormattingEditsForDocument**(`fileName`, `options`): [`TextChange`](TextChange.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6398

#### Parameters

##### fileName

`string`

##### options

[`FormatCodeSettings`](FormatCodeSettings.md) | [`FormatCodeOptions`](FormatCodeOptions.md)

#### Returns

[`TextChange`](TextChange.md)[]

***

### getFormattingEditsForRange()

> **getFormattingEditsForRange**(`fileName`, `start`, `end`, `options`): [`TextChange`](TextChange.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6397

#### Parameters

##### fileName

`string`

##### start

`number`

##### end

`number`

##### options

[`FormatCodeSettings`](FormatCodeSettings.md) | [`FormatCodeOptions`](FormatCodeOptions.md)

#### Returns

[`TextChange`](TextChange.md)[]

***

### getImplementationAtPosition()

> **getImplementationAtPosition**(`fileName`, `position`): `undefined` \| readonly [`ImplementationLocation`](ImplementationLocation.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6379

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

`undefined` \| readonly [`ImplementationLocation`](ImplementationLocation.md)[]

***

### getIndentationAtPosition()

> **getIndentationAtPosition**(`fileName`, `position`, `options`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6396

#### Parameters

##### fileName

`string`

##### position

`number`

##### options

[`EditorSettings`](EditorSettings.md) | [`EditorOptions`](EditorOptions.md)

#### Returns

`number`

***

### getJsxClosingTagAtPosition()

> **getJsxClosingTagAtPosition**(`fileName`, `position`): `undefined` \| [`JsxClosingTagInfo`](JsxClosingTagInfo.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6406

This will return a defined result if the position is after the `>` of the opening tag, or somewhere in the text, of a JSXElement with no closing tag.
Editors should call this after `>` is typed.

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

`undefined` \| [`JsxClosingTagInfo`](JsxClosingTagInfo.md)

***

### getNameOrDottedNameSpan()

> **getNameOrDottedNameSpan**(`fileName`, `startPos`, `endPos`): `undefined` \| [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6368

#### Parameters

##### fileName

`string`

##### startPos

`number`

##### endPos

`number`

#### Returns

`undefined` \| [`TextSpan`](TextSpan.md)

***

### getNavigateToItems()

> **getNavigateToItems**(`searchValue`, `maxResultCount?`, `fileName?`, `excludeDtsFiles?`): [`NavigateToItem`](NavigateToItem.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6386

#### Parameters

##### searchValue

`string`

##### maxResultCount?

`number`

##### fileName?

`string`

##### excludeDtsFiles?

`boolean`

#### Returns

[`NavigateToItem`](NavigateToItem.md)[]

***

### getNavigationBarItems()

> **getNavigationBarItems**(`fileName`): [`NavigationBarItem`](NavigationBarItem.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6387

#### Parameters

##### fileName

`string`

#### Returns

[`NavigationBarItem`](NavigationBarItem.md)[]

***

### getNavigationTree()

> **getNavigationTree**(`fileName`): [`NavigationTree`](NavigationTree.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6388

#### Parameters

##### fileName

`string`

#### Returns

[`NavigationTree`](NavigationTree.md)

***

### ~~getOccurrencesAtPosition()~~

> **getOccurrencesAtPosition**(`fileName`, `position`): `undefined` \| readonly [`ReferenceEntry`](ReferenceEntry.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6385

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

`undefined` \| readonly [`ReferenceEntry`](ReferenceEntry.md)[]

#### Deprecated

***

### getOutliningSpans()

> **getOutliningSpans**(`fileName`): [`OutliningSpan`](OutliningSpan.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6393

#### Parameters

##### fileName

`string`

#### Returns

[`OutliningSpan`](OutliningSpan.md)[]

***

### getProgram()

> **getProgram**(): `undefined` \| [`Program`](Program.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6425

#### Returns

`undefined` \| [`Program`](Program.md)

***

### getProps()?

> `optional` **getProps**(): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6433

#### Returns

`string`[]

***

### getQuickInfoAtPosition()

> **getQuickInfoAtPosition**(`fileName`, `position`): `undefined` \| [`QuickInfo`](QuickInfo.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6367

Gets semantic information about the identifier at a particular position in a
file. Quick info is what you typically see when you hover in an editor.

#### Parameters

##### fileName

`string`

The path to the file

##### position

`number`

A zero-based index of the character where you want the quick info

#### Returns

`undefined` \| [`QuickInfo`](QuickInfo.md)

***

### getReferencesAtPosition()

> **getReferencesAtPosition**(`fileName`, `position`): `undefined` \| [`ReferenceEntry`](ReferenceEntry.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6380

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

`undefined` \| [`ReferenceEntry`](ReferenceEntry.md)[]

***

### getRenameInfo()

#### Call Signature

> **getRenameInfo**(`fileName`, `position`, `preferences`): [`RenameInfo`](../type-aliases/RenameInfo.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6371

##### Parameters

###### fileName

`string`

###### position

`number`

###### preferences

[`UserPreferences`](UserPreferences.md)

##### Returns

[`RenameInfo`](../type-aliases/RenameInfo.md)

#### Call Signature

> **getRenameInfo**(`fileName`, `position`, `options?`): [`RenameInfo`](../type-aliases/RenameInfo.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6373

##### Parameters

###### fileName

`string`

###### position

`number`

###### options?

[`RenameInfoOptions`](RenameInfoOptions.md)

##### Returns

[`RenameInfo`](../type-aliases/RenameInfo.md)

##### Deprecated

Use the signature with `UserPreferences` instead.

***

### getSemanticClassifications()

#### Call Signature

> **getSemanticClassifications**(`fileName`, `span`): [`ClassifiedSpan`](ClassifiedSpan.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6323

##### Parameters

###### fileName

`string`

###### span

[`TextSpan`](TextSpan.md)

##### Returns

[`ClassifiedSpan`](ClassifiedSpan.md)[]

##### Deprecated

Use getEncodedSemanticClassifications instead.

#### Call Signature

> **getSemanticClassifications**(`fileName`, `span`, `format`): [`ClassifiedSpan`](ClassifiedSpan.md)[] \| [`ClassifiedSpan2020`](ClassifiedSpan2020.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6324

##### Parameters

###### fileName

`string`

###### span

[`TextSpan`](TextSpan.md)

###### format

[`SemanticClassificationFormat`](../enumerations/SemanticClassificationFormat.md)

##### Returns

[`ClassifiedSpan`](ClassifiedSpan.md)[] \| [`ClassifiedSpan2020`](ClassifiedSpan2020.md)[]

***

### getSemanticDiagnostics()

> **getSemanticDiagnostics**(`fileName`): [`Diagnostic`](Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6306

Gets warnings or errors indicating type system issues in a given file.
Requesting semantic diagnostics may start up the type system and
run deferred work, so the first call may take longer than subsequent calls.

Unlike the other get*Diagnostics functions, these diagnostics can potentially not
include a reference to a source file. Specifically, the first time this is called,
it will return global diagnostics with no associated location.

To contrast the differences between semantic and syntactic diagnostics, consider the
sentence: "The sun is green." is syntactically correct; those are real English words with
correct sentence structure. However, it is semantically invalid, because it is not true.

#### Parameters

##### fileName

`string`

A path to the file you want semantic diagnostics for

#### Returns

[`Diagnostic`](Diagnostic.md)[]

***

### getSignatureHelpItems()

> **getSignatureHelpItems**(`fileName`, `position`, `options`): `undefined` \| [`SignatureHelpItems`](SignatureHelpItems.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6370

#### Parameters

##### fileName

`string`

##### position

`number`

##### options

`undefined` | [`SignatureHelpItemsOptions`](SignatureHelpItemsOptions.md)

#### Returns

`undefined` \| [`SignatureHelpItems`](SignatureHelpItems.md)

***

### getSmartSelectionRange()

> **getSmartSelectionRange**(`fileName`, `position`): [`SelectionRange`](SelectionRange.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6375

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

[`SelectionRange`](SelectionRange.md)

***

### getSpanOfEnclosingComment()

> **getSpanOfEnclosingComment**(`fileName`, `position`, `onlyMultiLine`): `undefined` \| [`TextSpan`](TextSpan.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6407

#### Parameters

##### fileName

`string`

##### position

`number`

##### onlyMultiLine

`boolean`

#### Returns

`undefined` \| [`TextSpan`](TextSpan.md)

***

### getSuggestionDiagnostics()

> **getSuggestionDiagnostics**(`fileName`): [`DiagnosticWithLocation`](DiagnosticWithLocation.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6314

Gets suggestion diagnostics for a specific file. These diagnostics tend to
proactively suggest refactors, as opposed to diagnostics that indicate
potentially incorrect runtime behavior.

#### Parameters

##### fileName

`string`

A path to the file you want semantic diagnostics for

#### Returns

[`DiagnosticWithLocation`](DiagnosticWithLocation.md)[]

***

### getSyntacticClassifications()

#### Call Signature

> **getSyntacticClassifications**(`fileName`, `span`): [`ClassifiedSpan`](ClassifiedSpan.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6320

##### Parameters

###### fileName

`string`

###### span

[`TextSpan`](TextSpan.md)

##### Returns

[`ClassifiedSpan`](ClassifiedSpan.md)[]

##### Deprecated

Use getEncodedSyntacticClassifications instead.

#### Call Signature

> **getSyntacticClassifications**(`fileName`, `span`, `format`): [`ClassifiedSpan`](ClassifiedSpan.md)[] \| [`ClassifiedSpan2020`](ClassifiedSpan2020.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6321

##### Parameters

###### fileName

`string`

###### span

[`TextSpan`](TextSpan.md)

###### format

[`SemanticClassificationFormat`](../enumerations/SemanticClassificationFormat.md)

##### Returns

[`ClassifiedSpan`](ClassifiedSpan.md)[] \| [`ClassifiedSpan2020`](ClassifiedSpan2020.md)[]

***

### getSyntacticDiagnostics()

> **getSyntacticDiagnostics**(`fileName`): [`DiagnosticWithLocation`](DiagnosticWithLocation.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6290

Gets errors indicating invalid syntax in a file.

In English, "this cdeo have, erorrs" is syntactically invalid because it has typos,
grammatical errors, and misplaced punctuation. Likewise, examples of syntax
errors in TypeScript are missing parentheses in an `if` statement, mismatched
curly braces, and using a reserved keyword as a variable name.

These diagnostics are inexpensive to compute and don't require knowledge of
other files. Note that a non-empty result increases the likelihood of false positives
from `getSemanticDiagnostics`.

While these represent the majority of syntax-related diagnostics, there are some
that require the type system, which will be present in `getSemanticDiagnostics`.

#### Parameters

##### fileName

`string`

A path to the file you want syntactic diagnostics for

#### Returns

[`DiagnosticWithLocation`](DiagnosticWithLocation.md)[]

***

### getTodoComments()

> **getTodoComments**(`fileName`, `descriptors`): [`TodoComment`](TodoComment.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6394

#### Parameters

##### fileName

`string`

##### descriptors

[`TodoCommentDescriptor`](TodoCommentDescriptor.md)[]

#### Returns

[`TodoComment`](TodoComment.md)[]

***

### getTypeDefinitionAtPosition()

> **getTypeDefinitionAtPosition**(`fileName`, `position`): `undefined` \| readonly [`DefinitionInfo`](DefinitionInfo.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6378

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

`undefined` \| readonly [`DefinitionInfo`](DefinitionInfo.md)[]

***

### isValidBraceCompletionAtPosition()

> **isValidBraceCompletionAtPosition**(`fileName`, `position`, `openingBrace`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6401

#### Parameters

##### fileName

`string`

##### position

`number`

##### openingBrace

`number`

#### Returns

`boolean`

***

### organizeImports()

> **organizeImports**(`args`, `formatOptions`, `preferences`): readonly [`FileTextChanges`](FileTextChanges.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6422

#### Parameters

##### args

[`OrganizeImportsArgs`](OrganizeImportsArgs.md)

##### formatOptions

[`FormatCodeSettings`](FormatCodeSettings.md)

##### preferences

`undefined` | [`UserPreferences`](UserPreferences.md)

#### Returns

readonly [`FileTextChanges`](FileTextChanges.md)[]

***

### prepareCallHierarchy()

> **prepareCallHierarchy**(`fileName`, `position`): `undefined` \| [`CallHierarchyItem`](CallHierarchyItem.md) \| [`CallHierarchyItem`](CallHierarchyItem.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6389

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

`undefined` \| [`CallHierarchyItem`](CallHierarchyItem.md) \| [`CallHierarchyItem`](CallHierarchyItem.md)[]

***

### provideCallHierarchyIncomingCalls()

> **provideCallHierarchyIncomingCalls**(`fileName`, `position`): [`CallHierarchyIncomingCall`](CallHierarchyIncomingCall.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6390

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

[`CallHierarchyIncomingCall`](CallHierarchyIncomingCall.md)[]

***

### provideCallHierarchyOutgoingCalls()

> **provideCallHierarchyOutgoingCalls**(`fileName`, `position`): [`CallHierarchyOutgoingCall`](CallHierarchyOutgoingCall.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6391

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

[`CallHierarchyOutgoingCall`](CallHierarchyOutgoingCall.md)[]

***

### provideInlayHints()

> **provideInlayHints**(`fileName`, `span`, `preferences`): [`InlayHint`](InlayHint.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6392

#### Parameters

##### fileName

`string`

##### span

[`TextSpan`](TextSpan.md)

##### preferences

`undefined` | [`UserPreferences`](UserPreferences.md)

#### Returns

[`InlayHint`](InlayHint.md)[]

***

### toggleLineComment()

> **toggleLineComment**(`fileName`, `textRange`): [`TextChange`](TextChange.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6427

#### Parameters

##### fileName

`string`

##### textRange

[`TextRange`](TextRange.md)

#### Returns

[`TextChange`](TextChange.md)[]

***

### toggleMultilineComment()

> **toggleMultilineComment**(`fileName`, `textRange`): [`TextChange`](TextChange.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6428

#### Parameters

##### fileName

`string`

##### textRange

[`TextRange`](TextRange.md)

#### Returns

[`TextChange`](TextChange.md)[]

***

### toLineColumnOffset()?

> `optional` **toLineColumnOffset**(`fileName`, `position`): [`LineAndCharacter`](LineAndCharacter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6408

#### Parameters

##### fileName

`string`

##### position

`number`

#### Returns

[`LineAndCharacter`](LineAndCharacter.md)

***

### uncommentSelection()

> **uncommentSelection**(`fileName`, `textRange`): [`TextChange`](TextChange.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6430

#### Parameters

##### fileName

`string`

##### textRange

[`TextRange`](TextRange.md)

#### Returns

[`TextChange`](TextChange.md)[]

***

### updateRootFiles()?

> `optional` **updateRootFiles**(`rootFiles`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6432

#### Parameters

##### rootFiles

`string`[]

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/LanguageServiceHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / LanguageServiceHost

# Interface: LanguageServiceHost

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6222

Used by services to specify the minimum host area required to set up source files under any compilation settings

## Extends

- [`GetEffectiveTypeRootsHost`](GetEffectiveTypeRootsHost.md).[`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md)

## Properties

### shouldCompletionSortCustom?

> `optional` **shouldCompletionSortCustom**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6259

***

### uiProps?

> `optional` **uiProps**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6260

## Methods

### clearProps()?

> `optional` **clearProps**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6261

#### Returns

`void`

***

### directoryExists()?

> `optional` **directoryExists**(`directoryName`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4337

#### Parameters

##### directoryName

`string`

#### Returns

`boolean`

#### Inherited from

[`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md).[`directoryExists`](MinimalResolutionCacheHost.md#directoryexists)

***

### error()?

> `optional` **error**(`s`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6237

#### Parameters

##### s

`string`

#### Returns

`void`

***

### fileExists()

> **fileExists**(`path`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6242

#### Parameters

##### path

`string`

#### Returns

`boolean`

#### Overrides

[`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md).[`fileExists`](MinimalResolutionCacheHost.md#fileexists)

***

### getCancellationToken()?

> `optional` **getCancellationToken**(): [`HostCancellationToken`](HostCancellationToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6232

#### Returns

[`HostCancellationToken`](HostCancellationToken.md)

***

### getCompilationSettings()

> **getCompilationSettings**(): [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6223

#### Returns

[`CompilerOptions`](CompilerOptions.md)

#### Overrides

[`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md).[`getCompilationSettings`](MinimalResolutionCacheHost.md#getcompilationsettings)

***

### getCompilerHost()?

> `optional` **getCompilerHost**(): `undefined` \| [`CompilerHost`](CompilerHost.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3361

#### Returns

`undefined` \| [`CompilerHost`](CompilerHost.md)

#### Inherited from

[`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md).[`getCompilerHost`](MinimalResolutionCacheHost.md#getcompilerhost)

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6233

#### Returns

`string`

#### Overrides

[`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md).[`getCurrentDirectory`](MinimalResolutionCacheHost.md#getcurrentdirectory)

***

### getCustomTransformers()?

> `optional` **getCustomTransformers**(): `undefined` \| [`CustomTransformers`](CustomTransformers.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6251

Gets a set of custom transformers to use during emit.

#### Returns

`undefined` \| [`CustomTransformers`](CustomTransformers.md)

***

### getDefaultLibFileName()

> **getDefaultLibFileName**(`options`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6234

#### Parameters

##### options

[`CompilerOptions`](CompilerOptions.md)

#### Returns

`string`

***

### getDirectories()?

> `optional` **getDirectories**(`directoryName`): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6247

#### Parameters

##### directoryName

`string`

#### Returns

`string`[]

#### Overrides

[`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md).[`getDirectories`](MinimalResolutionCacheHost.md#getdirectories)

***

### getFileCheckedModuleInfo()?

> `optional` **getFileCheckedModuleInfo**(`containFilePath`): [`FileCheckModuleInfo`](FileCheckModuleInfo.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6258

#### Parameters

##### containFilePath

`string`

#### Returns

[`FileCheckModuleInfo`](FileCheckModuleInfo.md)

#### Overrides

[`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md).[`getFileCheckedModuleInfo`](MinimalResolutionCacheHost.md#getfilecheckedmoduleinfo)

***

### getJsDocNodeCheckedConfig()?

> `optional` **getJsDocNodeCheckedConfig**(`jsDocFileCheckInfo`, `symbolSourceFilePath`): [`JsDocNodeCheckConfig`](JsDocNodeCheckConfig.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6256

#### Parameters

##### jsDocFileCheckInfo

[`FileCheckModuleInfo`](FileCheckModuleInfo.md)

##### symbolSourceFilePath

`string`

#### Returns

[`JsDocNodeCheckConfig`](JsDocNodeCheckConfig.md)

#### Overrides

[`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md).[`getJsDocNodeCheckedConfig`](MinimalResolutionCacheHost.md#getjsdocnodecheckedconfig)

***

### getJsDocNodeConditionCheckedResult()?

> `optional` **getJsDocNodeConditionCheckedResult**(`jsDocFileCheckedInfo`, `jsDocs`): [`ConditionCheckResult`](ConditionCheckResult.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6257

#### Parameters

##### jsDocFileCheckedInfo

[`FileCheckModuleInfo`](FileCheckModuleInfo.md)

##### jsDocs

[`JsDocTagInfo`](JsDocTagInfo.md)[]

#### Returns

[`ConditionCheckResult`](ConditionCheckResult.md)

#### Overrides

[`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md).[`getJsDocNodeConditionCheckedResult`](MinimalResolutionCacheHost.md#getjsdocnodeconditioncheckedresult)

***

### getLocalizedDiagnosticMessages()?

> `optional` **getLocalizedDiagnosticMessages**(): `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6231

#### Returns

`any`

***

### getNewLine()?

> `optional` **getNewLine**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6224

#### Returns

`string`

***

### getParsedCommandLine()?

> `optional` **getParsedCommandLine**(`fileName`): `undefined` \| [`ParsedCommandLine`](ParsedCommandLine.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6255

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| [`ParsedCommandLine`](ParsedCommandLine.md)

***

### getProjectReferences()?

> `optional` **getProjectReferences**(): `undefined` \| readonly [`ProjectReference`](ProjectReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6230

#### Returns

`undefined` \| readonly [`ProjectReference`](ProjectReference.md)[]

***

### getProjectVersion()?

> `optional` **getProjectVersion**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6225

#### Returns

`string`

***

### getResolvedModuleWithFailedLookupLocationsFromCache()?

> `optional` **getResolvedModuleWithFailedLookupLocationsFromCache**(`modulename`, `containingFile`, `resolutionMode?`): `undefined` \| [`ResolvedModuleWithFailedLookupLocations`](ResolvedModuleWithFailedLookupLocations.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6245

#### Parameters

##### modulename

`string`

##### containingFile

`string`

##### resolutionMode?

[`CommonJS`](../enumerations/ModuleKind.md#commonjs) | [`ESNext`](../enumerations/ModuleKind.md#esnext)

#### Returns

`undefined` \| [`ResolvedModuleWithFailedLookupLocations`](ResolvedModuleWithFailedLookupLocations.md)

***

### getScriptFileNames()

> **getScriptFileNames**(): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6226

#### Returns

`string`[]

***

### getScriptKind()?

> `optional` **getScriptKind**(`fileName`): [`ScriptKind`](../enumerations/ScriptKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6227

#### Parameters

##### fileName

`string`

#### Returns

[`ScriptKind`](../enumerations/ScriptKind.md)

***

### getScriptSnapshot()

> **getScriptSnapshot**(`fileName`): `undefined` \| [`IScriptSnapshot`](IScriptSnapshot.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6229

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| [`IScriptSnapshot`](IScriptSnapshot.md)

***

### getScriptVersion()

> **getScriptVersion**(`fileName`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6228

#### Parameters

##### fileName

`string`

#### Returns

`string`

***

### getTypeRootsVersion()?

> `optional` **getTypeRootsVersion**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6243

#### Returns

`number`

***

### installPackage()?

> `optional` **installPackage**(`options`): `Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6253

#### Parameters

##### options

[`InstallPackageOptions`](InstallPackageOptions.md)

#### Returns

`Promise`\<[`ApplyCodeActionCommandResult`](ApplyCodeActionCommandResult.md)\>

***

### isKnownTypesPackageName()?

> `optional` **isKnownTypesPackageName**(`name`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6252

#### Parameters

##### name

`string`

#### Returns

`boolean`

***

### log()?

> `optional` **log**(`s`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6235

#### Parameters

##### s

`string`

#### Returns

`void`

***

### readDirectory()?

> `optional` **readDirectory**(`path`, `extensions?`, `exclude?`, `include?`, `depth?`): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6239

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6241

#### Parameters

##### path

`string`

##### encoding?

`string`

#### Returns

`undefined` \| `string`

#### Overrides

[`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md).[`readFile`](MinimalResolutionCacheHost.md#readfile)

***

### realpath()?

> `optional` **realpath**(`path`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6240

Resolve a symbolic link.

#### Parameters

##### path

`string`

#### Returns

`string`

#### See

https://nodejs.org/api/fs.html#fs_fs_realpathsync_path_options

#### Overrides

[`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md).[`realpath`](MinimalResolutionCacheHost.md#realpath)

***

### resolveModuleNames()?

> `optional` **resolveModuleNames**(`moduleNames`, `containingFile`, `reusedNames`, `redirectedReference`, `options`, `containingSourceFile?`): (`undefined` \| [`ResolvedModule`](ResolvedModule.md))[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6244

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

> `optional` **resolveTypeReferenceDirectives**(`typeDirectiveNames`, `containingFile`, `redirectedReference`, `options`, `containingFileMode?`): (`undefined` \| [`ResolvedTypeReferenceDirective`](ResolvedTypeReferenceDirective.md))[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6246

#### Parameters

##### typeDirectiveNames

`string`[] | [`FileReference`](FileReference.md)[]

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6236

#### Parameters

##### s

`string`

#### Returns

`void`

#### Overrides

[`MinimalResolutionCacheHost`](MinimalResolutionCacheHost.md).[`trace`](MinimalResolutionCacheHost.md#trace)

***

### useCaseSensitiveFileNames()?

> `optional` **useCaseSensitiveFileNames**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6238

#### Returns

`boolean`

#### Overrides

`MinimalResolutionCacheHost.useCaseSensitiveFileNames`

***

### writeFile()?

> `optional` **writeFile**(`fileName`, `content`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6254

#### Parameters

##### fileName

`string`

##### content

`string`

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/LeftHandSideExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / LeftHandSideExpression

# Interface: LeftHandSideExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1085

## Extends

- [`UpdateExpression`](UpdateExpression.md)

## Extended by

- [`PartiallyEmittedExpression`](PartiallyEmittedExpression.md)
- [`MemberExpression`](MemberExpression.md)
- [`CallExpression`](CallExpression.md)
- [`NonNullExpression`](NonNullExpression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`UpdateExpression`](UpdateExpression.md).[`_expressionBrand`](UpdateExpression.md#_expressionbrand)

***

### \_leftHandSideExpressionBrand

> **\_leftHandSideExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1086

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

> `readonly` **kind**: [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:598

#### Inherited from

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/LineAndCharacter.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / LineAndCharacter

# Interface: LineAndCharacter

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3276

## Properties

### character

> **character**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3279

***

### line

> **line**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3278

0-based.




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/LiteralExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / LiteralExpression

# Interface: LiteralExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1226

## Extends

- [`LiteralLikeNode`](LiteralLikeNode.md).[`PrimaryExpression`](PrimaryExpression.md)

## Extended by

- [`StringLiteral`](StringLiteral.md)
- [`RegularExpressionLiteral`](RegularExpressionLiteral.md)
- [`NoSubstitutionTemplateLiteral`](NoSubstitutionTemplateLiteral.md)
- [`NumericLiteral`](NumericLiteral.md)
- [`BigIntLiteral`](BigIntLiteral.md)

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

### \_literalExpressionBrand

> **\_literalExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1227

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/LiteralLikeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / LiteralLikeNode

# Interface: LiteralLikeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1218

## Extends

- [`Node`](Node.md)

## Extended by

- [`TemplateLiteralLikeNode`](TemplateLiteralLikeNode.md)
- [`LiteralExpression`](LiteralExpression.md)
- [`JsxText`](JsxText.md)

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

### hasExtendedUnicodeEscape?

> `optional` **hasExtendedUnicodeEscape**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1221

***

### isUnterminated?

> `optional` **isUnterminated**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1220

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

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1219

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/LiteralType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / LiteralType

# Interface: LiteralType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2776

## Extends

- [`Type`](Type.md)

## Extended by

- [`StringLiteralType`](StringLiteralType.md)
- [`NumberLiteralType`](NumberLiteralType.md)
- [`BigIntLiteralType`](BigIntLiteralType.md)

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

### freshType

> **freshType**: `LiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2778

***

### pattern?

> `optional` **pattern**: [`DestructuringPattern`](../type-aliases/DestructuringPattern.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2772

#### Inherited from

[`Type`](Type.md).[`pattern`](Type.md#pattern)

***

### regularType

> **regularType**: `LiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2779

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2771

#### Inherited from

[`Type`](Type.md).[`symbol`](Type.md#symbol)

***

### value

> **value**: `string` \| `number` \| [`PseudoBigInt`](PseudoBigInt.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2777

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/LiteralTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / LiteralTypeNode

# Interface: LiteralTypeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1035

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

> `readonly` **kind**: [`LiteralType`](../enumerations/SyntaxKind.md#literaltype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1036

#### Overrides

[`TypeNode`](TypeNode.md).[`kind`](TypeNode.md#kind)

***

### literal

> `readonly` **literal**: [`LiteralExpression`](LiteralExpression.md) \| [`PrefixUnaryExpression`](PrefixUnaryExpression.md) \| [`NullLiteral`](NullLiteral.md) \| [`BooleanLiteral`](../type-aliases/BooleanLiteral.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1037

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Map.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Map

# Interface: Map\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:64

ES6 Map interface.

## Extends

- [`ESMap`](ESMap.md)\<`string`, `T`\>

## Type Parameters

### T

`T`

## Properties

### size

> `readonly` **size**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:36

#### Inherited from

[`ESMap`](ESMap.md).[`size`](ESMap.md#size)

## Methods

### clear()

> **clear**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:43

#### Returns

`void`

#### Inherited from

[`ESMap`](ESMap.md).[`clear`](ESMap.md#clear)

***

### delete()

> **delete**(`key`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:42

#### Parameters

##### key

`string`

#### Returns

`boolean`

#### Inherited from

[`ESMap`](ESMap.md).[`delete`](ESMap.md#delete)

***

### entries()

> **entries**(): [`Iterator`](Iterator.md)\<\[`string`, `T`\]\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:49

#### Returns

[`Iterator`](Iterator.md)\<\[`string`, `T`\]\>

#### Inherited from

[`ESMap`](ESMap.md).[`entries`](ESMap.md#entries)

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

[`ESMap`](ESMap.md).[`forEach`](ESMap.md#foreach)

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

[`ESMap`](ESMap.md).[`get`](ESMap.md#get)

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

[`ESMap`](ESMap.md).[`has`](ESMap.md#has)

***

### keys()

> **keys**(): [`Iterator`](Iterator.md)\<`string`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:38

#### Returns

[`Iterator`](Iterator.md)\<`string`\>

#### Inherited from

[`ESMap`](ESMap.md).[`keys`](ESMap.md#keys)

***

### set()

> **set**(`key`, `value`): `this`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:59

#### Parameters

##### key

`string`

##### value

`T`

#### Returns

`this`

#### Inherited from

[`ESMap`](ESMap.md).[`set`](ESMap.md#set)

***

### values()

> **values**(): [`Iterator`](Iterator.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:48

#### Returns

[`Iterator`](Iterator.md)\<`T`\>

#### Inherited from

[`ESMap`](ESMap.md).[`values`](ESMap.md#values)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/MapLike.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / MapLike

# Interface: MapLike\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:25

Type of objects whose values are all of the same type.
The `in` and `for-in` operators can *not* be safely used,
since `Object.prototype` may be modified by outside code.

## Type Parameters

### T

`T`

## Indexable

\[`index`: `string`\]: `T`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/MappedTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / MappedTypeNode

# Interface: MappedTypeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1025

## Extends

- [`TypeNode`](TypeNode.md).[`Declaration`](Declaration.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`Declaration`](Declaration.md).[`_declarationBrand`](Declaration.md#_declarationbrand)

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

> `readonly` **kind**: [`MappedType`](../enumerations/SyntaxKind.md#mappedtype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1026

#### Overrides

[`Declaration`](Declaration.md).[`kind`](Declaration.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Declaration`](Declaration.md).[`locals`](Declaration.md#locals)

***

### members?

> `readonly` `optional` **members**: [`NodeArray`](NodeArray.md)\<[`TypeElement`](TypeElement.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1033

Used only to produce grammar errors

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

### nameType?

> `readonly` `optional` **nameType**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1029

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

### questionToken?

> `readonly` `optional` **questionToken**: [`QuestionToken`](../type-aliases/QuestionToken.md) \| [`PlusToken`](../type-aliases/PlusToken.md) \| [`MinusToken`](../type-aliases/MinusToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1030

***

### readonlyToken?

> `readonly` `optional` **readonlyToken**: [`ReadonlyKeyword`](../type-aliases/ReadonlyKeyword.md) \| [`PlusToken`](../type-aliases/PlusToken.md) \| [`MinusToken`](../type-aliases/MinusToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1027

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

### type?

> `readonly` `optional` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1031

***

### typeParameter

> `readonly` **typeParameter**: [`TypeParameterDeclaration`](TypeParameterDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1028

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/MemberExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / MemberExpression

# Interface: MemberExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1088

## Extends

- [`LeftHandSideExpression`](LeftHandSideExpression.md)

## Extended by

- [`PrimaryExpression`](PrimaryExpression.md)
- [`PropertyAccessExpression`](PropertyAccessExpression.md)
- [`ElementAccessExpression`](ElementAccessExpression.md)
- [`ExpressionWithTypeArguments`](ExpressionWithTypeArguments.md)
- [`TaggedTemplateExpression`](TaggedTemplateExpression.md)

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

### \_memberExpressionBrand

> **\_memberExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1089

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

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`LeftHandSideExpression`](LeftHandSideExpression.md).[`flags`](LeftHandSideExpression.md#flags)

***

### kind

> `readonly` **kind**: [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:598

#### Inherited from

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/MetaProperty.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / MetaProperty

# Interface: MetaProperty

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1393

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

### keywordToken

> `readonly` **keywordToken**: [`ImportKeyword`](../enumerations/SyntaxKind.md#importkeyword) \| [`NewKeyword`](../enumerations/SyntaxKind.md#newkeyword)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1395

***

### kind

> `readonly` **kind**: [`MetaProperty`](../enumerations/SyntaxKind.md#metaproperty)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1394

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

### name

> `readonly` **name**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1396

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/MethodDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / MethodDeclaration

# Interface: MethodDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:867

Several node kinds share function-like features such as a signature,
a name, and a body. These nodes should extend FunctionLikeDeclarationBase.
Examples:
- FunctionDeclaration
- MethodDeclaration
- AccessorDeclaration

## Extends

- [`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`ClassElement`](ClassElement.md).[`ObjectLiteralElement`](ObjectLiteralElement.md).[`JSDocContainer`](JSDocContainer.md)

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

### asteriskToken?

> `readonly` `optional` **asteriskToken**: [`AsteriskToken`](../type-aliases/AsteriskToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:847

#### Inherited from

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`asteriskToken`](FunctionLikeDeclarationBase.md#asterisktoken)

***

### body?

> `readonly` `optional` **body**: [`Block`](Block.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:872

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

> `readonly` **kind**: [`MethodDeclaration`](../enumerations/SyntaxKind.md#methoddeclaration)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:868

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:870

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:871

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

> `readonly` **parent**: [`ClassLikeDeclaration`](../type-aliases/ClassLikeDeclaration.md) \| [`ObjectLiteralExpression`](ObjectLiteralExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:869

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

[`FunctionLikeDeclarationBase`](FunctionLikeDeclarationBase.md).[`questionToken`](FunctionLikeDeclarationBase.md#questiontoken)

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/MethodSignature.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / MethodSignature

# Interface: MethodSignature

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:861

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

> `readonly` **kind**: [`MethodSignature`](../enumerations/SyntaxKind.md#methodsignature)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:862

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:864

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:865

#### Overrides

[`TypeElement`](TypeElement.md).[`name`](TypeElement.md#name)

***

### parameters

> `readonly` **parameters**: [`NodeArray`](NodeArray.md)\<[`ParameterDeclaration`](ParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:735

#### Inherited from

[`SignatureDeclarationBase`](SignatureDeclarationBase.md).[`parameters`](SignatureDeclarationBase.md#parameters)

***

### parent

> `readonly` **parent**: [`ObjectTypeDeclaration`](../type-aliases/ObjectTypeDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:863

#### Overrides

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



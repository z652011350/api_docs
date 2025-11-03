

============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeChecker.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeChecker

# Interface: TypeChecker

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2384

## Properties

### getIndexInfosOfIndexSymbol()

> **getIndexInfosOfIndexSymbol**: (`indexSymbol`) => [`IndexInfo`](IndexInfo.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2392

#### Parameters

##### indexSymbol

[`Symbol`](Symbol.md)

#### Returns

[`IndexInfo`](IndexInfo.md)[]

## Methods

### clearConstEnumRelate()?

> `optional` **clearConstEnumRelate**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2486

#### Returns

`void`

***

### deleteConstEnumRelate()?

> `optional` **deleteConstEnumRelate**(`path`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2487

#### Parameters

##### path

`string`

#### Returns

`void`

***

### getAliasedSymbol()

> **getAliasedSymbol**(`symbol`): [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2467

Follow all aliases to get the original symbol.

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

#### Returns

[`Symbol`](Symbol.md)

***

### getAmbientModules()

> **getAmbientModules**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2473

#### Returns

[`Symbol`](Symbol.md)[]

***

### getApparentType()

> **getApparentType**(`type`): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2475

#### Parameters

##### type

[`Type`](Type.md)

#### Returns

[`Type`](Type.md)

***

### getAugmentedPropertiesOfType()

> **getAugmentedPropertiesOfType**(`type`): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2448

#### Parameters

##### type

[`Type`](Type.md)

#### Returns

[`Symbol`](Symbol.md)[]

***

### getBaseConstraintOfType()

> **getBaseConstraintOfType**(`type`): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2476

#### Parameters

##### type

[`Type`](Type.md)

#### Returns

`undefined` \| [`Type`](Type.md)

***

### getBaseTypeOfLiteralType()

> **getBaseTypeOfLiteralType**(`type`): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2396

#### Parameters

##### type

[`Type`](Type.md)

#### Returns

[`Type`](Type.md)

***

### getBaseTypes()

> **getBaseTypes**(`type`): [`BaseType`](../type-aliases/BaseType.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2395

#### Parameters

##### type

[`InterfaceType`](InterfaceType.md)

#### Returns

[`BaseType`](../type-aliases/BaseType.md)[]

***

### getConstantValue()

> **getConstantValue**(`node`): `undefined` \| `string` \| `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2464

#### Parameters

##### node

[`EnumMember`](EnumMember.md) | [`PropertyAccessExpression`](PropertyAccessExpression.md) | [`ElementAccessExpression`](ElementAccessExpression.md)

#### Returns

`undefined` \| `string` \| `number`

***

### getConstEnumRelate()?

> `optional` **getConstEnumRelate**(): [`ESMap`](ESMap.md)\<`string`, [`ESMap`](ESMap.md)\<`string`, `string`\>\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2485

#### Returns

[`ESMap`](ESMap.md)\<`string`, [`ESMap`](ESMap.md)\<`string`, `string`\>\>

***

### getContextualType()

> **getContextualType**(`node`): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2451

#### Parameters

##### node

[`Expression`](Expression.md)

#### Returns

`undefined` \| [`Type`](Type.md)

***

### getDeclaredTypeOfSymbol()

> **getDeclaredTypeOfSymbol**(`symbol`): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2386

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

#### Returns

[`Type`](Type.md)

***

### getDefaultFromTypeParameter()

> **getDefaultFromTypeParameter**(`type`): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2477

#### Parameters

##### type

[`Type`](Type.md)

#### Returns

`undefined` \| [`Type`](Type.md)

***

### getExportsOfModule()

> **getExportsOfModule**(`moduleSymbol`): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2470

#### Parameters

##### moduleSymbol

[`Symbol`](Symbol.md)

#### Returns

[`Symbol`](Symbol.md)[]

***

### getExportSpecifierLocalTargetSymbol()

> **getExportSpecifierLocalTargetSymbol**(`location`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2428

#### Parameters

##### location

[`Identifier`](Identifier.md) | [`ExportSpecifier`](ExportSpecifier.md)

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

***

### getExportSymbolOfSymbol()

> **getExportSymbolOfSymbol**(`symbol`): [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2437

If a symbol is a local symbol with an associated exported symbol, returns the exported symbol.
Otherwise returns its input.
For example, at `export type T = number;`:
    - `getSymbolAtLocation` at the location `T` will return the exported symbol for `T`.
    - But the result of `getSymbolsInScope` will contain the *local* symbol for `T`, not the exported symbol.
    - Calling `getExportSymbolOfSymbol` on that local symbol will return the exported symbol.

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

#### Returns

[`Symbol`](Symbol.md)

***

### getFullyQualifiedName()

> **getFullyQualifiedName**(`symbol`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2447

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

#### Returns

`string`

***

### getImmediateAliasedSymbol()

> **getImmediateAliasedSymbol**(`symbol`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2469

Follow a *single* alias to get the immediately aliased symbol.

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

***

### getIndexInfoOfType()

> **getIndexInfoOfType**(`type`, `kind`): `undefined` \| [`IndexInfo`](IndexInfo.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2390

#### Parameters

##### type

[`Type`](Type.md)

##### kind

[`IndexKind`](../enumerations/IndexKind.md)

#### Returns

`undefined` \| [`IndexInfo`](IndexInfo.md)

***

### getIndexInfosOfType()

> **getIndexInfosOfType**(`type`): readonly [`IndexInfo`](IndexInfo.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2391

#### Parameters

##### type

[`Type`](Type.md)

#### Returns

readonly [`IndexInfo`](IndexInfo.md)[]

***

### getIndexTypeOfType()

> **getIndexTypeOfType**(`type`, `kind`): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2394

#### Parameters

##### type

[`Type`](Type.md)

##### kind

[`IndexKind`](../enumerations/IndexKind.md)

#### Returns

`undefined` \| [`Type`](Type.md)

***

### getJsxIntrinsicTagNamesAt()

> **getJsxIntrinsicTagNamesAt**(`location`): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2471

#### Parameters

##### location

[`Node`](Node.md)

#### Returns

[`Symbol`](Symbol.md)[]

***

### getNonNullableType()

> **getNonNullableType**(`type`): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2400

#### Parameters

##### type

[`Type`](Type.md)

#### Returns

[`Type`](Type.md)

***

### getNullableType()

> **getNullableType**(`type`, `flags`): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2399

#### Parameters

##### type

[`Type`](Type.md)

##### flags

[`TypeFlags`](../enumerations/TypeFlags.md)

#### Returns

[`Type`](Type.md)

***

### getPrivateIdentifierPropertyOfType()

> **getPrivateIdentifierPropertyOfType**(`leftType`, `name`, `location`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2389

#### Parameters

##### leftType

[`Type`](Type.md)

##### name

`string`

##### location

[`Node`](Node.md)

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

***

### getPropertiesOfType()

> **getPropertiesOfType**(`type`): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2387

#### Parameters

##### type

[`Type`](Type.md)

#### Returns

[`Symbol`](Symbol.md)[]

***

### getPropertyOfType()

> **getPropertyOfType**(`type`, `propertyName`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2388

#### Parameters

##### type

[`Type`](Type.md)

##### propertyName

`string`

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

***

### getPropertySymbolOfDestructuringAssignment()

> **getPropertySymbolOfDestructuringAssignment**(`location`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2438

#### Parameters

##### location

[`Identifier`](Identifier.md)

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

***

### getResolvedSignature()

> **getResolvedSignature**(`node`, `candidatesOutArray?`, `argumentCount?`): `undefined` \| [`Signature`](Signature.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2457

returns unknownSignature in the case of an error.
returns undefined if the node is not valid.

#### Parameters

##### node

[`CallLikeExpression`](../type-aliases/CallLikeExpression.md)

##### candidatesOutArray?

[`Signature`](Signature.md)[]

##### argumentCount?

`number`

Apparent number of arguments, passed in case of a possibly incomplete call. This should come from an ArgumentListInfo. See `signatureHelp.ts`.

#### Returns

`undefined` \| [`Signature`](Signature.md)

***

### getReturnTypeOfSignature()

> **getReturnTypeOfSignature**(`signature`): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2398

#### Parameters

##### signature

[`Signature`](Signature.md)

#### Returns

[`Type`](Type.md)

***

### getRootSymbols()

> **getRootSymbols**(`symbol`): readonly [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2449

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

#### Returns

readonly [`Symbol`](Symbol.md)[]

***

### getShorthandAssignmentValueSymbol()

> **getShorthandAssignmentValueSymbol**(`location`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2427

The function returns the value (local variable) symbol of an identifier in the short-hand property assignment.
This is necessary as an identifier in short-hand property assignment can contains two meaning: property name and property value.

#### Parameters

##### location

`undefined` | [`Node`](Node.md)

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

***

### getSignatureFromDeclaration()

> **getSignatureFromDeclaration**(`declaration`): `undefined` \| [`Signature`](Signature.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2459

#### Parameters

##### declaration

[`SignatureDeclaration`](../type-aliases/SignatureDeclaration.md)

#### Returns

`undefined` \| [`Signature`](Signature.md)

***

### getSignaturesOfType()

> **getSignaturesOfType**(`type`, `kind`): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2393

#### Parameters

##### type

[`Type`](Type.md)

##### kind

[`SignatureKind`](../enumerations/SignatureKind.md)

#### Returns

readonly [`Signature`](Signature.md)[]

***

### getSymbolAtLocation()

> **getSymbolAtLocation**(`node`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2421

#### Parameters

##### node

[`Node`](Node.md)

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

***

### getSymbolOfExpando()

> **getSymbolOfExpando**(`node`, `allowDeclaration`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2450

#### Parameters

##### node

[`Node`](Node.md)

##### allowDeclaration

`boolean`

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

***

### getSymbolsInScope()

> **getSymbolsInScope**(`location`, `meaning`): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2420

#### Parameters

##### location

[`Node`](Node.md)

##### meaning

[`SymbolFlags`](../enumerations/SymbolFlags.md)

#### Returns

[`Symbol`](Symbol.md)[]

***

### getSymbolsOfParameterPropertyDeclaration()

> **getSymbolsOfParameterPropertyDeclaration**(`parameter`, `parameterName`): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2422

#### Parameters

##### parameter

[`ParameterDeclaration`](ParameterDeclaration.md)

##### parameterName

`string`

#### Returns

[`Symbol`](Symbol.md)[]

***

### getTypeArguments()

> **getTypeArguments**(`type`): readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2401

#### Parameters

##### type

[`TypeReference`](TypeReference.md)

#### Returns

readonly [`Type`](Type.md)[]

***

### getTypeAtLocation()

> **getTypeAtLocation**(`node`): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2440

#### Parameters

##### node

[`Node`](Node.md)

#### Returns

[`Type`](Type.md)

***

### getTypeFromTypeNode()

> **getTypeFromTypeNode**(`node`): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2442

#### Parameters

##### node

[`TypeNode`](TypeNode.md)

#### Returns

[`Type`](Type.md)

***

### getTypeOfAssignmentPattern()

> **getTypeOfAssignmentPattern**(`pattern`): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2439

#### Parameters

##### pattern

[`AssignmentPattern`](../type-aliases/AssignmentPattern.md)

#### Returns

[`Type`](Type.md)

***

### getTypeOfSymbolAtLocation()

> **getTypeOfSymbolAtLocation**(`symbol`, `node`): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2385

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

##### node

[`Node`](Node.md)

#### Returns

[`Type`](Type.md)

***

### getTypePredicateOfSignature()

> **getTypePredicateOfSignature**(`signature`): `undefined` \| [`TypePredicate`](../type-aliases/TypePredicate.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2478

#### Parameters

##### signature

[`Signature`](Signature.md)

#### Returns

`undefined` \| [`TypePredicate`](../type-aliases/TypePredicate.md)

***

### getWidenedType()

> **getWidenedType**(`type`): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2397

#### Parameters

##### type

[`Type`](Type.md)

#### Returns

[`Type`](Type.md)

***

### indexInfoToIndexSignatureDeclaration()

> **indexInfoToIndexSignatureDeclaration**(`indexInfo`, `enclosingDeclaration`, `flags`): `undefined` \| [`IndexSignatureDeclaration`](IndexSignatureDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2409

Note that the resulting nodes cannot be checked.

#### Parameters

##### indexInfo

[`IndexInfo`](IndexInfo.md)

##### enclosingDeclaration

`undefined` | [`Node`](Node.md)

##### flags

`undefined` | [`NodeBuilderFlags`](../enumerations/NodeBuilderFlags.md)

#### Returns

`undefined` \| [`IndexSignatureDeclaration`](IndexSignatureDeclaration.md)

***

### isArgumentsSymbol()

> **isArgumentsSymbol**(`symbol`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2462

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

#### Returns

`boolean`

***

### isImplementationOfOverload()

> **isImplementationOfOverload**(`node`): `undefined` \| `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2460

#### Parameters

##### node

[`SignatureDeclaration`](../type-aliases/SignatureDeclaration.md)

#### Returns

`undefined` \| `boolean`

***

### isOptionalParameter()

> **isOptionalParameter**(`node`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2472

#### Parameters

##### node

[`ParameterDeclaration`](ParameterDeclaration.md)

#### Returns

`boolean`

***

### isUndefinedSymbol()

> **isUndefinedSymbol**(`symbol`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2461

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

#### Returns

`boolean`

***

### isUnknownSymbol()

> **isUnknownSymbol**(`symbol`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2463

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

#### Returns

`boolean`

***

### isValidPropertyAccess()

> **isValidPropertyAccess**(`node`, `propertyName`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2465

#### Parameters

##### node

[`PropertyAccessExpression`](PropertyAccessExpression.md) | [`QualifiedName`](QualifiedName.md) | [`ImportTypeNode`](ImportTypeNode.md)

##### propertyName

`string`

#### Returns

`boolean`

***

### runWithCancellationToken()

> **runWithCancellationToken**\<`T`\>(`token`, `cb`): `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2484

Depending on the operation performed, it may be appropriate to throw away the checker
if the cancellation token is triggered. Typically, if it is used for error checking
and the operation is cancelled, then it should be discarded, otherwise it is safe to keep.

#### Type Parameters

##### T

`T`

#### Parameters

##### token

[`CancellationToken`](CancellationToken.md)

##### cb

(`checker`) => `T`

#### Returns

`T`

***

### signatureToSignatureDeclaration()

> **signatureToSignatureDeclaration**(`signature`, `kind`, `enclosingDeclaration`, `flags`): `undefined` \| SignatureDeclaration & \{ typeArguments?: NodeArray\<TypeNode\> \| undefined; \}

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2405

Note that the resulting nodes cannot be checked.

#### Parameters

##### signature

[`Signature`](Signature.md)

##### kind

[`SyntaxKind`](../enumerations/SyntaxKind.md)

##### enclosingDeclaration

`undefined` | [`Node`](Node.md)

##### flags

`undefined` | [`NodeBuilderFlags`](../enumerations/NodeBuilderFlags.md)

#### Returns

`undefined` \| SignatureDeclaration & \{ typeArguments?: NodeArray\<TypeNode\> \| undefined; \}

***

### signatureToString()

> **signatureToString**(`signature`, `enclosingDeclaration?`, `flags?`, `kind?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2443

#### Parameters

##### signature

[`Signature`](Signature.md)

##### enclosingDeclaration?

[`Node`](Node.md)

##### flags?

[`TypeFormatFlags`](../enumerations/TypeFormatFlags.md)

##### kind?

[`SignatureKind`](../enumerations/SignatureKind.md)

#### Returns

`string`

***

### symbolToEntityName()

> **symbolToEntityName**(`symbol`, `meaning`, `enclosingDeclaration`, `flags`): `undefined` \| [`EntityName`](../type-aliases/EntityName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2411

Note that the resulting nodes cannot be checked.

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

##### meaning

[`SymbolFlags`](../enumerations/SymbolFlags.md)

##### enclosingDeclaration

`undefined` | [`Node`](Node.md)

##### flags

`undefined` | [`NodeBuilderFlags`](../enumerations/NodeBuilderFlags.md)

#### Returns

`undefined` \| [`EntityName`](../type-aliases/EntityName.md)

***

### symbolToExpression()

> **symbolToExpression**(`symbol`, `meaning`, `enclosingDeclaration`, `flags`): `undefined` \| [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2413

Note that the resulting nodes cannot be checked.

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

##### meaning

[`SymbolFlags`](../enumerations/SymbolFlags.md)

##### enclosingDeclaration

`undefined` | [`Node`](Node.md)

##### flags

`undefined` | [`NodeBuilderFlags`](../enumerations/NodeBuilderFlags.md)

#### Returns

`undefined` \| [`Expression`](Expression.md)

***

### symbolToParameterDeclaration()

> **symbolToParameterDeclaration**(`symbol`, `enclosingDeclaration`, `flags`): `undefined` \| [`ParameterDeclaration`](ParameterDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2417

Note that the resulting nodes cannot be checked.

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

##### enclosingDeclaration

`undefined` | [`Node`](Node.md)

##### flags

`undefined` | [`NodeBuilderFlags`](../enumerations/NodeBuilderFlags.md)

#### Returns

`undefined` \| [`ParameterDeclaration`](ParameterDeclaration.md)

***

### symbolToString()

> **symbolToString**(`symbol`, `enclosingDeclaration?`, `meaning?`, `flags?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2445

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

##### enclosingDeclaration?

[`Node`](Node.md)

##### meaning?

[`SymbolFlags`](../enumerations/SymbolFlags.md)

##### flags?

[`SymbolFormatFlags`](../enumerations/SymbolFormatFlags.md)

#### Returns

`string`

***

### symbolToTypeParameterDeclarations()

> **symbolToTypeParameterDeclarations**(`symbol`, `enclosingDeclaration`, `flags`): `undefined` \| [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2415

Note that the resulting nodes cannot be checked.

#### Parameters

##### symbol

[`Symbol`](Symbol.md)

##### enclosingDeclaration

`undefined` | [`Node`](Node.md)

##### flags

`undefined` | [`NodeBuilderFlags`](../enumerations/NodeBuilderFlags.md)

#### Returns

`undefined` \| [`NodeArray`](NodeArray.md)\<[`TypeParameterDeclaration`](TypeParameterDeclaration.md)\>

***

### tryGetMemberInModuleExports()

> **tryGetMemberInModuleExports**(`memberName`, `moduleSymbol`): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2474

#### Parameters

##### memberName

`string`

##### moduleSymbol

[`Symbol`](Symbol.md)

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

***

### tryGetResolvedSignatureWithoutCheck()

> **tryGetResolvedSignatureWithoutCheck**(`node`, `candidatesOutArray?`, `argumentCount?`): `undefined` \| [`Signature`](Signature.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2458

#### Parameters

##### node

[`CallLikeExpression`](../type-aliases/CallLikeExpression.md)

##### candidatesOutArray?

[`Signature`](Signature.md)[]

##### argumentCount?

`number`

#### Returns

`undefined` \| [`Signature`](Signature.md)

***

### tryGetTypeAtLocationWithoutCheck()

> **tryGetTypeAtLocationWithoutCheck**(`node`): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2441

#### Parameters

##### node

[`Node`](Node.md)

#### Returns

[`Type`](Type.md)

***

### typeParameterToDeclaration()

> **typeParameterToDeclaration**(`parameter`, `enclosingDeclaration`, `flags`): `undefined` \| [`TypeParameterDeclaration`](TypeParameterDeclaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2419

Note that the resulting nodes cannot be checked.

#### Parameters

##### parameter

[`TypeParameter`](TypeParameter.md)

##### enclosingDeclaration

`undefined` | [`Node`](Node.md)

##### flags

`undefined` | [`NodeBuilderFlags`](../enumerations/NodeBuilderFlags.md)

#### Returns

`undefined` \| [`TypeParameterDeclaration`](TypeParameterDeclaration.md)

***

### typePredicateToString()

> **typePredicateToString**(`predicate`, `enclosingDeclaration?`, `flags?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2446

#### Parameters

##### predicate

[`TypePredicate`](../type-aliases/TypePredicate.md)

##### enclosingDeclaration?

[`Node`](Node.md)

##### flags?

[`TypeFormatFlags`](../enumerations/TypeFormatFlags.md)

#### Returns

`string`

***

### typeToString()

> **typeToString**(`type`, `enclosingDeclaration?`, `flags?`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2444

#### Parameters

##### type

[`Type`](Type.md)

##### enclosingDeclaration?

[`Node`](Node.md)

##### flags?

[`TypeFormatFlags`](../enumerations/TypeFormatFlags.md)

#### Returns

`string`

***

### typeToTypeNode()

> **typeToTypeNode**(`type`, `enclosingDeclaration`, `flags`): `undefined` \| [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2403

Note that the resulting nodes cannot be checked.

#### Parameters

##### type

[`Type`](Type.md)

##### enclosingDeclaration

`undefined` | [`Node`](Node.md)

##### flags

`undefined` | [`NodeBuilderFlags`](../enumerations/NodeBuilderFlags.md)

#### Returns

`undefined` \| [`TypeNode`](TypeNode.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeElement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeElement

# Interface: TypeElement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1636

## Extends

- [`NamedDeclaration`](NamedDeclaration.md)

## Extended by

- [`CallSignatureDeclaration`](CallSignatureDeclaration.md)
- [`ConstructSignatureDeclaration`](ConstructSignatureDeclaration.md)
- [`PropertySignature`](PropertySignature.md)
- [`MethodSignature`](MethodSignature.md)
- [`GetAccessorDeclaration`](GetAccessorDeclaration.md)
- [`SetAccessorDeclaration`](SetAccessorDeclaration.md)
- [`IndexSignatureDeclaration`](IndexSignatureDeclaration.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`_declarationBrand`](NamedDeclaration.md#_declarationbrand)

***

### \_typeElementBrand

> **\_typeElementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1637

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1638

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

### questionToken?

> `readonly` `optional` **questionToken**: [`QuestionToken`](../type-aliases/QuestionToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1639

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeLiteralNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeLiteralNode

# Interface: TypeLiteralNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:964

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

> `readonly` **kind**: [`TypeLiteral`](../enumerations/SyntaxKind.md#typeliteral)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:965

#### Overrides

[`Declaration`](Declaration.md).[`kind`](Declaration.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`Declaration`](Declaration.md).[`locals`](Declaration.md#locals)

***

### members

> `readonly` **members**: [`NodeArray`](NodeArray.md)\<[`TypeElement`](TypeElement.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:966

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeNode

# Interface: TypeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:911

## Extends

- [`Node`](Node.md)

## Extended by

- [`KeywordTypeNode`](KeywordTypeNode.md)
- [`ThisTypeNode`](ThisTypeNode.md)
- [`FunctionOrConstructorTypeNodeBase`](FunctionOrConstructorTypeNodeBase.md)
- [`NodeWithTypeArguments`](NodeWithTypeArguments.md)
- [`TypePredicateNode`](TypePredicateNode.md)
- [`TypeLiteralNode`](TypeLiteralNode.md)
- [`ArrayTypeNode`](ArrayTypeNode.md)
- [`TupleTypeNode`](TupleTypeNode.md)
- [`NamedTupleMember`](NamedTupleMember.md)
- [`OptionalTypeNode`](OptionalTypeNode.md)
- [`RestTypeNode`](RestTypeNode.md)
- [`UnionTypeNode`](UnionTypeNode.md)
- [`IntersectionTypeNode`](IntersectionTypeNode.md)
- [`ConditionalTypeNode`](ConditionalTypeNode.md)
- [`InferTypeNode`](InferTypeNode.md)
- [`ParenthesizedTypeNode`](ParenthesizedTypeNode.md)
- [`TypeOperatorNode`](TypeOperatorNode.md)
- [`IndexedAccessTypeNode`](IndexedAccessTypeNode.md)
- [`MappedTypeNode`](MappedTypeNode.md)
- [`LiteralTypeNode`](LiteralTypeNode.md)
- [`TemplateLiteralTypeNode`](TemplateLiteralTypeNode.md)
- [`TemplateLiteralTypeSpan`](TemplateLiteralTypeSpan.md)
- [`JSDocTypeExpression`](JSDocTypeExpression.md)
- [`JSDocType`](JSDocType.md)

## Properties

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeOfExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeOfExpression

# Interface: TypeOfExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1117

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1119

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`flags`](UnaryExpression.md#flags)

***

### kind

> `readonly` **kind**: [`TypeOfExpression`](../enumerations/SyntaxKind.md#typeofexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1118

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeOperatorNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeOperatorNode

# Interface: TypeOperatorNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1015

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

> `readonly` **kind**: [`TypeOperator`](../enumerations/SyntaxKind.md#typeoperator)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1016

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

### operator

> `readonly` **operator**: [`KeyOfKeyword`](../enumerations/SyntaxKind.md#keyofkeyword) \| [`ReadonlyKeyword`](../enumerations/SyntaxKind.md#readonlykeyword) \| [`UniqueKeyword`](../enumerations/SyntaxKind.md#uniquekeyword)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1017

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1018

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeParameter.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeParameter

# Interface: TypeParameter

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2888

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeParameterDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeParameterDeclaration

# Interface: TypeParameterDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:721

## Extends

- [`NamedDeclaration`](NamedDeclaration.md)

## Properties

### \_declarationBrand

> **\_declarationBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:699

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`_declarationBrand`](NamedDeclaration.md#_declarationbrand)

***

### constraint?

> `readonly` `optional` **constraint**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:727

Note: Consider calling `getEffectiveConstraintOfTypeParameter`

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

### default?

> `readonly` `optional` **default**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:728

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`end`](NamedDeclaration.md#end)

***

### expression?

> `optional` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:729

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`flags`](NamedDeclaration.md#flags)

***

### kind

> `readonly` **kind**: [`TypeParameter`](../enumerations/SyntaxKind.md#typeparameter)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:722

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

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`Modifier`](../type-aliases/Modifier.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:724

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

> `readonly` **name**: [`Identifier`](Identifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:725

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`name`](NamedDeclaration.md#name)

***

### parent

> `readonly` **parent**: [`DeclarationWithTypeParameterChildren`](../type-aliases/DeclarationWithTypeParameterChildren.md) \| [`InferTypeNode`](InferTypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:723

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypePredicateBase.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypePredicateBase

# Interface: TypePredicateBase

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2577

## Extended by

- [`ThisTypePredicate`](ThisTypePredicate.md)
- [`IdentifierTypePredicate`](IdentifierTypePredicate.md)
- [`AssertsThisTypePredicate`](AssertsThisTypePredicate.md)
- [`AssertsIdentifierTypePredicate`](AssertsIdentifierTypePredicate.md)

## Properties

### kind

> **kind**: [`TypePredicateKind`](../enumerations/TypePredicateKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2578

***

### type

> **type**: `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2579




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypePredicateNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypePredicateNode

# Interface: TypePredicateNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:953

## Extends

- [`TypeNode`](TypeNode.md)

## Properties

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`TypeNode`](TypeNode.md).[`_typeNodeBrand`](TypeNode.md#_typenodebrand)

***

### assertsModifier?

> `readonly` `optional` **assertsModifier**: [`AssertsKeyword`](../type-aliases/AssertsKeyword.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:956

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

> `readonly` **kind**: [`TypePredicate`](../enumerations/SyntaxKind.md#typepredicate)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:954

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

### parameterName

> `readonly` **parameterName**: [`Identifier`](Identifier.md) \| [`ThisTypeNode`](ThisTypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:957

***

### parent

> `readonly` **parent**: [`SignatureDeclaration`](../type-aliases/SignatureDeclaration.md) \| [`JSDocTypeExpression`](JSDocTypeExpression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:955

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

### type?

> `readonly` `optional` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:958

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeQueryNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeQueryNode

# Interface: TypeQueryNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:960

## Extends

- [`NodeWithTypeArguments`](NodeWithTypeArguments.md)

## Properties

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`_typeNodeBrand`](NodeWithTypeArguments.md#_typenodebrand)

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

### exprName

> `readonly` **exprName**: [`EntityName`](../type-aliases/EntityName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:962

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`flags`](NodeWithTypeArguments.md#flags)

***

### kind

> `readonly` **kind**: [`TypeQuery`](../enumerations/SyntaxKind.md#typequery)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:961

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeReference.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeReference

# Interface: TypeReference

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2844

Type references (ObjectFlags.Reference). When a class or interface has type parameters or
a "this" type, references to the class or interface are made using type references. The
typeArguments property specifies the types to substitute for the type parameters of the
class or interface and optionally includes an extra element that specifies the type to
substitute for "this" in the resulting instantiation. When no extra argument is present,
the type reference itself is substituted for "this". The typeArguments property is undefined
if the class or interface has no type parameters and the reference isn't specifying an
explicit "this" argument.

## Extends

- [`ObjectType`](ObjectType.md)

## Extended by

- [`DeferredTypeReference`](DeferredTypeReference.md)
- [`GenericType`](GenericType.md)
- [`TupleTypeReference`](TupleTypeReference.md)

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

### flags

> **flags**: [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2770

#### Inherited from

[`ObjectType`](ObjectType.md).[`flags`](ObjectType.md#flags)

***

### node?

> `optional` **node**: [`TypeReferenceNode`](TypeReferenceNode.md) \| [`ArrayTypeNode`](ArrayTypeNode.md) \| [`TupleTypeNode`](TupleTypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2846

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

***

### target

> **target**: [`GenericType`](GenericType.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2845

***

### typeArguments?

> `optional` **typeArguments**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6145

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeReferenceDirectiveResolutionCache.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeReferenceDirectiveResolutionCache

# Interface: TypeReferenceDirectiveResolutionCache

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5362

Cached resolutions per containing directory.
This assumes that any module id will have the same resolution for sibling files located in the same folder.

## Extends

- [`PerDirectoryResolutionCache`](PerDirectoryResolutionCache.md)\<[`ResolvedTypeReferenceDirectiveWithFailedLookupLocations`](ResolvedTypeReferenceDirectiveWithFailedLookupLocations.md)\>.[`PackageJsonInfoCache`](PackageJsonInfoCache.md)

## Methods

### clear()

> **clear**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5378

#### Returns

`void`

#### Inherited from

[`PackageJsonInfoCache`](PackageJsonInfoCache.md).[`clear`](PackageJsonInfoCache.md#clear)

***

### getOrCreateCacheForDirectory()

> **getOrCreateCacheForDirectory**(`directoryName`, `redirectedReference?`): [`ModeAwareCache`](ModeAwareCache.md)\<[`ResolvedTypeReferenceDirectiveWithFailedLookupLocations`](ResolvedTypeReferenceDirectiveWithFailedLookupLocations.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5377

#### Parameters

##### directoryName

`string`

##### redirectedReference?

[`ResolvedProjectReference`](ResolvedProjectReference.md)

#### Returns

[`ModeAwareCache`](ModeAwareCache.md)\<[`ResolvedTypeReferenceDirectiveWithFailedLookupLocations`](ResolvedTypeReferenceDirectiveWithFailedLookupLocations.md)\>

#### Inherited from

[`PerDirectoryResolutionCache`](PerDirectoryResolutionCache.md).[`getOrCreateCacheForDirectory`](PerDirectoryResolutionCache.md#getorcreatecachefordirectory)

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

#### Inherited from

[`PerDirectoryResolutionCache`](PerDirectoryResolutionCache.md).[`update`](PerDirectoryResolutionCache.md#update)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/TypeReferenceNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / TypeReferenceNode

# Interface: TypeReferenceNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:949

## Extends

- [`NodeWithTypeArguments`](NodeWithTypeArguments.md)

## Properties

### \_typeNodeBrand

> **\_typeNodeBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:912

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`_typeNodeBrand`](NodeWithTypeArguments.md#_typenodebrand)

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

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`NodeWithTypeArguments`](NodeWithTypeArguments.md).[`flags`](NodeWithTypeArguments.md#flags)

***

### kind

> `readonly` **kind**: [`TypeReference`](../enumerations/SyntaxKind.md#typereference)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:950

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

***

### typeName

> `readonly` **typeName**: [`EntityName`](../type-aliases/EntityName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:951

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UnaryExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UnaryExpression

# Interface: UnaryExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1065

## Extends

- [`Expression`](Expression.md)

## Extended by

- [`UpdateExpression`](UpdateExpression.md)
- [`DeleteExpression`](DeleteExpression.md)
- [`TypeOfExpression`](TypeOfExpression.md)
- [`VoidExpression`](VoidExpression.md)
- [`AwaitExpression`](AwaitExpression.md)
- [`TypeAssertion`](TypeAssertion.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`Expression`](Expression.md).[`_expressionBrand`](Expression.md#_expressionbrand)

***

### \_unaryExpressionBrand

> **\_unaryExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1066

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

> `readonly` **kind**: [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:598

#### Inherited from

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UnderscoreEscapedMap.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UnderscoreEscapedMap

# Interface: UnderscoreEscapedMap\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2714

Map where keys are `__String`s.

## Extends

- [`ESMap`](ESMap.md)\<[`__String`](../type-aliases/String.md), `T`\>.[`ReadonlyUnderscoreEscapedMap`](ReadonlyUnderscoreEscapedMap.md)\<`T`\>

## Type Parameters

### T

`T`

## Properties

### size

> `readonly` **size**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:36

#### Inherited from

[`ReadonlyUnderscoreEscapedMap`](ReadonlyUnderscoreEscapedMap.md).[`size`](ReadonlyUnderscoreEscapedMap.md#size)

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

[`__String`](../type-aliases/String.md)

#### Returns

`boolean`

#### Inherited from

[`ESMap`](ESMap.md).[`delete`](ESMap.md#delete)

***

### entries()

> **entries**(): [`Iterator`](Iterator.md)\<\[[`__String`](../type-aliases/String.md), `T`\]\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:49

#### Returns

[`Iterator`](Iterator.md)\<\[[`__String`](../type-aliases/String.md), `T`\]\>

#### Inherited from

[`ReadonlyUnderscoreEscapedMap`](ReadonlyUnderscoreEscapedMap.md).[`entries`](ReadonlyUnderscoreEscapedMap.md#entries)

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

[`ReadonlyUnderscoreEscapedMap`](ReadonlyUnderscoreEscapedMap.md).[`forEach`](ReadonlyUnderscoreEscapedMap.md#foreach)

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

[`ReadonlyUnderscoreEscapedMap`](ReadonlyUnderscoreEscapedMap.md).[`get`](ReadonlyUnderscoreEscapedMap.md#get)

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

[`ReadonlyUnderscoreEscapedMap`](ReadonlyUnderscoreEscapedMap.md).[`has`](ReadonlyUnderscoreEscapedMap.md#has)

***

### keys()

> **keys**(): [`Iterator`](Iterator.md)\<[`__String`](../type-aliases/String.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:38

#### Returns

[`Iterator`](Iterator.md)\<[`__String`](../type-aliases/String.md)\>

#### Inherited from

[`ReadonlyUnderscoreEscapedMap`](ReadonlyUnderscoreEscapedMap.md).[`keys`](ReadonlyUnderscoreEscapedMap.md#keys)

***

### set()

> **set**(`key`, `value`): `this`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:59

#### Parameters

##### key

[`__String`](../type-aliases/String.md)

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

[`ReadonlyUnderscoreEscapedMap`](ReadonlyUnderscoreEscapedMap.md).[`values`](ReadonlyUnderscoreEscapedMap.md#values)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UnionOrIntersectionType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UnionOrIntersectionType

# Interface: UnionOrIntersectionType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2874

## Extends

- [`Type`](Type.md)

## Extended by

- [`UnionType`](UnionType.md)
- [`IntersectionType`](IntersectionType.md)

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

***

### types

> **types**: [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2875

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UnionType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UnionType

# Interface: UnionType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2877

## Extends

- [`UnionOrIntersectionType`](UnionOrIntersectionType.md)

## Properties

### aliasSymbol?

> `optional` **aliasSymbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2773

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`aliasSymbol`](UnionOrIntersectionType.md#aliassymbol)

***

### aliasTypeArguments?

> `optional` **aliasTypeArguments**: readonly [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2774

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`aliasTypeArguments`](UnionOrIntersectionType.md#aliastypearguments)

***

### flags

> **flags**: [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2770

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`flags`](UnionOrIntersectionType.md#flags)

***

### pattern?

> `optional` **pattern**: [`DestructuringPattern`](../type-aliases/DestructuringPattern.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2772

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`pattern`](UnionOrIntersectionType.md#pattern)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2771

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`symbol`](UnionOrIntersectionType.md#symbol)

***

### types

> **types**: [`Type`](Type.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2875

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`types`](UnionOrIntersectionType.md#types)

## Methods

### getApparentProperties()

> **getApparentProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6124

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`getApparentProperties`](UnionOrIntersectionType.md#getapparentproperties)

***

### getBaseTypes()

> **getBaseTypes**(): `undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6129

#### Returns

`undefined` \| [`BaseType`](../type-aliases/BaseType.md)[]

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`getBaseTypes`](UnionOrIntersectionType.md#getbasetypes)

***

### getCallSignatures()

> **getCallSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6125

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`getCallSignatures`](UnionOrIntersectionType.md#getcallsignatures)

***

### getConstraint()

> **getConstraint**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6131

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`getConstraint`](UnionOrIntersectionType.md#getconstraint)

***

### getConstructSignatures()

> **getConstructSignatures**(): readonly [`Signature`](Signature.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6126

#### Returns

readonly [`Signature`](Signature.md)[]

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`getConstructSignatures`](UnionOrIntersectionType.md#getconstructsignatures)

***

### getDefault()

> **getDefault**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6132

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`getDefault`](UnionOrIntersectionType.md#getdefault)

***

### getFlags()

> **getFlags**(): [`TypeFlags`](../enumerations/TypeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6120

#### Returns

[`TypeFlags`](../enumerations/TypeFlags.md)

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`getFlags`](UnionOrIntersectionType.md#getflags)

***

### getNonNullableType()

> **getNonNullableType**(): [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6130

#### Returns

[`Type`](Type.md)

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`getNonNullableType`](UnionOrIntersectionType.md#getnonnullabletype)

***

### getNumberIndexType()

> **getNumberIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6128

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`getNumberIndexType`](UnionOrIntersectionType.md#getnumberindextype)

***

### getProperties()

> **getProperties**(): [`Symbol`](Symbol.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6122

#### Returns

[`Symbol`](Symbol.md)[]

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`getProperties`](UnionOrIntersectionType.md#getproperties)

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

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`getProperty`](UnionOrIntersectionType.md#getproperty)

***

### getStringIndexType()

> **getStringIndexType**(): `undefined` \| [`Type`](Type.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6127

#### Returns

`undefined` \| [`Type`](Type.md)

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`getStringIndexType`](UnionOrIntersectionType.md#getstringindextype)

***

### getSymbol()

> **getSymbol**(): `undefined` \| [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6121

#### Returns

`undefined` \| [`Symbol`](Symbol.md)

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`getSymbol`](UnionOrIntersectionType.md#getsymbol)

***

### isClass()

> **isClass**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6141

#### Returns

`this is InterfaceType`

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`isClass`](UnionOrIntersectionType.md#isclass)

***

### isClassOrInterface()

> **isClassOrInterface**(): `this is InterfaceType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6140

#### Returns

`this is InterfaceType`

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`isClassOrInterface`](UnionOrIntersectionType.md#isclassorinterface)

***

### isIndexType()

> **isIndexType**(): `this is IndexType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6142

#### Returns

`this is IndexType`

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`isIndexType`](UnionOrIntersectionType.md#isindextype)

***

### isIntersection()

> **isIntersection**(): `this is IntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6134

#### Returns

`this is IntersectionType`

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`isIntersection`](UnionOrIntersectionType.md#isintersection)

***

### isLiteral()

> **isLiteral**(): `this is LiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6136

#### Returns

`this is LiteralType`

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`isLiteral`](UnionOrIntersectionType.md#isliteral)

***

### isNumberLiteral()

> **isNumberLiteral**(): `this is NumberLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6138

#### Returns

`this is NumberLiteralType`

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`isNumberLiteral`](UnionOrIntersectionType.md#isnumberliteral)

***

### isStringLiteral()

> **isStringLiteral**(): `this is StringLiteralType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6137

#### Returns

`this is StringLiteralType`

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`isStringLiteral`](UnionOrIntersectionType.md#isstringliteral)

***

### isTypeParameter()

> **isTypeParameter**(): `this is TypeParameter`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6139

#### Returns

`this is TypeParameter`

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`isTypeParameter`](UnionOrIntersectionType.md#istypeparameter)

***

### isUnion()

> **isUnion**(): `this is UnionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6133

#### Returns

`this is UnionType`

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`isUnion`](UnionOrIntersectionType.md#isunion)

***

### isUnionOrIntersection()

> **isUnionOrIntersection**(): `this is UnionOrIntersectionType`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6135

#### Returns

`this is UnionOrIntersectionType`

#### Inherited from

[`UnionOrIntersectionType`](UnionOrIntersectionType.md).[`isUnionOrIntersection`](UnionOrIntersectionType.md#isunionorintersection)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UnionTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UnionTypeNode

# Interface: UnionTypeNode

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:992

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

> `readonly` **kind**: [`UnionType`](../enumerations/SyntaxKind.md#uniontype)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:993

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

### types

> `readonly` **types**: [`NodeArray`](NodeArray.md)\<[`TypeNode`](TypeNode.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:994

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UniqueESSymbolType.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UniqueESSymbolType

# Interface: UniqueESSymbolType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2781

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

### escapedName

> **escapedName**: [`__String`](../type-aliases/String.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2783

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2782

#### Overrides

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UnparsedPrepend.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UnparsedPrepend

# Interface: UnparsedPrepend

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2201

## Extends

- [`UnparsedSection`](UnparsedSection.md)

## Properties

### data

> `readonly` **data**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2204

#### Overrides

[`UnparsedSection`](UnparsedSection.md).[`data`](UnparsedSection.md#data)

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

[`UnparsedSection`](UnparsedSection.md).[`decorators`](UnparsedSection.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`end`](UnparsedSection.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`flags`](UnparsedSection.md#flags)

***

### kind

> `readonly` **kind**: [`UnparsedPrepend`](../enumerations/SyntaxKind.md#unparsedprepend)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2202

#### Overrides

[`UnparsedSection`](UnparsedSection.md).[`kind`](UnparsedSection.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`locals`](UnparsedSection.md#locals)

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

[`UnparsedSection`](UnparsedSection.md).[`modifiers`](UnparsedSection.md#modifiers)

***

### parent

> `readonly` **parent**: [`UnparsedSource`](UnparsedSource.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2203

#### Overrides

[`UnparsedSection`](UnparsedSection.md).[`parent`](UnparsedSection.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`pos`](UnparsedSection.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`skipCheck`](UnparsedSection.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`symbol`](UnparsedSection.md#symbol)

***

### texts

> `readonly` **texts**: readonly [`UnparsedTextLike`](UnparsedTextLike.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2205

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

[`UnparsedSection`](UnparsedSection.md).[`forEachChild`](UnparsedSection.md#foreachchild)

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

[`UnparsedSection`](UnparsedSection.md).[`getChildAt`](UnparsedSection.md#getchildat)

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

[`UnparsedSection`](UnparsedSection.md).[`getChildCount`](UnparsedSection.md#getchildcount)

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

[`UnparsedSection`](UnparsedSection.md).[`getChildren`](UnparsedSection.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getEnd`](UnparsedSection.md#getend)

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

[`UnparsedSection`](UnparsedSection.md).[`getFirstToken`](UnparsedSection.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getFullStart`](UnparsedSection.md#getfullstart)

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

[`UnparsedSection`](UnparsedSection.md).[`getFullText`](UnparsedSection.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getFullWidth`](UnparsedSection.md#getfullwidth)

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

[`UnparsedSection`](UnparsedSection.md).[`getLastToken`](UnparsedSection.md#getlasttoken)

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

[`UnparsedSection`](UnparsedSection.md).[`getLeadingTriviaWidth`](UnparsedSection.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getSourceFile`](UnparsedSection.md#getsourcefile)

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

[`UnparsedSection`](UnparsedSection.md).[`getStart`](UnparsedSection.md#getstart)

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

[`UnparsedSection`](UnparsedSection.md).[`getText`](UnparsedSection.md#gettext)

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

[`UnparsedSection`](UnparsedSection.md).[`getWidth`](UnparsedSection.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UnparsedPrologue.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UnparsedPrologue

# Interface: UnparsedPrologue

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2196

## Extends

- [`UnparsedSection`](UnparsedSection.md)

## Properties

### data

> `readonly` **data**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2199

#### Overrides

[`UnparsedSection`](UnparsedSection.md).[`data`](UnparsedSection.md#data)

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

[`UnparsedSection`](UnparsedSection.md).[`decorators`](UnparsedSection.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`end`](UnparsedSection.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`flags`](UnparsedSection.md#flags)

***

### kind

> `readonly` **kind**: [`UnparsedPrologue`](../enumerations/SyntaxKind.md#unparsedprologue)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2197

#### Overrides

[`UnparsedSection`](UnparsedSection.md).[`kind`](UnparsedSection.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`locals`](UnparsedSection.md#locals)

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

[`UnparsedSection`](UnparsedSection.md).[`modifiers`](UnparsedSection.md#modifiers)

***

### parent

> `readonly` **parent**: [`UnparsedSource`](UnparsedSource.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2198

#### Overrides

[`UnparsedSection`](UnparsedSection.md).[`parent`](UnparsedSection.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`pos`](UnparsedSection.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`skipCheck`](UnparsedSection.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`symbol`](UnparsedSection.md#symbol)

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

[`UnparsedSection`](UnparsedSection.md).[`forEachChild`](UnparsedSection.md#foreachchild)

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

[`UnparsedSection`](UnparsedSection.md).[`getChildAt`](UnparsedSection.md#getchildat)

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

[`UnparsedSection`](UnparsedSection.md).[`getChildCount`](UnparsedSection.md#getchildcount)

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

[`UnparsedSection`](UnparsedSection.md).[`getChildren`](UnparsedSection.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getEnd`](UnparsedSection.md#getend)

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

[`UnparsedSection`](UnparsedSection.md).[`getFirstToken`](UnparsedSection.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getFullStart`](UnparsedSection.md#getfullstart)

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

[`UnparsedSection`](UnparsedSection.md).[`getFullText`](UnparsedSection.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getFullWidth`](UnparsedSection.md#getfullwidth)

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

[`UnparsedSection`](UnparsedSection.md).[`getLastToken`](UnparsedSection.md#getlasttoken)

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

[`UnparsedSection`](UnparsedSection.md).[`getLeadingTriviaWidth`](UnparsedSection.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getSourceFile`](UnparsedSection.md#getsourcefile)

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

[`UnparsedSection`](UnparsedSection.md).[`getStart`](UnparsedSection.md#getstart)

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

[`UnparsedSection`](UnparsedSection.md).[`getText`](UnparsedSection.md#gettext)

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

[`UnparsedSection`](UnparsedSection.md).[`getWidth`](UnparsedSection.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UnparsedSection.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UnparsedSection

# Interface: UnparsedSection

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2191

## Extends

- [`Node`](Node.md)

## Extended by

- [`UnparsedPrologue`](UnparsedPrologue.md)
- [`UnparsedPrepend`](UnparsedPrepend.md)
- [`UnparsedTextLike`](UnparsedTextLike.md)
- [`UnparsedSyntheticReference`](UnparsedSyntheticReference.md)

## Properties

### data?

> `readonly` `optional` **data**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2194

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2192

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

> `readonly` **parent**: [`UnparsedSource`](UnparsedSource.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2193

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UnparsedSource.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UnparsedSource

# Interface: UnparsedSource

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2174

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

### fileName

> **fileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2176

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Node`](Node.md).[`flags`](Node.md#flags)

***

### hasNoDefaultLib?

> `optional` **hasNoDefaultLib**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2183

***

### helpers

> **helpers**: `undefined` \| readonly [`UnscopedEmitHelper`](UnscopedEmitHelper.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2179

***

### kind

> `readonly` **kind**: [`UnparsedSource`](../enumerations/SyntaxKind.md#unparsedsource)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2175

#### Overrides

[`Node`](Node.md).[`kind`](Node.md#kind)

***

### libReferenceDirectives

> **libReferenceDirectives**: readonly [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2182

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

### prologues

> `readonly` **prologues**: readonly [`UnparsedPrologue`](UnparsedPrologue.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2178

***

### referencedFiles

> **referencedFiles**: readonly [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2180

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`Node`](Node.md).[`skipCheck`](Node.md#skipcheck)

***

### sourceMapPath?

> `optional` **sourceMapPath**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2184

***

### sourceMapText?

> `optional` **sourceMapText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2185

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`Node`](Node.md).[`symbol`](Node.md#symbol)

***

### syntheticReferences?

> `readonly` `optional` **syntheticReferences**: readonly [`UnparsedSyntheticReference`](UnparsedSyntheticReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2186

***

### text

> **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2177

***

### texts

> `readonly` **texts**: readonly [`UnparsedSourceText`](../type-aliases/UnparsedSourceText.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2187

***

### typeReferenceDirectives

> **typeReferenceDirectives**: `undefined` \| readonly [`FileReference`](FileReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2181

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UnparsedSyntheticReference.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UnparsedSyntheticReference

# Interface: UnparsedSyntheticReference

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2211

## Extends

- [`UnparsedSection`](UnparsedSection.md)

## Properties

### data?

> `readonly` `optional` **data**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2194

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`data`](UnparsedSection.md#data)

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

[`UnparsedSection`](UnparsedSection.md).[`decorators`](UnparsedSection.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`end`](UnparsedSection.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`flags`](UnparsedSection.md#flags)

***

### kind

> `readonly` **kind**: [`UnparsedSyntheticReference`](../enumerations/SyntaxKind.md#unparsedsyntheticreference)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2212

#### Overrides

[`UnparsedSection`](UnparsedSection.md).[`kind`](UnparsedSection.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`locals`](UnparsedSection.md#locals)

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

[`UnparsedSection`](UnparsedSection.md).[`modifiers`](UnparsedSection.md#modifiers)

***

### parent

> `readonly` **parent**: [`UnparsedSource`](UnparsedSource.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2213

#### Overrides

[`UnparsedSection`](UnparsedSection.md).[`parent`](UnparsedSection.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`pos`](UnparsedSection.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`skipCheck`](UnparsedSection.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`symbol`](UnparsedSection.md#symbol)

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

[`UnparsedSection`](UnparsedSection.md).[`forEachChild`](UnparsedSection.md#foreachchild)

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

[`UnparsedSection`](UnparsedSection.md).[`getChildAt`](UnparsedSection.md#getchildat)

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

[`UnparsedSection`](UnparsedSection.md).[`getChildCount`](UnparsedSection.md#getchildcount)

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

[`UnparsedSection`](UnparsedSection.md).[`getChildren`](UnparsedSection.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getEnd`](UnparsedSection.md#getend)

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

[`UnparsedSection`](UnparsedSection.md).[`getFirstToken`](UnparsedSection.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getFullStart`](UnparsedSection.md#getfullstart)

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

[`UnparsedSection`](UnparsedSection.md).[`getFullText`](UnparsedSection.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getFullWidth`](UnparsedSection.md#getfullwidth)

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

[`UnparsedSection`](UnparsedSection.md).[`getLastToken`](UnparsedSection.md#getlasttoken)

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

[`UnparsedSection`](UnparsedSection.md).[`getLeadingTriviaWidth`](UnparsedSection.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getSourceFile`](UnparsedSection.md#getsourcefile)

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

[`UnparsedSection`](UnparsedSection.md).[`getStart`](UnparsedSection.md#getstart)

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

[`UnparsedSection`](UnparsedSection.md).[`getText`](UnparsedSection.md#gettext)

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

[`UnparsedSection`](UnparsedSection.md).[`getWidth`](UnparsedSection.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UnparsedTextLike.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UnparsedTextLike

# Interface: UnparsedTextLike

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2207

## Extends

- [`UnparsedSection`](UnparsedSection.md)

## Properties

### data?

> `readonly` `optional` **data**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2194

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`data`](UnparsedSection.md#data)

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

[`UnparsedSection`](UnparsedSection.md).[`decorators`](UnparsedSection.md#decorators)

***

### end

> `readonly` **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:103

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`end`](UnparsedSection.md#end)

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`flags`](UnparsedSection.md#flags)

***

### kind

> `readonly` **kind**: [`UnparsedText`](../enumerations/SyntaxKind.md#unparsedtext) \| [`UnparsedInternalText`](../enumerations/SyntaxKind.md#unparsedinternaltext)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2208

#### Overrides

[`UnparsedSection`](UnparsedSection.md).[`kind`](UnparsedSection.md#kind)

***

### locals?

> `optional` **locals**: [`SymbolTable`](../type-aliases/SymbolTable.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:602

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`locals`](UnparsedSection.md#locals)

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

[`UnparsedSection`](UnparsedSection.md).[`modifiers`](UnparsedSection.md#modifiers)

***

### parent

> `readonly` **parent**: [`UnparsedSource`](UnparsedSource.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2209

#### Overrides

[`UnparsedSection`](UnparsedSection.md).[`parent`](UnparsedSection.md#parent)

***

### pos

> `readonly` **pos**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:102

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`pos`](UnparsedSection.md#pos)

***

### skipCheck?

> `optional` **skipCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:603

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`skipCheck`](UnparsedSection.md#skipcheck)

***

### symbol

> **symbol**: [`Symbol`](Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:601

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`symbol`](UnparsedSection.md#symbol)

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

[`UnparsedSection`](UnparsedSection.md).[`forEachChild`](UnparsedSection.md#foreachchild)

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

[`UnparsedSection`](UnparsedSection.md).[`getChildAt`](UnparsedSection.md#getchildat)

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

[`UnparsedSection`](UnparsedSection.md).[`getChildCount`](UnparsedSection.md#getchildcount)

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

[`UnparsedSection`](UnparsedSection.md).[`getChildren`](UnparsedSection.md#getchildren)

***

### getEnd()

> **getEnd**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6094

#### Returns

`number`

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getEnd`](UnparsedSection.md#getend)

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

[`UnparsedSection`](UnparsedSection.md).[`getFirstToken`](UnparsedSection.md#getfirsttoken)

***

### getFullStart()

> **getFullStart**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6093

#### Returns

`number`

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getFullStart`](UnparsedSection.md#getfullstart)

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

[`UnparsedSection`](UnparsedSection.md).[`getFullText`](UnparsedSection.md#getfulltext)

***

### getFullWidth()

> **getFullWidth**(): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6096

#### Returns

`number`

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getFullWidth`](UnparsedSection.md#getfullwidth)

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

[`UnparsedSection`](UnparsedSection.md).[`getLastToken`](UnparsedSection.md#getlasttoken)

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

[`UnparsedSection`](UnparsedSection.md).[`getLeadingTriviaWidth`](UnparsedSection.md#getleadingtriviawidth)

***

### getSourceFile()

> **getSourceFile**(): [`SourceFile`](SourceFile.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6088

#### Returns

[`SourceFile`](SourceFile.md)

#### Inherited from

[`UnparsedSection`](UnparsedSection.md).[`getSourceFile`](UnparsedSection.md#getsourcefile)

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

[`UnparsedSection`](UnparsedSection.md).[`getStart`](UnparsedSection.md#getstart)

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

[`UnparsedSection`](UnparsedSection.md).[`getText`](UnparsedSection.md#gettext)

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

[`UnparsedSection`](UnparsedSection.md).[`getWidth`](UnparsedSection.md#getwidth)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UnscopedEmitHelper.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UnscopedEmitHelper

# Interface: UnscopedEmitHelper

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3563

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

> `readonly` **scoped**: `false`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3564

#### Overrides

[`EmitHelperBase`](EmitHelperBase.md).[`scoped`](EmitHelperBase.md#scoped)

***

### text

> `readonly` **text**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3565

#### Overrides

[`EmitHelperBase`](EmitHelperBase.md).[`text`](EmitHelperBase.md#text)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UpdateBundleProject.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UpdateBundleProject

# Interface: UpdateBundleProject\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6005

## Extends

- [`InvalidatedProjectBase`](InvalidatedProjectBase.md)

## Type Parameters

### T

`T` *extends* [`BuilderProgram`](BuilderProgram.md)

## Properties

### kind

> `readonly` **kind**: [`UpdateBundle`](../enumerations/InvalidatedProjectKind.md#updatebundle)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6006

#### Overrides

[`InvalidatedProjectBase`](InvalidatedProjectBase.md).[`kind`](InvalidatedProjectBase.md#kind)

***

### project

> `readonly` **project**: [`ResolvedConfigFileName`](../type-aliases/ResolvedConfigFileName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5978

#### Inherited from

[`InvalidatedProjectBase`](InvalidatedProjectBase.md).[`project`](InvalidatedProjectBase.md#project)

## Methods

### done()

> **done**(`cancellationToken?`, `writeFile?`, `customTransformers?`): [`ExitStatus`](../enumerations/ExitStatus.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5982

To dispose this project and ensure that all the necessary actions are taken and state is updated accordingly

#### Parameters

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

##### writeFile?

[`WriteFileCallback`](../type-aliases/WriteFileCallback.md)

##### customTransformers?

[`CustomTransformers`](CustomTransformers.md)

#### Returns

[`ExitStatus`](../enumerations/ExitStatus.md)

#### Inherited from

[`InvalidatedProjectBase`](InvalidatedProjectBase.md).[`done`](InvalidatedProjectBase.md#done)

***

### emit()

> **emit**(`writeFile?`, `customTransformers?`): `undefined` \| [`EmitResult`](EmitResult.md) \| [`BuildInvalidedProject`](BuildInvalidedProject.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:6007

#### Parameters

##### writeFile?

[`WriteFileCallback`](../type-aliases/WriteFileCallback.md)

##### customTransformers?

[`CustomTransformers`](CustomTransformers.md)

#### Returns

`undefined` \| [`EmitResult`](EmitResult.md) \| [`BuildInvalidedProject`](BuildInvalidedProject.md)\<`T`\>

***

### getCompilerOptions()

> **getCompilerOptions**(): [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5983

#### Returns

[`CompilerOptions`](CompilerOptions.md)

#### Inherited from

[`InvalidatedProjectBase`](InvalidatedProjectBase.md).[`getCompilerOptions`](InvalidatedProjectBase.md#getcompileroptions)

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5984

#### Returns

`string`

#### Inherited from

[`InvalidatedProjectBase`](InvalidatedProjectBase.md).[`getCurrentDirectory`](InvalidatedProjectBase.md#getcurrentdirectory)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UpdateExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UpdateExpression

# Interface: UpdateExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1070

## Extends

- [`UnaryExpression`](UnaryExpression.md)

## Extended by

- [`PrefixUnaryExpression`](PrefixUnaryExpression.md)
- [`PostfixUnaryExpression`](PostfixUnaryExpression.md)
- [`LeftHandSideExpression`](LeftHandSideExpression.md)

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

### \_updateExpressionBrand

> **\_updateExpressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1071

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

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`flags`](UnaryExpression.md#flags)

***

### kind

> `readonly` **kind**: [`SyntaxKind`](../enumerations/SyntaxKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:598

#### Inherited from

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UpdateOutputFileStampsProject.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UpdateOutputFileStampsProject

# Interface: UpdateOutputFileStampsProject

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5986

## Extends

- [`InvalidatedProjectBase`](InvalidatedProjectBase.md)

## Properties

### kind

> `readonly` **kind**: [`UpdateOutputFileStamps`](../enumerations/InvalidatedProjectKind.md#updateoutputfilestamps)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5987

#### Overrides

[`InvalidatedProjectBase`](InvalidatedProjectBase.md).[`kind`](InvalidatedProjectBase.md#kind)

***

### project

> `readonly` **project**: [`ResolvedConfigFileName`](../type-aliases/ResolvedConfigFileName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5978

#### Inherited from

[`InvalidatedProjectBase`](InvalidatedProjectBase.md).[`project`](InvalidatedProjectBase.md#project)

## Methods

### done()

> **done**(`cancellationToken?`, `writeFile?`, `customTransformers?`): [`ExitStatus`](../enumerations/ExitStatus.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5982

To dispose this project and ensure that all the necessary actions are taken and state is updated accordingly

#### Parameters

##### cancellationToken?

[`CancellationToken`](CancellationToken.md)

##### writeFile?

[`WriteFileCallback`](../type-aliases/WriteFileCallback.md)

##### customTransformers?

[`CustomTransformers`](CustomTransformers.md)

#### Returns

[`ExitStatus`](../enumerations/ExitStatus.md)

#### Inherited from

[`InvalidatedProjectBase`](InvalidatedProjectBase.md).[`done`](InvalidatedProjectBase.md#done)

***

### getCompilerOptions()

> **getCompilerOptions**(): [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5983

#### Returns

[`CompilerOptions`](CompilerOptions.md)

#### Inherited from

[`InvalidatedProjectBase`](InvalidatedProjectBase.md).[`getCompilerOptions`](InvalidatedProjectBase.md#getcompileroptions)

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5984

#### Returns

`string`

#### Inherited from

[`InvalidatedProjectBase`](InvalidatedProjectBase.md).[`getCurrentDirectory`](InvalidatedProjectBase.md#getcurrentdirectory)

***

### updateOutputFileStatmps()

> **updateOutputFileStatmps**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5988

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/UserPreferences.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / UserPreferences

# Interface: UserPreferences

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4475

## Extended by

- [`GetCompletionsAtPositionOptions`](GetCompletionsAtPositionOptions.md)

## Properties

### allowIncompleteCompletions?

> `readonly` `optional` **allowIncompleteCompletions**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4486

***

### allowRenameOfImportPath?

> `readonly` `optional` **allowRenameOfImportPath**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4503

***

### allowTextChangesInNewFiles?

> `readonly` `optional` **allowTextChangesInNewFiles**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4490

***

### autoImportFileExcludePatterns?

> `readonly` `optional` **autoImportFileExcludePatterns**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4504

***

### disableSuggestions?

> `readonly` `optional` **disableSuggestions**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4476

***

### importModuleSpecifierEnding?

> `readonly` `optional` **importModuleSpecifierEnding**: `"index"` \| `"auto"` \| `"minimal"` \| `"js"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4489

Determines whether we import `foo/index.ts` as "foo", "foo/index", or "foo/index.js"

***

### importModuleSpecifierPreference?

> `readonly` `optional` **importModuleSpecifierPreference**: `"shortest"` \| `"project-relative"` \| `"relative"` \| `"non-relative"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4487

***

### includeAutomaticOptionalChainCompletions?

> `readonly` `optional` **includeAutomaticOptionalChainCompletions**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4481

***

### includeCompletionsForImportStatements?

> `readonly` `optional` **includeCompletionsForImportStatements**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4479

***

### includeCompletionsForModuleExports?

> `readonly` `optional` **includeCompletionsForModuleExports**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4478

***

### includeCompletionsWithClassMemberSnippets?

> `readonly` `optional` **includeCompletionsWithClassMemberSnippets**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4483

***

### includeCompletionsWithInsertText?

> `readonly` `optional` **includeCompletionsWithInsertText**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4482

***

### includeCompletionsWithObjectLiteralMethodSnippets?

> `readonly` `optional` **includeCompletionsWithObjectLiteralMethodSnippets**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4484

***

### includeCompletionsWithSnippetText?

> `readonly` `optional` **includeCompletionsWithSnippetText**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4480

***

### includeInlayEnumMemberValueHints?

> `readonly` `optional` **includeInlayEnumMemberValueHints**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4502

***

### includeInlayFunctionLikeReturnTypeHints?

> `readonly` `optional` **includeInlayFunctionLikeReturnTypeHints**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4501

***

### includeInlayFunctionParameterTypeHints?

> `readonly` `optional` **includeInlayFunctionParameterTypeHints**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4497

***

### includeInlayParameterNameHints?

> `readonly` `optional` **includeInlayParameterNameHints**: `"all"` \| `"none"` \| `"literals"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4495

***

### includeInlayParameterNameHintsWhenArgumentMatchesName?

> `readonly` `optional` **includeInlayParameterNameHintsWhenArgumentMatchesName**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4496

***

### includeInlayPropertyDeclarationTypeHints?

> `readonly` `optional` **includeInlayPropertyDeclarationTypeHints**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4500

***

### includeInlayVariableTypeHints?

> `readonly` `optional` **includeInlayVariableTypeHints**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4498

***

### includeInlayVariableTypeHintsWhenTypeMatchesName?

> `readonly` `optional` **includeInlayVariableTypeHintsWhenTypeMatchesName**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4499

***

### includePackageJsonAutoImports?

> `readonly` `optional` **includePackageJsonAutoImports**: `"on"` \| `"off"` \| `"auto"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4492

***

### jsxAttributeCompletionStyle?

> `readonly` `optional` **jsxAttributeCompletionStyle**: `"auto"` \| `"braces"` \| `"none"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4494

***

### providePrefixAndSuffixTextForRename?

> `readonly` `optional` **providePrefixAndSuffixTextForRename**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4491

***

### provideRefactorNotApplicableReason?

> `readonly` `optional` **provideRefactorNotApplicableReason**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4493

***

### quotePreference?

> `readonly` `optional` **quotePreference**: `"auto"` \| `"double"` \| `"single"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4477

***

### useLabelDetailsInCompletionEntries?

> `readonly` `optional` **useLabelDetailsInCompletionEntries**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:4485




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/VariableDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / VariableDeclaration

# Interface: VariableDeclaration

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:746

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

### exclamationToken?

> `readonly` `optional` **exclamationToken**: [`ExclamationToken`](../type-aliases/ExclamationToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:750

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`NamedDeclaration`](NamedDeclaration.md).[`flags`](NamedDeclaration.md#flags)

***

### initializer?

> `readonly` `optional` **initializer**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:752

***

### kind

> `readonly` **kind**: [`VariableDeclaration`](../enumerations/SyntaxKind.md#variabledeclaration)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:747

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

> `readonly` **name**: [`BindingName`](../type-aliases/BindingName.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:749

#### Overrides

[`NamedDeclaration`](NamedDeclaration.md).[`name`](NamedDeclaration.md#name)

***

### parent

> `readonly` **parent**: [`VariableDeclarationList`](VariableDeclarationList.md) \| [`CatchClause`](CatchClause.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:748

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

### type?

> `readonly` `optional` **type**: [`TypeNode`](TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:751

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/VariableDeclarationList.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / VariableDeclarationList

# Interface: VariableDeclarationList

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:754

## Extends

- [`Node`](Node.md)

## Properties

### declarations

> `readonly` **declarations**: [`NodeArray`](NodeArray.md)\<[`VariableDeclaration`](VariableDeclaration.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:757

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

> `readonly` **kind**: [`VariableDeclarationList`](../enumerations/SyntaxKind.md#variabledeclarationlist)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:755

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

> `readonly` **parent**: [`VariableStatement`](VariableStatement.md) \| [`ForStatement`](ForStatement.md) \| [`ForOfStatement`](ForOfStatement.md) \| [`ForInStatement`](ForInStatement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:756

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/VariableStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / VariableStatement

# Interface: VariableStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1498

## Extends

- [`Statement`](Statement.md)

## Properties

### \_statementBrand

> **\_statementBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1471

#### Inherited from

[`Statement`](Statement.md).[`_statementBrand`](Statement.md#_statementbrand)

***

### declarationList

> `readonly` **declarationList**: [`VariableDeclarationList`](VariableDeclarationList.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1501

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

> `readonly` **kind**: [`VariableStatement`](../enumerations/SyntaxKind.md#variablestatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1499

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

> `readonly` `optional` **modifiers**: [`NodeArray`](NodeArray.md)\<[`Modifier`](../type-aliases/Modifier.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1500

#### Deprecated

`modifiers` has been removed from `Node` and moved to the `Node` subtypes that support them.
Use `ts.canHaveModifiers()` to test whether a `Node` can have modifiers.
Use `ts.getModifiers()` to get the modifiers of a `Node`.

For example:
```ts
const modifiers = ts.canHaveModifiers(node) ? ts.getModifiers(node) : undefined;
```

#### Overrides

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/VoidExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / VoidExpression

# Interface: VoidExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1121

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1123

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`UnaryExpression`](UnaryExpression.md).[`flags`](UnaryExpression.md#flags)

***

### kind

> `readonly` **kind**: [`VoidExpression`](../enumerations/SyntaxKind.md#voidexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1122

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/Watch.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / Watch

# Interface: Watch\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5888

## Extended by

- [`WatchOfConfigFile`](WatchOfConfigFile.md)
- [`WatchOfFilesAndCompilerOptions`](WatchOfFilesAndCompilerOptions.md)

## Type Parameters

### T

`T`

## Methods

### close()

> **close**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5892

Closes the watch

#### Returns

`void`

***

### getProgram()

> **getProgram**(): `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5890

Synchronize with host and get updated program

#### Returns

`T`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/WatchCompilerHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / WatchCompilerHost

# Interface: WatchCompilerHost\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5852

Host that has watch functionality used in --watch mode

## Extends

- [`ProgramHost`](ProgramHost.md)\<`T`\>.[`WatchHost`](WatchHost.md)

## Extended by

- [`WatchCompilerHostOfFilesAndCompilerOptions`](WatchCompilerHostOfFilesAndCompilerOptions.md)
- [`WatchCompilerHostOfConfigFile`](WatchCompilerHostOfConfigFile.md)

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

## Methods

### afterProgramCreate()?

> `optional` **afterProgramCreate**(`program`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5858

If provided, callback to invoke after every new program creation

#### Parameters

##### program

`T`

#### Returns

`void`

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5856

If provided, use this method to get parsed command lines for referenced projects

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

### useSourceOfProjectReferenceRedirect()?

> `optional` **useSourceOfProjectReferenceRedirect**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5854

Instead of using output d.ts file from project reference, use its source file

#### Returns

`boolean`

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




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/WatchCompilerHostOfConfigFile.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / WatchCompilerHostOfConfigFile

# Interface: WatchCompilerHostOfConfigFile\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5875

Host to create watch with config file

## Extends

- [`WatchCompilerHost`](WatchCompilerHost.md)\<`T`\>.[`ConfigFileDiagnosticsReporter`](ConfigFileDiagnosticsReporter.md)

## Type Parameters

### T

`T` *extends* [`BuilderProgram`](BuilderProgram.md)

## Properties

### configFileName

> **configFileName**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5877

Name of the config file to compile

***

### createProgram

> **createProgram**: [`CreateProgram`](../type-aliases/CreateProgram.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5812

Used to create the program when need for program creation or recreation detected

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`createProgram`](WatchCompilerHost.md#createprogram)

***

### extraFileExtensions?

> `optional` **extraFileExtensions**: readonly [`FileExtensionInfo`](FileExtensionInfo.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5881

***

### onUnRecoverableConfigFileDiagnostic

> **onUnRecoverableConfigFileDiagnostic**: [`DiagnosticReporter`](../type-aliases/DiagnosticReporter.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5267

Reports unrecoverable error when parsing config file

#### Inherited from

[`ConfigFileDiagnosticsReporter`](ConfigFileDiagnosticsReporter.md).[`onUnRecoverableConfigFileDiagnostic`](ConfigFileDiagnosticsReporter.md#onunrecoverableconfigfilediagnostic)

***

### optionsToExtend?

> `optional` **optionsToExtend**: [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5879

Options to extend

***

### watchOptionsToExtend?

> `optional` **watchOptionsToExtend**: [`WatchOptions`](WatchOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5880

## Methods

### afterProgramCreate()?

> `optional` **afterProgramCreate**(`program`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5858

If provided, callback to invoke after every new program creation

#### Parameters

##### program

`T`

#### Returns

`void`

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`afterProgramCreate`](WatchCompilerHost.md#afterprogramcreate)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`clearTimeout`](WatchCompilerHost.md#cleartimeout)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`createHash`](WatchCompilerHost.md#createhash)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`directoryExists`](WatchCompilerHost.md#directoryexists)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`fileExists`](WatchCompilerHost.md#fileexists)

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5815

#### Returns

`string`

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`getCurrentDirectory`](WatchCompilerHost.md#getcurrentdirectory)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`getDefaultLibFileName`](WatchCompilerHost.md#getdefaultlibfilename)

***

### getDefaultLibLocation()?

> `optional` **getDefaultLibLocation**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5817

#### Returns

`string`

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`getDefaultLibLocation`](WatchCompilerHost.md#getdefaultliblocation)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`getDirectories`](WatchCompilerHost.md#getdirectories)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`getEnvironmentVariable`](WatchCompilerHost.md#getenvironmentvariable)

***

### getModuleResolutionCache()?

> `optional` **getModuleResolutionCache**(): `undefined` \| [`ModuleResolutionCache`](ModuleResolutionCache.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5850

Returns the module resolution cache used by a provided `resolveModuleNames` implementation so that any non-name module resolution operations (eg, package.json lookup) can reuse it

#### Returns

`undefined` \| [`ModuleResolutionCache`](ModuleResolutionCache.md)

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`getModuleResolutionCache`](WatchCompilerHost.md#getmoduleresolutioncache)

***

### getNewLine()

> **getNewLine**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5814

#### Returns

`string`

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`getNewLine`](WatchCompilerHost.md#getnewline)

***

### getParsedCommandLine()?

> `optional` **getParsedCommandLine**(`fileName`): `undefined` \| [`ParsedCommandLine`](ParsedCommandLine.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5856

If provided, use this method to get parsed command lines for referenced projects

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| [`ParsedCommandLine`](ParsedCommandLine.md)

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`getParsedCommandLine`](WatchCompilerHost.md#getparsedcommandline)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`hasInvalidatedResolutions`](WatchCompilerHost.md#hasinvalidatedresolutions)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`onWatchStatusChange`](WatchCompilerHost.md#onwatchstatuschange)

***

### readDirectory()

> **readDirectory**(`path`, `extensions?`, `exclude?`, `include?`, `depth?`): `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5886

Used to generate source file names from the config file and its include, exclude, files rules
and also to cache the directory stucture

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

#### Overrides

[`WatchCompilerHost`](WatchCompilerHost.md).[`readDirectory`](WatchCompilerHost.md#readdirectory)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`readFile`](WatchCompilerHost.md#readfile)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`realpath`](WatchCompilerHost.md#realpath)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`resolveModuleNames`](WatchCompilerHost.md#resolvemodulenames)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`resolveTypeReferenceDirectives`](WatchCompilerHost.md#resolvetypereferencedirectives)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`setTimeout`](WatchCompilerHost.md#settimeout)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`trace`](WatchCompilerHost.md#trace)

***

### useCaseSensitiveFileNames()

> **useCaseSensitiveFileNames**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5813

#### Returns

`boolean`

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`useCaseSensitiveFileNames`](WatchCompilerHost.md#usecasesensitivefilenames)

***

### useSourceOfProjectReferenceRedirect()?

> `optional` **useSourceOfProjectReferenceRedirect**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5854

Instead of using output d.ts file from project reference, use its source file

#### Returns

`boolean`

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`useSourceOfProjectReferenceRedirect`](WatchCompilerHost.md#usesourceofprojectreferenceredirect)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`watchDirectory`](WatchCompilerHost.md#watchdirectory)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`watchFile`](WatchCompilerHost.md#watchfile)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/WatchCompilerHostOfFilesAndCompilerOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / WatchCompilerHostOfFilesAndCompilerOptions

# Interface: WatchCompilerHostOfFilesAndCompilerOptions\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5863

Host to create watch with root files and options

## Extends

- [`WatchCompilerHost`](WatchCompilerHost.md)\<`T`\>

## Type Parameters

### T

`T` *extends* [`BuilderProgram`](BuilderProgram.md)

## Properties

### createProgram

> **createProgram**: [`CreateProgram`](../type-aliases/CreateProgram.md)\<`T`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5812

Used to create the program when need for program creation or recreation detected

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`createProgram`](WatchCompilerHost.md#createprogram)

***

### options

> **options**: [`CompilerOptions`](CompilerOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5867

Compiler options

***

### projectReferences?

> `optional` **projectReferences**: readonly [`ProjectReference`](ProjectReference.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5870

Project References

***

### rootFiles

> **rootFiles**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5865

root files to use to generate program

***

### watchOptions?

> `optional` **watchOptions**: [`WatchOptions`](WatchOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5868

## Methods

### afterProgramCreate()?

> `optional` **afterProgramCreate**(`program`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5858

If provided, callback to invoke after every new program creation

#### Parameters

##### program

`T`

#### Returns

`void`

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`afterProgramCreate`](WatchCompilerHost.md#afterprogramcreate)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`clearTimeout`](WatchCompilerHost.md#cleartimeout)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`createHash`](WatchCompilerHost.md#createhash)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`directoryExists`](WatchCompilerHost.md#directoryexists)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`fileExists`](WatchCompilerHost.md#fileexists)

***

### getCurrentDirectory()

> **getCurrentDirectory**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5815

#### Returns

`string`

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`getCurrentDirectory`](WatchCompilerHost.md#getcurrentdirectory)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`getDefaultLibFileName`](WatchCompilerHost.md#getdefaultlibfilename)

***

### getDefaultLibLocation()?

> `optional` **getDefaultLibLocation**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5817

#### Returns

`string`

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`getDefaultLibLocation`](WatchCompilerHost.md#getdefaultliblocation)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`getDirectories`](WatchCompilerHost.md#getdirectories)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`getEnvironmentVariable`](WatchCompilerHost.md#getenvironmentvariable)

***

### getModuleResolutionCache()?

> `optional` **getModuleResolutionCache**(): `undefined` \| [`ModuleResolutionCache`](ModuleResolutionCache.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5850

Returns the module resolution cache used by a provided `resolveModuleNames` implementation so that any non-name module resolution operations (eg, package.json lookup) can reuse it

#### Returns

`undefined` \| [`ModuleResolutionCache`](ModuleResolutionCache.md)

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`getModuleResolutionCache`](WatchCompilerHost.md#getmoduleresolutioncache)

***

### getNewLine()

> **getNewLine**(): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5814

#### Returns

`string`

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`getNewLine`](WatchCompilerHost.md#getnewline)

***

### getParsedCommandLine()?

> `optional` **getParsedCommandLine**(`fileName`): `undefined` \| [`ParsedCommandLine`](ParsedCommandLine.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5856

If provided, use this method to get parsed command lines for referenced projects

#### Parameters

##### fileName

`string`

#### Returns

`undefined` \| [`ParsedCommandLine`](ParsedCommandLine.md)

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`getParsedCommandLine`](WatchCompilerHost.md#getparsedcommandline)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`hasInvalidatedResolutions`](WatchCompilerHost.md#hasinvalidatedresolutions)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`onWatchStatusChange`](WatchCompilerHost.md#onwatchstatuschange)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`readDirectory`](WatchCompilerHost.md#readdirectory)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`readFile`](WatchCompilerHost.md#readfile)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`realpath`](WatchCompilerHost.md#realpath)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`resolveModuleNames`](WatchCompilerHost.md#resolvemodulenames)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`resolveTypeReferenceDirectives`](WatchCompilerHost.md#resolvetypereferencedirectives)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`setTimeout`](WatchCompilerHost.md#settimeout)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`trace`](WatchCompilerHost.md#trace)

***

### useCaseSensitiveFileNames()

> **useCaseSensitiveFileNames**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5813

#### Returns

`boolean`

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`useCaseSensitiveFileNames`](WatchCompilerHost.md#usecasesensitivefilenames)

***

### useSourceOfProjectReferenceRedirect()?

> `optional` **useSourceOfProjectReferenceRedirect**(): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5854

Instead of using output d.ts file from project reference, use its source file

#### Returns

`boolean`

#### Inherited from

[`WatchCompilerHost`](WatchCompilerHost.md).[`useSourceOfProjectReferenceRedirect`](WatchCompilerHost.md#usesourceofprojectreferenceredirect)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`watchDirectory`](WatchCompilerHost.md#watchdirectory)

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

[`WatchCompilerHost`](WatchCompilerHost.md).[`watchFile`](WatchCompilerHost.md#watchfile)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/WatchHost.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / WatchHost

# Interface: WatchHost

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5796

Host that has watch functionality used in --watch mode

## Extended by

- [`WatchCompilerHost`](WatchCompilerHost.md)
- [`SolutionBuilderWithWatchHost`](SolutionBuilderWithWatchHost.md)

## Methods

### clearTimeout()?

> `optional` **clearTimeout**(`timeoutId`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5806

If provided, will be used to reset existing delayed compilation

#### Parameters

##### timeoutId

`any`

#### Returns

`void`

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




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/WatchOfConfigFile.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / WatchOfConfigFile

# Interface: WatchOfConfigFile\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5897

Creates the watch what generates program using the config file

## Extends

- [`Watch`](Watch.md)\<`T`\>

## Type Parameters

### T

`T`

## Methods

### close()

> **close**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5892

Closes the watch

#### Returns

`void`

#### Inherited from

[`Watch`](Watch.md).[`close`](Watch.md#close)

***

### getProgram()

> **getProgram**(): `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5890

Synchronize with host and get updated program

#### Returns

`T`

#### Inherited from

[`Watch`](Watch.md).[`getProgram`](Watch.md#getprogram)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/WatchOfFilesAndCompilerOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / WatchOfFilesAndCompilerOptions

# Interface: WatchOfFilesAndCompilerOptions\<T\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5902

Creates the watch that generates program using the root files and compiler options

## Extends

- [`Watch`](Watch.md)\<`T`\>

## Type Parameters

### T

`T`

## Methods

### close()

> **close**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5892

Closes the watch

#### Returns

`void`

#### Inherited from

[`Watch`](Watch.md).[`close`](Watch.md#close)

***

### getProgram()

> **getProgram**(): `T`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5890

Synchronize with host and get updated program

#### Returns

`T`

#### Inherited from

[`Watch`](Watch.md).[`getProgram`](Watch.md#getprogram)

***

### updateRootFileNames()

> **updateRootFileNames**(`fileNames`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:5904

Updates the root files in the program, only if this is not config file compilation

#### Parameters

##### fileNames

`string`[]

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/WatchOptions.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / WatchOptions

# Interface: WatchOptions

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3225

## Indexable

\[`option`: `string`\]: [`CompilerOptionsValue`](../type-aliases/CompilerOptionsValue.md)

## Properties

### excludeDirectories?

> `optional` **excludeDirectories**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3230

***

### excludeFiles?

> `optional` **excludeFiles**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3231

***

### fallbackPolling?

> `optional` **fallbackPolling**: [`PollingWatchKind`](../enumerations/PollingWatchKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3228

***

### synchronousWatchDirectory?

> `optional` **synchronousWatchDirectory**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3229

***

### watchDirectory?

> `optional` **watchDirectory**: [`WatchDirectoryKind`](../enumerations/WatchDirectoryKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3227

***

### watchFile?

> `optional` **watchFile**: [`WatchFileKind`](../enumerations/WatchFileKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:3226




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/WhileStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / WhileStatement

# Interface: WhileStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1520

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1522

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`IterationStatement`](IterationStatement.md).[`flags`](IterationStatement.md#flags)

***

### kind

> `readonly` **kind**: [`WhileStatement`](../enumerations/SyntaxKind.md#whilestatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1521

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/WithStatement.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / WithStatement

# Interface: WithStatement

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1556

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

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1558

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Statement`](Statement.md).[`flags`](Statement.md#flags)

***

### kind

> `readonly` **kind**: [`WithStatement`](../enumerations/SyntaxKind.md#withstatement)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1557

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

### statement

> `readonly` **statement**: [`Statement`](Statement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1559

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
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/WriteFileCallbackData.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / WriteFileCallbackData

# Interface: WriteFileCallbackData

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:2255




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/interfaces/YieldExpression.md`
============================================================

[**ArkAnalyzer**](../../../../README.md)

***

[ArkAnalyzer](../../../../globals.md) / [ts](../README.md) / YieldExpression

# Interface: YieldExpression

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1129

## Extends

- [`Expression`](Expression.md)

## Properties

### \_expressionBrand

> **\_expressionBrand**: `any`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1056

#### Inherited from

[`Expression`](Expression.md).[`_expressionBrand`](Expression.md#_expressionbrand)

***

### asteriskToken?

> `readonly` `optional` **asteriskToken**: [`AsteriskToken`](../type-aliases/AsteriskToken.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1131

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

### expression?

> `readonly` `optional` **expression**: [`Expression`](Expression.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1132

***

### flags

> `readonly` **flags**: [`NodeFlags`](../enumerations/NodeFlags.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:599

#### Inherited from

[`Expression`](Expression.md).[`flags`](Expression.md#flags)

***

### kind

> `readonly` **kind**: [`YieldExpression`](../enumerations/SyntaxKind.md#yieldexpression)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:1130

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
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/README.md`
============================================================

[**ArkAnalyzer**](../../../../../README.md)

***

[ArkAnalyzer](../../../../../globals.md) / [ts](../../README.md) / ArkTSLinter\_1\_0

# ArkTSLinter\_1\_0

## Namespaces

- [Autofixer](namespaces/Autofixer/README.md)
- [Common](namespaces/Common/README.md)
- [DiagnosticCheckerNamespace](namespaces/DiagnosticCheckerNamespace/README.md)
- [LibraryTypeCallDiagnosticCheckerNamespace](namespaces/LibraryTypeCallDiagnosticCheckerNamespace/README.md)
- [Problems](namespaces/Problems/README.md)
- [Utils](namespaces/Utils/README.md)

## Classes

- [LinterConfig](classes/LinterConfig.md)
- [TSCCompiledProgram](classes/TSCCompiledProgram.md)
- [TypeScriptLinter](classes/TypeScriptLinter.md)

## Interfaces

- [ProblemInfo](interfaces/ProblemInfo.md)

## Variables

- [cookBookMsg](variables/cookBookMsg.md)
- [cookBookTag](variables/cookBookTag.md)

## Functions

- [runArkTSLinter](functions/runArkTSLinter.md)
- [translateDiag](functions/translateDiag.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/classes/LinterConfig.md`
============================================================

[**ArkAnalyzer**](../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../globals.md) / [ts](../../../README.md) / [ArkTSLinter\_1\_0](../README.md) / LinterConfig

# Class: LinterConfig

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8897

## Constructors

### Constructor

> **new LinterConfig**(): `LinterConfig`

#### Returns

`LinterConfig`

## Properties

### incrementOnlyTokens

> `static` **incrementOnlyTokens**: [`ESMap`](../../../interfaces/ESMap.md)\<[`SyntaxKind`](../../../enumerations/SyntaxKind.md), [`FaultID`](../namespaces/Problems/enumerations/FaultID.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8902

***

### nodeDesc

> `static` **nodeDesc**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8898

***

### terminalTokens

> `static` **terminalTokens**: [`Set`](../../../interfaces/Set.md)\<[`SyntaxKind`](../../../enumerations/SyntaxKind.md)\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8901

***

### tsSyntaxKindNames

> `static` **tsSyntaxKindNames**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8899

## Methods

### initStatic()

> `static` **initStatic**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8900

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/classes/TSCCompiledProgram.md`
============================================================

[**ArkAnalyzer**](../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../globals.md) / [ts](../../../README.md) / [ArkTSLinter\_1\_0](../README.md) / TSCCompiledProgram

# Class: TSCCompiledProgram

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:9044

## Constructors

### Constructor

> **new TSCCompiledProgram**(`program`): `TSCCompiledProgram`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:9046

#### Parameters

##### program

[`BuilderProgram`](../../../interfaces/BuilderProgram.md)

#### Returns

`TSCCompiledProgram`

## Methods

### doAllGetDiagnostics()

> **doAllGetDiagnostics**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:9050

#### Returns

`void`

***

### getBuilderProgram()

> **getBuilderProgram**(): [`BuilderProgram`](../../../interfaces/BuilderProgram.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:9048

#### Returns

[`BuilderProgram`](../../../interfaces/BuilderProgram.md)

***

### getProgram()

> **getProgram**(): [`Program`](../../../interfaces/Program.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:9047

#### Returns

[`Program`](../../../interfaces/Program.md)

***

### getStrictDiagnostics()

> **getStrictDiagnostics**(`fileName`): [`Diagnostic`](../../../interfaces/Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:9049

#### Parameters

##### fileName

`string`

#### Returns

[`Diagnostic`](../../../interfaces/Diagnostic.md)[]




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/classes/TypeScriptLinter.md`
============================================================

[**ArkAnalyzer**](../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../globals.md) / [ts](../../../README.md) / [ArkTSLinter\_1\_0](../README.md) / TypeScriptLinter

# Class: TypeScriptLinter

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8924

## Constructors

### Constructor

> **new TypeScriptLinter**(`sourceFile`, `tsProgram`, `tscStrictDiagnostics?`): `TypeScriptLinter`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8950

#### Parameters

##### sourceFile

[`SourceFile`](../../../interfaces/SourceFile.md)

##### tsProgram

[`Program`](../../../interfaces/Program.md)

##### tscStrictDiagnostics?

[`Map`](../../../interfaces/Map.md)\<[`Diagnostic`](../../../interfaces/Diagnostic.md)[]\>

#### Returns

`TypeScriptLinter`

## Properties

### currentErrorLine

> **currentErrorLine**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8945

***

### currentWarningLine

> **currentWarningLine**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8946

***

### handlersMap

> `readonly` **handlersMap**: [`ESMap`](../../../interfaces/ESMap.md)\<[`SyntaxKind`](../../../enumerations/SyntaxKind.md), (`node`) => `void`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8952

***

### libraryTypeCallDiagnosticChecker

> **libraryTypeCallDiagnosticChecker**: [`LibraryTypeCallDiagnosticChecker`](../namespaces/LibraryTypeCallDiagnosticCheckerNamespace/classes/LibraryTypeCallDiagnosticChecker.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8948

***

### skipArkTSStaticBlocksCheck

> **skipArkTSStaticBlocksCheck**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8949

***

### staticBlocks

> **staticBlocks**: [`Set`](../../../interfaces/Set.md)\<`string`\>

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8947

***

### errorLineNumbersString

> `static` **errorLineNumbersString**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8936

***

### filteredDiagnosticMessages

> `static` **filteredDiagnosticMessages**: [`DiagnosticMessageChain`](../../../interfaces/DiagnosticMessageChain.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8941

***

### ideMode

> `static` **ideMode**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8927

***

### lineCounters

> `static` **lineCounters**: `number`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8934

***

### lintEtsOnly

> `static` **lintEtsOnly**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8931

***

### logTscErrors

> `static` **logTscErrors**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8929

***

### nodeCounters

> `static` **nodeCounters**: `number`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8933

***

### problemsInfos

> `static` **problemsInfos**: [`ProblemInfo`](../interfaces/ProblemInfo.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8940

***

### reportDiagnostics

> `static` **reportDiagnostics**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8939

***

### strictMode

> `static` **strictMode**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8928

***

### totalErrorLines

> `static` **totalErrorLines**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8935

***

### totalVisitedNodes

> `static` **totalVisitedNodes**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8932

***

### totalWarningLines

> `static` **totalWarningLines**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8937

***

### tsTypeChecker

> `static` **tsTypeChecker**: [`TypeChecker`](../../../interfaces/TypeChecker.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8944

***

### warningLineNumbersString

> `static` **warningLineNumbersString**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8938

***

### warningsAsErrors

> `static` **warningsAsErrors**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8930

## Methods

### incrementCounters()

> **incrementCounters**(`node`, `faultId`, `autofixable?`, `autofix?`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8953

#### Parameters

##### node

[`Node`](../../../interfaces/Node.md) | [`CommentRange`](../../../interfaces/CommentRange.md)

##### faultId

`number`

##### autofixable?

`boolean`

##### autofix?

[`Autofix`](../namespaces/Autofixer/interfaces/Autofix.md)[]

#### Returns

`void`

***

### lint()

> **lint**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:9038

#### Returns

`void`

***

### visitTSNode()

> **visitTSNode**(`node`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8954

#### Parameters

##### node

[`Node`](../../../interfaces/Node.md)

#### Returns

`void`

***

### clearTsTypeChecker()

> `static` **clearTsTypeChecker**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8951

#### Returns

`void`

***

### initGlobals()

> `static` **initGlobals**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8942

#### Returns

`void`

***

### initStatic()

> `static` **initStatic**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8943

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/functions/runArkTSLinter.md`
============================================================

[**ArkAnalyzer**](../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../globals.md) / [ts](../../../README.md) / [ArkTSLinter\_1\_0](../README.md) / runArkTSLinter

# Function: runArkTSLinter()

> **runArkTSLinter**(`tsBuilderProgram`, `srcFile?`, `buildInfoWriteFile?`, `arkTSVersion?`): [`Diagnostic`](../../../interfaces/Diagnostic.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:9057

## Parameters

### tsBuilderProgram

[`BuilderProgram`](../../../interfaces/BuilderProgram.md)

### srcFile?

[`SourceFile`](../../../interfaces/SourceFile.md)

### buildInfoWriteFile?

[`WriteFileCallback`](../../../type-aliases/WriteFileCallback.md)

### arkTSVersion?

`string`

## Returns

[`Diagnostic`](../../../interfaces/Diagnostic.md)[]




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/functions/translateDiag.md`
============================================================

[**ArkAnalyzer**](../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../globals.md) / [ts](../../../README.md) / [ArkTSLinter\_1\_0](../README.md) / translateDiag

# Function: translateDiag()

> **translateDiag**(`srcFile`, `problemInfo`): [`Diagnostic`](../../../interfaces/Diagnostic.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:9056

## Parameters

### srcFile

[`SourceFile`](../../../interfaces/SourceFile.md)

### problemInfo

[`ProblemInfo`](../interfaces/ProblemInfo.md)

## Returns

[`Diagnostic`](../../../interfaces/Diagnostic.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/interfaces/ProblemInfo.md`
============================================================

[**ArkAnalyzer**](../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../globals.md) / [ts](../../../README.md) / [ArkTSLinter\_1\_0](../README.md) / ProblemInfo

# Interface: ProblemInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8910

## Properties

### autofix?

> `optional` **autofix**: [`Autofix`](../namespaces/Autofixer/interfaces/Autofix.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8922

***

### autofixable

> **autofixable**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8921

***

### column

> **column**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8912

***

### end

> **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8914

***

### line

> **line**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8911

***

### problem

> **problem**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8917

***

### rule

> **rule**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8919

***

### ruleTag

> **ruleTag**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8920

***

### severity

> **severity**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8916

***

### start

> **start**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8913

***

### suggest

> **suggest**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8918

***

### type

> **type**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8915




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Autofixer/README.md`
============================================================

[**ArkAnalyzer**](../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../globals.md) / [ts](../../../../README.md) / [ArkTSLinter\_1\_0](../../README.md) / Autofixer

# Autofixer

## Interfaces

- [Autofix](interfaces/Autofix.md)

## Variables

- [AUTOFIX\_ALL](variables/AUTOFIX_ALL.md)
- [autofixInfo](variables/autofixInfo.md)

## Functions

- [fixCtorParameterProperties](functions/fixCtorParameterProperties.md)
- [fixFunctionExpression](functions/fixFunctionExpression.md)
- [fixLiteralAsPropertyName](functions/fixLiteralAsPropertyName.md)
- [fixPropertyAccessByIndex](functions/fixPropertyAccessByIndex.md)
- [fixReturnType](functions/fixReturnType.md)
- [shouldAutofix](functions/shouldAutofix.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Autofixer/functions/fixCtorParameterProperties.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Autofixer](../README.md) / fixCtorParameterProperties

# Function: fixCtorParameterProperties()

> **fixCtorParameterProperties**(`ctorDecl`, `paramTypes`): `undefined` \| [`Autofix`](../interfaces/Autofix.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8890

## Parameters

### ctorDecl

[`ConstructorDeclaration`](../../../../../interfaces/ConstructorDeclaration.md)

### paramTypes

[`TypeNode`](../../../../../interfaces/TypeNode.md)[]

## Returns

`undefined` \| [`Autofix`](../interfaces/Autofix.md)[]




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Autofixer/functions/fixFunctionExpression.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Autofixer](../README.md) / fixFunctionExpression

# Function: fixFunctionExpression()

> **fixFunctionExpression**(`funcExpr`, `params?`, `retType?`): [`Autofix`](../interfaces/Autofix.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8888

## Parameters

### funcExpr

[`FunctionExpression`](../../../../../interfaces/FunctionExpression.md)

### params?

[`NodeArray`](../../../../../interfaces/NodeArray.md)\<[`ParameterDeclaration`](../../../../../interfaces/ParameterDeclaration.md)\>

### retType?

[`TypeNode`](../../../../../interfaces/TypeNode.md)

## Returns

[`Autofix`](../interfaces/Autofix.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Autofixer/functions/fixLiteralAsPropertyName.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Autofixer](../README.md) / fixLiteralAsPropertyName

# Function: fixLiteralAsPropertyName()

> **fixLiteralAsPropertyName**(`node`): `undefined` \| [`Autofix`](../interfaces/Autofix.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8886

## Parameters

### node

[`Node`](../../../../../interfaces/Node.md)

## Returns

`undefined` \| [`Autofix`](../interfaces/Autofix.md)[]




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Autofixer/functions/fixPropertyAccessByIndex.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Autofixer](../README.md) / fixPropertyAccessByIndex

# Function: fixPropertyAccessByIndex()

> **fixPropertyAccessByIndex**(`node`): `undefined` \| [`Autofix`](../interfaces/Autofix.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8887

## Parameters

### node

[`Node`](../../../../../interfaces/Node.md)

## Returns

`undefined` \| [`Autofix`](../interfaces/Autofix.md)[]




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Autofixer/functions/fixReturnType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Autofixer](../README.md) / fixReturnType

# Function: fixReturnType()

> **fixReturnType**(`funcLikeDecl`, `typeNode`): [`Autofix`](../interfaces/Autofix.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8889

## Parameters

### funcLikeDecl

[`FunctionLikeDeclaration`](../../../../../type-aliases/FunctionLikeDeclaration.md)

### typeNode

[`TypeNode`](../../../../../interfaces/TypeNode.md)

## Returns

[`Autofix`](../interfaces/Autofix.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Autofixer/functions/shouldAutofix.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Autofixer](../README.md) / shouldAutofix

# Function: shouldAutofix()

> **shouldAutofix**(`node`, `faultID`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8880

## Parameters

### node

[`Node`](../../../../../interfaces/Node.md)

### faultID

[`FaultID`](../../Problems/enumerations/FaultID.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Autofixer/interfaces/Autofix.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Autofixer](../README.md) / Autofix

# Interface: Autofix

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8881

## Properties

### end

> **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8884

***

### replacementText

> **replacementText**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8882

***

### start

> **start**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8883




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Autofixer/variables/AUTOFIX_ALL.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Autofixer](../README.md) / AUTOFIX\_ALL

# Variable: AUTOFIX\_ALL

> `const` **AUTOFIX\_ALL**: [`AutofixInfo`](../../Common/interfaces/AutofixInfo.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8878




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Autofixer/variables/autofixInfo.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Autofixer](../README.md) / autofixInfo

# Variable: autofixInfo

> `const` **autofixInfo**: [`AutofixInfo`](../../Common/interfaces/AutofixInfo.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8879




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Common/README.md`
============================================================

[**ArkAnalyzer**](../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../globals.md) / [ts](../../../../README.md) / [ArkTSLinter\_1\_0](../../README.md) / Common

# Common

## Interfaces

- [AutofixInfo](interfaces/AutofixInfo.md)
- [CommandLineOptions](interfaces/CommandLineOptions.md)
- [LintOptions](interfaces/LintOptions.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Common/interfaces/AutofixInfo.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Common](../README.md) / AutofixInfo

# Interface: AutofixInfo

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8568

## Properties

### end

> **end**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8571

***

### problemID

> **problemID**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8569

***

### start

> **start**: `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8570




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Common/interfaces/CommandLineOptions.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Common](../README.md) / CommandLineOptions

# Interface: CommandLineOptions

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8573

## Properties

### autofixInfo?

> `optional` **autofixInfo**: [`AutofixInfo`](AutofixInfo.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8580

***

### ideMode?

> `optional` **ideMode**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8575

***

### inputFiles

> **inputFiles**: `string`[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8579

***

### logTscErrors?

> `optional` **logTscErrors**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8576

***

### parsedConfigFile?

> `optional` **parsedConfigFile**: [`ParsedCommandLine`](../../../../../interfaces/ParsedCommandLine.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8578

***

### strictMode?

> `optional` **strictMode**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8574

***

### warningsAsErrors

> **warningsAsErrors**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8577




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Common/interfaces/LintOptions.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Common](../README.md) / LintOptions

# Interface: LintOptions

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8582

## Indexable

\[`key`: `string`\]: `any`

## Properties

### cmdOptions

> **cmdOptions**: [`CommandLineOptions`](CommandLineOptions.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8583

***

### tsProgram?

> `optional` **tsProgram**: [`Program`](../../../../../interfaces/Program.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8584




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/DiagnosticCheckerNamespace/README.md`
============================================================

[**ArkAnalyzer**](../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../globals.md) / [ts](../../../../README.md) / [ArkTSLinter\_1\_0](../../README.md) / DiagnosticCheckerNamespace

# DiagnosticCheckerNamespace

## Interfaces

- [DiagnosticChecker](interfaces/DiagnosticChecker.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/DiagnosticCheckerNamespace/interfaces/DiagnosticChecker.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [DiagnosticCheckerNamespace](../README.md) / DiagnosticChecker

# Interface: DiagnosticChecker

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8599

## Methods

### checkDiagnosticMessage()

> **checkDiagnosticMessage**(`msgText`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8600

#### Parameters

##### msgText

`string` | [`DiagnosticMessageChain`](../../../../../interfaces/DiagnosticMessageChain.md)

#### Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/LibraryTypeCallDiagnosticCheckerNamespace/README.md`
============================================================

[**ArkAnalyzer**](../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../globals.md) / [ts](../../../../README.md) / [ArkTSLinter\_1\_0](../../README.md) / LibraryTypeCallDiagnosticCheckerNamespace

# LibraryTypeCallDiagnosticCheckerNamespace

## Classes

- [LibraryTypeCallDiagnosticChecker](classes/LibraryTypeCallDiagnosticChecker.md)

## Variables

- [ARGUMENT\_OF\_TYPE\_0\_IS\_NOT\_ASSIGNABLE\_TO\_PARAMETER\_OF\_TYPE\_1\_ERROR\_CODE](variables/ARGUMENT_OF_TYPE_0_IS_NOT_ASSIGNABLE_TO_PARAMETER_OF_TYPE_1_ERROR_CODE.md)
- [ARGUMENT\_OF\_TYPE\_NULL\_IS\_NOT\_ASSIGNABLE\_TO\_PARAMETER\_OF\_TYPE\_1\_RE](variables/ARGUMENT_OF_TYPE_NULL_IS_NOT_ASSIGNABLE_TO_PARAMETER_OF_TYPE_1_RE.md)
- [ARGUMENT\_OF\_TYPE\_UNDEFINED\_IS\_NOT\_ASSIGNABLE\_TO\_PARAMETER\_OF\_TYPE\_1\_RE](variables/ARGUMENT_OF_TYPE_UNDEFINED_IS_NOT_ASSIGNABLE_TO_PARAMETER_OF_TYPE_1_RE.md)
- [NO\_OVERLOAD\_MATCHES\_THIS\_CALL\_ERROR\_CODE](variables/NO_OVERLOAD_MATCHES_THIS_CALL_ERROR_CODE.md)
- [TYPE\_0\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_ERROR\_CODE](variables/TYPE_0_IS_NOT_ASSIGNABLE_TO_TYPE_1_ERROR_CODE.md)
- [TYPE\_NULL\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_RE](variables/TYPE_NULL_IS_NOT_ASSIGNABLE_TO_TYPE_1_RE.md)
- [TYPE\_UNDEFINED\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_RE](variables/TYPE_UNDEFINED_IS_NOT_ASSIGNABLE_TO_TYPE_1_RE.md)
- [TYPE\_UNKNOWN\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_RE](variables/TYPE_UNKNOWN_IS_NOT_ASSIGNABLE_TO_TYPE_1_RE.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/LibraryTypeCallDiagnosticCheckerNamespace/classes/LibraryTypeCallDiagnosticChecker.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [LibraryTypeCallDiagnosticCheckerNamespace](../README.md) / LibraryTypeCallDiagnosticChecker

# Class: LibraryTypeCallDiagnosticChecker

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8617

## Implements

- [`DiagnosticChecker`](../../DiagnosticCheckerNamespace/interfaces/DiagnosticChecker.md)

## Constructors

### Constructor

> **new LibraryTypeCallDiagnosticChecker**(`filteredDiagnosticMessages`): `LibraryTypeCallDiagnosticChecker`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8621

#### Parameters

##### filteredDiagnosticMessages

[`DiagnosticMessageChain`](../../../../../interfaces/DiagnosticMessageChain.md)[]

#### Returns

`LibraryTypeCallDiagnosticChecker`

## Properties

### diagnosticMessages

> **diagnosticMessages**: `undefined` \| [`DiagnosticMessageChain`](../../../../../interfaces/DiagnosticMessageChain.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8619

***

### filteredDiagnosticMessages

> **filteredDiagnosticMessages**: [`DiagnosticMessageChain`](../../../../../interfaces/DiagnosticMessageChain.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8620

***

### inLibCall

> **inLibCall**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8618

## Methods

### checkDiagnosticMessage()

> **checkDiagnosticMessage**(`msgText`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8626

#### Parameters

##### msgText

`string` | [`DiagnosticMessageChain`](../../../../../interfaces/DiagnosticMessageChain.md)

#### Returns

`boolean`

#### Implementation of

[`DiagnosticChecker`](../../DiagnosticCheckerNamespace/interfaces/DiagnosticChecker.md).[`checkDiagnosticMessage`](../../DiagnosticCheckerNamespace/interfaces/DiagnosticChecker.md#checkdiagnosticmessage)

***

### checkFilteredDiagnosticMessages()

> **checkFilteredDiagnosticMessages**(`msgText`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8625

#### Parameters

##### msgText

`string` | [`DiagnosticMessageChain`](../../../../../interfaces/DiagnosticMessageChain.md)

#### Returns

`boolean`

***

### checkMessageChain()

> **checkMessageChain**(`chain`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8624

#### Parameters

##### chain

[`DiagnosticMessageChain`](../../../../../interfaces/DiagnosticMessageChain.md)

#### Returns

`boolean`

***

### checkMessageText()

> **checkMessageText**(`msg`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8623

#### Parameters

##### msg

`string`

#### Returns

`boolean`

***

### configure()

> **configure**(`inLibCall`, `diagnosticMessages`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8622

#### Parameters

##### inLibCall

`boolean`

##### diagnosticMessages

[`DiagnosticMessageChain`](../../../../../interfaces/DiagnosticMessageChain.md)[]

#### Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/LibraryTypeCallDiagnosticCheckerNamespace/variables/ARGUMENT_OF_TYPE_0_IS_NOT_ASSIGNABLE_TO_PARAMETER_OF_TYPE_1_ERROR_CODE.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [LibraryTypeCallDiagnosticCheckerNamespace](../README.md) / ARGUMENT\_OF\_TYPE\_0\_IS\_NOT\_ASSIGNABLE\_TO\_PARAMETER\_OF\_TYPE\_1\_ERROR\_CODE

# Variable: ARGUMENT\_OF\_TYPE\_0\_IS\_NOT\_ASSIGNABLE\_TO\_PARAMETER\_OF\_TYPE\_1\_ERROR\_CODE

> `const` **ARGUMENT\_OF\_TYPE\_0\_IS\_NOT\_ASSIGNABLE\_TO\_PARAMETER\_OF\_TYPE\_1\_ERROR\_CODE**: `2345` = `2345`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8613




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/LibraryTypeCallDiagnosticCheckerNamespace/variables/ARGUMENT_OF_TYPE_NULL_IS_NOT_ASSIGNABLE_TO_PARAMETER_OF_TYPE_1_RE.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [LibraryTypeCallDiagnosticCheckerNamespace](../README.md) / ARGUMENT\_OF\_TYPE\_NULL\_IS\_NOT\_ASSIGNABLE\_TO\_PARAMETER\_OF\_TYPE\_1\_RE

# Variable: ARGUMENT\_OF\_TYPE\_NULL\_IS\_NOT\_ASSIGNABLE\_TO\_PARAMETER\_OF\_TYPE\_1\_RE

> `const` **ARGUMENT\_OF\_TYPE\_NULL\_IS\_NOT\_ASSIGNABLE\_TO\_PARAMETER\_OF\_TYPE\_1\_RE**: `RegExp`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8614




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/LibraryTypeCallDiagnosticCheckerNamespace/variables/ARGUMENT_OF_TYPE_UNDEFINED_IS_NOT_ASSIGNABLE_TO_PARAMETER_OF_TYPE_1_RE.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [LibraryTypeCallDiagnosticCheckerNamespace](../README.md) / ARGUMENT\_OF\_TYPE\_UNDEFINED\_IS\_NOT\_ASSIGNABLE\_TO\_PARAMETER\_OF\_TYPE\_1\_RE

# Variable: ARGUMENT\_OF\_TYPE\_UNDEFINED\_IS\_NOT\_ASSIGNABLE\_TO\_PARAMETER\_OF\_TYPE\_1\_RE

> `const` **ARGUMENT\_OF\_TYPE\_UNDEFINED\_IS\_NOT\_ASSIGNABLE\_TO\_PARAMETER\_OF\_TYPE\_1\_RE**: `RegExp`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8615




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/LibraryTypeCallDiagnosticCheckerNamespace/variables/NO_OVERLOAD_MATCHES_THIS_CALL_ERROR_CODE.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [LibraryTypeCallDiagnosticCheckerNamespace](../README.md) / NO\_OVERLOAD\_MATCHES\_THIS\_CALL\_ERROR\_CODE

# Variable: NO\_OVERLOAD\_MATCHES\_THIS\_CALL\_ERROR\_CODE

> `const` **NO\_OVERLOAD\_MATCHES\_THIS\_CALL\_ERROR\_CODE**: `2769` = `2769`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8616




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/LibraryTypeCallDiagnosticCheckerNamespace/variables/TYPE_0_IS_NOT_ASSIGNABLE_TO_TYPE_1_ERROR_CODE.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [LibraryTypeCallDiagnosticCheckerNamespace](../README.md) / TYPE\_0\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_ERROR\_CODE

# Variable: TYPE\_0\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_ERROR\_CODE

> `const` **TYPE\_0\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_ERROR\_CODE**: `2322` = `2322`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8609




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/LibraryTypeCallDiagnosticCheckerNamespace/variables/TYPE_NULL_IS_NOT_ASSIGNABLE_TO_TYPE_1_RE.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [LibraryTypeCallDiagnosticCheckerNamespace](../README.md) / TYPE\_NULL\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_RE

# Variable: TYPE\_NULL\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_RE

> `const` **TYPE\_NULL\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_RE**: `RegExp`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8611




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/LibraryTypeCallDiagnosticCheckerNamespace/variables/TYPE_UNDEFINED_IS_NOT_ASSIGNABLE_TO_TYPE_1_RE.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [LibraryTypeCallDiagnosticCheckerNamespace](../README.md) / TYPE\_UNDEFINED\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_RE

# Variable: TYPE\_UNDEFINED\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_RE

> `const` **TYPE\_UNDEFINED\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_RE**: `RegExp`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8612




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/LibraryTypeCallDiagnosticCheckerNamespace/variables/TYPE_UNKNOWN_IS_NOT_ASSIGNABLE_TO_TYPE_1_RE.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [LibraryTypeCallDiagnosticCheckerNamespace](../README.md) / TYPE\_UNKNOWN\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_RE

# Variable: TYPE\_UNKNOWN\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_RE

> `const` **TYPE\_UNKNOWN\_IS\_NOT\_ASSIGNABLE\_TO\_TYPE\_1\_RE**: `RegExp`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8610




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Problems/README.md`
============================================================

[**ArkAnalyzer**](../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../globals.md) / [ts](../../../../README.md) / [ArkTSLinter\_1\_0](../../README.md) / Problems

# Problems

## Enumerations

- [FaultID](enumerations/FaultID.md)

## Classes

- [FaultAttributs](classes/FaultAttributs.md)

## Variables

- [faultsAttrs](variables/faultsAttrs.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Problems/classes/FaultAttributs.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Problems](../README.md) / FaultAttributs

# Class: FaultAttributs

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8864

## Constructors

### Constructor

> **new FaultAttributs**(): `FaultAttributs`

#### Returns

`FaultAttributs`

## Properties

### cookBookRef

> **cookBookRef**: `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8867

***

### migratable?

> `optional` **migratable**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8865

***

### warning?

> `optional` **warning**: `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8866




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Problems/enumerations/FaultID.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Problems](../README.md) / FaultID

# Enumeration: FaultID

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8777

## Enumeration Members

### AnyType

> **AnyType**: `0`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8778

***

### ArrayLiteralNoContextType

> **ArrayLiteralNoContextType**: `3`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8781

***

### CallSignature

> **CallSignature**: `39`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8817

***

### CatchWithUnsupportedType

> **CatchWithUnsupportedType**: `32`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8810

***

### ClassAsObject

> **ClassAsObject**: `46`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8824

***

### ClassExpression

> **ClassExpression**: `28`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8806

***

### CommaOperator

> **CommaOperator**: `25`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8803

***

### ComputedPropertyName

> **ComputedPropertyName**: `4`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8782

***

### ConditionalType

> **ConditionalType**: `43`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8821

***

### ConstAssertion

> **ConstAssertion**: `75`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8853

***

### ConstructorFuncs

> **ConstructorFuncs**: `38`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8816

***

### ConstructorIface

> **ConstructorIface**: `37`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8815

***

### ConstructorType

> **ConstructorType**: `36`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8814

***

### DeclWithDuplicateName

> **DeclWithDuplicateName**: `34`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8812

***

### DefaultImport

> **DefaultImport**: `59`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8837

***

### DefiniteAssignment

> **DefiniteAssignment**: `69`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8847

***

### DeleteOperator

> **DeleteOperator**: `33`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8811

***

### DestructuringAssignment

> **DestructuringAssignment**: `29`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8807

***

### DestructuringDeclaration

> **DestructuringDeclaration**: `30`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8808

***

### DestructuringParameter

> **DestructuringParameter**: `9`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8787

***

### EnumMemberNonConstInit

> **EnumMemberNonConstInit**: `52`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8830

***

### EnumMerging

> **EnumMerging**: `12`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8790

***

### ErrorSuppression

> **ErrorSuppression**: `79`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8857

***

### EsObjectType

> **EsObjectType**: `83`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8861

***

### ExportAssignment

> **ExportAssignment**: `60`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8838

***

### ForInStatement

> **ForInStatement**: `19`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8797

***

### FunctionApplyBindCall

> **FunctionApplyBindCall**: `74`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8852

***

### FunctionContainsThis

> **FunctionContainsThis**: `49`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8827

***

### FunctionExpression

> **FunctionExpression**: `22`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8800

***

### GeneratorFunction

> **GeneratorFunction**: `48`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8826

***

### GenericCallNoTypeArgs

> **GenericCallNoTypeArgs**: `62`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8840

***

### GlobalThis

> **GlobalThis**: `71`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8849

***

### ImplementsClass

> **ImplementsClass**: `53`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8831

***

### ImportAfterStatement

> **ImportAfterStatement**: `82`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8860

***

### ImportAssertion

> **ImportAssertion**: `76`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8854

***

### ImportAssignment

> **ImportAssignment**: `61`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8839

***

### ImportFromPath

> **ImportFromPath**: `21`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8799

***

### IndexedAccessType

> **IndexedAccessType**: `17`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8795

***

### IndexMember

> **IndexMember**: `14`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8792

***

### InOperator

> **InOperator**: `20`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8798

***

### InstanceofUnsupported

> **InstanceofUnsupported**: `64`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8842

***

### IntefaceExtendDifProps

> **IntefaceExtendDifProps**: `57`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8835

***

### InterfaceExtendsClass

> **InterfaceExtendsClass**: `13`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8791

***

### InterfaceMerging

> **InterfaceMerging**: `11`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8789

***

### IntersectionType

> **IntersectionType**: `23`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8801

***

### IsOperator

> **IsOperator**: `8`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8786

***

### JsxElement

> **JsxElement**: `51`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8829

***

### LambdaWithTypeParameters

> **LambdaWithTypeParameters**: `27`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8805

***

### LAST\_ID

> **LAST\_ID**: `84`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8862

***

### LimitedReturnTypeInference

> **LimitedReturnTypeInference**: `26`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8804

***

### LimitedStdLibApi

> **LimitedStdLibApi**: `78`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8856

***

### LiteralAsPropertyName

> **LiteralAsPropertyName**: `5`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8783

***

### LocalFunction

> **LocalFunction**: `42`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8820

***

### MappedType

> **MappedType**: `44`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8822

***

### MultipleStaticBlocks

> **MultipleStaticBlocks**: `55`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8833

***

### NamespaceAsObject

> **NamespaceAsObject**: `45`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8823

***

### NewTarget

> **NewTarget**: `68`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8846

***

### NonDeclarationInNamespace

> **NonDeclarationInNamespace**: `47`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8825

***

### NoUndefinedPropAccess

> **NoUndefinedPropAccess**: `54`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8832

***

### ObjectLiteralNoContextType

> **ObjectLiteralNoContextType**: `2`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8780

***

### ObjectTypeLiteral

> **ObjectTypeLiteral**: `24`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8802

***

### ParameterProperties

> **ParameterProperties**: `63`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8841

***

### PrivateIdentifier

> **PrivateIdentifier**: `41`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8819

***

### PropertyAccessByIndex

> **PropertyAccessByIndex**: `50`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8828

***

### PropertyDeclOnFunction

> **PropertyDeclOnFunction**: `73`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8851

***

### Prototype

> **Prototype**: `70`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8848

***

### RegexLiteral

> **RegexLiteral**: `7`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8785

***

### ShorthandAmbientModuleDecl

> **ShorthandAmbientModuleDecl**: `65`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8843

***

### SpreadOperator

> **SpreadOperator**: `77`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8855

***

### StrictDiagnostic

> **StrictDiagnostic**: `80`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8858

***

### StructuralIdentity

> **StructuralIdentity**: `58`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8836

***

### SymbolType

> **SymbolType**: `1`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8779

***

### ThisType

> **ThisType**: `56`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8834

***

### ThrowStatement

> **ThrowStatement**: `16`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8794

***

### TypeAssertion

> **TypeAssertion**: `40`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8818

***

### TypeQuery

> **TypeQuery**: `6`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8784

***

### UMDModuleDefinition

> **UMDModuleDefinition**: `67`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8845

***

### UnaryArithmNotNumber

> **UnaryArithmNotNumber**: `35`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8813

***

### UnknownType

> **UnknownType**: `18`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8796

***

### UnsupportedDecorators

> **UnsupportedDecorators**: `81`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8859

***

### UtilityType

> **UtilityType**: `72`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8850

***

### VarDeclaration

> **VarDeclaration**: `31`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8809

***

### WildcardsInModuleName

> **WildcardsInModuleName**: `66`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8844

***

### WithStatement

> **WithStatement**: `15`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8793

***

### YieldExpression

> **YieldExpression**: `10`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8788




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Problems/variables/faultsAttrs.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Problems](../README.md) / faultsAttrs

# Variable: faultsAttrs

> `const` **faultsAttrs**: [`FaultAttributs`](../classes/FaultAttributs.md)[]

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8869




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/README.md`
============================================================

[**ArkAnalyzer**](../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../globals.md) / [ts](../../../../README.md) / [ArkTSLinter\_1\_0](../../README.md) / Utils

# Utils

## Enumerations

- [CheckType](enumerations/CheckType.md)
- [ProblemSeverity](enumerations/ProblemSeverity.md)

## Variables

- [ALLOWED\_STD\_SYMBOL\_API](variables/ALLOWED_STD_SYMBOL_API.md)
- [ARKTS\_IGNORE\_DIRS](variables/ARKTS_IGNORE_DIRS.md)
- [ARKTS\_IGNORE\_FILES](variables/ARKTS_IGNORE_FILES.md)
- [ARKUI\_DECORATORS](variables/ARKUI_DECORATORS.md)
- [ES\_OBJECT](variables/ES_OBJECT.md)
- [FUNCTION\_HAS\_NO\_RETURN\_ERROR\_CODE](variables/FUNCTION_HAS_NO_RETURN_ERROR_CODE.md)
- [LIMITED\_STANDARD\_UTILITY\_TYPES](variables/LIMITED_STANDARD_UTILITY_TYPES.md)
- [LIMITED\_STD\_GLOBAL\_FUNC](variables/LIMITED_STD_GLOBAL_FUNC.md)
- [LIMITED\_STD\_OBJECT\_API](variables/LIMITED_STD_OBJECT_API.md)
- [LIMITED\_STD\_PROXYHANDLER\_API](variables/LIMITED_STD_PROXYHANDLER_API.md)
- [LIMITED\_STD\_REFLECT\_API](variables/LIMITED_STD_REFLECT_API.md)
- [NON\_INITIALIZABLE\_PROPERTY\_ClASS\_DECORATORS](variables/NON_INITIALIZABLE_PROPERTY_ClASS_DECORATORS.md)
- [NON\_INITIALIZABLE\_PROPERTY\_DECORATORS](variables/NON_INITIALIZABLE_PROPERTY_DECORATORS.md)
- [NON\_RETURN\_FUNCTION\_DECORATORS](variables/NON_RETURN_FUNCTION_DECORATORS.md)
- [PROPERTY\_HAS\_NO\_INITIALIZER\_ERROR\_CODE](variables/PROPERTY_HAS_NO_INITIALIZER_ERROR_CODE.md)
- [STANDARD\_LIBRARIES](variables/STANDARD_LIBRARIES.md)
- [TYPED\_ARRAYS](variables/TYPED_ARRAYS.md)

## Functions

- [clearTrueSymbolAtLocationCache](functions/clearTrueSymbolAtLocationCache.md)
- [clearTypeChecker](functions/clearTypeChecker.md)
- [decodeAutofixInfo](functions/decodeAutofixInfo.md)
- [encodeProblemInfo](functions/encodeProblemInfo.md)
- [entityNameToString](functions/entityNameToString.md)
- [findParentIf](functions/findParentIf.md)
- [followIfAliased](functions/followIfAliased.md)
- [getAccessModifier](functions/getAccessModifier.md)
- [getDeclaration](functions/getDeclaration.md)
- [getEndPos](functions/getEndPos.md)
- [getModifier](functions/getModifier.md)
- [getParentSymbolName](functions/getParentSymbolName.md)
- [getScriptKind](functions/getScriptKind.md)
- [getStartPos](functions/getStartPos.md)
- [getSymbolDeclarationTypeNode](functions/getSymbolDeclarationTypeNode.md)
- [getSymbolOfCallExpression](functions/getSymbolOfCallExpression.md)
- [getVariableDeclarationTypeNode](functions/getVariableDeclarationTypeNode.md)
- [hasAccessModifier](functions/hasAccessModifier.md)
- [hasEsObjectType](functions/hasEsObjectType.md)
- [hasLibraryType](functions/hasLibraryType.md)
- [hasMethods](functions/hasMethods.md)
- [hasModifier](functions/hasModifier.md)
- [hasPredecessor](functions/hasPredecessor.md)
- [isAnonymousType](functions/isAnonymousType.md)
- [isAnyType](functions/isAnyType.md)
- [isAssignmentOperator](functions/isAssignmentOperator.md)
- [isBooleanType](functions/isBooleanType.md)
- [isCallToFunctionWithOmittedReturnType](functions/isCallToFunctionWithOmittedReturnType.md)
- [isCompileTimeExpression](functions/isCompileTimeExpression.md)
- [isConst](functions/isConst.md)
- [isDefaultImport](functions/isDefaultImport.md)
- [isDerivedFrom](functions/isDerivedFrom.md)
- [isDestructuringAssignmentLHS](functions/isDestructuringAssignmentLHS.md)
- [isDynamicLiteralInitializer](functions/isDynamicLiteralInitializer.md)
- [isDynamicType](functions/isDynamicType.md)
- [isEnumMemberType](functions/isEnumMemberType.md)
- [isEnumType](functions/isEnumType.md)
- [isEsObjectPossiblyAllowed](functions/isEsObjectPossiblyAllowed.md)
- [isEsObjectSymbol](functions/isEsObjectSymbol.md)
- [isEsObjectType](functions/isEsObjectType.md)
- [isExpressionAssignableToType](functions/isExpressionAssignableToType.md)
- [isFunctionOrMethod](functions/isFunctionOrMethod.md)
- [isFunctionSymbol](functions/isFunctionSymbol.md)
- [isGenericArrayType](functions/isGenericArrayType.md)
- [isGlobalSymbol](functions/isGlobalSymbol.md)
- [isInsideBlock](functions/isInsideBlock.md)
- [isIntegerConstantValue](functions/isIntegerConstantValue.md)
- [isInterfaceType](functions/isInterfaceType.md)
- [isIntrinsicObjectType](functions/isIntrinsicObjectType.md)
- [isLibrarySymbol](functions/isLibrarySymbol.md)
- [isLibraryType](functions/isLibraryType.md)
- [isLiteralType](functions/isLiteralType.md)
- [isMethodAssignment](functions/isMethodAssignment.md)
- [isNullType](functions/isNullType.md)
- [isNumberConstantValue](functions/isNumberConstantValue.md)
- [isNumberLikeType](functions/isNumberLikeType.md)
- [isNumberType](functions/isNumberType.md)
- [isObjectLiteralType](functions/isObjectLiteralType.md)
- [isObjectType](functions/isObjectType.md)
- [isPrimitiveEnumMemberType](functions/isPrimitiveEnumMemberType.md)
- [isPrimitiveEnumType](functions/isPrimitiveEnumType.md)
- [isPrimitiveType](functions/isPrimitiveType.md)
- [isPrototypeSymbol](functions/isPrototypeSymbol.md)
- [isReferenceType](functions/isReferenceType.md)
- [isStdLibrarySymbol](functions/isStdLibrarySymbol.md)
- [isStdLibraryType](functions/isStdLibraryType.md)
- [isStdPartialType](functions/isStdPartialType.md)
- [isStdReadonlyType](functions/isStdReadonlyType.md)
- [isStdRecordType](functions/isStdRecordType.md)
- [isStdRequiredType](functions/isStdRequiredType.md)
- [isStdSymbol](functions/isStdSymbol.md)
- [isStringConstantValue](functions/isStringConstantValue.md)
- [isStringLikeType](functions/isStringLikeType.md)
- [isStringType](functions/isStringType.md)
- [isStruct](functions/isStruct.md)
- [isStructDeclaration](functions/isStructDeclaration.md)
- [isStructDeclarationKind](functions/isStructDeclarationKind.md)
- [isStructObjectInitializer](functions/isStructObjectInitializer.md)
- [isSupportedType](functions/isSupportedType.md)
- [isSymbolAPI](functions/isSymbolAPI.md)
- [isSymbolIterator](functions/isSymbolIterator.md)
- [isThisOrSuperExpr](functions/isThisOrSuperExpr.md)
- [isType](functions/isType.md)
- [isTypedArray](functions/isTypedArray.md)
- [isTypeDeclSyntaxKind](functions/isTypeDeclSyntaxKind.md)
- [isTypeReference](functions/isTypeReference.md)
- [isTypeSymbol](functions/isTypeSymbol.md)
- [isUnknownType](functions/isUnknownType.md)
- [isUnsupportedType](functions/isUnsupportedType.md)
- [isUnsupportedUnionType](functions/isUnsupportedUnionType.md)
- [isValidEnumMemberInit](functions/isValidEnumMemberInit.md)
- [isValueAssignableToESObject](functions/isValueAssignableToESObject.md)
- [logTscDiagnostic](functions/logTscDiagnostic.md)
- [needToDeduceStructuralIdentity](functions/needToDeduceStructuralIdentity.md)
- [pathContainsDirectory](functions/pathContainsDirectory.md)
- [processParentTypes](functions/processParentTypes.md)
- [processParentTypesCheck](functions/processParentTypesCheck.md)
- [relatedByInheritanceOrIdentical](functions/relatedByInheritanceOrIdentical.md)
- [setTestMode](functions/setTestMode.md)
- [setTypeChecker](functions/setTypeChecker.md)
- [symbolHasDuplicateName](functions/symbolHasDuplicateName.md)
- [symbolHasEsObjectType](functions/symbolHasEsObjectType.md)
- [trueSymbolAtLocation](functions/trueSymbolAtLocation.md)
- [typeIsRecursive](functions/typeIsRecursive.md)
- [unwrapParenthesized](functions/unwrapParenthesized.md)
- [unwrapParenthesizedType](functions/unwrapParenthesizedType.md)
- [validateFields](functions/validateFields.md)
- [validateObjectLiteralType](functions/validateObjectLiteralType.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/enumerations/CheckType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / CheckType

# Enumeration: CheckType

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8719

## Enumeration Members

### Array

> **Array**: `0`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8720

***

### Error

> **Error**: `"Error"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8724

***

### Map

> **Map**: `"Map"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8723

***

### Set

> **Set**: `"Set"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8722

***

### String

> **String**: `"String"`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8721




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/enumerations/ProblemSeverity.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / ProblemSeverity

# Enumeration: ProblemSeverity

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8640

## Enumeration Members

### ERROR

> **ERROR**: `2`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8642

***

### WARNING

> **WARNING**: `1`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8641




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/clearTrueSymbolAtLocationCache.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / clearTrueSymbolAtLocationCache

# Function: clearTrueSymbolAtLocationCache()

> **clearTrueSymbolAtLocationCache**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8672

## Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/clearTypeChecker.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / clearTypeChecker

# Function: clearTypeChecker()

> **clearTypeChecker**(): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8647

## Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/decodeAutofixInfo.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / decodeAutofixInfo

# Function: decodeAutofixInfo()

> **decodeAutofixInfo**(`info`): [`AutofixInfo`](../../Common/interfaces/AutofixInfo.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8707

## Parameters

### info

`string`

## Returns

[`AutofixInfo`](../../Common/interfaces/AutofixInfo.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/encodeProblemInfo.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / encodeProblemInfo

# Function: encodeProblemInfo()

> **encodeProblemInfo**(`problem`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8706

## Parameters

### problem

[`ProblemInfo`](../../../interfaces/ProblemInfo.md)

## Returns

`string`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/entityNameToString.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / entityNameToString

# Function: entityNameToString()

> **entityNameToString**(`name`): `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8654

## Parameters

### name

[`EntityName`](../../../../../type-aliases/EntityName.md)

## Returns

`string`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/findParentIf.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / findParentIf

# Function: findParentIf()

> **findParentIf**(`asExpr`): `null` \| [`IfStatement`](../../../../../interfaces/IfStatement.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8662

## Parameters

### asExpr

[`AsExpression`](../../../../../interfaces/AsExpression.md)

## Returns

`null` \| [`IfStatement`](../../../../../interfaces/IfStatement.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/followIfAliased.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / followIfAliased

# Function: followIfAliased()

> **followIfAliased**(`sym`): [`Symbol`](../../../../../interfaces/Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8670

## Parameters

### sym

[`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

[`Symbol`](../../../../../interfaces/Symbol.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/getAccessModifier.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / getAccessModifier

# Function: getAccessModifier()

> **getAccessModifier**(`modifiers`): `undefined` \| [`Modifier`](../../../../../type-aliases/Modifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8744

## Parameters

### modifiers

`undefined` | readonly [`Modifier`](../../../../../type-aliases/Modifier.md)[]

## Returns

`undefined` \| [`Modifier`](../../../../../type-aliases/Modifier.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/getDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / getDeclaration

# Function: getDeclaration()

> **getDeclaration**(`tsSymbol`): `undefined` \| [`Declaration`](../../../../../interfaces/Declaration.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8692

## Parameters

### tsSymbol

`undefined` | [`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`undefined` \| [`Declaration`](../../../../../interfaces/Declaration.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/getEndPos.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / getEndPos

# Function: getEndPos()

> **getEndPos**(`nodeOrComment`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8650

## Parameters

### nodeOrComment

[`Node`](../../../../../interfaces/Node.md) | [`CommentRange`](../../../../../interfaces/CommentRange.md)

## Returns

`number`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/getModifier.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / getModifier

# Function: getModifier()

> **getModifier**(`modifiers`, `modifierKind`): `undefined` \| [`Modifier`](../../../../../type-aliases/Modifier.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8743

## Parameters

### modifiers

`undefined` | readonly [`Modifier`](../../../../../type-aliases/Modifier.md)[]

### modifierKind

[`SyntaxKind`](../../../../../enumerations/SyntaxKind.md)

## Returns

`undefined` \| [`Modifier`](../../../../../type-aliases/Modifier.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/getParentSymbolName.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / getParentSymbolName

# Function: getParentSymbolName()

> **getParentSymbolName**(`symbol`): `undefined` \| `string`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8736

## Parameters

### symbol

[`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`undefined` \| `string`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/getScriptKind.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / getScriptKind

# Function: getScriptKind()

> **getScriptKind**(`srcFile`): [`ScriptKind`](../../../../../enumerations/ScriptKind.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8753

## Parameters

### srcFile

[`SourceFile`](../../../../../interfaces/SourceFile.md)

## Returns

[`ScriptKind`](../../../../../enumerations/ScriptKind.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/getStartPos.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / getStartPos

# Function: getStartPos()

> **getStartPos**(`nodeOrComment`): `number`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8649

## Parameters

### nodeOrComment

[`Node`](../../../../../interfaces/Node.md) | [`CommentRange`](../../../../../interfaces/CommentRange.md)

## Returns

`number`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/getSymbolDeclarationTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / getSymbolDeclarationTypeNode

# Function: getSymbolDeclarationTypeNode()

> **getSymbolDeclarationTypeNode**(`sym`): `undefined` \| [`TypeNode`](../../../../../interfaces/TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8764

## Parameters

### sym

[`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`undefined` \| [`TypeNode`](../../../../../interfaces/TypeNode.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/getSymbolOfCallExpression.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / getSymbolOfCallExpression

# Function: getSymbolOfCallExpression()

> **getSymbolOfCallExpression**(`callExpr`): `undefined` \| [`Symbol`](../../../../../interfaces/Symbol.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8769

## Parameters

### callExpr

[`CallExpression`](../../../../../interfaces/CallExpression.md)

## Returns

`undefined` \| [`Symbol`](../../../../../interfaces/Symbol.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/getVariableDeclarationTypeNode.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / getVariableDeclarationTypeNode

# Function: getVariableDeclarationTypeNode()

> **getVariableDeclarationTypeNode**(`node`): `undefined` \| [`TypeNode`](../../../../../interfaces/TypeNode.md)

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8763

## Parameters

### node

[`Node`](../../../../../interfaces/Node.md)

## Returns

`undefined` \| [`TypeNode`](../../../../../interfaces/TypeNode.md)




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/hasAccessModifier.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / hasAccessModifier

# Function: hasAccessModifier()

> **hasAccessModifier**(`decl`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8742

## Parameters

### decl

[`Declaration`](../../../../../interfaces/Declaration.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/hasEsObjectType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / hasEsObjectType

# Function: hasEsObjectType()

> **hasEsObjectType**(`node`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8765

## Parameters

### node

[`Node`](../../../../../interfaces/Node.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/hasLibraryType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / hasLibraryType

# Function: hasLibraryType()

> **hasLibraryType**(`node`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8750

## Parameters

### node

[`Node`](../../../../../interfaces/Node.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/hasMethods.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / hasMethods

# Function: hasMethods()

> **hasMethods**(`type`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8713

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/hasModifier.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / hasModifier

# Function: hasModifier()

> **hasModifier**(`tsModifiers`, `tsModifierKind`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8668

## Parameters

### tsModifiers

`undefined` | readonly [`Modifier`](../../../../../type-aliases/Modifier.md)[]

### tsModifierKind

`number`

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/hasPredecessor.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / hasPredecessor

# Function: hasPredecessor()

> **hasPredecessor**(`node`, `predicate`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8701

## Parameters

### node

[`Node`](../../../../../interfaces/Node.md)

### predicate

(`node`) => `boolean`

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isAnonymousType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isAnonymousType

# Function: isAnonymousType()

> **isAnonymousType**(`type`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8768

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isAnyType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isAnyType

# Function: isAnyType()

> **isAnyType**(`tsType`): `tsType is TypeReference`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8686

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`tsType is TypeReference`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isAssignmentOperator.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isAssignmentOperator

# Function: isAssignmentOperator()

> **isAssignmentOperator**(`tsBinOp`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8651

## Parameters

### tsBinOp

[`BinaryOperatorToken`](../../../../../type-aliases/BinaryOperatorToken.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isBooleanType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isBooleanType

# Function: isBooleanType()

> **isBooleanType**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8656

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isCallToFunctionWithOmittedReturnType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isCallToFunctionWithOmittedReturnType

# Function: isCallToFunctionWithOmittedReturnType()

> **isCallToFunctionWithOmittedReturnType**(`tsExpr`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8708

## Parameters

### tsExpr

[`Expression`](../../../../../interfaces/Expression.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isCompileTimeExpression.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isCompileTimeExpression

# Function: isCompileTimeExpression()

> **isCompileTimeExpression**(`tsExpr`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8694

## Parameters

### tsExpr

[`Expression`](../../../../../interfaces/Expression.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isConst.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isConst

# Function: isConst()

> **isConst**(`tsNode`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8695

## Parameters

### tsNode

[`Node`](../../../../../interfaces/Node.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isDefaultImport.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isDefaultImport

# Function: isDefaultImport()

> **isDefaultImport**(`importSpec`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8741

## Parameters

### importSpec

[`ImportSpecifier`](../../../../../interfaces/ImportSpecifier.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isDerivedFrom.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isDerivedFrom

# Function: isDerivedFrom()

> **isDerivedFrom**(`tsType`, `checkType`): `tsType is TypeReference`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8679

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

### checkType

[`CheckType`](../enumerations/CheckType.md)

## Returns

`tsType is TypeReference`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isDestructuringAssignmentLHS.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isDestructuringAssignmentLHS

# Function: isDestructuringAssignmentLHS()

> **isDestructuringAssignmentLHS**(`tsExpr`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8663

## Parameters

### tsExpr

[`ObjectLiteralExpression`](../../../../../interfaces/ObjectLiteralExpression.md) | [`ArrayLiteralExpression`](../../../../../interfaces/ArrayLiteralExpression.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isDynamicLiteralInitializer.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isDynamicLiteralInitializer

# Function: isDynamicLiteralInitializer()

> **isDynamicLiteralInitializer**(`expr`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8758

## Parameters

### expr

[`Expression`](../../../../../interfaces/Expression.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isDynamicType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isDynamicType

# Function: isDynamicType()

> **isDynamicType**(`type`): `undefined` \| `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8757

## Parameters

### type

`undefined` | [`Type`](../../../../../interfaces/Type.md)

## Returns

`undefined` \| `boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isEnumMemberType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isEnumMemberType

# Function: isEnumMemberType()

> **isEnumMemberType**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8665

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isEnumType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isEnumType

# Function: isEnumType()

> **isEnumType**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8664

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isEsObjectPossiblyAllowed.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isEsObjectPossiblyAllowed

# Function: isEsObjectPossiblyAllowed()

> **isEsObjectPossiblyAllowed**(`typeRef`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8761

## Parameters

### typeRef

[`TypeReferenceNode`](../../../../../interfaces/TypeReferenceNode.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isEsObjectSymbol.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isEsObjectSymbol

# Function: isEsObjectSymbol()

> **isEsObjectSymbol**(`sym`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8767

## Parameters

### sym

[`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isEsObjectType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isEsObjectType

# Function: isEsObjectType()

> **isEsObjectType**(`typeNode`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8759

## Parameters

### typeNode

[`TypeNode`](../../../../../interfaces/TypeNode.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isExpressionAssignableToType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isExpressionAssignableToType

# Function: isExpressionAssignableToType()

> **isExpressionAssignableToType**(`lhsType`, `rhsExpr`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8714

## Parameters

### lhsType

`undefined` | [`Type`](../../../../../interfaces/Type.md)

### rhsExpr

[`Expression`](../../../../../interfaces/Expression.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isFunctionOrMethod.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isFunctionOrMethod

# Function: isFunctionOrMethod()

> **isFunctionOrMethod**(`tsSymbol`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8690

## Parameters

### tsSymbol

`undefined` | [`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isFunctionSymbol.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isFunctionSymbol

# Function: isFunctionSymbol()

> **isFunctionSymbol**(`symbol`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8684

## Parameters

### symbol

`undefined` | [`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isGenericArrayType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isGenericArrayType

# Function: isGenericArrayType()

> **isGenericArrayType**(`tsType`): `tsType is TypeReference`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8678

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`tsType is TypeReference`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isGlobalSymbol.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isGlobalSymbol

# Function: isGlobalSymbol()

> **isGlobalSymbol**(`symbol`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8737

## Parameters

### symbol

[`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isInsideBlock.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isInsideBlock

# Function: isInsideBlock()

> **isInsideBlock**(`node`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8760

## Parameters

### node

[`Node`](../../../../../interfaces/Node.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isIntegerConstantValue.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isIntegerConstantValue

# Function: isIntegerConstantValue()

> **isIntegerConstantValue**(`tsExpr`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8697

## Parameters

### tsExpr

[`EnumMember`](../../../../../interfaces/EnumMember.md) | [`NumericLiteral`](../../../../../interfaces/NumericLiteral.md) | [`PropertyAccessExpression`](../../../../../interfaces/PropertyAccessExpression.md) | [`ElementAccessExpression`](../../../../../interfaces/ElementAccessExpression.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isInterfaceType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isInterfaceType

# Function: isInterfaceType()

> **isInterfaceType**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8685

## Parameters

### tsType

`undefined` | [`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isIntrinsicObjectType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isIntrinsicObjectType

# Function: isIntrinsicObjectType()

> **isIntrinsicObjectType**(`type`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8756

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isLibrarySymbol.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isLibrarySymbol

# Function: isLibrarySymbol()

> **isLibrarySymbol**(`sym`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8751

## Parameters

### sym

`undefined` | [`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isLibraryType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isLibraryType

# Function: isLibraryType()

> **isLibraryType**(`type`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8749

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isLiteralType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isLiteralType

# Function: isLiteralType()

> **isLiteralType**(`type`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8715

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isMethodAssignment.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isMethodAssignment

# Function: isMethodAssignment()

> **isMethodAssignment**(`tsSymbol`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8691

## Parameters

### tsSymbol

`undefined` | [`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isNullType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isNullType

# Function: isNullType()

> **isNullType**(`tsTypeNode`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8681

## Parameters

### tsTypeNode

[`TypeNode`](../../../../../interfaces/TypeNode.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isNumberConstantValue.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isNumberConstantValue

# Function: isNumberConstantValue()

> **isNumberConstantValue**(`tsExpr`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8696

## Parameters

### tsExpr

[`EnumMember`](../../../../../interfaces/EnumMember.md) | [`NumericLiteral`](../../../../../interfaces/NumericLiteral.md) | [`PropertyAccessExpression`](../../../../../interfaces/PropertyAccessExpression.md) | [`ElementAccessExpression`](../../../../../interfaces/ElementAccessExpression.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isNumberLikeType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isNumberLikeType

# Function: isNumberLikeType()

> **isNumberLikeType**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8667

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isNumberType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isNumberType

# Function: isNumberType()

> **isNumberType**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8655

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isObjectLiteralType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isObjectLiteralType

# Function: isObjectLiteralType()

> **isObjectLiteralType**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8666

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isObjectType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isObjectType

# Function: isObjectType()

> **isObjectType**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8704

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isPrimitiveEnumMemberType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isPrimitiveEnumMemberType

# Function: isPrimitiveEnumMemberType()

> **isPrimitiveEnumMemberType**(`type`, `primitiveType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8660

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

### primitiveType

[`TypeFlags`](../../../../../enumerations/TypeFlags.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isPrimitiveEnumType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isPrimitiveEnumType

# Function: isPrimitiveEnumType()

> **isPrimitiveEnumType**(`type`, `primitiveType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8659

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

### primitiveType

[`TypeFlags`](../../../../../enumerations/TypeFlags.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isPrimitiveType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isPrimitiveType

# Function: isPrimitiveType()

> **isPrimitiveType**(`type`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8676

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isPrototypeSymbol.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isPrototypeSymbol

# Function: isPrototypeSymbol()

> **isPrototypeSymbol**(`symbol`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8683

## Parameters

### symbol

`undefined` | [`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isReferenceType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isReferenceType

# Function: isReferenceType()

> **isReferenceType**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8675

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStdLibrarySymbol.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStdLibrarySymbol

# Function: isStdLibrarySymbol()

> **isStdLibrarySymbol**(`sym`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8755

## Parameters

### sym

`undefined` | [`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStdLibraryType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStdLibraryType

# Function: isStdLibraryType()

> **isStdLibraryType**(`type`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8754

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStdPartialType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStdPartialType

# Function: isStdPartialType()

> **isStdPartialType**(`type`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8746

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStdReadonlyType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStdReadonlyType

# Function: isStdReadonlyType()

> **isStdReadonlyType**(`type`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8748

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStdRecordType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStdRecordType

# Function: isStdRecordType()

> **isStdRecordType**(`type`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8745

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStdRequiredType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStdRequiredType

# Function: isStdRequiredType()

> **isStdRequiredType**(`type`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8747

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStdSymbol.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStdSymbol

# Function: isStdSymbol()

> **isStdSymbol**(`symbol`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8739

## Parameters

### symbol

[`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStringConstantValue.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStringConstantValue

# Function: isStringConstantValue()

> **isStringConstantValue**(`tsExpr`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8698

## Parameters

### tsExpr

[`EnumMember`](../../../../../interfaces/EnumMember.md) | [`PropertyAccessExpression`](../../../../../interfaces/PropertyAccessExpression.md) | [`ElementAccessExpression`](../../../../../interfaces/ElementAccessExpression.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStringLikeType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStringLikeType

# Function: isStringLikeType()

> **isStringLikeType**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8657

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStringType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStringType

# Function: isStringType()

> **isStringType**(`type`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8658

## Parameters

### type

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStruct.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStruct

# Function: isStruct()

> **isStruct**(`symbol`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8718

## Parameters

### symbol

[`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStructDeclaration.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStructDeclaration

# Function: isStructDeclaration()

> **isStructDeclaration**(`node`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8711

## Parameters

### node

[`Node`](../../../../../interfaces/Node.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStructDeclarationKind.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStructDeclarationKind

# Function: isStructDeclarationKind()

> **isStructDeclarationKind**(`kind`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8710

## Parameters

### kind

[`SyntaxKind`](../../../../../enumerations/SyntaxKind.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isStructObjectInitializer.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isStructObjectInitializer

# Function: isStructObjectInitializer()

> **isStructObjectInitializer**(`objectLiteral`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8712

## Parameters

### objectLiteral

[`ObjectLiteralExpression`](../../../../../interfaces/ObjectLiteralExpression.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isSupportedType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isSupportedType

# Function: isSupportedType()

> **isSupportedType**(`typeNode`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8717

## Parameters

### typeNode

[`TypeNode`](../../../../../interfaces/TypeNode.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isSymbolAPI.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isSymbolAPI

# Function: isSymbolAPI()

> **isSymbolAPI**(`symbol`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8738

## Parameters

### symbol

[`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isSymbolIterator.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isSymbolIterator

# Function: isSymbolIterator()

> **isSymbolIterator**(`symbol`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8740

## Parameters

### symbol

[`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isThisOrSuperExpr.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isThisOrSuperExpr

# Function: isThisOrSuperExpr()

> **isThisOrSuperExpr**(`tsExpr`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8682

## Parameters

### tsExpr

[`Expression`](../../../../../interfaces/Expression.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isType

# Function: isType()

> **isType**(`tsType`, `checkType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8653

## Parameters

### tsType

`undefined` | [`TypeNode`](../../../../../interfaces/TypeNode.md)

### checkType

`string`

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isTypeDeclSyntaxKind.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isTypeDeclSyntaxKind

# Function: isTypeDeclSyntaxKind()

> **isTypeDeclSyntaxKind**(`kind`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8673

## Parameters

### kind

[`SyntaxKind`](../../../../../enumerations/SyntaxKind.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isTypeReference.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isTypeReference

# Function: isTypeReference()

> **isTypeReference**(`tsType`): `tsType is TypeReference`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8680

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`tsType is TypeReference`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isTypeSymbol.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isTypeSymbol

# Function: isTypeSymbol()

> **isTypeSymbol**(`symbol`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8677

## Parameters

### symbol

`undefined` | [`Symbol`](../../../../../interfaces/Symbol.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isTypedArray.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isTypedArray

# Function: isTypedArray()

> **isTypedArray**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8652

## Parameters

### tsType

`undefined` | [`TypeNode`](../../../../../interfaces/TypeNode.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isUnknownType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isUnknownType

# Function: isUnknownType()

> **isUnknownType**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8687

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isUnsupportedType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isUnsupportedType

# Function: isUnsupportedType()

> **isUnsupportedType**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8688

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isUnsupportedUnionType.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isUnsupportedUnionType

# Function: isUnsupportedUnionType()

> **isUnsupportedUnionType**(`tsType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8689

## Parameters

### tsType

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isValidEnumMemberInit.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isValidEnumMemberInit

# Function: isValidEnumMemberInit()

> **isValidEnumMemberInit**(`tsExpr`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8693

## Parameters

### tsExpr

[`Expression`](../../../../../interfaces/Expression.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/isValueAssignableToESObject.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / isValueAssignableToESObject

# Function: isValueAssignableToESObject()

> **isValueAssignableToESObject**(`node`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8762

## Parameters

### node

[`Node`](../../../../../interfaces/Node.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/logTscDiagnostic.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / logTscDiagnostic

# Function: logTscDiagnostic()

> **logTscDiagnostic**(`diagnostics`, `log`): `void`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8705

## Parameters

### diagnostics

readonly [`Diagnostic`](../../../../../interfaces/Diagnostic.md)[]

### log

(`message`, ...`args`) => `void`

## Returns

`void`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/needToDeduceStructuralIdentity.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / needToDeduceStructuralIdentity

# Function: needToDeduceStructuralIdentity()

> **needToDeduceStructuralIdentity**(`typeFrom`, `typeTo`, `allowPromotion?`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8700

## Parameters

### typeFrom

[`Type`](../../../../../interfaces/Type.md)

### typeTo

[`Type`](../../../../../interfaces/Type.md)

### allowPromotion?

`boolean`

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/pathContainsDirectory.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / pathContainsDirectory

# Function: pathContainsDirectory()

> **pathContainsDirectory**(`targetPath`, `dir`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8752

## Parameters

### targetPath

`string`

### dir

`string`

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/processParentTypes.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / processParentTypes

# Function: processParentTypes()

> **processParentTypes**(`parentTypes`, `typeB`, `processInterfaces`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8702

## Parameters

### parentTypes

[`NodeArray`](../../../../../interfaces/NodeArray.md)\<[`ExpressionWithTypeArguments`](../../../../../interfaces/ExpressionWithTypeArguments.md)\>

### typeB

[`Type`](../../../../../interfaces/Type.md)

### processInterfaces

`boolean`

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/processParentTypesCheck.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / processParentTypesCheck

# Function: processParentTypesCheck()

> **processParentTypesCheck**(`parentTypes`, `checkType`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8703

## Parameters

### parentTypes

[`NodeArray`](../../../../../interfaces/NodeArray.md)\<[`ExpressionWithTypeArguments`](../../../../../interfaces/ExpressionWithTypeArguments.md)\>

### checkType

[`CheckType`](../enumerations/CheckType.md)

## Returns

`boolean`




============================================================
## FILE: `ArkAnalyzer/namespaces/ts/namespaces/ArkTSLinter_1_0/namespaces/Utils/functions/relatedByInheritanceOrIdentical.md`
============================================================

[**ArkAnalyzer**](../../../../../../../../README.md)

***

[ArkAnalyzer](../../../../../../../../globals.md) / [ts](../../../../../README.md) / [ArkTSLinter\_1\_0](../../../README.md) / [Utils](../README.md) / relatedByInheritanceOrIdentical

# Function: relatedByInheritanceOrIdentical()

> **relatedByInheritanceOrIdentical**(`typeA`, `typeB`): `boolean`

Defined in: node\_modules/ohos-typescript/lib/typescript.d.ts:8699

## Parameters

### typeA

[`Type`](../../../../../interfaces/Type.md)

### typeB

[`Type`](../../../../../interfaces/Type.md)

## Returns

`boolean`



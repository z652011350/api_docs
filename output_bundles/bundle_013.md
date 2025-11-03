

============================================================
## FILE: `classes/PointerAnalysis.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PointerAnalysis

# Class: PointerAnalysis

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:38

## Extends

- [`AbstractAnalysis`](AbstractAnalysis.md)

## Constructors

### Constructor

> **new PointerAnalysis**(`p`, `cg`, `s`, `config`): `PointerAnalysis`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:49

#### Parameters

##### p

[`Pag`](Pag.md)

##### cg

[`CallGraph`](CallGraph.md)

##### s

[`Scene`](Scene.md)

##### config

[`PointerAnalysisConfig`](PointerAnalysisConfig.md)

#### Returns

`PointerAnalysis`

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

### getHandledFuncs()

> **getHandledFuncs**(): `number`[]

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:624

#### Returns

`number`[]

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

### getPTAConfig()

> **getPTAConfig**(): [`PointerAnalysisConfig`](PointerAnalysisConfig.md)

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:628

#### Returns

[`PointerAnalysisConfig`](PointerAnalysisConfig.md)

***

### getPTD()

> **getPTD**(): [`DiffPTData`](DiffPTData.md)\<`number`, `number`, `IPtsCollection`\<`number`\>\>

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:132

#### Returns

[`DiffPTData`](DiffPTData.md)\<`number`, `number`, `IPtsCollection`\<`number`\>\>

***

### getRelatedNodes()

> **getRelatedNodes**(`value`): `Set`\<[`Value`](../interfaces/Value.md)\>

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:503

#### Parameters

##### value

[`Value`](../interfaces/Value.md)

#### Returns

`Set`\<[`Value`](../interfaces/Value.md)\>

***

### getScene()

> **getScene**(): [`Scene`](Scene.md)

Defined in: src/callgraph/algorithm/AbstractAnalysis.ts:43

#### Returns

[`Scene`](Scene.md)

#### Inherited from

[`AbstractAnalysis`](AbstractAnalysis.md).[`getScene`](AbstractAnalysis.md#getscene)

***

### getStat()

> **getStat**(): `string`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:136

#### Returns

`string`

***

### getTypeDiffMap()

> **getTypeDiffMap**(): `Map`\<[`Value`](../interfaces/Value.md), `Set`\<[`Type`](Type.md)\>\>

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:612

#### Returns

`Map`\<[`Value`](../interfaces/Value.md), `Set`\<[`Type`](Type.md)\>\>

***

### getUnhandledFuncs()

> **getUnhandledFuncs**(): `number`[]

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:620

#### Returns

`number`[]

***

### init()

> `protected` **init**(): `void`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:98

#### Returns

`void`

#### Overrides

[`AbstractAnalysis`](AbstractAnalysis.md).[`init`](AbstractAnalysis.md#init)

***

### mayAlias()

> **mayAlias**(`leftValue`, `rightValue`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:499

#### Parameters

##### leftValue

[`Value`](../interfaces/Value.md)

##### rightValue

[`Value`](../interfaces/Value.md)

#### Returns

`boolean`

***

### mergeInstanceFieldMap()

> **mergeInstanceFieldMap**(`src`, `dst`): `Map`\<`number`, `number`[]\>

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:662

#### Parameters

##### src

`Map`\<`number`, `number`[]\>

##### dst

`Map`\<`number`, `number`[]\>

#### Returns

`Map`\<`number`, `number`[]\>

***

### noAlias()

> **noAlias**(`leftValue`, `rightValue`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:464

compare interface

#### Parameters

##### leftValue

[`Value`](../interfaces/Value.md)

##### rightValue

[`Value`](../interfaces/Value.md)

#### Returns

`boolean`

***

### preProcessMethod()

> `protected` **preProcessMethod**(`funcID`): [`CallSite`](CallSite.md)[]

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:144

#### Parameters

##### funcID

`number`

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

> `protected` **resolveCall**(`sourceMethod`, `invokeStmt`): [`CallSite`](CallSite.md)[]

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:616

#### Parameters

##### sourceMethod

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

### setEntries()

> **setEntries**(`fIds`): `void`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:149

#### Parameters

##### fIds

`number`[]

#### Returns

`void`

***

### start()

> **start**(): `void`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:110

#### Returns

`void`

#### Overrides

[`AbstractAnalysis`](AbstractAnalysis.md).[`start`](AbstractAnalysis.md#start)

***

### pointerAnalysisForMethod()

> `static` **pointerAnalysisForMethod**(`s`, `method`, `config?`): `PointerAnalysis`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:82

#### Parameters

##### s

[`Scene`](Scene.md)

##### method

[`ArkMethod`](ArkMethod.md)

##### config?

[`PointerAnalysisConfig`](PointerAnalysisConfig.md)

#### Returns

`PointerAnalysis`

***

### pointerAnalysisForWholeProject()

> `static` **pointerAnalysisForWholeProject**(`projectScene`, `config?`): `PointerAnalysis`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysis.ts:59

#### Parameters

##### projectScene

[`Scene`](Scene.md)

##### config?

[`PointerAnalysisConfig`](PointerAnalysisConfig.md)

#### Returns

`PointerAnalysis`




============================================================
## FILE: `classes/PointerAnalysisConfig.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PointerAnalysisConfig

# Class: PointerAnalysisConfig

Defined in: src/callgraph/pointerAnalysis/PointerAnalysisConfig.ts:25

## Constructors

### Constructor

> **new PointerAnalysisConfig**(`kLimit`, `outputDirectory`, `detectTypeDiff`, `dotDump`, `unhandledFuncDump`, `analysisScale`, `ptsCoType`): `PointerAnalysisConfig`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysisConfig.ts:41

#### Parameters

##### kLimit

`number`

##### outputDirectory

`string`

##### detectTypeDiff

`boolean` = `false`

##### dotDump

`boolean` = `false`

##### unhandledFuncDump

`boolean` = `false`

##### analysisScale

`PtaAnalysisScale` = `PtaAnalysisScale.WholeProgram`

##### ptsCoType

`PtsCollectionType` = `PtsCollectionType.Set`

#### Returns

`PointerAnalysisConfig`

## Properties

### analysisScale

> **analysisScale**: `PtaAnalysisScale`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysisConfig.ts:33

***

### detectTypeDiff

> **detectTypeDiff**: `boolean`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysisConfig.ts:30

***

### dotDump

> **dotDump**: `boolean`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysisConfig.ts:31

***

### kLimit

> **kLimit**: `number`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysisConfig.ts:28

***

### outputDirectory

> **outputDirectory**: `string`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysisConfig.ts:29

***

### ptsCollectionCtor()

> **ptsCollectionCtor**: () => `IPtsCollection`\<`number`\>

Defined in: src/callgraph/pointerAnalysis/PointerAnalysisConfig.ts:35

#### Returns

`IPtsCollection`\<`number`\>

***

### ptsCollectionType

> **ptsCollectionType**: `PtsCollectionType`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysisConfig.ts:34

***

### unhandledFuncDump

> **unhandledFuncDump**: `boolean`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysisConfig.ts:32

## Methods

### create()

> `static` **create**(`kLimit`, `outputDirectory`, `detectTypeDiff`, `dotDump`, `unhandledFuncDump`, `analysisScale`, `ptsCoType`): `PointerAnalysisConfig`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysisConfig.ts:71

#### Parameters

##### kLimit

`number`

##### outputDirectory

`string`

##### detectTypeDiff

`boolean` = `false`

##### dotDump

`boolean` = `false`

##### unhandledFuncDump

`boolean` = `false`

##### analysisScale

`PtaAnalysisScale` = `PtaAnalysisScale.WholeProgram`

##### ptsCoType

`PtsCollectionType` = `PtsCollectionType.Set`

#### Returns

`PointerAnalysisConfig`

***

### getInstance()

> `static` **getInstance**(): `PointerAnalysisConfig`

Defined in: src/callgraph/pointerAnalysis/PointerAnalysisConfig.ts:95

#### Returns

`PointerAnalysisConfig`




============================================================
## FILE: `classes/PrimitiveType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PrimitiveType

# Class: `abstract` PrimitiveType

Defined in: src/core/base/Type.ts:120

primitive type

## Extends

- [`Type`](Type.md)

## Extended by

- [`BooleanType`](BooleanType.md)
- [`NumberType`](NumberType.md)
- [`BigIntType`](BigIntType.md)
- [`StringType`](StringType.md)
- [`NullType`](NullType.md)
- [`UndefinedType`](UndefinedType.md)
- [`LiteralType`](LiteralType.md)

## Constructors

### Constructor

> **new PrimitiveType**(`name`): `PrimitiveType`

Defined in: src/core/base/Type.ts:123

#### Parameters

##### name

`string`

#### Returns

`PrimitiveType`

#### Overrides

[`Type`](Type.md).[`constructor`](Type.md#constructor)

## Methods

### getName()

> **getName**(): `string`

Defined in: src/core/base/Type.ts:128

#### Returns

`string`

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:132

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
## FILE: `classes/Printer.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Printer

# Class: `abstract` Printer

Defined in: src/save/Printer.ts:21

## Extended by

- [`DotMethodPrinter`](DotMethodPrinter.md)
- [`DotClassPrinter`](DotClassPrinter.md)
- [`DotNamespacePrinter`](DotNamespacePrinter.md)
- [`DotFilePrinter`](DotFilePrinter.md)
- [`SourceFilePrinter`](SourceFilePrinter.md)
- [`JsonPrinter`](JsonPrinter.md)
- [`GraphPrinter`](GraphPrinter.md)
- [`ViewTreePrinter`](ViewTreePrinter.md)

## Constructors

### Constructor

> **new Printer**(`indent`): `Printer`

Defined in: src/save/Printer.ts:24

#### Parameters

##### indent

`string` = `''`

#### Returns

`Printer`

## Properties

### printer

> `protected` **printer**: `ArkCodeBuffer`

Defined in: src/save/Printer.ts:22

## Methods

### dump()

> `abstract` **dump**(): `string`

Defined in: src/save/Printer.ts:31

ArkIR dump

#### Returns

`string`




============================================================
## FILE: `classes/PrinterBuilder.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PrinterBuilder

# Class: PrinterBuilder

Defined in: src/save/PrinterBuilder.ts:47

## Example

```ts
// dump method IR to ts source
let method: Method = xx;
let srcPrinter = new SourceMethodPrinter(method);
PrinterBuilder.dump(srcPrinter, 'output.ts');

// dump method cfg to dot
let dotPrinter = new DotMethodPrinter(method);
PrinterBuilder.dump(dotPrinter, 'output.dot');

// dump project
let printer = new PrinterBuilder('output');
for (let f of scene.getFiles()) {
    printer.dumpToTs(f);
}
```

## Constructors

### Constructor

> **new PrinterBuilder**(`outputDir`): `PrinterBuilder`

Defined in: src/save/PrinterBuilder.ts:49

#### Parameters

##### outputDir

`string` = `''`

#### Returns

`PrinterBuilder`

## Properties

### outputDir

> **outputDir**: `string`

Defined in: src/save/PrinterBuilder.ts:48

## Methods

### dumpToDot()

> **dumpToDot**(`arkFile`, `output`): `void`

Defined in: src/save/PrinterBuilder.ts:65

#### Parameters

##### arkFile

[`ArkFile`](ArkFile.md)

##### output

`undefined` | `string`

#### Returns

`void`

***

### dumpToIR()

> **dumpToIR**(`arkFile`, `output`): `void`

Defined in: src/save/PrinterBuilder.ts:101

#### Parameters

##### arkFile

[`ArkFile`](ArkFile.md)

##### output

`undefined` | `string`

#### Returns

`void`

***

### dumpToJson()

> **dumpToJson**(`arkFile`, `output`): `void`

Defined in: src/save/PrinterBuilder.ts:90

#### Parameters

##### arkFile

[`ArkFile`](ArkFile.md)

##### output

`undefined` | `string`

#### Returns

`void`

***

### dumpToTs()

> **dumpToTs**(`arkFile`, `output`): `void`

Defined in: src/save/PrinterBuilder.ts:76

#### Parameters

##### arkFile

[`ArkFile`](ArkFile.md)

##### output

`undefined` | `string`

#### Returns

`void`

***

### getOutputDir()

> `protected` **getOutputDir**(`arkFile`): `string`

Defined in: src/save/PrinterBuilder.ts:57

#### Parameters

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

`string`

***

### dump()

> `static` **dump**(`source`, `output`): `void`

Defined in: src/save/PrinterBuilder.ts:53

#### Parameters

##### source

[`Printer`](Printer.md)

##### output

`string`

#### Returns

`void`




============================================================
## FILE: `classes/PtsSet.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PtsSet

# Class: PtsSet\<T\>

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:50

## Type Parameters

### T

`T` *extends* `Idx`

## Implements

- `IPtsCollection`\<`T`\>

## Constructors

### Constructor

> **new PtsSet**\<`T`\>(): `PtsSet`\<`T`\>

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:53

#### Returns

`PtsSet`\<`T`\>

## Properties

### pts

> **pts**: `Set`\<`T`\>

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:51

## Methods

### \[iterator\]()

> **\[iterator\]**(): `IterableIterator`\<`T`\>

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:137

#### Returns

`IterableIterator`\<`T`\>

#### Implementation of

`IPtsCollection.[iterator]`

***

### clear()

> **clear**(): `void`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:101

#### Returns

`void`

#### Implementation of

`IPtsCollection.clear`

***

### clone()

> **clone**(): `this`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:77

#### Returns

`this`

#### Implementation of

`IPtsCollection.clone`

***

### contains()

> **contains**(`elem`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:57

#### Parameters

##### elem

`T`

#### Returns

`boolean`

#### Implementation of

`IPtsCollection.contains`

***

### count()

> **count**(): `number`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:105

#### Returns

`number`

#### Implementation of

`IPtsCollection.count`

***

### getProtoPtsSet()

> **getProtoPtsSet**(): `Set`\<`T`\>

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:133

#### Returns

`Set`\<`T`\>

#### Implementation of

`IPtsCollection.getProtoPtsSet`

***

### insert()

> **insert**(`elem`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:61

#### Parameters

##### elem

`T`

#### Returns

`boolean`

#### Implementation of

`IPtsCollection.insert`

***

### intersect()

> **intersect**(`other`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:124

#### Parameters

##### other

`this`

#### Returns

`boolean`

#### Implementation of

`IPtsCollection.intersect`

***

### isEmpty()

> **isEmpty**(): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:109

#### Returns

`boolean`

#### Implementation of

`IPtsCollection.isEmpty`

***

### remove()

> **remove**(`elem`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:69

#### Parameters

##### elem

`T`

#### Returns

`boolean`

#### Implementation of

`IPtsCollection.remove`

***

### subtract()

> **subtract**(`other`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:92

#### Parameters

##### other

`this`

#### Returns

`boolean`

#### Implementation of

`IPtsCollection.subtract`

***

### superset()

> **superset**(`other`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:114

#### Parameters

##### other

`this`

#### Returns

`boolean`

#### Implementation of

`IPtsCollection.superset`

***

### union()

> **union**(`other`): `boolean`

Defined in: src/callgraph/pointerAnalysis/PtsDS.ts:84

#### Parameters

##### other

`this`

#### Returns

`boolean`

#### Implementation of

`IPtsCollection.union`




============================================================
## FILE: `classes/RapidTypeAnalysis.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / RapidTypeAnalysis

# Class: RapidTypeAnalysis

Defined in: src/callgraph/algorithm/RapidTypeAnalysis.ts:29

## Extends

- [`AbstractAnalysis`](AbstractAnalysis.md)

## Constructors

### Constructor

> **new RapidTypeAnalysis**(`scene`, `cg`): `RapidTypeAnalysis`

Defined in: src/callgraph/algorithm/RapidTypeAnalysis.ts:35

#### Parameters

##### scene

[`Scene`](Scene.md)

##### cg

[`CallGraph`](CallGraph.md)

#### Returns

`RapidTypeAnalysis`

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

### addIgnoredCalls()

> **addIgnoredCalls**(`arkClass`, `callerID`, `calleeID`, `invokeStmt`): `void`

Defined in: src/callgraph/algorithm/RapidTypeAnalysis.ts:148

#### Parameters

##### arkClass

[`ClassSignature`](ClassSignature.md)

##### callerID

`number`

##### calleeID

`number`

##### invokeStmt

[`Stmt`](Stmt.md)

#### Returns

`void`

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

> `protected` **preProcessMethod**(`funcID`): [`CallSite`](CallSite.md)[]

Defined in: src/callgraph/algorithm/RapidTypeAnalysis.ts:101

#### Parameters

##### funcID

`number`

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

Defined in: src/callgraph/algorithm/RapidTypeAnalysis.ts:39

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
## FILE: `classes/RefUseReplacer.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / RefUseReplacer

# Class: RefUseReplacer

Defined in: src/core/common/RefUseReplacer.ts:23

Replace old use of a Ref inplace

## Constructors

### Constructor

> **new RefUseReplacer**(`oldUse`, `newUse`): `RefUseReplacer`

Defined in: src/core/common/RefUseReplacer.ts:27

#### Parameters

##### oldUse

[`Value`](../interfaces/Value.md)

##### newUse

[`Value`](../interfaces/Value.md)

#### Returns

`RefUseReplacer`

## Methods

### caseRef()

> **caseRef**(`ref`): `void`

Defined in: src/core/common/RefUseReplacer.ts:32

#### Parameters

##### ref

[`AbstractRef`](AbstractRef.md)

#### Returns

`void`




============================================================
## FILE: `classes/SCCDetection.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / SCCDetection

# Class: SCCDetection\<Graph\>

Defined in: src/core/graph/Scc.ts:60

Detect strongly connected components in a directed graph
A topological graph is an extra product from this algorithm
Advanced Nuutila’s algorithm which come from the following paper:
  Wave Propagation and Deep Propagation for pointer Analysis
  CGO 2009

## Type Parameters

### Graph

`Graph` *extends* `GraphTraits`\<[`BaseNode`](BaseNode.md)\>

## Constructors

### Constructor

> **new SCCDetection**\<`Graph`\>(`GT`): `SCCDetection`\<`Graph`\>

Defined in: src/core/graph/Scc.ts:84

#### Parameters

##### GT

`Graph`

#### Returns

`SCCDetection`\<`Graph`\>

## Methods

### find()

> **find**(): `void`

Defined in: src/core/graph/Scc.ts:218

Start to detect and collapse SCC

#### Returns

`void`

***

### getMySCCNodes()

> **getMySCCNodes**(`n`): `NodeSet`

Defined in: src/core/graph/Scc.ts:255

#### Parameters

##### n

`number`

#### Returns

`NodeSet`

***

### getNode2SCCInfoMap()

> **getNode2SCCInfoMap**(): `Node2RepSCCInfoMap`

Defined in: src/core/graph/Scc.ts:233

#### Returns

`Node2RepSCCInfoMap`

***

### getRepNode()

> **getRepNode**(`n`): `number`

Defined in: src/core/graph/Scc.ts:206

Get the rep node
If not found return itself

#### Parameters

##### n

`number`

#### Returns

`number`

***

### getRepNodes()

> **getRepNodes**(): `NodeSet`

Defined in: src/core/graph/Scc.ts:275

#### Returns

`NodeSet`

***

### getSubNodes()

> **getSubNodes**(`n`): `NodeSet`

Defined in: src/core/graph/Scc.ts:261

#### Parameters

##### n

`number`

#### Returns

`NodeSet`

***

### getTopoAndCollapsedNodeStack()

> **getTopoAndCollapsedNodeStack**(): `NodeStack`

Defined in: src/core/graph/Scc.ts:229

#### Returns

`NodeStack`

***

### nodeIsInCycle()

> **nodeIsInCycle**(`n`): `boolean`

Defined in: src/core/graph/Scc.ts:238

#### Parameters

##### n

`number`

#### Returns

`boolean`




============================================================
## FILE: `classes/Scene.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Scene

# Class: Scene

Defined in: src/Scene.ts:61

The Scene class includes everything in the analyzed project.
We should be able to re-generate the project's code based on this class.

## Constructors

### Constructor

> **new Scene**(): `Scene`

Defined in: src/Scene.ts:100

#### Returns

`Scene`

## Methods

### addToMethodsMap()

> **addToMethodsMap**(`method`): `void`

Defined in: src/Scene.ts:953

#### Parameters

##### method

[`ArkMethod`](ArkMethod.md)

#### Returns

`void`

***

### buildBasicInfo()

> **buildBasicInfo**(`sceneConfig`): `void`

Defined in: src/Scene.ts:174

Set the basic information of the scene using a config,
such as the project's name, real path and files.

#### Parameters

##### sceneConfig

[`SceneConfig`](SceneConfig.md)

the config used to set the basic information of scene.

#### Returns

`void`

***

### buildClassDone()

> **buildClassDone**(): `boolean`

Defined in: src/Scene.ts:1363

#### Returns

`boolean`

***

### buildModuleScene()

> **buildModuleScene**(`moduleName`, `modulePath`, `supportFileExts`): `void`

Defined in: src/Scene.ts:625

#### Parameters

##### moduleName

`string`

##### modulePath

`string`

##### supportFileExts

`string`[]

#### Returns

`void`

***

### buildScene4HarmonyProject()

> **buildScene4HarmonyProject**(): `void`

Defined in: src/Scene.ts:603

Build the scene for harmony project. It resolves the file path of the project first, and then fetches
dependencies from this file. Next, build a `ModuleScene` for this project to generate [ArkFile](ArkFile.md). Finally,
it build bodies of all methods, generate extended classes, and add DefaultConstructors.

#### Returns

`void`

***

### buildSceneFromFiles()

> **buildSceneFromFiles**(`sceneConfig`): `void`

Defined in: src/Scene.ts:162

#### Parameters

##### sceneConfig

[`SceneConfig`](SceneConfig.md)

#### Returns

`void`

***

### buildSceneFromProjectDir()

> **buildSceneFromProjectDir**(`sceneConfig`): `void`

Defined in: src/Scene.ts:157

Build scene object according to the [SceneConfig](SceneConfig.md). This API implements 3 functions.
First is to build scene object from [SceneConfig](SceneConfig.md), second is to generate [ArkFile](ArkFile.md)s,
and the last is to collect project import infomation.

#### Parameters

##### sceneConfig

[`SceneConfig`](SceneConfig.md)

a sceneConfig object, which is usally defined by user or Json file.

#### Returns

`void`

#### Example

1. Build Scene object from scene config

```typescript
// build config
const projectDir = ... ...;
const sceneConfig = new SceneConfig();
sceneConfig.buildFromProjectDir(projectDir);

// build scene
const scene = new Scene();
scene.buildSceneFromProjectDir(sceneConfig);
```

***

### clear()

> **clear**(): `void`

Defined in: src/Scene.ts:114

#### Returns

`void`

***

### getbaseUrl()

> **getbaseUrl**(): `undefined` \| `string`

Defined in: src/Scene.ts:1379

#### Returns

`undefined` \| `string`

***

### getClass()

> **getClass**(`classSignature`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/Scene.ts:847

Returns the class according to the input class signature.

#### Parameters

##### classSignature

[`ClassSignature`](ClassSignature.md)

signature of the class to be obtained.

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

A class.

***

### getClasses()

> **getClasses**(): [`ArkClass`](ArkClass.md)[]

Defined in: src/Scene.ts:889

#### Returns

[`ArkClass`](ArkClass.md)[]

***

### getClassMap()

> **getClassMap**(): `Map`\<[`NamespaceSignature`](NamespaceSignature.md) \| [`FileSignature`](FileSignature.md), [`ArkClass`](ArkClass.md)[]\>

Defined in: src/Scene.ts:1170

#### Returns

`Map`\<[`NamespaceSignature`](NamespaceSignature.md) \| [`FileSignature`](FileSignature.md), [`ArkClass`](ArkClass.md)[]\>

***

### getEntryPoints()

> **getEntryPoints**(): [`MethodSignature`](MethodSignature.md)[]

Defined in: src/Scene.ts:978

#### Returns

[`MethodSignature`](MethodSignature.md)[]

***

### getFile()

> **getFile**(`fileSignature`): `null` \| [`ArkFile`](ArkFile.md)

Defined in: src/Scene.ts:722

Returns the file based on its signature.
If no file can be found according to the input signature, **null** will be returned.
A typical [ArkFile](ArkFile.md) contains: file's name (i.e., its relative path), project's name,
project's dir, file's signature etc.

#### Parameters

##### fileSignature

[`FileSignature`](FileSignature.md)

the signature of file.

#### Returns

`null` \| [`ArkFile`](ArkFile.md)

a file defined by ArkAnalyzer. **null** will be returned if no file could be found.

#### Example

1. get ArkFile based on file signature.

```typescript
if (...) {
const fromSignature = new FileSignature();
fromSignature.setProjectName(im.getDeclaringArkFile().getProjectName());
fromSignature.setFileName(fileName);
return scene.getFile(fromSignature);
}
```

***

### getFileLanguages()

> **getFileLanguages**(): `Map`\<`string`, `Language`\>

Defined in: src/Scene.ts:784

#### Returns

`Map`\<`string`, `Language`\>

***

### getFiles()

> **getFiles**(): [`ArkFile`](ArkFile.md)[]

Defined in: src/Scene.ts:780

Get files of a Scene. Generally, a project includes several ets/ts files that define the different
class. We need to generate [ArkFile](ArkFile.md) objects from these ets/ts files.

#### Returns

[`ArkFile`](ArkFile.md)[]

The array of [ArkFile](ArkFile.md) from `scene.filesMap.values()`.

#### Example

1. In inferSimpleTypes() to check arkClass and arkMethod.
```typescript
public inferSimpleTypes(): void {
  for (let arkFile of this.getFiles()) {
      for (let arkClass of arkFile.getClasses()) {
          for (let arkMethod of arkClass.getMethods()) {
          // ... ...;
          }
      }
  }
}
```
2. To iterate each method
```typescript
for (const file of this.getFiles()) {
    for (const cls of file.getClasses()) {
        for (const method of cls.getMethods()) {
            // ... ...
        }
    }
}
```

***

### getGlobalModule2PathMapping()

> **getGlobalModule2PathMapping**(): `undefined` \| \{[`k`: `string`]: `string`[]; \}

Defined in: src/Scene.ts:1375

#### Returns

`undefined` \| \{[`k`: `string`]: `string`[]; \}

***

### getGlobalVariableMap()

> **getGlobalVariableMap**(): `Map`\<[`NamespaceSignature`](NamespaceSignature.md) \| [`FileSignature`](FileSignature.md), [`Local`](Local.md)[]\>

Defined in: src/Scene.ts:1317

#### Returns

`Map`\<[`NamespaceSignature`](NamespaceSignature.md) \| [`FileSignature`](FileSignature.md), [`Local`](Local.md)[]\>

***

### getMethod()

> **getMethod**(`methodSignature`, `refresh?`): `null` \| [`ArkMethod`](ArkMethod.md)

Defined in: src/Scene.ts:893

#### Parameters

##### methodSignature

[`MethodSignature`](MethodSignature.md)

##### refresh?

`boolean`

#### Returns

`null` \| [`ArkMethod`](ArkMethod.md)

***

### getMethods()

> **getMethods**(): [`ArkMethod`](ArkMethod.md)[]

Defined in: src/Scene.ts:949

Returns the method associated with the method signature.
If no method is associated with this signature, **null** will be returned.
An [ArkMethod](ArkMethod.md) includes:
- Name: the **string** name of method.
- Code: the **string** code of the method.
- Line: a **number** indicating the line location, initialized as -1.
- Column: a **number** indicating the column location, initialized as -1.
- Parameters & Types of parameters: the parameters of method and their types.
- View tree: the view tree of the method.
- ...

#### Returns

[`ArkMethod`](ArkMethod.md)[]

The method associated with the method signature.

#### Example

1. get method from getMethod.

```typescript
const methodSignatures = this.CHA.resolveCall(xxx, yyy);
for (const methodSignature of methodSignatures) {
const method = this.scene.getMethod(methodSignature);
... ...
}
```

***

### getModuleScene()

> **getModuleScene**(`moduleName`): `undefined` \| `ModuleScene`

Defined in: src/Scene.ts:1367

#### Parameters

##### moduleName

`string`

#### Returns

`undefined` \| `ModuleScene`

***

### getModuleSceneMap()

> **getModuleSceneMap**(): `Map`\<`string`, `ModuleScene`\>

Defined in: src/Scene.ts:1371

#### Returns

`Map`\<`string`, `ModuleScene`\>

***

### getModuleSdkMap()

> **getModuleSdkMap**(): `Map`\<`string`, `Sdk`[]\>

Defined in: src/Scene.ts:792

#### Returns

`Map`\<`string`, `Sdk`[]\>

***

### getNamespace()

> **getNamespace**(`namespaceSignature`): `null` \| [`ArkNamespace`](ArkNamespace.md)

Defined in: src/Scene.ts:800

#### Parameters

##### namespaceSignature

[`NamespaceSignature`](NamespaceSignature.md)

#### Returns

`null` \| [`ArkNamespace`](ArkNamespace.md)

***

### getNamespaces()

> **getNamespaces**(): [`ArkNamespace`](ArkNamespace.md)[]

Defined in: src/Scene.ts:838

#### Returns

[`ArkNamespace`](ArkNamespace.md)[]

***

### getOhPkgContent()

> **getOhPkgContent**(): `object`

Defined in: src/Scene.ts:987

#### Returns

`object`

***

### getOhPkgContentMap()

> **getOhPkgContentMap**(): `Map`\<`string`, \{[`p`: `string`]: `unknown`; \}\>

Defined in: src/Scene.ts:991

#### Returns

`Map`\<`string`, \{[`p`: `string`]: `unknown`; \}\>

***

### getOhPkgFilePath()

> **getOhPkgFilePath**(): `string`

Defined in: src/Scene.ts:995

#### Returns

`string`

***

### getOptions()

> **getOptions**(): `SceneOptions`

Defined in: src/Scene.ts:102

#### Returns

`SceneOptions`

***

### getOverRideDependencyMap()

> **getOverRideDependencyMap**(): `Map`\<`string`, `unknown`\>

Defined in: src/Scene.ts:110

#### Returns

`Map`\<`string`, `unknown`\>

***

### getOverRides()

> **getOverRides**(): `Map`\<`string`, `string`\>

Defined in: src/Scene.ts:106

#### Returns

`Map`\<`string`, `string`\>

***

### getProjectFiles()

> **getProjectFiles**(): `string`[]

Defined in: src/Scene.ts:695

#### Returns

`string`[]

***

### getProjectName()

> **getProjectName**(): `string`

Defined in: src/Scene.ts:691

Returns the **string** name of the project.

#### Returns

`string`

The name of the project.

***

### getProjectSdkMap()

> **getProjectSdkMap**(): `Map`\<`string`, `Sdk`\>

Defined in: src/Scene.ts:796

#### Returns

`Map`\<`string`, `Sdk`\>

***

### getRealProjectDir()

> **getRealProjectDir**(): `string`

Defined in: src/Scene.ts:683

Get the absolute path of current project.

#### Returns

`string`

The real project's directiory.

#### Example

1. get real project directory, such as:
```typescript
let projectDir = projectScene.getRealProjectDir(); 
```

***

### getSdkArkFiles()

> **getSdkArkFiles**(): [`ArkFile`](ArkFile.md)[]

Defined in: src/Scene.ts:788

#### Returns

[`ArkFile`](ArkFile.md)[]

***

### getSdkGlobal()

> **getSdkGlobal**(`globalName`): `null` \| `ArkExport`

Defined in: src/Scene.ts:699

#### Parameters

##### globalName

`string`

#### Returns

`null` \| `ArkExport`

***

### getStage()

> **getStage**(): `SceneBuildStage`

Defined in: src/Scene.ts:134

#### Returns

`SceneBuildStage`

***

### getStaticInitMethods()

> **getStaticInitMethods**(): [`ArkMethod`](ArkMethod.md)[]

Defined in: src/Scene.ts:1353

#### Returns

[`ArkMethod`](ArkMethod.md)[]

***

### getUnhandledFilePaths()

> **getUnhandledFilePaths**(): `string`[]

Defined in: src/Scene.ts:733

#### Returns

`string`[]

***

### getUnhandledSdkFilePaths()

> **getUnhandledSdkFilePaths**(): `string`[]

Defined in: src/Scene.ts:740

#### Returns

`string`[]

***

### getVisibleValue()

> **getVisibleValue**(): [`VisibleValue`](VisibleValue.md)

Defined in: src/Scene.ts:983

get values that is visible in curr scope

#### Returns

[`VisibleValue`](VisibleValue.md)

***

### hasMainMethod()

> **hasMainMethod**(): `boolean`

Defined in: src/Scene.ts:973

#### Returns

`boolean`

***

### hasSdkFile()

> **hasSdkFile**(`fileSignature`): `boolean`

Defined in: src/Scene.ts:748

#### Parameters

##### fileSignature

[`FileSignature`](FileSignature.md)

#### Returns

`boolean`

***

### inferSimpleTypes()

> **inferSimpleTypes**(): `void`

Defined in: src/Scene.ts:1063

Iterate all assignment statements in methods,
and set the type of left operand based on the type of right operand
if the left operand is a local variable as well as an unknown.

#### Returns

`void`

#### Deprecated

#### Example

1. Infer simple type when scene building.

```typescript
let scene = new Scene();
scene.buildSceneFromProjectDir(config);
scene.inferSimpleTypes();
```

***

### inferTypes()

> **inferTypes**(): `void`

Defined in: src/Scene.ts:1025

Infer type for each non-default method. It infers the type of each field/local/reference.
For example, the statement `let b = 5;`, the type of local `b` is `NumberType`; and for the statement `let s =
'hello';`, the type of local `s` is `StringType`. The detailed types are defined in the Type.ts file.

#### Returns

`void`

#### Example

1. Infer the type of each class field and method field.
```typescript
const scene = new Scene();
scene.buildSceneFromProjectDir(sceneConfig);
scene.inferTypes();
```

***

### makeCallGraphCHA()

> **makeCallGraphCHA**(`entryPoints`): [`CallGraph`](CallGraph.md)

Defined in: src/Scene.ts:999

#### Parameters

##### entryPoints

[`MethodSignature`](MethodSignature.md)[]

#### Returns

[`CallGraph`](CallGraph.md)

***

### makeCallGraphRTA()

> **makeCallGraphRTA**(`entryPoints`): [`CallGraph`](CallGraph.md)

Defined in: src/Scene.ts:1006

#### Parameters

##### entryPoints

[`MethodSignature`](MethodSignature.md)[]

#### Returns

[`CallGraph`](CallGraph.md)

***

### removeClass()

> **removeClass**(`arkClass`): `boolean`

Defined in: src/Scene.ts:961

#### Parameters

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`boolean`

***

### removeFile()

> **removeFile**(`file`): `boolean`

Defined in: src/Scene.ts:969

#### Parameters

##### file

[`ArkFile`](ArkFile.md)

#### Returns

`boolean`

***

### removeMethod()

> **removeMethod**(`method`): `boolean`

Defined in: src/Scene.ts:957

#### Parameters

##### method

[`ArkMethod`](ArkMethod.md)

#### Returns

`boolean`

***

### removeNamespace()

> **removeNamespace**(`namespace`): `boolean`

Defined in: src/Scene.ts:965

#### Parameters

##### namespace

[`ArkNamespace`](ArkNamespace.md)

#### Returns

`boolean`

***

### setFile()

> **setFile**(`file`): `void`

Defined in: src/Scene.ts:744

#### Parameters

##### file

[`ArkFile`](ArkFile.md)

#### Returns

`void`




============================================================
## FILE: `classes/SceneConfig.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / SceneConfig

# Class: SceneConfig

Defined in: src/Config.ts:54

## Constructors

### Constructor

> **new SceneConfig**(`options?`): `SceneConfig`

Defined in: src/Config.ts:69

#### Parameters

##### options?

`SceneOptions`

#### Returns

`SceneConfig`

## Methods

### buildConfig()

> **buildConfig**(`targetProjectName`, `targetProjectDirectory`, `sdks`, `fullFilePath?`): `void`

Defined in: src/Config.ts:86

Set the scene's config,
such as  the target project's name, the used sdks and the full path.

#### Parameters

##### targetProjectName

`string`

the target project's name.

##### targetProjectDirectory

`string`

the target project's directory.

##### sdks

`Sdk`[]

sdks used in this scene.

##### fullFilePath?

`string`[]

the full file path.

#### Returns

`void`

***

### buildFromJson()

> **buildFromJson**(`configJsonPath`): `void`

Defined in: src/Config.ts:171

#### Parameters

##### configJsonPath

`string`

#### Returns

`void`

***

### buildFromProjectDir()

> **buildFromProjectDir**(`targetProjectDirectory`): `void`

Defined in: src/Config.ts:109

Create a sceneConfig object for a specified project path and set the target project directory to the
targetProjectDirectory property of the sceneConfig object.

#### Parameters

##### targetProjectDirectory

`string`

the target project directory, such as xxx/xxx/xxx, started from project
    directory.

#### Returns

`void`

#### Example

1. build a sceneConfig object.
```typescript
const projectDir = 'xxx/xxx/xxx';
const sceneConfig: SceneConfig = new SceneConfig();
sceneConfig.buildFromProjectDir(projectDir);
```

***

### buildFromProjectFiles()

> **buildFromProjectFiles**(`projectName`, `projectDir`, `filesAndDirectorys`, `sdks?`, `languageTags?`): `void`

Defined in: src/Config.ts:115

#### Parameters

##### projectName

`string`

##### projectDir

`string`

##### filesAndDirectorys

`string`[]

##### sdks?

`Sdk`[]

##### languageTags?

`Map`\<`string`, `Language`\>

#### Returns

`void`

***

### getEtsSdkPath()

> **getEtsSdkPath**(): `string`

Defined in: src/Config.ts:228

#### Returns

`string`

***

### getFileLanguages()

> **getFileLanguages**(): `Map`\<`string`, `Language`\>

Defined in: src/Config.ts:216

#### Returns

`Map`\<`string`, `Language`\>

***

### getOptions()

> **getOptions**(): `SceneOptions`

Defined in: src/Config.ts:74

#### Returns

`SceneOptions`

***

### getProjectFiles()

> **getProjectFiles**(): `string`[]

Defined in: src/Config.ts:212

#### Returns

`string`[]

***

### getSdkFiles()

> **getSdkFiles**(): `string`[]

Defined in: src/Config.ts:220

#### Returns

`string`[]

***

### getSdkFilesMap()

> **getSdkFilesMap**(): `Map`\<`string`[], `string`\>

Defined in: src/Config.ts:224

#### Returns

`Map`\<`string`[], `string`\>

***

### getSdksObj()

> **getSdksObj**(): `Sdk`[]

Defined in: src/Config.ts:232

#### Returns

`Sdk`[]

***

### getTargetProjectDirectory()

> **getTargetProjectDirectory**(): `string`

Defined in: src/Config.ts:208

#### Returns

`string`

***

### getTargetProjectName()

> **getTargetProjectName**(): `string`

Defined in: src/Config.ts:204

#### Returns

`string`




============================================================
## FILE: `classes/SceneManager.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / SceneManager

# Class: SceneManager

Defined in: src/utils/callGraphUtils.ts:75

## Constructors

### Constructor

> **new SceneManager**(): `SceneManager`

#### Returns

`SceneManager`

## Accessors

### scene

#### Get Signature

> **get** **scene**(): [`Scene`](Scene.md)

Defined in: src/utils/callGraphUtils.ts:78

##### Returns

[`Scene`](Scene.md)

#### Set Signature

> **set** **scene**(`value`): `void`

Defined in: src/utils/callGraphUtils.ts:82

##### Parameters

###### value

[`Scene`](Scene.md)

##### Returns

`void`

## Methods

### getClass()

> **getClass**(`arkClass`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/utils/callGraphUtils.ts:104

#### Parameters

##### arkClass

[`ClassSignature`](ClassSignature.md)

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

***

### getExtendedClasses()

> **getExtendedClasses**(`arkClass`): [`ArkClass`](ArkClass.md)[]

Defined in: src/utils/callGraphUtils.ts:124

#### Parameters

##### arkClass

[`ClassSignature`](ClassSignature.md)

#### Returns

[`ArkClass`](ArkClass.md)[]

***

### getMethod()

> **getMethod**(`method`): `null` \| [`ArkMethod`](ArkMethod.md)

Defined in: src/utils/callGraphUtils.ts:86

#### Parameters

##### method

[`MethodSignature`](MethodSignature.md)

#### Returns

`null` \| [`ArkMethod`](ArkMethod.md)




============================================================
## FILE: `classes/Scope.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Scope

# Class: Scope

Defined in: src/core/common/VisibleValue.ts:195

## Constructors

### Constructor

> **new Scope**(`values`, `depth`, `arkModel`): `Scope`

Defined in: src/core/common/VisibleValue.ts:199

#### Parameters

##### values

[`Value`](../interfaces/Value.md)[]

##### depth

`number` = `-1`

##### arkModel

`null` | `ArkModel`

#### Returns

`Scope`

## Properties

### arkModel

> **arkModel**: `null` \| `ArkModel`

Defined in: src/core/common/VisibleValue.ts:198

***

### depth

> **depth**: `number`

Defined in: src/core/common/VisibleValue.ts:197

***

### values

> **values**: [`Value`](../interfaces/Value.md)[]

Defined in: src/core/common/VisibleValue.ts:196




============================================================
## FILE: `classes/SourceClassPrinter.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / SourceClassPrinter

# Class: SourceClassPrinter

Defined in: src/save/source/SourceClass.ts:32

## Extends

- `SourceBase`

## Constructors

### Constructor

> **new SourceClassPrinter**(`cls`, `indent`): `SourceClass`

Defined in: src/save/source/SourceClass.ts:36

#### Parameters

##### cls

[`ArkClass`](ArkClass.md)

##### indent

`string` = `''`

#### Returns

`SourceClass`

#### Overrides

`SourceBase.constructor`

## Properties

### arkFile

> `protected` **arkFile**: [`ArkFile`](ArkFile.md)

Defined in: src/save/source/SourceBase.ts:27

#### Inherited from

`SourceBase.arkFile`

***

### cls

> `protected` **cls**: [`ArkClass`](ArkClass.md)

Defined in: src/save/source/SourceClass.ts:33

***

### inBuilder

> `protected` **inBuilder**: `boolean` = `false`

Defined in: src/save/source/SourceBase.ts:28

#### Inherited from

`SourceBase.inBuilder`

***

### printer

> `protected` **printer**: `ArkCodeBuffer`

Defined in: src/save/Printer.ts:22

#### Inherited from

`SourceBase.printer`

## Methods

### classOriginTypeToString()

> `protected` **classOriginTypeToString**(`clsCategory`): `string`

Defined in: src/save/base/BasePrinter.ts:75

#### Parameters

##### clsCategory

`ClassCategory`

#### Returns

`string`

#### Inherited from

`SourceBase.classOriginTypeToString`

***

### dump()

> **dump**(): `string`

Defined in: src/save/source/SourceClass.ts:50

ArkIR dump

#### Returns

`string`

#### Overrides

`SourceBase.dump`

***

### getArkFile()

> **getArkFile**(): [`ArkFile`](ArkFile.md)

Defined in: src/save/source/SourceBase.ts:39

#### Returns

[`ArkFile`](ArkFile.md)

#### Inherited from

`SourceBase.getArkFile`

***

### getClass()

> **getClass**(`signature`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/save/source/SourceBase.ts:47

#### Parameters

##### signature

[`ClassSignature`](ClassSignature.md)

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

#### Inherited from

`SourceBase.getClass`

***

### getDeclaringArkNamespace()

> **getDeclaringArkNamespace**(): `undefined` \| [`ArkNamespace`](ArkNamespace.md)

Defined in: src/save/source/SourceClass.ts:42

#### Returns

`undefined` \| [`ArkNamespace`](ArkNamespace.md)

#### Overrides

`SourceBase.getDeclaringArkNamespace`

***

### getLine()

> **getLine**(): `number`

Defined in: src/save/source/SourceClass.ts:46

#### Returns

`number`

#### Overrides

`SourceBase.getLine`

***

### getMethod()

> **getMethod**(`signature`): `null` \| [`ArkMethod`](ArkMethod.md)

Defined in: src/save/source/SourceBase.ts:43

#### Parameters

##### signature

[`MethodSignature`](MethodSignature.md)

#### Returns

`null` \| [`ArkMethod`](ArkMethod.md)

#### Inherited from

`SourceBase.getMethod`

***

### getPrinter()

> **getPrinter**(): `ArkCodeBuffer`

Defined in: src/save/source/SourceBase.ts:51

#### Returns

`ArkCodeBuffer`

#### Inherited from

`SourceBase.getPrinter`

***

### isInBuilderMethod()

> **isInBuilderMethod**(): `boolean`

Defined in: src/save/source/SourceBase.ts:59

#### Returns

`boolean`

#### Inherited from

`SourceBase.isInBuilderMethod`

***

### modifiersToString()

> `protected` **modifiersToString**(`modifiers`): `string`

Defined in: src/save/base/BasePrinter.ts:57

#### Parameters

##### modifiers

`number`

#### Returns

`string`

#### Inherited from

`SourceBase.modifiersToString`

***

### printComments()

> `protected` **printComments**(`commentsMetadata`): `void`

Defined in: src/save/base/BasePrinter.ts:50

#### Parameters

##### commentsMetadata

`CommentsMetadata`

#### Returns

`void`

#### Inherited from

`SourceBase.printComments`

***

### printDecorator()

> `protected` **printDecorator**(`docorator`): `void`

Defined in: src/save/base/BasePrinter.ts:44

#### Parameters

##### docorator

[`Decorator`](Decorator.md)[]

#### Returns

`void`

#### Inherited from

`SourceBase.printDecorator`

***

### printMethods()

> `protected` **printMethods**(): `Dump`[]

Defined in: src/save/source/SourceClass.ts:153

#### Returns

`Dump`[]

***

### resolveKeywordType()

> `protected` **resolveKeywordType**(`keywordStr`): `string`

Defined in: src/save/source/SourceBase.ts:63

#### Parameters

##### keywordStr

`string`

#### Returns

`string`

#### Inherited from

`SourceBase.resolveKeywordType`

***

### resolveMethodName()

> `protected` **resolveMethodName**(`name`): `string`

Defined in: src/save/base/BasePrinter.ts:62

#### Parameters

##### name

`string`

#### Returns

`string`

#### Inherited from

`SourceBase.resolveMethodName`

***

### transTemp2Code()

> **transTemp2Code**(`temp`): `string`

Defined in: src/save/source/SourceBase.ts:55

#### Parameters

##### temp

[`Local`](Local.md)

#### Returns

`string`

#### Inherited from

`SourceBase.transTemp2Code`

***

### getPrinterOptions()

> `static` **getPrinterOptions**(): `PrinterOptions`

Defined in: src/save/base/BasePrinter.ts:85

#### Returns

`PrinterOptions`

#### Inherited from

`SourceBase.getPrinterOptions`




============================================================
## FILE: `classes/SourceFilePrinter.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / SourceFilePrinter

# Class: SourceFilePrinter

Defined in: src/save/source/SourceFilePrinter.ts:49

## Extends

- [`Printer`](Printer.md)

## Constructors

### Constructor

> **new SourceFilePrinter**(`arkFile`): `SourceFilePrinter`

Defined in: src/save/source/SourceFilePrinter.ts:53

#### Parameters

##### arkFile

[`ArkFile`](ArkFile.md)

#### Returns

`SourceFilePrinter`

#### Overrides

[`Printer`](Printer.md).[`constructor`](Printer.md#constructor)

## Properties

### arkFile

> **arkFile**: [`ArkFile`](ArkFile.md)

Defined in: src/save/source/SourceFilePrinter.ts:50

***

### items

> **items**: `Dump`[] = `[]`

Defined in: src/save/source/SourceFilePrinter.ts:51

***

### printer

> `protected` **printer**: `ArkCodeBuffer`

Defined in: src/save/Printer.ts:22

#### Inherited from

[`Printer`](Printer.md).[`printer`](Printer.md#printer)

## Methods

### dump()

> **dump**(): `string`

Defined in: src/save/source/SourceFilePrinter.ts:68

ArkIR dump

#### Returns

`string`

#### Overrides

[`Printer`](Printer.md).[`dump`](Printer.md#dump)




============================================================
## FILE: `classes/SourceMethodPrinter.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / SourceMethodPrinter

# Class: SourceMethodPrinter

Defined in: src/save/source/SourceMethod.ts:34

## Extends

- `SourceBase`

## Constructors

### Constructor

> **new SourceMethodPrinter**(`method`, `indent`): `SourceMethod`

Defined in: src/save/source/SourceMethod.ts:38

#### Parameters

##### method

[`ArkMethod`](ArkMethod.md)

##### indent

`string` = `''`

#### Returns

`SourceMethod`

#### Overrides

`SourceBase.constructor`

## Properties

### arkFile

> `protected` **arkFile**: [`ArkFile`](ArkFile.md)

Defined in: src/save/source/SourceBase.ts:27

#### Inherited from

`SourceBase.arkFile`

***

### inBuilder

> `protected` **inBuilder**: `boolean` = `false`

Defined in: src/save/source/SourceBase.ts:28

#### Inherited from

`SourceBase.inBuilder`

***

### printer

> `protected` **printer**: `ArkCodeBuffer`

Defined in: src/save/Printer.ts:22

#### Inherited from

`SourceBase.printer`

## Methods

### classOriginTypeToString()

> `protected` **classOriginTypeToString**(`clsCategory`): `string`

Defined in: src/save/base/BasePrinter.ts:75

#### Parameters

##### clsCategory

`ClassCategory`

#### Returns

`string`

#### Inherited from

`SourceBase.classOriginTypeToString`

***

### dump()

> **dump**(): `string`

Defined in: src/save/source/SourceMethod.ts:53

ArkIR dump

#### Returns

`string`

#### Overrides

`SourceBase.dump`

***

### dumpDefaultMethod()

> **dumpDefaultMethod**(): `SourceStmt`[]

Defined in: src/save/source/SourceMethod.ts:98

#### Returns

`SourceStmt`[]

***

### getArkFile()

> **getArkFile**(): [`ArkFile`](ArkFile.md)

Defined in: src/save/source/SourceBase.ts:39

#### Returns

[`ArkFile`](ArkFile.md)

#### Inherited from

`SourceBase.getArkFile`

***

### getClass()

> **getClass**(`signature`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/save/source/SourceBase.ts:47

#### Parameters

##### signature

[`ClassSignature`](ClassSignature.md)

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

#### Inherited from

`SourceBase.getClass`

***

### getDeclaringArkNamespace()

> **getDeclaringArkNamespace**(): `undefined` \| [`ArkNamespace`](ArkNamespace.md)

Defined in: src/save/source/SourceMethod.ts:45

#### Returns

`undefined` \| [`ArkNamespace`](ArkNamespace.md)

#### Overrides

`SourceBase.getDeclaringArkNamespace`

***

### getLine()

> **getLine**(): `number`

Defined in: src/save/source/SourceMethod.ts:70

#### Returns

`number`

#### Overrides

`SourceBase.getLine`

***

### getMethod()

> **getMethod**(`signature`): `null` \| [`ArkMethod`](ArkMethod.md)

Defined in: src/save/source/SourceBase.ts:43

#### Parameters

##### signature

[`MethodSignature`](MethodSignature.md)

#### Returns

`null` \| [`ArkMethod`](ArkMethod.md)

#### Inherited from

`SourceBase.getMethod`

***

### getPrinter()

> **getPrinter**(): `ArkCodeBuffer`

Defined in: src/save/source/SourceBase.ts:51

#### Returns

`ArkCodeBuffer`

#### Inherited from

`SourceBase.getPrinter`

***

### isInBuilderMethod()

> **isInBuilderMethod**(): `boolean`

Defined in: src/save/source/SourceBase.ts:59

#### Returns

`boolean`

#### Inherited from

`SourceBase.isInBuilderMethod`

***

### modifiersToString()

> `protected` **modifiersToString**(`modifiers`): `string`

Defined in: src/save/base/BasePrinter.ts:57

#### Parameters

##### modifiers

`number`

#### Returns

`string`

#### Inherited from

`SourceBase.modifiersToString`

***

### printComments()

> `protected` **printComments**(`commentsMetadata`): `void`

Defined in: src/save/base/BasePrinter.ts:50

#### Parameters

##### commentsMetadata

`CommentsMetadata`

#### Returns

`void`

#### Inherited from

`SourceBase.printComments`

***

### printDecorator()

> `protected` **printDecorator**(`docorator`): `void`

Defined in: src/save/base/BasePrinter.ts:44

#### Parameters

##### docorator

[`Decorator`](Decorator.md)[]

#### Returns

`void`

#### Inherited from

`SourceBase.printDecorator`

***

### resolveKeywordType()

> `protected` **resolveKeywordType**(`keywordStr`): `string`

Defined in: src/save/source/SourceBase.ts:63

#### Parameters

##### keywordStr

`string`

#### Returns

`string`

#### Inherited from

`SourceBase.resolveKeywordType`

***

### resolveMethodName()

> `protected` **resolveMethodName**(`name`): `string`

Defined in: src/save/base/BasePrinter.ts:62

#### Parameters

##### name

`string`

#### Returns

`string`

#### Inherited from

`SourceBase.resolveMethodName`

***

### setInBuilder()

> **setInBuilder**(`inBuilder`): `void`

Defined in: src/save/source/SourceMethod.ts:49

#### Parameters

##### inBuilder

`boolean`

#### Returns

`void`

***

### toArrowFunctionTypeString()

> **toArrowFunctionTypeString**(): `string`

Defined in: src/save/source/SourceMethod.ts:192

#### Returns

`string`

***

### transTemp2Code()

> **transTemp2Code**(`temp`): `string`

Defined in: src/save/source/SourceBase.ts:55

#### Parameters

##### temp

[`Local`](Local.md)

#### Returns

`string`

#### Inherited from

`SourceBase.transTemp2Code`

***

### getPrinterOptions()

> `static` **getPrinterOptions**(): `PrinterOptions`

Defined in: src/save/base/BasePrinter.ts:85

#### Returns

`PrinterOptions`

#### Inherited from

`SourceBase.getPrinterOptions`




============================================================
## FILE: `classes/SourceNamespacePrinter.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / SourceNamespacePrinter

# Class: SourceNamespacePrinter

Defined in: src/save/source/SourceNamespace.ts:29

## Extends

- `SourceBase`

## Constructors

### Constructor

> **new SourceNamespacePrinter**(`ns`, `indent`): `SourceNamespace`

Defined in: src/save/source/SourceNamespace.ts:32

#### Parameters

##### ns

[`ArkNamespace`](ArkNamespace.md)

##### indent

`string` = `''`

#### Returns

`SourceNamespace`

#### Overrides

`SourceBase.constructor`

## Properties

### arkFile

> `protected` **arkFile**: [`ArkFile`](ArkFile.md)

Defined in: src/save/source/SourceBase.ts:27

#### Inherited from

`SourceBase.arkFile`

***

### inBuilder

> `protected` **inBuilder**: `boolean` = `false`

Defined in: src/save/source/SourceBase.ts:28

#### Inherited from

`SourceBase.inBuilder`

***

### ns

> **ns**: [`ArkNamespace`](ArkNamespace.md)

Defined in: src/save/source/SourceNamespace.ts:30

***

### printer

> `protected` **printer**: `ArkCodeBuffer`

Defined in: src/save/Printer.ts:22

#### Inherited from

`SourceBase.printer`

## Methods

### classOriginTypeToString()

> `protected` **classOriginTypeToString**(`clsCategory`): `string`

Defined in: src/save/base/BasePrinter.ts:75

#### Parameters

##### clsCategory

`ClassCategory`

#### Returns

`string`

#### Inherited from

`SourceBase.classOriginTypeToString`

***

### dump()

> **dump**(): `string`

Defined in: src/save/source/SourceNamespace.ts:51

ArkIR dump

#### Returns

`string`

#### Overrides

`SourceBase.dump`

***

### getArkFile()

> **getArkFile**(): [`ArkFile`](ArkFile.md)

Defined in: src/save/source/SourceBase.ts:39

#### Returns

[`ArkFile`](ArkFile.md)

#### Inherited from

`SourceBase.getArkFile`

***

### getClass()

> **getClass**(`signature`): `null` \| [`ArkClass`](ArkClass.md)

Defined in: src/save/source/SourceBase.ts:47

#### Parameters

##### signature

[`ClassSignature`](ClassSignature.md)

#### Returns

`null` \| [`ArkClass`](ArkClass.md)

#### Inherited from

`SourceBase.getClass`

***

### getDeclaringArkNamespace()

> **getDeclaringArkNamespace**(): `undefined` \| [`ArkNamespace`](ArkNamespace.md)

Defined in: src/save/source/SourceBase.ts:35

#### Returns

`undefined` \| [`ArkNamespace`](ArkNamespace.md)

#### Inherited from

`SourceBase.getDeclaringArkNamespace`

***

### getLine()

> **getLine**(): `number`

Defined in: src/save/source/SourceNamespace.ts:37

#### Returns

`number`

#### Overrides

`SourceBase.getLine`

***

### getMethod()

> **getMethod**(`signature`): `null` \| [`ArkMethod`](ArkMethod.md)

Defined in: src/save/source/SourceBase.ts:43

#### Parameters

##### signature

[`MethodSignature`](MethodSignature.md)

#### Returns

`null` \| [`ArkMethod`](ArkMethod.md)

#### Inherited from

`SourceBase.getMethod`

***

### getPrinter()

> **getPrinter**(): `ArkCodeBuffer`

Defined in: src/save/source/SourceBase.ts:51

#### Returns

`ArkCodeBuffer`

#### Inherited from

`SourceBase.getPrinter`

***

### isInBuilderMethod()

> **isInBuilderMethod**(): `boolean`

Defined in: src/save/source/SourceBase.ts:59

#### Returns

`boolean`

#### Inherited from

`SourceBase.isInBuilderMethod`

***

### modifiersToString()

> `protected` **modifiersToString**(`modifiers`): `string`

Defined in: src/save/base/BasePrinter.ts:57

#### Parameters

##### modifiers

`number`

#### Returns

`string`

#### Inherited from

`SourceBase.modifiersToString`

***

### printComments()

> `protected` **printComments**(`commentsMetadata`): `void`

Defined in: src/save/base/BasePrinter.ts:50

#### Parameters

##### commentsMetadata

`CommentsMetadata`

#### Returns

`void`

#### Inherited from

`SourceBase.printComments`

***

### printDecorator()

> `protected` **printDecorator**(`docorator`): `void`

Defined in: src/save/base/BasePrinter.ts:44

#### Parameters

##### docorator

[`Decorator`](Decorator.md)[]

#### Returns

`void`

#### Inherited from

`SourceBase.printDecorator`

***

### resolveKeywordType()

> `protected` **resolveKeywordType**(`keywordStr`): `string`

Defined in: src/save/source/SourceBase.ts:63

#### Parameters

##### keywordStr

`string`

#### Returns

`string`

#### Inherited from

`SourceBase.resolveKeywordType`

***

### resolveMethodName()

> `protected` **resolveMethodName**(`name`): `string`

Defined in: src/save/base/BasePrinter.ts:62

#### Parameters

##### name

`string`

#### Returns

`string`

#### Inherited from

`SourceBase.resolveMethodName`

***

### transTemp2Code()

> **transTemp2Code**(`temp`): `string`

Defined in: src/save/source/SourceBase.ts:55

#### Parameters

##### temp

[`Local`](Local.md)

#### Returns

`string`

#### Inherited from

`SourceBase.transTemp2Code`

***

### getPrinterOptions()

> `static` **getPrinterOptions**(): `PrinterOptions`

Defined in: src/save/base/BasePrinter.ts:85

#### Returns

`PrinterOptions`

#### Inherited from

`SourceBase.getPrinterOptions`




============================================================
## FILE: `classes/StaticSingleAssignmentFormer.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / StaticSingleAssignmentFormer

# Class: StaticSingleAssignmentFormer

Defined in: src/transformer/StaticSingleAssignmentFormer.ts:25

## Constructors

### Constructor

> **new StaticSingleAssignmentFormer**(): `StaticSingleAssignmentFormer`

#### Returns

`StaticSingleAssignmentFormer`

## Methods

### transformBody()

> **transformBody**(`body`): `void`

Defined in: src/transformer/StaticSingleAssignmentFormer.ts:26

#### Parameters

##### body

[`ArkBody`](ArkBody.md)

#### Returns

`void`




============================================================
## FILE: `classes/Stmt.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Stmt

# Class: `abstract` Stmt

Defined in: src/core/base/Stmt.ts:32

## Extended by

- [`ArkAssignStmt`](ArkAssignStmt.md)
- [`ArkInvokeStmt`](ArkInvokeStmt.md)
- [`ArkIfStmt`](ArkIfStmt.md)
- [`ArkReturnStmt`](ArkReturnStmt.md)
- [`ArkReturnVoidStmt`](ArkReturnVoidStmt.md)
- [`ArkThrowStmt`](ArkThrowStmt.md)
- [`ArkAliasTypeDefineStmt`](ArkAliasTypeDefineStmt.md)

## Constructors

### Constructor

> **new Stmt**(): `Stmt`

#### Returns

`Stmt`

## Properties

### cfg

> `protected` **cfg**: [`Cfg`](Cfg.md)

Defined in: src/core/base/Stmt.ts:36

***

### metadata?

> `optional` **metadata**: `ArkMetadata`

Defined in: src/core/base/Stmt.ts:39

***

### operandOriginalPositions?

> `protected` `optional` **operandOriginalPositions**: [`FullPosition`](FullPosition.md)[]

Defined in: src/core/base/Stmt.ts:37

***

### originalPosition

> `protected` **originalPosition**: [`LineColPosition`](LineColPosition.md) = `LineColPosition.DEFAULT`

Defined in: src/core/base/Stmt.ts:35

***

### originalText?

> `protected` `optional` **originalText**: `string`

Defined in: src/core/base/Stmt.ts:34

***

### text?

> `protected` `optional` **text**: `string`

Defined in: src/core/base/Stmt.ts:33

## Methods

### containsArrayRef()

> **containsArrayRef**(): `boolean`

Defined in: src/core/base/Stmt.ts:199

#### Returns

`boolean`

***

### containsFieldRef()

> **containsFieldRef**(): `boolean`

Defined in: src/core/base/Stmt.ts:225

#### Returns

`boolean`

***

### containsInvokeExpr()

> **containsInvokeExpr**(): `boolean`

Defined in: src/core/base/Stmt.ts:137

#### Returns

`boolean`

***

### getArrayRef()

> **getArrayRef**(): `undefined` \| [`ArkArrayRef`](ArkArrayRef.md)

Defined in: src/core/base/Stmt.ts:211

#### Returns

`undefined` \| [`ArkArrayRef`](ArkArrayRef.md)

***

### getCfg()

> **getCfg**(): [`Cfg`](Cfg.md)

Defined in: src/core/base/Stmt.ts:116

Get the CFG (i.e., control flow graph) of an [ArkBody](ArkBody.md) in which the statement is.
A CFG contains a set of basic blocks and statements corresponding to each basic block.
Note that, "source code" and "three-address" are two types of Stmt in ArkAnalyzer.
Source code Stmt represents the statement of ets/ts source code, while three-address code Stmt
represents the statement after it has been converted into three-address code.  Since the source code Stmt does not save its CFG reference, it returns **null**, while the `getCfg()` of the third address code
Stmt will return its CFG reference.

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

***

### getDefAndUses()

> **getDefAndUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Stmt.ts:87

#### Returns

[`Value`](../interfaces/Value.md)[]

***

### getExpectedSuccessorCount()

> **getExpectedSuccessorCount**(): `number`

Defined in: src/core/base/Stmt.ts:133

Return the number of statements which this statement may go to

#### Returns

`number`

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

***

### getFieldRef()

> **getFieldRef**(): `undefined` \| [`AbstractFieldRef`](AbstractFieldRef.md)

Defined in: src/core/base/Stmt.ts:238

#### Returns

`undefined` \| [`AbstractFieldRef`](AbstractFieldRef.md)

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

***

### getMetadata()

> **getMetadata**(`kind`): `undefined` \| `ArkMetadataType`

Defined in: src/core/base/Stmt.ts:41

#### Parameters

##### kind

`ArkMetadataKind`

#### Returns

`undefined` \| `ArkMetadataType`

***

### getOperandOriginalPosition()

> **getOperandOriginalPosition**(`indexOrOperand`): `null` \| [`FullPosition`](FullPosition.md)

Defined in: src/core/base/Stmt.ts:299

#### Parameters

##### indexOrOperand

`number` | [`Value`](../interfaces/Value.md)

#### Returns

`null` \| [`FullPosition`](FullPosition.md)

***

### getOperandOriginalPositions()

> **getOperandOriginalPositions**(): `undefined` \| [`FullPosition`](FullPosition.md)[]

Defined in: src/core/base/Stmt.ts:295

#### Returns

`undefined` \| [`FullPosition`](FullPosition.md)[]

***

### getOriginalText()

> **getOriginalText**(): `undefined` \| `string`

Defined in: src/core/base/Stmt.ts:287

#### Returns

`undefined` \| `string`

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

***

### getTypeExprs()

> **getTypeExprs**(): `AbstractTypeExpr`[]

Defined in: src/core/base/Stmt.ts:188

#### Returns

`AbstractTypeExpr`[]

***

### getUses()

> **getUses**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/base/Stmt.ts:53

Return a list of values which are uesd in this statement

#### Returns

[`Value`](../interfaces/Value.md)[]

***

### isBranch()

> **isBranch**(): `boolean`

Defined in: src/core/base/Stmt.ts:128

Return true if the following statement may not execute after this statement.
The ArkIfStmt and ArkGotoStmt will return true.

#### Returns

`boolean`

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

***

### setCfg()

> **setCfg**(`cfg`): `void`

Defined in: src/core/base/Stmt.ts:120

#### Parameters

##### cfg

[`Cfg`](Cfg.md)

#### Returns

`void`

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

***

### setOperandOriginalPositions()

> **setOperandOriginalPositions**(`operandOriginalPositions`): `void`

Defined in: src/core/base/Stmt.ts:291

#### Parameters

##### operandOriginalPositions

[`FullPosition`](FullPosition.md)[]

#### Returns

`void`

***

### setOriginalText()

> **setOriginalText**(`originalText`): `void`

Defined in: src/core/base/Stmt.ts:283

#### Parameters

##### originalText

`string`

#### Returns

`void`

***

### setOriginPositionInfo()

> **setOriginPositionInfo**(`originPositionInfo`): `void`

Defined in: src/core/base/Stmt.ts:250

#### Parameters

##### originPositionInfo

[`LineColPosition`](LineColPosition.md)

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

***

### toString()

> `abstract` **toString**(): `string`

Defined in: src/core/base/Stmt.ts:277

#### Returns

`string`




============================================================
## FILE: `classes/StmtUseReplacer.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / StmtUseReplacer

# Class: StmtUseReplacer

Defined in: src/core/common/StmtUseReplacer.ts:27

Replace old use(Value) of a Stmt inplace

## Constructors

### Constructor

> **new StmtUseReplacer**(`oldUse`, `newUse`): `StmtUseReplacer`

Defined in: src/core/common/StmtUseReplacer.ts:31

#### Parameters

##### oldUse

[`Value`](../interfaces/Value.md)

##### newUse

[`Value`](../interfaces/Value.md)

#### Returns

`StmtUseReplacer`

## Methods

### caseStmt()

> **caseStmt**(`stmt`): `void`

Defined in: src/core/common/StmtUseReplacer.ts:36

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`void`




============================================================
## FILE: `classes/StringType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / StringType

# Class: StringType

Defined in: src/core/base/Type.ts:177

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

> `static` **getInstance**(): `StringType`

Defined in: src/core/base/Type.ts:184

#### Returns

`StringType`




============================================================
## FILE: `classes/ThisPagEdge.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ThisPagEdge

# Class: ThisPagEdge

Defined in: src/callgraph/pointerAnalysis/Pag.ts:122

## Extends

- [`PagEdge`](PagEdge.md)

## Constructors

### Constructor

> **new ThisPagEdge**(`n`, `d`, `s`): `ThisPagEdge`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:123

#### Parameters

##### n

[`PagNode`](PagNode.md)

##### d

[`PagNode`](PagNode.md)

##### s

[`Stmt`](Stmt.md)

#### Returns

`ThisPagEdge`

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
## FILE: `classes/TupleType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / TupleType

# Class: TupleType

Defined in: src/core/base/Type.ts:527

Tuple type

## Example

```typescript
// types are number and string, dimension is 1, readonlyFlag is true
let a: readonly number[] = [1, 2, 3];

// baseType is number, dimension is 1, readonlyFlag is undefined
let a: number[] = [1, 2, 3];
```

## Extends

- [`Type`](Type.md)

## Constructors

### Constructor

> **new TupleType**(`types`): `TupleType`

Defined in: src/core/base/Type.ts:531

#### Parameters

##### types

[`Type`](Type.md)[]

#### Returns

`TupleType`

#### Overrides

[`Type`](Type.md).[`constructor`](Type.md#constructor)

## Methods

### getReadonlyFlag()

> **getReadonlyFlag**(): `undefined` \| `boolean`

Defined in: src/core/base/Type.ts:544

#### Returns

`undefined` \| `boolean`

***

### getTypes()

> **getTypes**(): [`Type`](Type.md)[]

Defined in: src/core/base/Type.ts:536

#### Returns

[`Type`](Type.md)[]

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:548

#### Returns

`string`

#### Overrides

[`Type`](Type.md).[`getTypeString`](Type.md#gettypestring)

***

### setReadonlyFlag()

> **setReadonlyFlag**(`readonlyFlag`): `void`

Defined in: src/core/base/Type.ts:540

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
## FILE: `classes/Type.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Type

# Class: `abstract` Type

Defined in: src/core/base/Type.ts:37

## Extended by

- [`AnyType`](AnyType.md)
- [`UnknownType`](UnknownType.md)
- [`UnclearReferenceType`](UnclearReferenceType.md)
- [`PrimitiveType`](PrimitiveType.md)
- [`UnionType`](UnionType.md)
- [`IntersectionType`](IntersectionType.md)
- [`VoidType`](VoidType.md)
- [`NeverType`](NeverType.md)
- [`FunctionType`](FunctionType.md)
- [`ClassType`](ClassType.md)
- [`ArrayType`](ArrayType.md)
- [`TupleType`](TupleType.md)
- [`AliasType`](AliasType.md)
- [`GenericType`](GenericType.md)
- [`AnnotationType`](AnnotationType.md)
- [`LexicalEnvType`](LexicalEnvType.md)
- [`EnumValueType`](EnumValueType.md)

## Constructors

### Constructor

> **new Type**(): `Type`

#### Returns

`Type`

## Methods

### getTypeString()

> `abstract` **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:42

#### Returns

`string`

***

### toString()

> **toString**(): `string`

Defined in: src/core/base/Type.ts:38

#### Returns

`string`




============================================================
## FILE: `classes/TypeInference.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / TypeInference

# Class: TypeInference

Defined in: src/core/common/TypeInference.ts:90

## Constructors

### Constructor

> **new TypeInference**(): `TypeInference`

#### Returns

`TypeInference`

## Methods

### buildTypeFromStr()

> `static` **buildTypeFromStr**(`typeStr`): [`Type`](Type.md)

Defined in: src/core/common/TypeInference.ts:469

#### Parameters

##### typeStr

`string`

#### Returns

[`Type`](Type.md)

***

### inferBaseType()

> `static` **inferBaseType**(`baseName`, `arkClass`): `null` \| [`Type`](Type.md)

Defined in: src/core/common/TypeInference.ts:745

Find out the original object and type for a given base name.
It returns original type.
The original type is null if failed to infer the type.

#### Parameters

##### baseName

`string`

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`Type`](Type.md)

***

### inferDynamicImportType()

> `static` **inferDynamicImportType**(`from`, `arkClass`): `null` \| [`Type`](Type.md)

Defined in: src/core/common/TypeInference.ts:797

#### Parameters

##### from

`string`

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`Type`](Type.md)

***

### inferFieldType()

> `static` **inferFieldType**(`baseType`, `fieldName`, `declareClass`): `null` \| \[`any`, [`Type`](Type.md)\]

Defined in: src/core/common/TypeInference.ts:673

Find out the original object and type for a given base type and the field name.
It returns an array with 2 items, original object and original type.
The original object is null if there is no object, or it failed to find the object.
The original type is null if it failed to infer the type.

#### Parameters

##### baseType

[`Type`](Type.md)

##### fieldName

`string`

##### declareClass

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| \[`any`, [`Type`](Type.md)\]

***

### inferFunctionType()

> `static` **inferFunctionType**(`argType`, `paramSubSignature`, `realTypes`): `void`

Defined in: src/core/common/TypeInference.ts:864

#### Parameters

##### argType

[`FunctionType`](FunctionType.md)

##### paramSubSignature

`undefined` | [`MethodSubSignature`](MethodSubSignature.md)

##### realTypes

`undefined` | [`Type`](Type.md)[]

#### Returns

`void`

***

### inferGenericType()

> `static` **inferGenericType**(`types`, `arkClass`): `void`

Defined in: src/core/common/TypeInference.ts:582

#### Parameters

##### types

`undefined` | [`GenericType`](GenericType.md)[]

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`void`

***

### inferParameterType()

> `static` **inferParameterType**(`param`, `arkMethod`): `void`

Defined in: src/core/common/TypeInference.ts:508

#### Parameters

##### param

`MethodParameter`

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

`void`

***

### inferRealGenericTypes()

> `static` **inferRealGenericTypes**(`realTypes`, `arkClass`): `void`

Defined in: src/core/common/TypeInference.ts:782

#### Parameters

##### realTypes

`undefined` | [`Type`](Type.md)[]

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`void`

***

### inferSignatureReturnType()

> `static` **inferSignatureReturnType**(`oldSignature`, `arkMethod`): `void`

Defined in: src/core/common/TypeInference.ts:524

#### Parameters

##### oldSignature

[`MethodSignature`](MethodSignature.md)

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

`void`

***

### inferSimpleTypeInMethod()

> `static` **inferSimpleTypeInMethod**(`arkMethod`): `void`

Defined in: src/core/common/TypeInference.ts:229

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

`void`

#### Deprecated

***

### inferSimpleTypeInStmt()

> `static` **inferSimpleTypeInStmt**(`stmt`): `void`

Defined in: src/core/common/TypeInference.ts:455

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`void`

***

### inferTypeByName()

> `static` **inferTypeByName**(`typeName`, `arkClass`): `null` \| [`Type`](Type.md)

Defined in: src/core/common/TypeInference.ts:767

#### Parameters

##### typeName

`string`

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`Type`](Type.md)

***

### inferTypeInArkField()

> `static` **inferTypeInArkField**(`arkField`): `void`

Defined in: src/core/common/TypeInference.ts:91

#### Parameters

##### arkField

[`ArkField`](ArkField.md)

#### Returns

`void`

***

### inferTypeInMethod()

> `static` **inferTypeInMethod**(`arkMethod`): `void`

Defined in: src/core/common/TypeInference.ts:174

#### Parameters

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

`void`

***

### inferUnclearedType()

> `static` **inferUnclearedType**(`leftOpType`, `declaringArkClass`, `visited`): `undefined` \| `null` \| [`Type`](Type.md)

Defined in: src/core/common/TypeInference.ts:136

Infer type for a given unclear type.
It returns an array with 2 items, original object and original type.
The original object is null if there is no object, or it failed to find the object.
The original type is null if failed to infer the type.

#### Parameters

##### leftOpType

[`Type`](Type.md)

##### declaringArkClass

[`ArkClass`](ArkClass.md)

##### visited

`Set`\<[`Type`](Type.md)\> = `...`

#### Returns

`undefined` \| `null` \| [`Type`](Type.md)

***

### inferUnclearRefName()

> `static` **inferUnclearRefName**(`refName`, `arkClass`): `null` \| [`Type`](Type.md)

Defined in: src/core/common/TypeInference.ts:627

Find out the original object and type for a given unclear reference type name.
It returns original type.
The original type is null if it failed to infer the type.

#### Parameters

##### refName

`string`

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`Type`](Type.md)

***

### inferUnclearRefType()

> `static` **inferUnclearRefType**(`urType`, `arkClass`): `null` \| [`Type`](Type.md)

Defined in: src/core/common/TypeInference.ts:609

Infer type for a given [UnclearReferenceType](UnclearReferenceType.md) type.
It returns original type.
The original type is null if it failed to infer the type.

#### Parameters

##### urType

[`UnclearReferenceType`](UnclearReferenceType.md)

##### arkClass

[`ArkClass`](ArkClass.md)

#### Returns

`null` \| [`Type`](Type.md)

***

### inferValueType()

> `static` **inferValueType**(`value`, `arkMethod`): `null` \| [`Type`](Type.md)

Defined in: src/core/common/TypeInference.ts:498

#### Parameters

##### value

[`Value`](../interfaces/Value.md)

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

`null` \| [`Type`](Type.md)

***

### isUnclearType()

> `static` **isUnclearType**(`type`): `boolean`

Defined in: src/core/common/TypeInference.ts:404

#### Parameters

##### type

`undefined` | `null` | [`Type`](Type.md)

#### Returns

`boolean`

***

### parseArkExport2Type()

> `static` **parseArkExport2Type**(`arkExport`): `null` \| [`Type`](Type.md)

Defined in: src/core/common/TypeInference.ts:312

#### Parameters

##### arkExport

`undefined` | `null` | `ArkExport`

#### Returns

`null` \| [`Type`](Type.md)

***

### replaceAliasType()

> `static` **replaceAliasType**(`type`): [`Type`](Type.md)

Defined in: src/core/common/TypeInference.ts:856

#### Parameters

##### type

[`Type`](Type.md)

#### Returns

[`Type`](Type.md)

***

### replaceRecursiveType()

> `static` **replaceRecursiveType**(`type`, `visited`, `realTypes?`): [`Type`](Type.md)

Defined in: src/core/common/TypeInference.ts:822

#### Parameters

##### type

[`Type`](Type.md)

##### visited

`Set`\<[`Type`](Type.md)\>

##### realTypes?

[`Type`](Type.md)[]

#### Returns

[`Type`](Type.md)

***

### replaceTypeWithReal()

> `static` **replaceTypeWithReal**(`type`, `realTypes?`, `visited?`): [`Type`](Type.md)

Defined in: src/core/common/TypeInference.ts:806

#### Parameters

##### type

[`Type`](Type.md)

##### realTypes?

[`Type`](Type.md)[]

##### visited?

`Set`\<[`Type`](Type.md)\> = `...`

#### Returns

[`Type`](Type.md)

***

### resolveArkAssignStmt()

> `static` **resolveArkAssignStmt**(`stmt`, `arkMethod`): `void`

Defined in: src/core/common/TypeInference.ts:339

infer and pass type for ArkAssignStmt right and left

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

##### arkMethod

[`ArkMethod`](ArkMethod.md)

#### Returns

`void`




============================================================
## FILE: `classes/UnclearReferenceType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UnclearReferenceType

# Class: UnclearReferenceType

Defined in: src/core/base/Type.ts:89

unclear type

## Extends

- [`Type`](Type.md)

## Constructors

### Constructor

> **new UnclearReferenceType**(`name`, `genericTypes`): `UnclearReferenceType`

Defined in: src/core/base/Type.ts:93

#### Parameters

##### name

`string`

##### genericTypes

[`Type`](Type.md)[] = `[]`

#### Returns

`UnclearReferenceType`

#### Overrides

[`Type`](Type.md).[`constructor`](Type.md#constructor)

## Methods

### getGenericTypes()

> **getGenericTypes**(): [`Type`](Type.md)[]

Defined in: src/core/base/Type.ts:103

#### Returns

[`Type`](Type.md)[]

***

### getName()

> **getName**(): `string`

Defined in: src/core/base/Type.ts:99

#### Returns

`string`

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:107

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
## FILE: `classes/UndefinedType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UndefinedType

# Class: UndefinedType

Defined in: src/core/base/Type.ts:209

undefined type

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

> `static` **getInstance**(): `UndefinedType`

Defined in: src/core/base/Type.ts:212

#### Returns

`UndefinedType`




============================================================
## FILE: `classes/UndefinedVariableChecker.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UndefinedVariableChecker

# Class: UndefinedVariableChecker

Defined in: src/core/dataflow/UndefinedVariable.ts:36

## Extends

- [`DataflowProblem`](DataflowProblem.md)\<[`Value`](../interfaces/Value.md)\>

## Constructors

### Constructor

> **new UndefinedVariableChecker**(`stmt`, `method`): `UndefinedVariableChecker`

Defined in: src/core/dataflow/UndefinedVariable.ts:44

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

##### method

[`ArkMethod`](ArkMethod.md)

#### Returns

`UndefinedVariableChecker`

#### Overrides

[`DataflowProblem`](DataflowProblem.md).[`constructor`](DataflowProblem.md#constructor)

## Properties

### classMap

> **classMap**: `Map`\<[`NamespaceSignature`](NamespaceSignature.md) \| [`FileSignature`](FileSignature.md), [`ArkClass`](ArkClass.md)[]\>

Defined in: src/core/dataflow/UndefinedVariable.ts:41

***

### entryMethod

> **entryMethod**: [`ArkMethod`](ArkMethod.md)

Defined in: src/core/dataflow/UndefinedVariable.ts:39

***

### entryPoint

> **entryPoint**: [`Stmt`](Stmt.md)

Defined in: src/core/dataflow/UndefinedVariable.ts:38

***

### globalVariableMap

> **globalVariableMap**: `Map`\<[`NamespaceSignature`](NamespaceSignature.md) \| [`FileSignature`](FileSignature.md), [`Local`](Local.md)[]\>

Defined in: src/core/dataflow/UndefinedVariable.ts:42

***

### outcomes

> **outcomes**: `Outcome`[] = `[]`

Defined in: src/core/dataflow/UndefinedVariable.ts:43

***

### scene

> **scene**: [`Scene`](Scene.md)

Defined in: src/core/dataflow/UndefinedVariable.ts:40

***

### zeroValue

> **zeroValue**: [`Constant`](Constant.md)

Defined in: src/core/dataflow/UndefinedVariable.ts:37

## Methods

### addParameters()

> **addParameters**(`srcStmt`, `dataFact`, `method`, `ret`): `void`

Defined in: src/core/dataflow/UndefinedVariable.ts:185

#### Parameters

##### srcStmt

[`Stmt`](Stmt.md)

##### dataFact

[`Value`](../interfaces/Value.md)

##### method

[`ArkMethod`](ArkMethod.md)

##### ret

`Set`\<[`Value`](../interfaces/Value.md)\>

#### Returns

`void`

***

### addUndefinedField()

> **addUndefinedField**(`field`, `method`, `ret`): `void`

Defined in: src/core/dataflow/UndefinedVariable.ts:170

#### Parameters

##### field

[`ArkField`](ArkField.md)

##### method

[`ArkMethod`](ArkMethod.md)

##### ret

`Set`\<[`Value`](../interfaces/Value.md)\>

#### Returns

`void`

***

### createZeroValue()

> **createZeroValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/core/dataflow/UndefinedVariable.ts:234

#### Returns

[`Value`](../interfaces/Value.md)

#### Overrides

[`DataflowProblem`](DataflowProblem.md).[`createZeroValue`](DataflowProblem.md#createzerovalue)

***

### factEqual()

> **factEqual**(`d1`, `d2`): `boolean`

Defined in: src/core/dataflow/UndefinedVariable.ts:242

#### Parameters

##### d1

[`Value`](../interfaces/Value.md)

##### d2

[`Value`](../interfaces/Value.md)

#### Returns

`boolean`

#### Overrides

[`DataflowProblem`](DataflowProblem.md).[`factEqual`](DataflowProblem.md#factequal)

***

### getCallFlowFunction()

> **getCallFlowFunction**(`srcStmt`, `method`): [`FlowFunction`](../interfaces/FlowFunction.md)\<[`Value`](../interfaces/Value.md)\>

Defined in: src/core/dataflow/UndefinedVariable.ts:117

#### Parameters

##### srcStmt

[`Stmt`](Stmt.md)

##### method

[`ArkMethod`](ArkMethod.md)

#### Returns

[`FlowFunction`](../interfaces/FlowFunction.md)\<[`Value`](../interfaces/Value.md)\>

#### Overrides

[`DataflowProblem`](DataflowProblem.md).[`getCallFlowFunction`](DataflowProblem.md#getcallflowfunction)

***

### getCallToReturnFlowFunction()

> **getCallToReturnFlowFunction**(`srcStmt`, `tgtStmt`): [`FlowFunction`](../interfaces/FlowFunction.md)\<[`Value`](../interfaces/Value.md)\>

Defined in: src/core/dataflow/UndefinedVariable.ts:217

#### Parameters

##### srcStmt

[`Stmt`](Stmt.md)

##### tgtStmt

[`Stmt`](Stmt.md)

#### Returns

[`FlowFunction`](../interfaces/FlowFunction.md)\<[`Value`](../interfaces/Value.md)\>

#### Overrides

[`DataflowProblem`](DataflowProblem.md).[`getCallToReturnFlowFunction`](DataflowProblem.md#getcalltoreturnflowfunction)

***

### getEntryMethod()

> **getEntryMethod**(): [`ArkMethod`](ArkMethod.md)

Defined in: src/core/dataflow/UndefinedVariable.ts:57

#### Returns

[`ArkMethod`](ArkMethod.md)

#### Overrides

[`DataflowProblem`](DataflowProblem.md).[`getEntryMethod`](DataflowProblem.md#getentrymethod)

***

### getEntryPoint()

> **getEntryPoint**(): [`Stmt`](Stmt.md)

Defined in: src/core/dataflow/UndefinedVariable.ts:53

#### Returns

[`Stmt`](Stmt.md)

#### Overrides

[`DataflowProblem`](DataflowProblem.md).[`getEntryPoint`](DataflowProblem.md#getentrypoint)

***

### getExitToReturnFlowFunction()

> **getExitToReturnFlowFunction**(`srcStmt`, `tgtStmt`, `callStmt`): [`FlowFunction`](../interfaces/FlowFunction.md)\<[`Value`](../interfaces/Value.md)\>

Defined in: src/core/dataflow/UndefinedVariable.ts:204

#### Parameters

##### srcStmt

[`Stmt`](Stmt.md)

##### tgtStmt

[`Stmt`](Stmt.md)

##### callStmt

[`Stmt`](Stmt.md)

#### Returns

[`FlowFunction`](../interfaces/FlowFunction.md)\<[`Value`](../interfaces/Value.md)\>

#### Overrides

[`DataflowProblem`](DataflowProblem.md).[`getExitToReturnFlowFunction`](DataflowProblem.md#getexittoreturnflowfunction)

***

### getNormalFlowFunction()

> **getNormalFlowFunction**(`srcStmt`, `tgtStmt`): [`FlowFunction`](../interfaces/FlowFunction.md)\<[`Value`](../interfaces/Value.md)\>

Defined in: src/core/dataflow/UndefinedVariable.ts:71

Transfer the outFact of srcStmt to the inFact of tgtStmt

Return true if keeping progagation (i.e., tgtStmt will be added to the WorkList for further analysis)

#### Parameters

##### srcStmt

[`Stmt`](Stmt.md)

##### tgtStmt

[`Stmt`](Stmt.md)

#### Returns

[`FlowFunction`](../interfaces/FlowFunction.md)\<[`Value`](../interfaces/Value.md)\>

#### Overrides

[`DataflowProblem`](DataflowProblem.md).[`getNormalFlowFunction`](DataflowProblem.md#getnormalflowfunction)

***

### getOutcomes()

> **getOutcomes**(): `Outcome`[]

Defined in: src/core/dataflow/UndefinedVariable.ts:253

#### Returns

`Outcome`[]

***

### getZeroValue()

> **getZeroValue**(): [`Value`](../interfaces/Value.md)

Defined in: src/core/dataflow/UndefinedVariable.ts:238

#### Returns

[`Value`](../interfaces/Value.md)

***

### insideCallFlowFunction()

> **insideCallFlowFunction**(`ret`, `method`): `void`

Defined in: src/core/dataflow/UndefinedVariable.ts:151

#### Parameters

##### ret

`Set`\<[`Value`](../interfaces/Value.md)\>

##### method

[`ArkMethod`](ArkMethod.md)

#### Returns

`void`

***

### insideNormalFlowFunction()

> **insideNormalFlowFunction**(`ret`, `srcStmt`, `dataFact`): `void`

Defined in: src/core/dataflow/UndefinedVariable.ts:88

#### Parameters

##### ret

`Set`\<[`Value`](../interfaces/Value.md)\>

##### srcStmt

[`ArkAssignStmt`](ArkAssignStmt.md)

##### dataFact

[`Value`](../interfaces/Value.md)

#### Returns

`void`




============================================================
## FILE: `classes/UndefinedVariableSolver.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UndefinedVariableSolver

# Class: UndefinedVariableSolver

Defined in: src/core/dataflow/UndefinedVariable.ts:258

## Extends

- [`DataflowSolver`](DataflowSolver.md)\<[`Value`](../interfaces/Value.md)\>

## Constructors

### Constructor

> **new UndefinedVariableSolver**(`problem`, `scene`): `UndefinedVariableSolver`

Defined in: src/core/dataflow/UndefinedVariable.ts:259

#### Parameters

##### problem

[`UndefinedVariableChecker`](UndefinedVariableChecker.md)

##### scene

[`Scene`](Scene.md)

#### Returns

`UndefinedVariableSolver`

#### Overrides

[`DataflowSolver`](DataflowSolver.md).[`constructor`](DataflowSolver.md#constructor)

## Properties

### CHA

> `protected` **CHA**: [`ClassHierarchyAnalysis`](ClassHierarchyAnalysis.md)

Defined in: src/core/dataflow/DataflowSolver.ts:49

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`CHA`](DataflowSolver.md#cha)

***

### endSummary

> `protected` **endSummary**: `Map`\<[`PathEdgePoint`](PathEdgePoint.md)\<[`Value`](../interfaces/Value.md)\>, `Set`\<[`PathEdgePoint`](PathEdgePoint.md)\<[`Value`](../interfaces/Value.md)\>\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:46

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`endSummary`](DataflowSolver.md#endsummary)

***

### inComing

> `protected` **inComing**: `Map`\<[`PathEdgePoint`](PathEdgePoint.md)\<[`Value`](../interfaces/Value.md)\>, `Set`\<[`PathEdgePoint`](PathEdgePoint.md)\<[`Value`](../interfaces/Value.md)\>\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:45

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`inComing`](DataflowSolver.md#incoming)

***

### laterEdges

> `protected` **laterEdges**: `Set`\<[`PathEdge`](PathEdge.md)\<[`Value`](../interfaces/Value.md)\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:51

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`laterEdges`](DataflowSolver.md#lateredges)

***

### pathEdgeSet

> `protected` **pathEdgeSet**: `Set`\<[`PathEdge`](PathEdge.md)\<[`Value`](../interfaces/Value.md)\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:43

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`pathEdgeSet`](DataflowSolver.md#pathedgeset)

***

### problem

> `protected` **problem**: [`DataflowProblem`](DataflowProblem.md)\<[`Value`](../interfaces/Value.md)\>

Defined in: src/core/dataflow/DataflowSolver.ts:41

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`problem`](DataflowSolver.md#problem)

***

### scene

> `protected` **scene**: [`Scene`](Scene.md)

Defined in: src/core/dataflow/DataflowSolver.ts:48

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`scene`](DataflowSolver.md#scene)

***

### stmtNexts

> `protected` **stmtNexts**: `Map`\<[`Stmt`](Stmt.md), `Set`\<[`Stmt`](Stmt.md)\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:50

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`stmtNexts`](DataflowSolver.md#stmtnexts)

***

### summaryEdge

> `protected` **summaryEdge**: `Set`\<`CallToReturnCacheEdge`\<[`Value`](../interfaces/Value.md)\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:47

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`summaryEdge`](DataflowSolver.md#summaryedge)

***

### workList

> `protected` **workList**: [`PathEdge`](PathEdge.md)\<[`Value`](../interfaces/Value.md)\>[]

Defined in: src/core/dataflow/DataflowSolver.ts:42

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`workList`](DataflowSolver.md#worklist)

***

### zeroFact

> `protected` **zeroFact**: [`Value`](../interfaces/Value.md)

Defined in: src/core/dataflow/DataflowSolver.ts:44

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`zeroFact`](DataflowSolver.md#zerofact)

## Methods

### buildStmtMapInBlock()

> `protected` **buildStmtMapInBlock**(`block`): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:113

#### Parameters

##### block

[`BasicBlock`](BasicBlock.md)

#### Returns

`void`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`buildStmtMapInBlock`](DataflowSolver.md#buildstmtmapinblock)

***

### buildStmtMapInClass()

> `protected` **buildStmtMapInClass**(): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:98

#### Returns

`void`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`buildStmtMapInClass`](DataflowSolver.md#buildstmtmapinclass)

***

### callNodeFactPropagate()

> `protected` **callNodeFactPropagate**(`edge`, `firstStmt`, `fact`, `returnSite`): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:288

#### Parameters

##### edge

[`PathEdge`](PathEdge.md)\<[`Value`](../interfaces/Value.md)\>

##### firstStmt

[`Stmt`](Stmt.md)

##### fact

[`Value`](../interfaces/Value.md)

##### returnSite

[`Stmt`](Stmt.md)

#### Returns

`void`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`callNodeFactPropagate`](DataflowSolver.md#callnodefactpropagate)

***

### computeResult()

> `protected` **computeResult**(`stmt`, `d`): `boolean`

Defined in: src/core/dataflow/DataflowSolver.ts:71

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

##### d

[`Value`](../interfaces/Value.md)

#### Returns

`boolean`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`computeResult`](DataflowSolver.md#computeresult)

***

### doSolve()

> `protected` **doSolve**(): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:320

#### Returns

`void`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`doSolve`](DataflowSolver.md#dosolve)

***

### getAllCalleeMethods()

> `protected` **getAllCalleeMethods**(`callNode`): `Set`\<[`ArkMethod`](ArkMethod.md)\>

Defined in: src/core/dataflow/DataflowSolver.ts:137

#### Parameters

##### callNode

[`ArkInvokeStmt`](ArkInvokeStmt.md)

#### Returns

`Set`\<[`ArkMethod`](ArkMethod.md)\>

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`getAllCalleeMethods`](DataflowSolver.md#getallcalleemethods)

***

### getChildren()

> `protected` **getChildren**(`stmt`): [`Stmt`](Stmt.md)[]

Defined in: src/core/dataflow/DataflowSolver.ts:80

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

[`Stmt`](Stmt.md)[]

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`getChildren`](DataflowSolver.md#getchildren)

***

### getPathEdgeSet()

> **getPathEdgeSet**(): `Set`\<[`PathEdge`](PathEdge.md)\<[`Value`](../interfaces/Value.md)\>\>

Defined in: src/core/dataflow/DataflowSolver.ts:355

#### Returns

`Set`\<[`PathEdge`](PathEdge.md)\<[`Value`](../interfaces/Value.md)\>\>

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`getPathEdgeSet`](DataflowSolver.md#getpathedgeset)

***

### getReturnSiteOfCall()

> `protected` **getReturnSiteOfCall**(`call`): [`Stmt`](Stmt.md)

Defined in: src/core/dataflow/DataflowSolver.ts:152

#### Parameters

##### call

[`Stmt`](Stmt.md)

#### Returns

[`Stmt`](Stmt.md)

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`getReturnSiteOfCall`](DataflowSolver.md#getreturnsiteofcall)

***

### getStartOfCallerMethod()

> `protected` **getStartOfCallerMethod**(`call`): [`Stmt`](Stmt.md)

Defined in: src/core/dataflow/DataflowSolver.ts:156

#### Parameters

##### call

[`Stmt`](Stmt.md)

#### Returns

[`Stmt`](Stmt.md)

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`getStartOfCallerMethod`](DataflowSolver.md#getstartofcallermethod)

***

### init()

> `protected` **init**(): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:84

#### Returns

`void`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`init`](DataflowSolver.md#init)

***

### isCallStatement()

> `protected` **isCallStatement**(`stmt`): `boolean`

Defined in: src/core/dataflow/DataflowSolver.ts:337

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`boolean`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`isCallStatement`](DataflowSolver.md#iscallstatement)

***

### isExitStatement()

> `protected` **isExitStatement**(`stmt`): `boolean`

Defined in: src/core/dataflow/DataflowSolver.ts:351

#### Parameters

##### stmt

[`Stmt`](Stmt.md)

#### Returns

`boolean`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`isExitStatement`](DataflowSolver.md#isexitstatement)

***

### pathEdgeSetHasEdge()

> `protected` **pathEdgeSetHasEdge**(`edge`): `boolean`

Defined in: src/core/dataflow/DataflowSolver.ts:162

#### Parameters

##### edge

[`PathEdge`](PathEdge.md)\<[`Value`](../interfaces/Value.md)\>

#### Returns

`boolean`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`pathEdgeSetHasEdge`](DataflowSolver.md#pathedgesethasedge)

***

### processCallNode()

> `protected` **processCallNode**(`edge`): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:254

#### Parameters

##### edge

[`PathEdge`](PathEdge.md)\<[`Value`](../interfaces/Value.md)\>

#### Returns

`void`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`processCallNode`](DataflowSolver.md#processcallnode)

***

### processExitNode()

> `protected` **processExitNode**(`edge`): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:191

#### Parameters

##### edge

[`PathEdge`](PathEdge.md)\<[`Value`](../interfaces/Value.md)\>

#### Returns

`void`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`processExitNode`](DataflowSolver.md#processexitnode)

***

### processNormalNode()

> `protected` **processNormalNode**(`edge`): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:238

#### Parameters

##### edge

[`PathEdge`](PathEdge.md)\<[`Value`](../interfaces/Value.md)\>

#### Returns

`void`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`processNormalNode`](DataflowSolver.md#processnormalnode)

***

### propagate()

> `protected` **propagate**(`edge`): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:177

#### Parameters

##### edge

[`PathEdge`](PathEdge.md)\<[`Value`](../interfaces/Value.md)\>

#### Returns

`void`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`propagate`](DataflowSolver.md#propagate)

***

### setCfg4AllStmt()

> `protected` **setCfg4AllStmt**(): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:129

#### Returns

`void`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`setCfg4AllStmt`](DataflowSolver.md#setcfg4allstmt)

***

### solve()

> **solve**(): `void`

Defined in: src/core/dataflow/DataflowSolver.ts:66

#### Returns

`void`

#### Inherited from

[`DataflowSolver`](DataflowSolver.md).[`solve`](DataflowSolver.md#solve)




============================================================
## FILE: `classes/UnionType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UnionType

# Class: UnionType

Defined in: src/core/base/Type.ts:249

union type

## Extends

- [`Type`](Type.md)

## Constructors

### Constructor

> **new UnionType**(`types`, `currType`): `UnionType`

Defined in: src/core/base/Type.ts:252

#### Parameters

##### types

[`Type`](Type.md)[]

##### currType

[`Type`](Type.md) = `...`

#### Returns

`UnionType`

#### Overrides

[`Type`](Type.md).[`constructor`](Type.md#constructor)

## Methods

### flatType()

> **flatType**(): [`Type`](Type.md)[]

Defined in: src/core/base/Type.ts:283

#### Returns

[`Type`](Type.md)[]

***

### getCurrType()

> **getCurrType**(): [`Type`](Type.md)

Defined in: src/core/base/Type.ts:262

#### Returns

[`Type`](Type.md)

***

### getTypes()

> **getTypes**(): [`Type`](Type.md)[]

Defined in: src/core/base/Type.ts:258

#### Returns

[`Type`](Type.md)[]

***

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:270

#### Returns

`string`

#### Overrides

[`Type`](Type.md).[`getTypeString`](Type.md#gettypestring)

***

### setCurrType()

> **setCurrType**(`newType`): `void`

Defined in: src/core/base/Type.ts:266

#### Parameters

##### newType

[`Type`](Type.md)

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
## FILE: `classes/UnknownType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UnknownType

# Class: UnknownType

Defined in: src/core/base/Type.ts:69

unknown type

## Extends

- [`Type`](Type.md)

## Methods

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:80

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

> `static` **getInstance**(): `UnknownType`

Defined in: src/core/base/Type.ts:72

#### Returns

`UnknownType`




============================================================
## FILE: `classes/ValueUtil.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ValueUtil

# Class: ValueUtil

Defined in: src/core/common/ValueUtil.ts:20

## Constructors

### Constructor

> **new ValueUtil**(): `ValueUtil`

#### Returns

`ValueUtil`

## Properties

### EMPTY\_STRING\_CONSTANT

> `readonly` `static` **EMPTY\_STRING\_CONSTANT**: `StringConstant`

Defined in: src/core/common/ValueUtil.ts:22

## Methods

### createBigIntConst()

> `static` **createBigIntConst**(`bigInt`): `BigIntConstant`

Defined in: src/core/common/ValueUtil.ts:33

#### Parameters

##### bigInt

`bigint`

#### Returns

`BigIntConstant`

***

### createConst()

> `static` **createConst**(`str`): [`Constant`](Constant.md)

Defined in: src/core/common/ValueUtil.ts:44

#### Parameters

##### str

`string`

#### Returns

[`Constant`](Constant.md)

***

### createStringConst()

> `static` **createStringConst**(`str`): [`Constant`](Constant.md)

Defined in: src/core/common/ValueUtil.ts:37

#### Parameters

##### str

`string`

#### Returns

[`Constant`](Constant.md)

***

### getBooleanConstant()

> `static` **getBooleanConstant**(`value`): [`Constant`](Constant.md)

Defined in: src/core/common/ValueUtil.ts:60

#### Parameters

##### value

`boolean`

#### Returns

[`Constant`](Constant.md)

***

### getNullConstant()

> `static` **getNullConstant**(): [`Constant`](Constant.md)

Defined in: src/core/common/ValueUtil.ts:56

#### Returns

[`Constant`](Constant.md)

***

### getOrCreateNumberConst()

> `static` **getOrCreateNumberConst**(`n`): [`Constant`](Constant.md)

Defined in: src/core/common/ValueUtil.ts:24

#### Parameters

##### n

`number`

#### Returns

[`Constant`](Constant.md)

***

### getUndefinedConst()

> `static` **getUndefinedConst**(): [`Constant`](Constant.md)

Defined in: src/core/common/ValueUtil.ts:52

#### Returns

[`Constant`](Constant.md)




============================================================
## FILE: `classes/ViewTreePrinter.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ViewTreePrinter

# Class: ViewTreePrinter

Defined in: src/save/ViewTreePrinter.ts:27

## Extends

- [`Printer`](Printer.md)

## Constructors

### Constructor

> **new ViewTreePrinter**(`viewTree`): `ViewTreePrinter`

Defined in: src/save/ViewTreePrinter.ts:31

#### Parameters

##### viewTree

[`ViewTree`](../interfaces/ViewTree.md)

#### Returns

`ViewTreePrinter`

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

Defined in: src/save/ViewTreePrinter.ts:37

ArkIR dump

#### Returns

`string`

#### Overrides

[`Printer`](Printer.md).[`dump`](Printer.md#dump)




============================================================
## FILE: `classes/VisibleValue.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / VisibleValue

# Class: VisibleValue

Defined in: src/core/common/VisibleValue.ts:30

## Constructors

### Constructor

> **new VisibleValue**(): `VisibleValue`

Defined in: src/core/common/VisibleValue.ts:35

#### Returns

`VisibleValue`

## Methods

### getCurrVisibleValues()

> **getCurrVisibleValues**(): [`Value`](../interfaces/Value.md)[]

Defined in: src/core/common/VisibleValue.ts:43

get values that is visible in curr scope

#### Returns

[`Value`](../interfaces/Value.md)[]

***

### getScopeChain()

> **getScopeChain**(): [`Scope`](Scope.md)[]

Defined in: src/core/common/VisibleValue.ts:47

#### Returns

[`Scope`](Scope.md)[]

***

### updateIntoScope()

> **updateIntoScope**(`model`): `void`

Defined in: src/core/common/VisibleValue.ts:52

udpate visible values after entered a scope, only support step by step

#### Parameters

##### model

`ArkModel`

#### Returns

`void`

***

### updateOutScope()

> **updateOutScope**(): `void`

Defined in: src/core/common/VisibleValue.ts:79

udpate visible values after left a scope, only support step by step

#### Returns

`void`




============================================================
## FILE: `classes/VoidType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / VoidType

# Class: VoidType

Defined in: src/core/base/Type.ts:329

types for function void return type

## Extends

- [`Type`](Type.md)

## Methods

### getTypeString()

> **getTypeString**(): `string`

Defined in: src/core/base/Type.ts:340

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

> `static` **getInstance**(): `VoidType`

Defined in: src/core/base/Type.ts:332

#### Returns

`VoidType`




============================================================
## FILE: `classes/WritePagEdge.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / WritePagEdge

# Class: WritePagEdge

Defined in: src/callgraph/pointerAnalysis/Pag.ts:116

## Extends

- [`PagEdge`](PagEdge.md)

## Constructors

### Constructor

> **new WritePagEdge**(`n`, `d`, `s`): `WritePagEdge`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:117

#### Parameters

##### n

[`PagNode`](PagNode.md)

##### d

[`PagNode`](PagNode.md)

##### s

[`Stmt`](Stmt.md)

#### Returns

`WritePagEdge`

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
## FILE: `enumerations/CallGraphNodeKind.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / CallGraphNodeKind

# Enumeration: CallGraphNodeKind

Defined in: src/callgraph/model/CallGraph.ts:33

## Enumeration Members

### blank

> **blank**: `4`

Defined in: src/callgraph/model/CallGraph.ts:38

***

### constructor

> **constructor**: `3`

Defined in: src/callgraph/model/CallGraph.ts:37

***

### intrinsic

> **intrinsic**: `2`

Defined in: src/callgraph/model/CallGraph.ts:36

***

### real

> **real**: `0`

Defined in: src/callgraph/model/CallGraph.ts:34

***

### vitual

> **vitual**: `1`

Defined in: src/callgraph/model/CallGraph.ts:35




============================================================
## FILE: `enumerations/LOG_LEVEL.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / LOG\_LEVEL

# Enumeration: LOG\_LEVEL

Defined in: src/utils/logger.ts:19

## Enumeration Members

### DEBUG

> **DEBUG**: `"DEBUG"`

Defined in: src/utils/logger.ts:23

***

### ERROR

> **ERROR**: `"ERROR"`

Defined in: src/utils/logger.ts:20

***

### INFO

> **INFO**: `"INFO"`

Defined in: src/utils/logger.ts:22

***

### TRACE

> **TRACE**: `"TRACE"`

Defined in: src/utils/logger.ts:24

***

### WARN

> **WARN**: `"WARN"`

Defined in: src/utils/logger.ts:21




============================================================
## FILE: `enumerations/LOG_MODULE_TYPE.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / LOG\_MODULE\_TYPE

# Enumeration: LOG\_MODULE\_TYPE

Defined in: src/utils/logger.ts:27

## Enumeration Members

### ARKANALYZER

> **ARKANALYZER**: `"ArkAnalyzer"`

Defined in: src/utils/logger.ts:29

***

### DEFAULT

> **DEFAULT**: `"default"`

Defined in: src/utils/logger.ts:28

***

### HOMECHECK

> **HOMECHECK**: `"HomeCheck"`

Defined in: src/utils/logger.ts:30

***

### TOOL

> **TOOL**: `"Tool"`

Defined in: src/utils/logger.ts:31




============================================================
## FILE: `enumerations/NormalBinaryOperator.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / NormalBinaryOperator

# Enumeration: NormalBinaryOperator

Defined in: src/core/base/Expr.ts:537

## Enumeration Members

### Addition

> **Addition**: `"+"`

Defined in: src/core/base/Expr.ts:544

***

### BitwiseAnd

> **BitwiseAnd**: `"&"`

Defined in: src/core/base/Expr.ts:555

***

### BitwiseOr

> **BitwiseOr**: "\|"

Defined in: src/core/base/Expr.ts:556

***

### BitwiseXor

> **BitwiseXor**: `"^"`

Defined in: src/core/base/Expr.ts:557

***

### Division

> **Division**: `"/"`

Defined in: src/core/base/Expr.ts:543

***

### Exponentiation

> **Exponentiation**: `"**"`

Defined in: src/core/base/Expr.ts:542

***

### LeftShift

> **LeftShift**: `"<<"`

Defined in: src/core/base/Expr.ts:550

***

### LogicalAnd

> **LogicalAnd**: `"&&"`

Defined in: src/core/base/Expr.ts:560

***

### LogicalOr

> **LogicalOr**: "\|\|"

Defined in: src/core/base/Expr.ts:561

***

### Multiplication

> **Multiplication**: `"*"`

Defined in: src/core/base/Expr.ts:546

***

### NullishCoalescing

> **NullishCoalescing**: `"??"`

Defined in: src/core/base/Expr.ts:539

***

### Remainder

> **Remainder**: `"%"`

Defined in: src/core/base/Expr.ts:547

***

### RightShift

> **RightShift**: `">>"`

Defined in: src/core/base/Expr.ts:551

***

### Subtraction

> **Subtraction**: `"-"`

Defined in: src/core/base/Expr.ts:545

***

### UnsignedRightShift

> **UnsignedRightShift**: `">>>"`

Defined in: src/core/base/Expr.ts:552




============================================================
## FILE: `enumerations/PagEdgeKind.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagEdgeKind

# Enumeration: PagEdgeKind

Defined in: src/callgraph/pointerAnalysis/Pag.ts:45

## Enumeration Members

### Address

> **Address**: `0`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:46

***

### Copy

> **Copy**: `1`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:47

***

### InterProceduralCopy

> **InterProceduralCopy**: `6`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:52

***

### Load

> **Load**: `2`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:48

***

### This

> **This**: `4`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:50

***

### Unknown

> **Unknown**: `5`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:51

***

### Write

> **Write**: `3`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:49




============================================================
## FILE: `enumerations/PagNodeKind.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagNodeKind

# Enumeration: PagNodeKind

Defined in: src/callgraph/pointerAnalysis/Pag.ts:130

## Enumeration Members

### ExportInfo

> **ExportInfo**: `7`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:138

***

### Function

> **Function**: `5`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:136

***

### GlobalThis

> **GlobalThis**: `6`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:137

***

### HeapObj

> **HeapObj**: `0`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:131

***

### LocalVar

> **LocalVar**: `1`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:132

***

### Param

> **Param**: `3`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:134

***

### RefVar

> **RefVar**: `2`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:133

***

### ThisRef

> **ThisRef**: `4`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:135




============================================================
## FILE: `enumerations/RelationalBinaryOperator.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / RelationalBinaryOperator

# Enumeration: RelationalBinaryOperator

Defined in: src/core/base/Expr.ts:564

## Enumeration Members

### Equality

> **Equality**: `"=="`

Defined in: src/core/base/Expr.ts:569

***

### GreaterThan

> **GreaterThan**: `">"`

Defined in: src/core/base/Expr.ts:567

***

### GreaterThanOrEqual

> **GreaterThanOrEqual**: `">="`

Defined in: src/core/base/Expr.ts:568

***

### InEquality

> **InEquality**: `"!="`

Defined in: src/core/base/Expr.ts:570

***

### isPropertyOf

> **isPropertyOf**: `"in"`

Defined in: src/core/base/Expr.ts:573

***

### LessThan

> **LessThan**: `"<"`

Defined in: src/core/base/Expr.ts:565

***

### LessThanOrEqual

> **LessThanOrEqual**: `"<="`

Defined in: src/core/base/Expr.ts:566

***

### StrictEquality

> **StrictEquality**: `"==="`

Defined in: src/core/base/Expr.ts:571

***

### StrictInequality

> **StrictInequality**: `"!=="`

Defined in: src/core/base/Expr.ts:572




============================================================
## FILE: `enumerations/StorageLinkEdgeType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / StorageLinkEdgeType

# Enumeration: StorageLinkEdgeType

Defined in: src/callgraph/pointerAnalysis/Pag.ts:61

## Enumeration Members

### Local2Property

> **Local2Property**: `1`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:63

***

### Property2Local

> **Property2Local**: `0`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:62

***

### TwoWay

> **TwoWay**: `2`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:64




============================================================
## FILE: `enumerations/StorageType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / StorageType

# Enumeration: StorageType

Defined in: src/callgraph/pointerAnalysis/Pag.ts:55

## Enumeration Members

### APP\_STORAGE

> **APP\_STORAGE**: `0`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:56

***

### LOCAL\_STORAGE

> **LOCAL\_STORAGE**: `1`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:57

***

### Undefined

> **Undefined**: `2`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:58




============================================================
## FILE: `enumerations/UnaryOperator.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UnaryOperator

# Enumeration: UnaryOperator

Defined in: src/core/base/Expr.ts:958

## Enumeration Members

### BitwiseNot

> **BitwiseNot**: `"~"`

Defined in: src/core/base/Expr.ts:960

***

### LogicalNot

> **LogicalNot**: `"!"`

Defined in: src/core/base/Expr.ts:961

***

### Neg

> **Neg**: `"-"`

Defined in: src/core/base/Expr.ts:959




============================================================
## FILE: `functions/addCfg2Stmt.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / addCfg2Stmt

# Function: addCfg2Stmt()

> **addCfg2Stmt**(`method`): `void`

Defined in: src/utils/entryMethodUtils.ts:116

## Parameters

### method

[`ArkMethod`](../classes/ArkMethod.md)

## Returns

`void`




============================================================
## FILE: `functions/classSignatureCompare.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / classSignatureCompare

# Function: classSignatureCompare()

> **classSignatureCompare**(`leftSig`, `rightSig`): `boolean`

Defined in: src/core/model/ArkSignature.ts:462

## Parameters

### leftSig

[`ClassSignature`](../classes/ClassSignature.md)

### rightSig

[`ClassSignature`](../classes/ClassSignature.md)

## Returns

`boolean`




============================================================
## FILE: `functions/extractLastBracketContent.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / extractLastBracketContent

# Function: extractLastBracketContent()

> **extractLastBracketContent**(`input`): `string`

Defined in: src/utils/callGraphUtils.ts:203

## Parameters

### input

`string`

## Returns

`string`




============================================================
## FILE: `functions/fetchDependenciesFromFile.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / fetchDependenciesFromFile

# Function: fetchDependenciesFromFile()

> **fetchDependenciesFromFile**(`filePath`): `object`

Defined in: src/utils/json5parser.ts:22

## Parameters

### filePath

`string`

## Returns

`object`




============================================================
## FILE: `functions/fieldSignatureCompare.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / fieldSignatureCompare

# Function: fieldSignatureCompare()

> **fieldSignatureCompare**(`leftSig`, `rightSig`): `boolean`

Defined in: src/core/model/ArkSignature.ts:434

## Parameters

### leftSig

[`FieldSignature`](../classes/FieldSignature.md)

### rightSig

[`FieldSignature`](../classes/FieldSignature.md)

## Returns

`boolean`




============================================================
## FILE: `functions/fileSignatureCompare.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / fileSignatureCompare

# Function: fileSignatureCompare()

> **fileSignatureCompare**(`leftSig`, `rightSig`): `boolean`

Defined in: src/core/model/ArkSignature.ts:469

## Parameters

### leftSig

[`FileSignature`](../classes/FileSignature.md)

### rightSig

[`FileSignature`](../classes/FileSignature.md)

## Returns

`boolean`




============================================================
## FILE: `functions/genSignature4ImportClause.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / genSignature4ImportClause

# Function: genSignature4ImportClause()

> **genSignature4ImportClause**(`arkFileName`, `importClauseName`): `string`

Defined in: src/core/model/ArkSignature.ts:488

## Parameters

### arkFileName

`string`

### importClauseName

`string`

## Returns

`string`




============================================================
## FILE: `functions/getAllFiles.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / getAllFiles

# Function: getAllFiles()

> **getAllFiles**(`srcPath`, `exts`, `ignore`, `filenameArr`, `visited`): `string`[]

Defined in: src/utils/getAllFiles.ts:29

从指定目录中提取指定后缀名的所有文件

## Parameters

### srcPath

`string`

string 要提取文件的项目入口，相对或绝对路径都可

### exts

`string`[]

string[] 要提取的文件扩展名数组，每个扩展名需以点开头

### ignore

`string`[] = `[]`

### filenameArr

`string`[] = `[]`

string[] 用来存放提取出的文件的原始路径的数组，可不传，默认为空数组

### visited

`Set`\<`string`\> = `...`

## Returns

`string`[]

string[] 提取出的文件的原始路径数组




============================================================
## FILE: `functions/getCallbackMethodFromStmt.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / getCallbackMethodFromStmt

# Function: getCallbackMethodFromStmt()

> **getCallbackMethodFromStmt**(`stmt`, `scene`): `null` \| [`ArkMethod`](../classes/ArkMethod.md)

Defined in: src/utils/entryMethodUtils.ts:94

## Parameters

### stmt

[`Stmt`](../classes/Stmt.md)

### scene

[`Scene`](../classes/Scene.md)

## Returns

`null` \| [`ArkMethod`](../classes/ArkMethod.md)




============================================================
## FILE: `functions/getFileRecursively.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / getFileRecursively

# Function: getFileRecursively()

> **getFileRecursively**(`srcDir`, `fileName`, `visited`): `string`

Defined in: src/utils/FileUtils.ts:107

## Parameters

### srcDir

`string`

### fileName

`string`

### visited

`Set`\<`string`\> = `...`

## Returns

`string`




============================================================
## FILE: `functions/isEtsAtomicComponent.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / isEtsAtomicComponent

# Function: isEtsAtomicComponent()

> **isEtsAtomicComponent**(`name`): `boolean`

Defined in: src/core/common/EtsConst.ts:988

## Parameters

### name

`string`

## Returns

`boolean`




============================================================
## FILE: `functions/isEtsContainerComponent.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / isEtsContainerComponent

# Function: isEtsContainerComponent()

> **isEtsContainerComponent**(`name`): `boolean`

Defined in: src/core/common/EtsConst.ts:996

## Parameters

### name

`string`

## Returns

`boolean`




============================================================
## FILE: `functions/isEtsSystemComponent.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / isEtsSystemComponent

# Function: isEtsSystemComponent()

> **isEtsSystemComponent**(`name`): `boolean`

Defined in: src/core/common/EtsConst.ts:992

## Parameters

### name

`string`

## Returns

`boolean`




============================================================
## FILE: `functions/isItemRegistered.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / isItemRegistered

# Function: isItemRegistered()

> **isItemRegistered**\<`T`\>(`item`, `array`, `compareFunc`): `boolean`

Defined in: src/utils/callGraphUtils.ts:156

## Type Parameters

### T

`T`

## Parameters

### item

`T`

### array

`T`[]

### compareFunc

(`a`, `b`) => `boolean`

## Returns

`boolean`




============================================================
## FILE: `functions/methodSignatureCompare.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / methodSignatureCompare

# Function: methodSignatureCompare()

> **methodSignatureCompare**(`leftSig`, `rightSig`): `boolean`

Defined in: src/core/model/ArkSignature.ts:441

## Parameters

### leftSig

[`MethodSignature`](../classes/MethodSignature.md)

### rightSig

[`MethodSignature`](../classes/MethodSignature.md)

## Returns

`boolean`




============================================================
## FILE: `functions/methodSubSignatureCompare.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / methodSubSignatureCompare

# Function: methodSubSignatureCompare()

> **methodSubSignatureCompare**(`leftSig`, `rightSig`): `boolean`

Defined in: src/core/model/ArkSignature.ts:451

## Parameters

### leftSig

[`MethodSubSignature`](../classes/MethodSubSignature.md)

### rightSig

[`MethodSubSignature`](../classes/MethodSubSignature.md)

## Returns

`boolean`




============================================================
## FILE: `functions/parseJsonText.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / parseJsonText

# Function: parseJsonText()

> **parseJsonText**(`text`): `object`

Defined in: src/utils/json5parser.ts:39

## Parameters

### text

`string`

## Returns

`object`




============================================================
## FILE: `functions/printCallGraphDetails.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / printCallGraphDetails

# Function: printCallGraphDetails()

> **printCallGraphDetails**(`methods`, `calls`, `rootDir`): `void`

Defined in: src/utils/callGraphUtils.ts:179

## Parameters

### methods

`Set`\<[`MethodSignature`](../classes/MethodSignature.md)\>

### calls

`Map`\<[`MethodSignature`](../classes/MethodSignature.md), [`MethodSignature`](../classes/MethodSignature.md)[]\>

### rootDir

`string`

## Returns

`void`




============================================================
## FILE: `functions/splitStringWithRegex.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / splitStringWithRegex

# Function: splitStringWithRegex()

> **splitStringWithRegex**(`input`): `string`[]

Defined in: src/utils/callGraphUtils.ts:165

## Parameters

### input

`string`

## Returns

`string`[]




============================================================
## FILE: `functions/transfer2UnixPath.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / transfer2UnixPath

# Function: transfer2UnixPath()

> **transfer2UnixPath**(`path2Do`): `string`

Defined in: src/utils/pathTransfer.ts:18

## Parameters

### path2Do

`string`

## Returns

`string`




============================================================
## FILE: `globals.md`
============================================================

[**ArkAnalyzer**](README.md)

***

# ArkAnalyzer API 1.0.0

## core/base

- [Constant](classes/Constant.md)
- [Decorator](classes/Decorator.md)
- [LineColPosition](classes/LineColPosition.md)
- [Local](classes/Local.md)
- [Value](interfaces/Value.md)

## core/base/expr

- [AbstractBinopExpr](classes/AbstractBinopExpr.md)
- [AbstractExpr](classes/AbstractExpr.md)
- [AbstractInvokeExpr](classes/AbstractInvokeExpr.md)
- [AliasTypeExpr](classes/AliasTypeExpr.md)
- [ArkAwaitExpr](classes/ArkAwaitExpr.md)
- [ArkCastExpr](classes/ArkCastExpr.md)
- [ArkConditionExpr](classes/ArkConditionExpr.md)
- [ArkDeleteExpr](classes/ArkDeleteExpr.md)
- [ArkInstanceInvokeExpr](classes/ArkInstanceInvokeExpr.md)
- [ArkInstanceOfExpr](classes/ArkInstanceOfExpr.md)
- [ArkNewArrayExpr](classes/ArkNewArrayExpr.md)
- [ArkNewExpr](classes/ArkNewExpr.md)
- [ArkNormalBinopExpr](classes/ArkNormalBinopExpr.md)
- [ArkPhiExpr](classes/ArkPhiExpr.md)
- [ArkStaticInvokeExpr](classes/ArkStaticInvokeExpr.md)
- [ArkTypeOfExpr](classes/ArkTypeOfExpr.md)
- [ArkUnopExpr](classes/ArkUnopExpr.md)
- [ArkYieldExpr](classes/ArkYieldExpr.md)

## core/base/stmt

- [ArkAliasTypeDefineStmt](classes/ArkAliasTypeDefineStmt.md)
- [ArkAssignStmt](classes/ArkAssignStmt.md)
- [ArkIfStmt](classes/ArkIfStmt.md)
- [ArkInvokeStmt](classes/ArkInvokeStmt.md)
- [ArkReturnStmt](classes/ArkReturnStmt.md)
- [ArkReturnVoidStmt](classes/ArkReturnVoidStmt.md)
- [ArkThrowStmt](classes/ArkThrowStmt.md)
- [Stmt](classes/Stmt.md)

## core/base/type

- [AliasType](classes/AliasType.md)
- [AnnotationNamespaceType](classes/AnnotationNamespaceType.md)
- [AnnotationType](classes/AnnotationType.md)
- [AnnotationTypeQueryType](classes/AnnotationTypeQueryType.md)
- [AnyType](classes/AnyType.md)
- [ArrayType](classes/ArrayType.md)
- [BigIntType](classes/BigIntType.md)
- [BooleanType](classes/BooleanType.md)
- [ClassType](classes/ClassType.md)
- [ClosureType](classes/ClosureType.md)
- [EnumValueType](classes/EnumValueType.md)
- [FunctionType](classes/FunctionType.md)
- [GenericType](classes/GenericType.md)
- [IntersectionType](classes/IntersectionType.md)
- [LexicalEnvType](classes/LexicalEnvType.md)
- [LiteralType](classes/LiteralType.md)
- [NeverType](classes/NeverType.md)
- [NullType](classes/NullType.md)
- [NumberType](classes/NumberType.md)
- [PrimitiveType](classes/PrimitiveType.md)
- [StringType](classes/StringType.md)
- [TupleType](classes/TupleType.md)
- [Type](classes/Type.md)
- [UnclearReferenceType](classes/UnclearReferenceType.md)
- [UndefinedType](classes/UndefinedType.md)
- [UnionType](classes/UnionType.md)
- [UnknownType](classes/UnknownType.md)
- [VoidType](classes/VoidType.md)

## core/base/ref

- [AbstractFieldRef](classes/AbstractFieldRef.md)
- [AbstractRef](classes/AbstractRef.md)
- [ArkArrayRef](classes/ArkArrayRef.md)
- [ArkCaughtExceptionRef](classes/ArkCaughtExceptionRef.md)
- [ArkInstanceFieldRef](classes/ArkInstanceFieldRef.md)
- [ArkParameterRef](classes/ArkParameterRef.md)
- [ArkStaticFieldRef](classes/ArkStaticFieldRef.md)
- [ArkThisRef](classes/ArkThisRef.md)
- [ClosureFieldRef](classes/ClosureFieldRef.md)
- [GlobalRef](classes/GlobalRef.md)

## core/model

- [ArkClass](classes/ArkClass.md)
- [ArkField](classes/ArkField.md)
- [ArkFile](classes/ArkFile.md)
- [ArkMethod](classes/ArkMethod.md)
- [ArkNamespace](classes/ArkNamespace.md)
- [ExportInfo](classes/ExportInfo.md)
- [FileSignature](classes/FileSignature.md)
- [ImportInfo](classes/ImportInfo.md)
- [MethodSignature](classes/MethodSignature.md)

## core/graph

- [Cfg](classes/Cfg.md)
- [ViewTree](interfaces/ViewTree.md)
- [ViewTreeNode](interfaces/ViewTreeNode.md)

## Other

- [ts](ArkAnalyzer/namespaces/ts/README.md)
- [CallGraphNodeKind](enumerations/CallGraphNodeKind.md)
- [LOG\_LEVEL](enumerations/LOG_LEVEL.md)
- [LOG\_MODULE\_TYPE](enumerations/LOG_MODULE_TYPE.md)
- [NormalBinaryOperator](enumerations/NormalBinaryOperator.md)
- [PagEdgeKind](enumerations/PagEdgeKind.md)
- [PagNodeKind](enumerations/PagNodeKind.md)
- [RelationalBinaryOperator](enumerations/RelationalBinaryOperator.md)
- [StorageLinkEdgeType](enumerations/StorageLinkEdgeType.md)
- [StorageType](enumerations/StorageType.md)
- [UnaryOperator](enumerations/UnaryOperator.md)
- [AbstractAnalysis](classes/AbstractAnalysis.md)
- [AddrPagEdge](classes/AddrPagEdge.md)
- [AliasClassSignature](classes/AliasClassSignature.md)
- [AliasTypeSignature](classes/AliasTypeSignature.md)
- [ArkBody](classes/ArkBody.md)
- [ArkPtrInvokeExpr](classes/ArkPtrInvokeExpr.md)
- [ArkSignatureBuilder](classes/ArkSignatureBuilder.md)
- [AstTreeUtils](classes/AstTreeUtils.md)
- [BaseEdge](classes/BaseEdge.md)
- [BaseExplicitGraph](classes/BaseExplicitGraph.md)
- [BaseNode](classes/BaseNode.md)
- [CallGraph](classes/CallGraph.md)
- [CallGraphBuilder](classes/CallGraphBuilder.md)
- [CallGraphEdge](classes/CallGraphEdge.md)
- [CallGraphNode](classes/CallGraphNode.md)
- [CallSite](classes/CallSite.md)
- [CGStat](classes/CGStat.md)
- [ClassHierarchyAnalysis](classes/ClassHierarchyAnalysis.md)
- [ClassSignature](classes/ClassSignature.md)
- [CopyPagEdge](classes/CopyPagEdge.md)
- [CSFuncID](classes/CSFuncID.md)
- [DataflowProblem](classes/DataflowProblem.md)
- [DataflowResult](classes/DataflowResult.md)
- [DataflowSolver](classes/DataflowSolver.md)
- [DefUseChain](classes/DefUseChain.md)
- [DiffPTData](classes/DiffPTData.md)
- [DominanceFinder](classes/DominanceFinder.md)
- [DominanceTree](classes/DominanceTree.md)
- [DummyCallCreator](classes/DummyCallCreator.md)
- [DummyMainCreater](classes/DummyMainCreater.md)
- [DVFG](classes/DVFG.md)
- [DVFGBuilder](classes/DVFGBuilder.md)
- [DynCallSite](classes/DynCallSite.md)
- [ExprUseReplacer](classes/ExprUseReplacer.md)
- [Fact](classes/Fact.md)
- [FieldSignature](classes/FieldSignature.md)
- [FileUtils](classes/FileUtils.md)
- [FullPosition](classes/FullPosition.md)
- [FuncPag](classes/FuncPag.md)
- [InterFuncPag](classes/InterFuncPag.md)
- [IRUtils](classes/IRUtils.md)
- [KLimitedContextSensitive](classes/KLimitedContextSensitive.md)
- [LoadPagEdge](classes/LoadPagEdge.md)
- [LocalSignature](classes/LocalSignature.md)
- [Logger](classes/Logger.md)
- [MethodSignatureManager](classes/MethodSignatureManager.md)
- [MethodSubSignature](classes/MethodSubSignature.md)
- [ModelUtils](classes/ModelUtils.md)
- [ModulePath](classes/ModulePath.md)
- [NamespaceSignature](classes/NamespaceSignature.md)
- [Pag](classes/Pag.md)
- [PagArrayNode](classes/PagArrayNode.md)
- [PagBuilder](classes/PagBuilder.md)
- [PagEdge](classes/PagEdge.md)
- [PagFuncNode](classes/PagFuncNode.md)
- [PagGlobalThisNode](classes/PagGlobalThisNode.md)
- [PagInstanceFieldNode](classes/PagInstanceFieldNode.md)
- [PagLocalNode](classes/PagLocalNode.md)
- [PagNewContainerExprNode](classes/PagNewContainerExprNode.md)
- [PagNewExprNode](classes/PagNewExprNode.md)
- [PagNode](classes/PagNode.md)
- [PagParamNode](classes/PagParamNode.md)
- [PAGStat](classes/PAGStat.md)
- [PagStaticFieldNode](classes/PagStaticFieldNode.md)
- [PagThisRefNode](classes/PagThisRefNode.md)
- [PathEdge](classes/PathEdge.md)
- [PathEdgePoint](classes/PathEdgePoint.md)
- [PointerAnalysis](classes/PointerAnalysis.md)
- [PointerAnalysisConfig](classes/PointerAnalysisConfig.md)
- [PTAStat](classes/PTAStat.md)
- [PtsSet](classes/PtsSet.md)
- [RapidTypeAnalysis](classes/RapidTypeAnalysis.md)
- [RefUseReplacer](classes/RefUseReplacer.md)
- [SCCDetection](classes/SCCDetection.md)
- [Scene](classes/Scene.md)
- [SceneConfig](classes/SceneConfig.md)
- [SceneManager](classes/SceneManager.md)
- [Scope](classes/Scope.md)
- [StaticSingleAssignmentFormer](classes/StaticSingleAssignmentFormer.md)
- [StmtUseReplacer](classes/StmtUseReplacer.md)
- [ThisPagEdge](classes/ThisPagEdge.md)
- [TypeInference](classes/TypeInference.md)
- [UndefinedVariableChecker](classes/UndefinedVariableChecker.md)
- [UndefinedVariableSolver](classes/UndefinedVariableSolver.md)
- [ValueUtil](classes/ValueUtil.md)
- [VisibleValue](classes/VisibleValue.md)
- [WritePagEdge](classes/WritePagEdge.md)
- [AbilityMessage](interfaces/AbilityMessage.md)
- [ArkSignature](interfaces/ArkSignature.md)
- [FlowFunction](interfaces/FlowFunction.md)
- [ICallSite](interfaces/ICallSite.md)
- [AliasTypeOriginalModel](type-aliases/AliasTypeOriginalModel.md)
- [BaseSignature](type-aliases/BaseSignature.md)
- [BinaryOperator](type-aliases/BinaryOperator.md)
- [FuncID](type-aliases/FuncID.md)
- [InterProceduralEdge](type-aliases/InterProceduralEdge.md)
- [InterProceduralSrcType](type-aliases/InterProceduralSrcType.md)
- [IntraProceduralEdge](type-aliases/IntraProceduralEdge.md)
- [Kind](type-aliases/Kind.md)
- [Method](type-aliases/Method.md)
- [NodeID](type-aliases/NodeID.md)
- [PagNodeType](type-aliases/PagNodeType.md)
- [Signature](type-aliases/Signature.md)
- [ALL](variables/ALL.md)
- [ANONYMOUS\_CLASS\_DELIMITER](variables/ANONYMOUS_CLASS_DELIMITER.md)
- [ANONYMOUS\_CLASS\_PREFIX](variables/ANONYMOUS_CLASS_PREFIX.md)
- [ANONYMOUS\_METHOD\_PREFIX](variables/ANONYMOUS_METHOD_PREFIX.md)
- [ANY\_KEYWORD](variables/ANY_KEYWORD.md)
- [ARKTS\_STATIC\_MARK](variables/ARKTS_STATIC_MARK.md)
- [BIGINT\_KEYWORD](variables/BIGINT_KEYWORD.md)
- [BOOLEAN\_KEYWORD](variables/BOOLEAN_KEYWORD.md)
- [BUILD\_PROFILE\_JSON5](variables/BUILD_PROFILE_JSON5.md)
- [BUILDER\_DECORATOR](variables/BUILDER_DECORATOR.md)
- [BUILDER\_PARAM\_DECORATOR](variables/BUILDER_PARAM_DECORATOR.md)
- [BUILDIN\_ATOMIC\_COMPONENT](variables/BUILDIN_ATOMIC_COMPONENT.md)
- [BUILDIN\_SYSTEM\_COMPONENT](variables/BUILDIN_SYSTEM_COMPONENT.md)
- [CALL\_BACK](variables/CALL_BACK.md)
- [CALL\_SIGNATURE\_NAME](variables/CALL_SIGNATURE_NAME.md)
- [CALLBACK\_METHOD\_NAME](variables/CALLBACK_METHOD_NAME.md)
- [COMPONENT\_ATTRIBUTE](variables/COMPONENT_ATTRIBUTE.md)
- [COMPONENT\_BRANCH\_FUNCTION](variables/COMPONENT_BRANCH_FUNCTION.md)
- [COMPONENT\_BUILD\_FUNCTION](variables/COMPONENT_BUILD_FUNCTION.md)
- [COMPONENT\_COMMON](variables/COMPONENT_COMMON.md)
- [COMPONENT\_CREATE\_FUNCTION](variables/COMPONENT_CREATE_FUNCTION.md)
- [COMPONENT\_CUSTOMVIEW](variables/COMPONENT_CUSTOMVIEW.md)
- [COMPONENT\_DECORATOR](variables/COMPONENT_DECORATOR.md)
- [COMPONENT\_FOR\_EACH](variables/COMPONENT_FOR_EACH.md)
- [COMPONENT\_IF](variables/COMPONENT_IF.md)
- [COMPONENT\_IF\_BRANCH](variables/COMPONENT_IF_BRANCH.md)
- [COMPONENT\_INSTANCE](variables/COMPONENT_INSTANCE.md)
- [COMPONENT\_LAZY\_FOR\_EACH](variables/COMPONENT_LAZY_FOR_EACH.md)
- [COMPONENT\_LIFECYCLE\_METHOD\_NAME](variables/COMPONENT_LIFECYCLE_METHOD_NAME.md)
- [COMPONENT\_POP\_FUNCTION](variables/COMPONENT_POP_FUNCTION.md)
- [COMPONENT\_REPEAT](variables/COMPONENT_REPEAT.md)
- [CONSTRUCTOR\_NAME](variables/CONSTRUCTOR_NAME.md)
- [DECLARE\_KEYWORD](variables/DECLARE_KEYWORD.md)
- [DEFAULT](variables/DEFAULT.md)
- [DEFAULT\_ARK\_CLASS\_NAME](variables/DEFAULT_ARK_CLASS_NAME.md)
- [DEFAULT\_ARK\_METHOD\_NAME](variables/DEFAULT_ARK_METHOD_NAME.md)
- [DEFAULT\_NAME](variables/DEFAULT_NAME.md)
- [ENTRY\_DECORATOR](variables/ENTRY_DECORATOR.md)
- [ETS\_COMPILER\_OPTIONS](variables/ETS_COMPILER_OPTIONS.md)
- [FUNCTION](variables/FUNCTION.md)
- [GLOBAL\_THIS\_NAME](variables/GLOBAL_THIS_NAME.md)
- [IMPORT](variables/IMPORT.md)
- [INSTANCE\_INIT\_METHOD\_NAME](variables/INSTANCE_INIT_METHOD_NAME.md)
- [LEXICAL\_ENV\_NAME\_PREFIX](variables/LEXICAL_ENV_NAME_PREFIX.md)
- [LIFECYCLE\_METHOD\_NAME](variables/LIFECYCLE_METHOD_NAME.md)
- [NAME\_DELIMITER](variables/NAME_DELIMITER.md)
- [NAME\_PREFIX](variables/NAME_PREFIX.md)
- [NEVER\_KEYWORD](variables/NEVER_KEYWORD.md)
- [NULL\_KEYWORD](variables/NULL_KEYWORD.md)
- [NUMBER\_KEYWORD](variables/NUMBER_KEYWORD.md)
- [OH\_PACKAGE\_JSON5](variables/OH_PACKAGE_JSON5.md)
- [ON\_OFF](variables/ON_OFF.md)
- [PROMISE](variables/PROMISE.md)
- [SPECIAL\_CONTAINER\_COMPONENT](variables/SPECIAL_CONTAINER_COMPONENT.md)
- [STATIC\_BLOCK\_METHOD\_NAME\_PREFIX](variables/STATIC_BLOCK_METHOD_NAME_PREFIX.md)
- [STATIC\_INIT\_METHOD\_NAME](variables/STATIC_INIT_METHOD_NAME.md)
- [STRING\_KEYWORD](variables/STRING_KEYWORD.md)
- [SUPER\_NAME](variables/SUPER_NAME.md)
- [TEMP\_LOCAL\_PREFIX](variables/TEMP_LOCAL_PREFIX.md)
- [THIS\_NAME](variables/THIS_NAME.md)
- [TSCONFIG\_JSON](variables/TSCONFIG_JSON.md)
- [UNDEFINED\_KEYWORD](variables/UNDEFINED_KEYWORD.md)
- [UNKNOWN\_CLASS\_NAME](variables/UNKNOWN_CLASS_NAME.md)
- [UNKNOWN\_FIELD\_NAME](variables/UNKNOWN_FIELD_NAME.md)
- [UNKNOWN\_FILE\_NAME](variables/UNKNOWN_FILE_NAME.md)
- [UNKNOWN\_KEYWORD](variables/UNKNOWN_KEYWORD.md)
- [UNKNOWN\_METHOD\_NAME](variables/UNKNOWN_METHOD_NAME.md)
- [UNKNOWN\_NAME](variables/UNKNOWN_NAME.md)
- [UNKNOWN\_NAMESPACE\_NAME](variables/UNKNOWN_NAMESPACE_NAME.md)
- [UNKNOWN\_PROJECT\_NAME](variables/UNKNOWN_PROJECT_NAME.md)
- [VOID\_KEYWORD](variables/VOID_KEYWORD.md)
- [addCfg2Stmt](functions/addCfg2Stmt.md)
- [classSignatureCompare](functions/classSignatureCompare.md)
- [extractLastBracketContent](functions/extractLastBracketContent.md)
- [fetchDependenciesFromFile](functions/fetchDependenciesFromFile.md)
- [fieldSignatureCompare](functions/fieldSignatureCompare.md)
- [fileSignatureCompare](functions/fileSignatureCompare.md)
- [genSignature4ImportClause](functions/genSignature4ImportClause.md)
- [getAllFiles](functions/getAllFiles.md)
- [getCallbackMethodFromStmt](functions/getCallbackMethodFromStmt.md)
- [getFileRecursively](functions/getFileRecursively.md)
- [isEtsAtomicComponent](functions/isEtsAtomicComponent.md)
- [isEtsContainerComponent](functions/isEtsContainerComponent.md)
- [isEtsSystemComponent](functions/isEtsSystemComponent.md)
- [isItemRegistered](functions/isItemRegistered.md)
- [methodSignatureCompare](functions/methodSignatureCompare.md)
- [methodSubSignatureCompare](functions/methodSubSignatureCompare.md)
- [parseJsonText](functions/parseJsonText.md)
- [printCallGraphDetails](functions/printCallGraphDetails.md)
- [splitStringWithRegex](functions/splitStringWithRegex.md)
- [transfer2UnixPath](functions/transfer2UnixPath.md)

## core/graph
A `BasicBlock` is composed of:
- ID: a **number** that uniquely identify the basic block, initialized as -1.
- Statements: an **array** of statements in the basic block.
- Predecessors:  an **array** of basic blocks in front of the current basic block. More accurately, these basic
    blocks can reach the current block through edges.
- Successors: an **array** of basic blocks after the current basic block. More accurately, the current block can
    reach these basic blocks through edges.

- [BasicBlock](classes/BasicBlock.md)

## save

- [DotClassPrinter](classes/DotClassPrinter.md)
- [DotFilePrinter](classes/DotFilePrinter.md)
- [DotMethodPrinter](classes/DotMethodPrinter.md)
- [DotNamespacePrinter](classes/DotNamespacePrinter.md)
- [GraphPrinter](classes/GraphPrinter.md)
- [JsonPrinter](classes/JsonPrinter.md)
- [Printer](classes/Printer.md)
- [PrinterBuilder](classes/PrinterBuilder.md)
- [SourceClassPrinter](classes/SourceClassPrinter.md)
- [SourceFilePrinter](classes/SourceFilePrinter.md)
- [SourceMethodPrinter](classes/SourceMethodPrinter.md)
- [SourceNamespacePrinter](classes/SourceNamespacePrinter.md)
- [ViewTreePrinter](classes/ViewTreePrinter.md)




============================================================
## FILE: `interfaces/AbilityMessage.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / AbilityMessage

# Interface: AbilityMessage

Defined in: src/utils/entryMethodUtils.ts:88

## Properties

### name

> **name**: `string`

Defined in: src/utils/entryMethodUtils.ts:90

***

### srcEntrance

> **srcEntrance**: `string`

Defined in: src/utils/entryMethodUtils.ts:91

***

### srcEntry

> **srcEntry**: `string`

Defined in: src/utils/entryMethodUtils.ts:89




============================================================
## FILE: `interfaces/ArkSignature.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ArkSignature

# Interface: ArkSignature

Defined in: src/core/model/ArkSignature.ts:33

## Methods

### getSignature()

> **getSignature**(): [`Signature`](../type-aliases/Signature.md)

Defined in: src/core/model/ArkSignature.ts:34

#### Returns

[`Signature`](../type-aliases/Signature.md)




============================================================
## FILE: `interfaces/FlowFunction.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / FlowFunction

# Interface: FlowFunction\<D\>

Defined in: src/core/dataflow/DataflowProblem.ts:52

## Type Parameters

### D

`D`

## Methods

### getDataFacts()

> **getDataFacts**(`d`): `Set`\<`D`\>

Defined in: src/core/dataflow/DataflowProblem.ts:53

#### Parameters

##### d

`D`

#### Returns

`Set`\<`D`\>




============================================================
## FILE: `interfaces/ICallSite.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ICallSite

# Interface: ICallSite

Defined in: src/callgraph/model/CallSite.ts:23

## Properties

### args

> **args**: `undefined` \| [`Value`](Value.md)[]

Defined in: src/callgraph/model/CallSite.ts:25

***

### callerFuncID

> **callerFuncID**: `number`

Defined in: src/callgraph/model/CallSite.ts:26

***

### callStmt

> **callStmt**: [`Stmt`](../classes/Stmt.md)

Defined in: src/callgraph/model/CallSite.ts:24




============================================================
## FILE: `interfaces/Value.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Value

# Interface: Value

Defined in: src/core/base/Value.ts:21

## Methods

### getType()

> **getType**(): [`Type`](../classes/Type.md)

Defined in: src/core/base/Value.ts:48

Return the type of this value. The interface is encapsulated in Value. 
The `Type` is defined in type.ts, such as **Any**, **Unknown**, **TypeParameter**, 
**UnclearReference**, **Primitive**, **Number**, **String**, etc.

#### Returns

[`Type`](../classes/Type.md)

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

***

### getUses()

> **getUses**(): `Value`[]

Defined in: src/core/base/Value.ts:27

Return a list of values which are contained in this Value.
Value is a core interface in ArkAnalyzer, which may represent any value or expression.

#### Returns

`Value`[]

An **array** of values used by this value.




============================================================
## FILE: `interfaces/ViewTree.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ViewTree

# Interface: ViewTree

Defined in: src/core/graph/ViewTree.ts:118

ArkUI Component Tree

## Example

```ts
// Component Class get ViewTree
let arkClas: ArkClass = ...;
let viewtree = arkClas.getViewTree();

// get viewtree root node
let root: ViewTreeNode = viewtree.getRoot();

// get viewtree stateValues Map
let stateValues: Map<ArkField, Set<ViewTreeNode>> = viewtree.getStateValues();

// walk all nodes
root.walk((node) => {
  // check node is builder
  if (node.isBuilder()) {
     xx
  }

  // check node is sub CustomComponent
  if (node.isCustomComponent()) {
     xx
  }

  if (xxx) {
     // Skip the remaining nodes and end the traversal
     return true;
  }

  return false;
})
```

## Methods

### ~~getClassFieldType()~~

> **getClassFieldType**(`name`): `undefined` \| [`Decorator`](../classes/Decorator.md) \| [`Type`](../classes/Type.md)

Defined in: src/core/graph/ViewTree.ts:127

#### Parameters

##### name

`string`

#### Returns

`undefined` \| [`Decorator`](../classes/Decorator.md) \| [`Type`](../classes/Type.md)

#### Deprecated

Use [getStateValues](#getstatevalues) instead.

***

### getRoot()

> **getRoot**(): `null` \| [`ViewTreeNode`](ViewTreeNode.md)

Defined in: src/core/graph/ViewTree.ts:139

ViewTree root node.

#### Returns

`null` \| [`ViewTreeNode`](ViewTreeNode.md)

root node

***

### getStateValues()

> **getStateValues**(): `Map`\<[`ArkField`](../classes/ArkField.md), `Set`\<[`ViewTreeNode`](ViewTreeNode.md)\>\>

Defined in: src/core/graph/ViewTree.ts:133

Map of the component controlled by the state variable

#### Returns

`Map`\<[`ArkField`](../classes/ArkField.md), `Set`\<[`ViewTreeNode`](ViewTreeNode.md)\>\>

***

### ~~isClassField()~~

> **isClassField**(`name`): `boolean`

Defined in: src/core/graph/ViewTree.ts:122

#### Parameters

##### name

`string`

#### Returns

`boolean`

#### Deprecated

Use [getStateValues](#getstatevalues) instead.




============================================================
## FILE: `interfaces/ViewTreeNode.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ViewTreeNode

# Interface: ViewTreeNode

Defined in: src/core/graph/ViewTree.ts:28

## Properties

### attributes

> **attributes**: `Map`\<`string`, \[[`Stmt`](../classes/Stmt.md), ([`Constant`](../classes/Constant.md) \| [`MethodSignature`](../classes/MethodSignature.md) \| [`ArkInstanceFieldRef`](../classes/ArkInstanceFieldRef.md))[]\]\>

Defined in: src/core/graph/ViewTree.ts:34

Component attribute stmts, key is attribute name, value is [Stmt, [Uses Values]].

***

### builder?

> `optional` **builder**: [`MethodSignature`](../classes/MethodSignature.md)

Defined in: src/core/graph/ViewTree.ts:59

builderParam bind builder method signature.

***

### builderParam?

> `optional` **builderParam**: [`ArkField`](../classes/ArkField.md)

Defined in: src/core/graph/ViewTree.ts:56

BuilderParam placeholders ArkField.

***

### children

> **children**: `ViewTreeNode`[]

Defined in: src/core/graph/ViewTree.ts:40

Node's children.

***

### ~~classSignature?~~

> `optional` **classSignature**: [`MethodSignature`](../classes/MethodSignature.md) \| [`ClassSignature`](../classes/ClassSignature.md)

Defined in: src/core/graph/ViewTree.ts:42

#### Deprecated

Use [signature](#signature) instead.

***

### name

> **name**: `string`

Defined in: src/core/graph/ViewTree.ts:30

Component node name

***

### parent

> **parent**: `null` \| `ViewTreeNode`

Defined in: src/core/graph/ViewTree.ts:38

Node's parent, CustomComponent and root node no parent.

***

### signature?

> `optional` **signature**: [`MethodSignature`](../classes/MethodSignature.md) \| [`ClassSignature`](../classes/ClassSignature.md)

Defined in: src/core/graph/ViewTree.ts:44

CustomComponent class signature or Builder method signature.

***

### stateValues

> **stateValues**: `Set`\<[`ArkField`](../classes/ArkField.md)\>

Defined in: src/core/graph/ViewTree.ts:36

Used state values.

***

### stateValuesTransfer?

> `optional` **stateValuesTransfer**: `Map`\<[`ArkField`](../classes/ArkField.md), [`ArkField`](../classes/ArkField.md) \| [`ArkMethod`](../classes/ArkMethod.md)\>

Defined in: src/core/graph/ViewTree.ts:53

Custom component value transfer
- key: ArkField, child custom component class stateValue field.
- value: ArkField | ArkMethod, parent component transfer value.
    key is BuilderParam, the value is Builder ArkMethod.
    Others, the value is parent class stateValue field.

***

### ~~stmts~~

> **stmts**: `Map`\<`string`, \[[`Stmt`](../classes/Stmt.md), ([`Constant`](../classes/Constant.md) \| [`MethodSignature`](../classes/MethodSignature.md) \| [`ArkInstanceFieldRef`](../classes/ArkInstanceFieldRef.md))[]\]\>

Defined in: src/core/graph/ViewTree.ts:32

#### Deprecated

Use [attributes](#attributes) instead.

## Methods

### isBuilder()

> **isBuilder**(): `boolean`

Defined in: src/core/graph/ViewTree.ts:74

Whether the node type is Builder.

#### Returns

`boolean`

true: node is Builder, false others.

***

### isCustomComponent()

> **isCustomComponent**(): `boolean`

Defined in: src/core/graph/ViewTree.ts:80

Whether the node type is custom component.

#### Returns

`boolean`

true: node is custom component, false others.

***

### walk()

> **walk**(`selector`): `boolean`

Defined in: src/core/graph/ViewTree.ts:68

walk node and node's children

#### Parameters

##### selector

(`item`) => `boolean`

Node selector function, return true skipping the follow-up nodes.

#### Returns

`boolean`

- true: There are nodes that meet the selector.
 - false: does not exist.




============================================================
## FILE: `tree.md`
============================================================

.
├── _media
│   ├── globals.md
│   ├── HowToCreatePR.md
│   └── README.md
├── 项目背景.md
├── ArkAnalyzer
│   └── namespaces
│       └── ts
│           ├── classes
│           │   ├── ArkTSLinterTimePrinter.md
│           │   └── OperationCanceledException.md
│           ├── enumerations
│           │   ├── ClassificationType.md
│           │   ├── ClassificationTypeNames.md
│           │   ├── CompletionInfoFlags.md
│           │   ├── CompletionTriggerKind.md
│           │   ├── DiagnosticCategory.md
│           │   ├── ElementFlags.md
│           │   ├── EmitFlags.md
│           │   ├── EmitHint.md
│           │   ├── EndOfLineState.md
│           │   ├── EtsFlags.md
│           │   ├── ExitStatus.md
│           │   ├── Extension.md
│           │   ├── FileWatcherEventKind.md
│           │   ├── FlowFlags.md
│           │   ├── GeneratedIdentifierFlags.md
│           │   ├── HighlightSpanKind.md
│           │   ├── ImportsNotUsedAsValues.md
│           │   ├── IndentStyle.md
│           │   ├── IndexKind.md
│           │   ├── InferencePriority.md
│           │   ├── InlayHintKind.md
│           │   ├── InternalSymbolName.md
│           │   ├── InvalidatedProjectKind.md
│           │   ├── JsxEmit.md
│           │   ├── JsxFlags.md
│           │   ├── LanguageServiceMode.md
│           │   ├── LanguageVariant.md
│           │   ├── ListFormat.md
│           │   ├── ModifierFlags.md
│           │   ├── ModuleDetectionKind.md
│           │   ├── ModuleKind.md
│           │   ├── ModuleResolutionKind.md
│           │   ├── NewLineKind.md
│           │   ├── NodeBuilderFlags.md
│           │   ├── NodeFlags.md
│           │   ├── ObjectFlags.md
│           │   ├── OrganizeImportsMode.md
│           │   ├── OuterExpressionKinds.md
│           │   ├── OutliningSpanKind.md
│           │   ├── OutputFileType.md
│           │   ├── PollingWatchKind.md
│           │   ├── ScriptElementKind.md
│           │   ├── ScriptElementKindModifier.md
│           │   ├── ScriptKind.md
│           │   ├── ScriptTarget.md
│           │   ├── SemanticClassificationFormat.md
│           │   ├── SemicolonPreference.md
│           │   ├── SignatureKind.md
│           │   ├── SymbolDisplayPartKind.md
│           │   ├── SymbolFlags.md
│           │   ├── SymbolFormatFlags.md
│           │   ├── SyntaxKind.md
│           │   ├── TimePhase.md
│           │   ├── TokenClass.md
│           │   ├── TokenFlags.md
│           │   ├── TypeFlags.md
│           │   ├── TypeFormatFlags.md
│           │   ├── TypePredicateKind.md
│           │   ├── WatchDirectoryFlags.md
│           │   ├── WatchDirectoryKind.md
│           │   └── WatchFileKind.md
│           ├── functions
│           │   ├── addEmitHelper.md
│           │   ├── addEmitHelpers.md
│           │   ├── addSyntheticLeadingComment.md
│           │   ├── addSyntheticTrailingComment.md
│           │   ├── canHaveDecorators.md
│           │   ├── canHaveModifiers.md
│           │   ├── choosePathContainsModules.md
│           │   ├── classicNameResolver.md
│           │   ├── collapseTextChangeRangesAcrossMultipleVersions.md
│           │   ├── concatenateDecoratorsAndModifiers.md
│           │   ├── convertCompilerOptionsFromJson.md
│           │   ├── convertToObject.md
│           │   ├── convertTypeAcquisitionFromJson.md
│           │   ├── couldStartTrivia.md
│           │   ├── createAbstractBuilder.md
│           │   ├── createBuilderStatusReporter.md
│           │   ├── createClassifier.md
│           │   ├── createCompilerHost.md
│           │   ├── createDocumentRegistry.md
│           │   ├── createEmitAndSemanticDiagnosticsBuilderProgram.md
│           │   ├── createEmitAndSemanticDiagnosticsBuilderProgramForArkTs.md
│           │   ├── createIncrementalCompilerHost.md
│           │   ├── createIncrementalProgram.md
│           │   ├── createIncrementalProgramForArkTs.md
│           │   ├── createInputFiles.md
│           │   ├── createLanguageService.md
│           │   ├── createLanguageServiceSourceFile.md
│           │   ├── createModuleResolutionCache.md
│           │   ├── createObfTextSingleLineWriter.md
│           │   ├── createPrinter.md
│           │   ├── createProgram.md
│           │   ├── createScanner.md
│           │   ├── createSemanticDiagnosticsBuilderProgram.md
│           │   ├── createSolutionBuilder.md
│           │   ├── createSolutionBuilderHost.md
│           │   ├── createSolutionBuilderWithWatch.md
│           │   ├── createSolutionBuilderWithWatchHost.md
│           │   ├── createSourceFile.md
│           │   ├── createSourceMapGenerator.md
│           │   ├── createSourceMapSource.md
│           │   ├── createTextChangeRange.md
│           │   ├── createTextSpan.md
│           │   ├── createTextSpanFromBounds.md
│           │   ├── createTextWriter.md
│           │   ├── createTypeReferenceDirectiveResolutionCache.md
│           │   ├── createUnparsedSourceFile.md
│           │   ├── createWatchCompilerHost.md
│           │   ├── createWatchProgram.md
│           │   ├── decodedTextSpanIntersectsWith.md
│           │   ├── displayPartsToString.md
│           │   ├── disposeEmitNodes.md
│           │   ├── escapeLeadingUnderscores.md
│           │   ├── findAncestor.md
│           │   ├── findConfigFile.md
│           │   ├── flattenDiagnosticMessageText.md
│           │   ├── forEachChild.md
│           │   ├── forEachLeadingCommentRange.md
│           │   ├── forEachTrailingCommentRange.md
│           │   ├── formatDiagnostic.md
│           │   ├── formatDiagnostics.md
│           │   ├── formatDiagnosticsWithColorAndContext.md
│           │   ├── getAllDecorators.md
│           │   ├── getAllJSDocTags.md
│           │   ├── getAllJSDocTagsOfKind.md
│           │   ├── getAutomaticTypeDirectiveNames.md
│           │   ├── getCombinedModifierFlags.md
│           │   ├── getCombinedNodeFlags.md
│           │   ├── getCommentRange.md
│           │   ├── getConfigFileParsingDiagnostics.md
│           │   ├── getConstantValue.md
│           │   ├── getDecorators.md
│           │   ├── getDefaultCompilerOptions.md
│           │   ├── getDefaultFormatCodeSettings.md
│           │   ├── getDefaultLibFileName.md
│           │   ├── getDefaultLibFilePath.md
│           │   ├── getEffectiveConstraintOfTypeParameter.md
│           │   ├── getEffectiveTypeParameterDeclarations.md
│           │   ├── getEffectiveTypeRoots.md
│           │   ├── getEmitHelpers.md
│           │   ├── getIllegalDecorators.md
│           │   ├── getImpliedNodeFormatForFile.md
│           │   ├── getJSDocAugmentsTag.md
│           │   ├── getJSDocClassTag.md
│           │   ├── getJSDocDeprecatedTag.md
│           │   ├── getJSDocEnumTag.md
│           │   ├── getJSDocImplementsTags.md
│           │   ├── getJSDocOverrideTagNoCache.md
│           │   ├── getJSDocParameterTags.md
│           │   ├── getJSDocPrivateTag.md
│           │   ├── getJSDocProtectedTag.md
│           │   ├── getJSDocPublicTag.md
│           │   ├── getJSDocReadonlyTag.md
│           │   ├── getJSDocReturnTag.md
│           │   ├── getJSDocReturnType.md
│           │   ├── getJSDocTags.md
│           │   ├── getJSDocTemplateTag.md
│           │   ├── getJSDocThisTag.md
│           │   ├── getJSDocType.md
│           │   ├── getJSDocTypeParameterTags.md
│           │   ├── getJSDocTypeTag.md
│           │   ├── getLeadingCommentRanges.md
│           │   ├── getLeadingCommentRangesOfNode.md
│           │   ├── getLineAndCharacterOfPosition.md
│           │   ├── getModeForFileReference.md
│           │   ├── getModeForResolutionAtIndex.md
│           │   ├── getModeForUsageLocation.md
│           │   ├── getModifiers.md
│           │   ├── getModuleByPMType.md
│           │   ├── getModulePathPartByPMType.md
│           │   ├── getNameOfDeclaration.md
│           │   ├── getNameOfJSDocTypedef.md
│           │   ├── getNodeMajorVersion.md
│           │   ├── getOriginalNode.md
│           │   ├── getOutputFileNames.md
│           │   ├── getPackageJsonByPMType.md
│           │   ├── getParsedCommandLineOfConfigFile.md
│           │   ├── getParseTreeNode.md
│           │   ├── getPositionOfLineAndCharacter.md
│           │   ├── getPreEmitDiagnostics.md
│           │   ├── getShebang.md
│           │   ├── getSourceMapRange.md
│           │   ├── getSupportedCodeFixes.md
│           │   ├── getSyntheticLeadingComments.md
│           │   ├── getSyntheticTrailingComments.md
│           │   ├── getTextOfJSDocComment.md
│           │   ├── getTokenSourceMapRange.md
│           │   ├── getTrailingCommentRanges.md
│           │   ├── getTsBuildInfoEmitOutputFilePath.md
│           │   ├── getTsBuildInfoEmitOutputFilePathForLinter.md
│           │   ├── getTypeExportImportAndConstEnumTransformer.md
│           │   ├── getTypeParameterOwner.md
│           │   ├── hasJSDocParameterTags.md
│           │   ├── hasOnlyExpressionInitializer.md
│           │   ├── hasRestParameter.md
│           │   ├── hasTsNoCheckOrTsIgnoreFlag.md
│           │   ├── idText.md
│           │   ├── isAccessor.md
│           │   ├── isArrayBindingPattern.md
│           │   ├── isArrayLiteralExpression.md
│           │   ├── isArrayTypeNode.md
│           │   ├── isArrowFunction.md
│           │   ├── isAsExpression.md
│           │   ├── isAssertClause.md
│           │   ├── isAssertEntry.md
│           │   ├── isAssertionExpression.md
│           │   ├── isAssertionKey.md
│           │   ├── isAsteriskToken.md
│           │   ├── isAutoAccessorPropertyDeclaration.md
│           │   ├── isAwaitExpression.md
│           │   ├── isBigIntLiteral.md
│           │   ├── isBinaryExpression.md
│           │   ├── isBindingElement.md
│           │   ├── isBindingName.md
│           │   ├── isBlock.md
│           │   ├── isBreakOrContinueStatement.md
│           │   ├── isBreakStatement.md
│           │   ├── isBundle.md
│           │   ├── isCallChain.md
│           │   ├── isCallExpression.md
│           │   ├── isCallLikeExpression.md
│           │   ├── isCallOrNewExpression.md
│           │   ├── isCallSignatureDeclaration.md
│           │   ├── isCaseBlock.md
│           │   ├── isCaseClause.md
│           │   ├── isCaseOrDefaultClause.md
│           │   ├── isCatchClause.md
│           │   ├── isClassDeclaration.md
│           │   ├── isClassElement.md
│           │   ├── isClassExpression.md
│           │   ├── isClassLike.md
│           │   ├── isClassOrTypeElement.md
│           │   ├── isClassStaticBlockDeclaration.md
│           │   ├── isCommaListExpression.md
│           │   ├── isComputedPropertyName.md
│           │   ├── isConditionalExpression.md
│           │   ├── isConditionalTypeNode.md
│           │   ├── isConstructorDeclaration.md
│           │   ├── isConstructorTypeNode.md
│           │   ├── isConstructSignatureDeclaration.md
│           │   ├── isConstTypeReference.md
│           │   ├── isContinueStatement.md
│           │   ├── isDebuggerStatement.md
│           │   ├── isDecorator.md
│           │   ├── isDefaultClause.md
│           │   ├── isDeleteExpression.md
│           │   ├── isDoStatement.md
│           │   ├── isDotDotDotToken.md
│           │   ├── isElementAccessChain.md
│           │   ├── isElementAccessExpression.md
│           │   ├── isEmptyBindingElement.md
│           │   ├── isEmptyBindingPattern.md
│           │   ├── isEmptyStatement.md
│           │   ├── isEntityName.md
│           │   ├── isEnumDeclaration.md
│           │   ├── isEnumMember.md
│           │   ├── isEtsComponentExpression.md
│           │   ├── isEtsFunctionDecorators.md
│           │   ├── isExportAssignment.md
│           │   ├── isExportDeclaration.md
│           │   ├── isExportSpecifier.md
│           │   ├── isExpressionStatement.md
│           │   ├── isExpressionWithTypeArguments.md
│           │   ├── isExternalModule.md
│           │   ├── isExternalModuleNameRelative.md
│           │   ├── isExternalModuleReference.md
│           │   ├── isForInStatement.md
│           │   ├── isForOfStatement.md
│           │   ├── isForStatement.md
│           │   ├── isFunctionDeclaration.md
│           │   ├── isFunctionExpression.md
│           │   ├── isFunctionLike.md
│           │   ├── isFunctionOrConstructorTypeNode.md
│           │   ├── isFunctionTypeNode.md
│           │   ├── isGetAccessor.md
│           │   ├── isGetAccessorDeclaration.md
│           │   ├── isHeritageClause.md
│           │   ├── isIdentifier.md
│           │   ├── isIdentifierPart.md
│           │   ├── isIdentifierStart.md
│           │   ├── isIfStatement.md
│           │   ├── isImportClause.md
│           │   ├── isImportDeclaration.md
│           │   ├── isImportEqualsDeclaration.md
│           │   ├── isImportOrExportSpecifier.md
│           │   ├── isImportSpecifier.md
│           │   ├── isImportTypeAssertionContainer.md
│           │   ├── isImportTypeNode.md
│           │   ├── isIndexedAccessTypeNode.md
│           │   ├── isIndexSignatureDeclaration.md
│           │   ├── isInferTypeNode.md
│           │   ├── isInterfaceDeclaration.md
│           │   ├── isIntersectionTypeNode.md
│           │   ├── isIterationStatement.md
│           │   ├── isJSDoc.md
│           │   ├── isJSDocAllType.md
│           │   ├── isJSDocAugmentsTag.md
│           │   ├── isJSDocAuthorTag.md
│           │   ├── isJSDocCallbackTag.md
│           │   ├── isJSDocClassTag.md
│           │   ├── isJSDocCommentContainingNode.md
│           │   ├── isJSDocDeprecatedTag.md
│           │   ├── isJSDocEnumTag.md
│           │   ├── isJSDocFunctionType.md
│           │   ├── isJSDocImplementsTag.md
│           │   ├── isJSDocLink.md
│           │   ├── isJSDocLinkCode.md
│           │   ├── isJSDocLinkLike.md
│           │   ├── isJSDocLinkPlain.md
│           │   ├── isJSDocMemberName.md
│           │   ├── isJSDocNamepathType.md
│           │   ├── isJSDocNameReference.md
│           │   ├── isJSDocNonNullableType.md
│           │   ├── isJSDocNullableType.md
│           │   ├── isJSDocOptionalType.md
│           │   ├── isJSDocOverrideTag.md
│           │   ├── isJSDocParameterTag.md
│           │   ├── isJSDocPrivateTag.md
│           │   ├── isJSDocPropertyLikeTag.md
│           │   ├── isJSDocPropertyTag.md
│           │   ├── isJSDocProtectedTag.md
│           │   ├── isJSDocPublicTag.md
│           │   ├── isJSDocReadonlyTag.md
│           │   ├── isJSDocReturnTag.md
│           │   ├── isJSDocSeeTag.md
│           │   ├── isJSDocSignature.md
│           │   ├── isJSDocTemplateTag.md
│           │   ├── isJSDocThisTag.md
│           │   ├── isJSDocTypedefTag.md
│           │   ├── isJSDocTypeExpression.md
│           │   ├── isJSDocTypeLiteral.md
│           │   ├── isJSDocTypeTag.md
│           │   ├── isJSDocUnknownTag.md
│           │   ├── isJSDocUnknownType.md
│           │   ├── isJSDocVariadicType.md
│           │   ├── isJsxAttribute.md
│           │   ├── isJsxAttributes.md
│           │   ├── isJsxClosingElement.md
│           │   ├── isJsxClosingFragment.md
│           │   ├── isJsxElement.md
│           │   ├── isJsxExpression.md
│           │   ├── isJsxFragment.md
│           │   ├── isJsxOpeningElement.md
│           │   ├── isJsxOpeningFragment.md
│           │   ├── isJsxOpeningLikeElement.md
│           │   ├── isJsxSelfClosingElement.md
│           │   ├── isJsxSpreadAttribute.md
│           │   ├── isJsxText.md
│           │   ├── isLabeledStatement.md
│           │   ├── isLineBreak.md
│           │   ├── isLiteralExpression.md
│           │   ├── isLiteralTypeNode.md
│           │   ├── isMappedTypeNode.md
│           │   ├── isMemberName.md
│           │   ├── isMetaProperty.md
│           │   ├── isMethodDeclaration.md
│           │   ├── isMethodSignature.md
│           │   ├── isMinusToken.md
│           │   ├── isMissingDeclaration.md
│           │   ├── isModifier.md
│           │   ├── isModifierLike.md
│           │   ├── isModuleBlock.md
│           │   ├── isModuleDeclaration.md
│           │   ├── isNamedExportBindings.md
│           │   ├── isNamedExports.md
│           │   ├── isNamedImports.md
│           │   ├── isNamedTupleMember.md
│           │   ├── isNamespaceExport.md
│           │   ├── isNamespaceExportDeclaration.md
│           │   ├── isNamespaceImport.md
│           │   ├── isNewExpression.md
│           │   ├── isNonNullChain.md
│           │   ├── isNonNullExpression.md
│           │   ├── isNoSubstitutionTemplateLiteral.md
│           │   ├── isNotEmittedStatement.md
│           │   ├── isNullishCoalesce.md
│           │   ├── isNumericLiteral.md
│           │   ├── isObjectBindingPattern.md
│           │   ├── isObjectLiteralElement.md
│           │   ├── isObjectLiteralElementLike.md
│           │   ├── isObjectLiteralExpression.md
│           │   ├── isOHModules.md
│           │   ├── isOHModulesDirectory.md
│           │   ├── isOhpm.md
│           │   ├── isOhpmAndOhModules.md
│           │   ├── isOmittedExpression.md
│           │   ├── isOptionalChain.md
│           │   ├── isOptionalTypeNode.md
│           │   ├── isParameter.md
│           │   ├── isParameterPropertyDeclaration.md
│           │   ├── isParenthesizedExpression.md
│           │   ├── isParenthesizedTypeNode.md
│           │   ├── isParseTreeNode.md
│           │   ├── isPartiallyEmittedExpression.md
│           │   ├── isPlusToken.md
│           │   ├── isPostfixUnaryExpression.md
│           │   ├── isPrefixUnaryExpression.md
│           │   ├── isPrivateIdentifier.md
│           │   ├── isPropertyAccessChain.md
│           │   ├── isPropertyAccessExpression.md
│           │   ├── isPropertyAccessOrQualifiedName.md
│           │   ├── isPropertyAssignment.md
│           │   ├── isPropertyDeclaration.md
│           │   ├── isPropertyName.md
│           │   ├── isPropertySignature.md
│           │   ├── isQualifiedName.md
│           │   ├── isRegularExpressionLiteral.md
│           │   ├── isRestParameter.md
│           │   ├── isRestTypeNode.md
│           │   ├── isReturnStatement.md
│           │   ├── isSatisfiesExpression.md
│           │   ├── isSemicolonClassElement.md
│           │   ├── isSetAccessor.md
│           │   ├── isSetAccessorDeclaration.md
│           │   ├── isShorthandPropertyAssignment.md
│           │   ├── isSourceFile.md
│           │   ├── isSpreadAssignment.md
│           │   ├── isSpreadElement.md
│           │   ├── isStringLiteral.md
│           │   ├── isStringLiteralLike.md
│           │   ├── isStringTextContainingNode.md
│           │   ├── isStruct.md
│           │   ├── isStructDeclaration.md
│           │   ├── isSwitchStatement.md
│           │   ├── isSyntheticExpression.md
│           │   ├── isTaggedTemplateExpression.md
│           │   ├── isTargetModulesDerectory.md
│           │   ├── isTemplateExpression.md
│           │   ├── isTemplateHead.md
│           │   ├── isTemplateLiteral.md
│           │   ├── isTemplateLiteralToken.md
│           │   ├── isTemplateLiteralTypeNode.md
│           │   ├── isTemplateLiteralTypeSpan.md
│           │   ├── isTemplateMiddle.md
│           │   ├── isTemplateMiddleOrTemplateTail.md
│           │   ├── isTemplateSpan.md
│           │   ├── isTemplateTail.md
│           │   ├── isThisTypeNode.md
│           │   ├── isThrowStatement.md
│           │   ├── isToken.md
│           │   ├── isTokenKind.md
│           │   ├── isTryStatement.md
│           │   ├── isTupleTypeNode.md
│           │   ├── isTypeAliasDeclaration.md
│           │   ├── isTypeAssertionExpression.md
│           │   ├── isTypeElement.md
│           │   ├── isTypeLiteralNode.md
│           │   ├── isTypeNode.md
│           │   ├── isTypeOfExpression.md
│           │   ├── isTypeOnlyImportOrExportDeclaration.md
│           │   ├── isTypeOperatorNode.md
│           │   ├── isTypeParameterDeclaration.md
│           │   ├── isTypePredicateNode.md
│           │   ├── isTypeQueryNode.md
│           │   ├── isTypeReferenceNode.md
│           │   ├── isUnionTypeNode.md
│           │   ├── isUnparsedNode.md
│           │   ├── isUnparsedPrepend.md
│           │   ├── isUnparsedSource.md
│           │   ├── isUnparsedTextLike.md
│           │   ├── isVariableDeclaration.md
│           │   ├── isVariableDeclarationList.md
│           │   ├── isVariableStatement.md
│           │   ├── isVoidExpression.md
│           │   ├── isWhileStatement.md
│           │   ├── isWhiteSpaceLike.md
│           │   ├── isWhiteSpaceSingleLine.md
│           │   ├── isWithStatement.md
│           │   ├── isYieldExpression.md
│           │   ├── moveEmitHelpers.md
│           │   ├── moveSyntheticComments.md
│           │   ├── nodeModuleNameResolver.md
│           │   ├── parseCommandLine.md
│           │   ├── parseConfigFileTextToJson.md
│           │   ├── parseIsolatedEntityName.md
│           │   ├── parseJsonConfigFileContent.md
│           │   ├── parseJsonSourceFileConfigFileContent.md
│           │   ├── parseJsonText.md
│           │   ├── parseModuleFromPath.md
│           │   ├── pathContainsOHModules.md
│           │   ├── preProcessFile.md
│           │   ├── readBuilderProgram.md
│           │   ├── readConfigFile.md
│           │   ├── readJsonConfigFile.md
│           │   ├── reduceEachLeadingCommentRange.md
│           │   ├── reduceEachTrailingCommentRange.md
│           │   ├── removeEmitHelper.md
│           │   ├── resolveModuleName.md
│           │   ├── resolveModuleNameFromCache.md
│           │   ├── resolveProjectReferencePath.md
│           │   ├── resolveTripleslashReference.md
│           │   ├── resolveTypeReferenceDirective.md
│           │   ├── setCommentRange.md
│           │   ├── setConstantValue.md
│           │   ├── setEmitFlags.md
│           │   ├── setOriginalNode.md
│           │   ├── setParentRecursive.md
│           │   ├── setSourceMapRange.md
│           │   ├── setSyntheticLeadingComments.md
│           │   ├── setSyntheticTrailingComments.md
│           │   ├── setTextRange.md
│           │   ├── setTokenSourceMapRange.md
│           │   ├── skipPartiallyEmittedExpressions.md
│           │   ├── sortAndDeduplicateDiagnostics.md
│           │   ├── symbolName.md
│           │   ├── textChangeRangeIsUnchanged.md
│           │   ├── textChangeRangeNewSpan.md
│           │   ├── textSpanContainsPosition.md
│           │   ├── textSpanContainsTextSpan.md
│           │   ├── textSpanEnd.md
│           │   ├── textSpanIntersection.md
│           │   ├── textSpanIntersectsWith.md
│           │   ├── textSpanIntersectsWithPosition.md
│           │   ├── textSpanIntersectsWithTextSpan.md
│           │   ├── textSpanIsEmpty.md
│           │   ├── textSpanOverlap.md
│           │   ├── textSpanOverlapsWith.md
│           │   ├── toEditorSettings.md
│           │   ├── tokenToString.md
│           │   ├── transform.md
│           │   ├── transformTypeExportImportAndConstEnumInTypeScript.md
│           │   ├── transpile.md
│           │   ├── transpileModule.md
│           │   ├── unescapeLeadingUnderscores.md
│           │   ├── updateLanguageServiceSourceFile.md
│           │   ├── updateSourceFile.md
│           │   ├── validateLocaleAndSetLanguage.md
│           │   ├── visitEachChild.md
│           │   ├── visitFunctionBody.md
│           │   ├── visitIterationBody.md
│           │   ├── visitLexicalEnvironment.md
│           │   ├── visitNode.md
│           │   ├── visitNodes.md
│           │   ├── visitParameterList.md
│           │   └── walkUpBindingElementsAndPatterns.md
│           ├── interfaces
│           │   ├── AmdDependency.md
│           │   ├── ApplicableRefactorInfo.md
│           │   ├── ApplyCodeActionCommandResult.md
│           │   ├── ArrayBindingPattern.md
│           │   ├── ArrayDestructuringAssignment.md
│           │   ├── ArrayLiteralExpression.md
│           │   ├── ArrayTypeNode.md
│           │   ├── ArrowFunction.md
│           │   ├── AsExpression.md
│           │   ├── AssertClause.md
│           │   ├── AssertEntry.md
│           │   ├── AssertsIdentifierTypePredicate.md
│           │   ├── AssertsThisTypePredicate.md
│           │   ├── AssignmentExpression.md
│           │   ├── AutoAccessorPropertyDeclaration.md
│           │   ├── AwaitExpression.md
│           │   ├── BigIntLiteral.md
│           │   ├── BigIntLiteralType.md
│           │   ├── BinaryExpression.md
│           │   ├── BindingElement.md
│           │   ├── Block.md
│           │   ├── BreakStatement.md
│           │   ├── BuilderProgram.md
│           │   ├── BuilderProgramHost.md
│           │   ├── BuildInvalidedProject.md
│           │   ├── BuildOptions.md
│           │   ├── Bundle.md
│           │   ├── CallChain.md
│           │   ├── CallExpression.md
│           │   ├── CallHierarchyIncomingCall.md
│           │   ├── CallHierarchyItem.md
│           │   ├── CallHierarchyOutgoingCall.md
│           │   ├── CallSignatureDeclaration.md
│           │   ├── CancellationToken.md
│           │   ├── CaseBlock.md
│           │   ├── CaseClause.md
│           │   ├── CatchClause.md
│           │   ├── CheckJsDirective.md
│           │   ├── ClassDeclaration.md
│           │   ├── ClassElement.md
│           │   ├── ClassExpression.md
│           │   ├── ClassificationInfo.md
│           │   ├── ClassificationResult.md
│           │   ├── Classifications.md
│           │   ├── ClassifiedSpan.md
│           │   ├── ClassifiedSpan2020.md
│           │   ├── Classifier.md
│           │   ├── ClassLikeDeclarationBase.md
│           │   ├── ClassStaticBlockDeclaration.md
│           │   ├── CodeAction.md
│           │   ├── CodeFixAction.md
│           │   ├── Collection.md
│           │   ├── CombinedCodeActions.md
│           │   ├── CombinedCodeFixScope.md
│           │   ├── CommaListExpression.md
│           │   ├── CommentRange.md
│           │   ├── CompilerHost.md
│           │   ├── CompilerOptions.md
│           │   ├── CompletionEntry.md
│           │   ├── CompletionEntryDataAutoImport.md
│           │   ├── CompletionEntryDataResolved.md
│           │   ├── CompletionEntryDataUnresolved.md
│           │   ├── CompletionEntryDetails.md
│           │   ├── CompletionEntryLabelDetails.md
│           │   ├── CompletionInfo.md
│           │   ├── ComputedPropertyName.md
│           │   ├── ConditionalExpression.md
│           │   ├── ConditionalRoot.md
│           │   ├── ConditionalType.md
│           │   ├── ConditionalTypeNode.md
│           │   ├── ConditionCheckResult.md
│           │   ├── ConfigFileDiagnosticsReporter.md
│           │   ├── ConstructorDeclaration.md
│           │   ├── ConstructorTypeNode.md
│           │   ├── ConstructSignatureDeclaration.md
│           │   ├── ContinueStatement.md
│           │   ├── CoreTransformationContext.md
│           │   ├── CreateProgramOptions.md
│           │   ├── CreateSourceFileOptions.md
│           │   ├── CustomTransformer.md
│           │   ├── CustomTransformers.md
│           │   ├── DebuggerStatement.md
│           │   ├── Declaration.md
│           │   ├── DeclarationStatement.md
│           │   ├── Decorator.md
│           │   ├── DefaultClause.md
│           │   ├── DeferredTypeReference.md
│           │   ├── DefinitionInfo.md
│           │   ├── DefinitionInfoAndBoundSpan.md
│           │   ├── DeleteExpression.md
│           │   ├── Diagnostic.md
│           │   ├── DiagnosticMessage.md
│           │   ├── DiagnosticMessageChain.md
│           │   ├── DiagnosticRelatedInformation.md
│           │   ├── DiagnosticWithLocation.md
│           │   ├── DocCommentTemplateOptions.md
│           │   ├── DocumentHighlights.md
│           │   ├── DocumentRegistry.md
│           │   ├── DocumentSpan.md
│           │   ├── DoStatement.md
│           │   ├── EditorOptions.md
│           │   ├── EditorSettings.md
│           │   ├── ElementAccessChain.md
│           │   ├── ElementAccessExpression.md
│           │   ├── EmitAndSemanticDiagnosticsBuilderProgram.md
│           │   ├── EmitHelperBase.md
│           │   ├── EmitHost.md
│           │   ├── EmitOutput.md
│           │   ├── EmitResult.md
│           │   ├── EmitTextWriter.md
│           │   ├── EmptyStatement.md
│           │   ├── EnumDeclaration.md
│           │   ├── EnumMember.md
│           │   ├── EnumType.md
│           │   ├── ESMap.md
│           │   ├── EtsComponentExpression.md
│           │   ├── EtsOptions.md
│           │   ├── EvolvingArrayType.md
│           │   ├── ExportAssignment.md
│           │   ├── ExportDeclaration.md
│           │   ├── ExportSpecifier.md
│           │   ├── Expression.md
│           │   ├── ExpressionStatement.md
│           │   ├── ExpressionWithTypeArguments.md
│           │   ├── ExtendedConfigCacheEntry.md
│           │   ├── ExternalModuleReference.md
│           │   ├── FalseLiteral.md
│           │   ├── FileCheckModuleInfo.md
│           │   ├── FileExtensionInfo.md
│           │   ├── FileReference.md
│           │   ├── FileTextChanges.md
│           │   ├── FileWatcher.md
│           │   ├── FlowArrayMutation.md
│           │   ├── FlowAssignment.md
│           │   ├── FlowCall.md
│           │   ├── FlowCondition.md
│           │   ├── FlowLabel.md
│           │   ├── FlowNodeBase.md
│           │   ├── FlowReduceLabel.md
│           │   ├── FlowStart.md
│           │   ├── FlowSwitchClause.md
│           │   ├── ForInStatement.md
│           │   ├── FormatCodeOptions.md
│           │   ├── FormatCodeSettings.md
│           │   ├── FormatDiagnosticsHost.md
│           │   ├── ForOfStatement.md
│           │   ├── ForStatement.md
│           │   ├── FunctionDeclaration.md
│           │   ├── FunctionExpression.md
│           │   ├── FunctionLikeDeclarationBase.md
│           │   ├── FunctionOrConstructorTypeNodeBase.md
│           │   ├── FunctionTypeNode.md
│           │   ├── GenericType.md
│           │   ├── GetAccessorDeclaration.md
│           │   ├── GetCompletionsAtPositionOptions.md
│           │   ├── GetEffectiveTypeRootsHost.md
│           │   ├── HeritageClause.md
│           │   ├── HighlightSpan.md
│           │   ├── HostCancellationToken.md
│           │   ├── Identifier.md
│           │   ├── IdentifierTypePredicate.md
│           │   ├── IfStatement.md
│           │   ├── ImplementationLocation.md
│           │   ├── ImportCall.md
│           │   ├── ImportClause.md
│           │   ├── ImportDeclaration.md
│           │   ├── ImportEqualsDeclaration.md
│           │   ├── ImportExpression.md
│           │   ├── ImportSpecifier.md
│           │   ├── ImportTypeAssertionContainer.md
│           │   ├── ImportTypeNode.md
│           │   ├── IncompleteCompletionsCache.md
│           │   ├── IncompleteType.md
│           │   ├── IncrementalProgramOptions.md
│           │   ├── IndexedAccessType.md
│           │   ├── IndexedAccessTypeNode.md
│           │   ├── IndexInfo.md
│           │   ├── IndexSignatureDeclaration.md
│           │   ├── IndexType.md
│           │   ├── InferTypeNode.md
│           │   ├── InlayHint.md
│           │   ├── InlayHintsContext.md
│           │   ├── InputFiles.md
│           │   ├── InstallPackageAction.md
│           │   ├── InstallPackageOptions.md
│           │   ├── InstantiableType.md
│           │   ├── InterfaceDeclaration.md
│           │   ├── InterfaceType.md
│           │   ├── InterfaceTypeWithDeclaredMembers.md
│           │   ├── IntersectionType.md
│           │   ├── IntersectionTypeNode.md
│           │   ├── InvalidatedProjectBase.md
│           │   ├── IScriptSnapshot.md
│           │   ├── IterationStatement.md
│           │   ├── Iterator.md
│           │   ├── JSDoc.md
│           │   ├── JSDocAllType.md
│           │   ├── JSDocAugmentsTag.md
│           │   ├── JSDocAuthorTag.md
│           │   ├── JSDocCallbackTag.md
│           │   ├── JSDocClassTag.md
│           │   ├── JSDocContainer.md
│           │   ├── JSDocDeprecatedTag.md
│           │   ├── JSDocEnumTag.md
│           │   ├── JSDocFunctionType.md
│           │   ├── JSDocImplementsTag.md
│           │   ├── JSDocLink.md
│           │   ├── JSDocLinkCode.md
│           │   ├── JSDocLinkDisplayPart.md
│           │   ├── JSDocLinkPlain.md
│           │   ├── JSDocMemberName.md
│           │   ├── JSDocNamepathType.md
│           │   ├── JSDocNameReference.md
│           │   ├── JSDocNamespaceDeclaration.md
│           │   ├── JsDocNodeCheckConfig.md
│           │   ├── JsDocNodeCheckConfigItem.md
│           │   ├── JSDocNonNullableType.md
│           │   ├── JSDocNullableType.md
│           │   ├── JSDocOptionalType.md
│           │   ├── JSDocOverrideTag.md
│           │   ├── JSDocParameterTag.md
│           │   ├── JSDocPrivateTag.md
│           │   ├── JSDocPropertyLikeTag.md
│           │   ├── JSDocPropertyTag.md
│           │   ├── JSDocProtectedTag.md
│           │   ├── JSDocPublicTag.md
│           │   ├── JSDocReadonlyTag.md
│           │   ├── JSDocReturnTag.md
│           │   ├── JSDocSeeTag.md
│           │   ├── JSDocSignature.md
│           │   ├── JSDocTag.md
│           │   ├── JSDocTagInfo-1.md
│           │   ├── JsDocTagInfo.md
│           │   ├── JSDocTemplateTag.md
│           │   ├── JSDocText.md
│           │   ├── JSDocThisTag.md
│           │   ├── JSDocType.md
│           │   ├── JSDocTypedefTag.md
│           │   ├── JSDocTypeExpression.md
│           │   ├── JSDocTypeLiteral.md
│           │   ├── JSDocTypeTag.md
│           │   ├── JSDocUnknownTag.md
│           │   ├── JSDocUnknownType.md
│           │   ├── JSDocVariadicType.md
│           │   ├── JsonMinusNumericLiteral.md
│           │   ├── JsonObjectExpressionStatement.md
│           │   ├── JsonSourceFile.md
│           │   ├── JsxAttribute.md
│           │   ├── JsxAttributes.md
│           │   ├── JsxClosingElement.md
│           │   ├── JsxClosingFragment.md
│           │   ├── JsxClosingTagInfo.md
│           │   ├── JsxElement.md
│           │   ├── JsxExpression.md
│           │   ├── JsxFragment.md
│           │   ├── JsxOpeningElement.md
│           │   ├── JsxOpeningFragment.md
│           │   ├── JsxSelfClosingElement.md
│           │   ├── JsxSpreadAttribute.md
│           │   ├── JsxTagNamePropertyAccess.md
│           │   ├── JsxText.md
│           │   ├── KeywordToken.md
│           │   ├── KeywordTypeNode.md
│           │   ├── LabeledStatement.md
│           │   ├── LanguageService.md
│           │   ├── LanguageServiceHost.md
│           │   ├── LeftHandSideExpression.md
│           │   ├── LineAndCharacter.md
│           │   ├── LiteralExpression.md
│           │   ├── LiteralLikeNode.md
│           │   ├── LiteralType.md
│           │   ├── LiteralTypeNode.md
│           │   ├── Map.md
│           │   ├── MapLike.md
│           │   ├── MappedTypeNode.md
│           │   ├── MemberExpression.md
│           │   ├── MetaProperty.md
│           │   ├── MethodDeclaration.md
│           │   ├── MethodSignature.md
│           │   ├── MinimalResolutionCacheHost.md
│           │   ├── MissingDeclaration.md
│           │   ├── ModeAwareCache.md
│           │   ├── ModifierToken.md
│           │   ├── ModuleBlock.md
│           │   ├── ModuleDeclaration.md
│           │   ├── ModulePath.md
│           │   ├── ModuleResolutionCache.md
│           │   ├── ModuleResolutionHost.md
│           │   ├── ModuleSpecifierCache.md
│           │   ├── ModuleSpecifierOptions.md
│           │   ├── ModuleSpecifierResolutionHost.md
│           │   ├── NamedDeclaration.md
│           │   ├── NamedExports.md
│           │   ├── NamedImports.md
│           │   ├── NamedTupleMember.md
│           │   ├── NamespaceDeclaration.md
│           │   ├── NamespaceExport.md
│           │   ├── NamespaceExportDeclaration.md
│           │   ├── NamespaceImport.md
│           │   ├── NavigateToItem.md
│           │   ├── NavigationBarItem.md
│           │   ├── NavigationTree.md
│           │   ├── NewExpression.md
│           │   ├── Node.md
│           │   ├── NodeArray.md
│           │   ├── NodeFactory.md
│           │   ├── NodesVisitor.md
│           │   ├── NodeVisitor.md
│           │   ├── NodeWithTypeArguments.md
│           │   ├── NonNullChain.md
│           │   ├── NonNullExpression.md
│           │   ├── NonRelativeModuleNameResolutionCache.md
│           │   ├── NoSubstitutionTemplateLiteral.md
│           │   ├── NotEmittedStatement.md
│           │   ├── NullLiteral.md
│           │   ├── NumberLiteralType.md
│           │   ├── NumericLiteral.md
│           │   ├── ObjectBindingPattern.md
│           │   ├── ObjectDestructuringAssignment.md
│           │   ├── ObjectLiteralElement.md
│           │   ├── ObjectLiteralExpression.md
│           │   ├── ObjectLiteralExpressionBase.md
│           │   ├── ObjectType.md
│           │   ├── OmittedExpression.md
│           │   ├── OptionalTypeNode.md
│           │   ├── OrganizeImportsArgs.md
│           │   ├── OutliningSpan.md
│           │   ├── OutputFile.md
│           │   ├── PackageId.md
│           │   ├── PackageJsonInfoCache.md
│           │   ├── ParameterDeclaration.md
│           │   ├── ParenthesizedExpression.md
│           │   ├── ParenthesizedTypeNode.md
│           │   ├── ParseConfigFileHost.md
│           │   ├── ParseConfigHost.md
│           │   ├── ParsedCommandLine.md
│           │   ├── ParsedTsconfig.md
│           │   ├── PartiallyEmittedExpression.md
│           │   ├── PerDirectoryResolutionCache.md
│           │   ├── PerformanceEvent.md
│           │   ├── PerModuleNameCache.md
│           │   ├── PluginImport.md
│           │   ├── PostfixUnaryExpression.md
│           │   ├── PrefixUnaryExpression.md
│           │   ├── PreProcessedFileInfo.md
│           │   ├── PrimaryExpression.md
│           │   ├── Printer.md
│           │   ├── PrinterOptions.md
│           │   ├── PrintHandlers.md
│           │   ├── PrivateIdentifier.md
│           │   ├── Program.md
│           │   ├── ProgramHost.md
│           │   ├── ProjectReference.md
│           │   ├── PropertyAccessChain.md
│           │   ├── PropertyAccessEntityNameExpression.md
│           │   ├── PropertyAccessExpression.md
│           │   ├── PropertyAssignment.md
│           │   ├── PropertyDeclaration.md
│           │   ├── PropertyLikeDeclaration.md
│           │   ├── PropertySignature.md
│           │   ├── PseudoBigInt.md
│           │   ├── PunctuationToken.md
│           │   ├── Push.md
│           │   ├── QualifiedName.md
│           │   ├── QuickInfo.md
│           │   ├── RawSourceMap.md
│           │   ├── ReadBuildProgramHost.md
│           │   ├── ReadonlyCollection.md
│           │   ├── ReadonlyESMap.md
│           │   ├── ReadonlyMap.md
│           │   ├── ReadonlySet.md
│           │   ├── ReadonlyTextRange.md
│           │   ├── ReadonlyUnderscoreEscapedMap.md
│           │   ├── RefactorActionInfo.md
│           │   ├── RefactorEditInfo.md
│           │   ├── ReferencedSymbol.md
│           │   ├── ReferencedSymbolDefinitionInfo.md
│           │   ├── ReferencedSymbolEntry.md
│           │   ├── ReferenceEntry.md
│           │   ├── RegularExpressionLiteral.md
│           │   ├── RenameInfoFailure.md
│           │   ├── RenameInfoOptions.md
│           │   ├── RenameInfoSuccess.md
│           │   ├── RenameLocation.md
│           │   ├── ReportFileInError.md
│           │   ├── ResolvedModule.md
│           │   ├── ResolvedModuleFull.md
│           │   ├── ResolvedModuleSpecifierInfo.md
│           │   ├── ResolvedModuleWithFailedLookupLocations.md
│           │   ├── ResolvedProjectReference.md
│           │   ├── ResolvedTypeReferenceDirective.md
│           │   ├── ResolvedTypeReferenceDirectiveWithFailedLookupLocations.md
│           │   ├── ResolveProjectReferencePathHost.md
│           │   ├── RestTypeNode.md
│           │   ├── ReturnStatement.md
│           │   ├── SatisfiesExpression.md
│           │   ├── Scanner.md
│           │   ├── ScopedEmitHelper.md
│           │   ├── ScriptReferenceHost.md
│           │   ├── SelectionRange.md
│           │   ├── SemanticDiagnosticsBuilderProgram.md
│           │   ├── SemicolonClassElement.md
│           │   ├── Set.md
│           │   ├── SetAccessorDeclaration.md
│           │   ├── ShorthandPropertyAssignment.md
│           │   ├── Signature.md
│           │   ├── SignatureDeclarationBase.md
│           │   ├── SignatureHelpCharacterTypedReason.md
│           │   ├── SignatureHelpInvokedReason.md
│           │   ├── SignatureHelpItem.md
│           │   ├── SignatureHelpItems.md
│           │   ├── SignatureHelpItemsOptions.md
│           │   ├── SignatureHelpParameter.md
│           │   ├── SignatureHelpRetriggeredReason.md
│           │   ├── SolutionBuilder.md
│           │   ├── SolutionBuilderHost.md
│           │   ├── SolutionBuilderHostBase.md
│           │   ├── SolutionBuilderWithWatchHost.md
│           │   ├── SortedArray.md
│           │   ├── SortedReadonlyArray.md
│           │   ├── SourceFile.md
│           │   ├── SourceFileLike.md
│           │   ├── SourceFileMayBeEmittedHost.md
│           │   ├── SourceMapGenerator.md
│           │   ├── SourceMapGeneratorOptions.md
│           │   ├── SourceMapRange.md
│           │   ├── SourceMapSource.md
│           │   ├── SourceMapSpan.md
│           │   ├── SpreadAssignment.md
│           │   ├── SpreadElement.md
│           │   ├── Statement.md
│           │   ├── StringLiteral.md
│           │   ├── StringLiteralType.md
│           │   ├── StringMappingType.md
│           │   ├── StructDeclaration.md
│           │   ├── SubstitutionType.md
│           │   ├── SuperCall.md
│           │   ├── SuperElementAccessExpression.md
│           │   ├── SuperExpression.md
│           │   ├── SuperPropertyAccessExpression.md
│           │   ├── SwitchStatement.md
│           │   ├── Symbol.md
│           │   ├── SymbolDisplayPart.md
│           │   ├── SymbolTracker.md
│           │   ├── SyntaxList.md
│           │   ├── SynthesizedComment.md
│           │   ├── SyntheticExpression.md
│           │   ├── System.md
│           │   ├── TagCheckConfig.md
│           │   ├── TagCheckParam.md
│           │   ├── TaggedTemplateExpression.md
│           │   ├── TemplateExpression.md
│           │   ├── TemplateHead.md
│           │   ├── TemplateLiteralLikeNode.md
│           │   ├── TemplateLiteralType.md
│           │   ├── TemplateLiteralTypeNode.md
│           │   ├── TemplateLiteralTypeSpan.md
│           │   ├── TemplateMiddle.md
│           │   ├── TemplateSpan.md
│           │   ├── TemplateTail.md
│           │   ├── TextChange.md
│           │   ├── TextChangeRange.md
│           │   ├── TextInsertion.md
│           │   ├── TextRange.md
│           │   ├── TextSpan.md
│           │   ├── ThisExpression.md
│           │   ├── ThisTypeNode.md
│           │   ├── ThisTypePredicate.md
│           │   ├── ThrowStatement.md
│           │   ├── TodoComment.md
│           │   ├── TodoCommentDescriptor.md
│           │   ├── Token.md
│           │   ├── TransformationContext.md
│           │   ├── TransformationResult.md
│           │   ├── TransientIdentifier.md
│           │   ├── TranspileOptions.md
│           │   ├── TranspileOutput.md
│           │   ├── TrueLiteral.md
│           │   ├── TryStatement.md
│           │   ├── TsConfigSourceFile.md
│           │   ├── TupleType.md
│           │   ├── TupleTypeNode.md
│           │   ├── TupleTypeReference.md
│           │   ├── Type.md
│           │   ├── TypeAcquisition.md
│           │   ├── TypeAliasDeclaration.md
│           │   ├── TypeAssertion.md
│           │   ├── TypeChecker.md
│           │   ├── TypeElement.md
│           │   ├── TypeLiteralNode.md
│           │   ├── TypeNode.md
│           │   ├── TypeOfExpression.md
│           │   ├── TypeOperatorNode.md
│           │   ├── TypeParameter.md
│           │   ├── TypeParameterDeclaration.md
│           │   ├── TypePredicateBase.md
│           │   ├── TypePredicateNode.md
│           │   ├── TypeQueryNode.md
│           │   ├── TypeReference.md
│           │   ├── TypeReferenceDirectiveResolutionCache.md
│           │   ├── TypeReferenceNode.md
│           │   ├── UnaryExpression.md
│           │   ├── UnderscoreEscapedMap.md
│           │   ├── UnionOrIntersectionType.md
│           │   ├── UnionType.md
│           │   ├── UnionTypeNode.md
│           │   ├── UniqueESSymbolType.md
│           │   ├── UnparsedPrepend.md
│           │   ├── UnparsedPrologue.md
│           │   ├── UnparsedSection.md
│           │   ├── UnparsedSource.md
│           │   ├── UnparsedSyntheticReference.md
│           │   ├── UnparsedTextLike.md
│           │   ├── UnscopedEmitHelper.md
│           │   ├── UpdateBundleProject.md
│           │   ├── UpdateExpression.md
│           │   ├── UpdateOutputFileStampsProject.md
│           │   ├── UserPreferences.md
│           │   ├── VariableDeclaration.md
│           │   ├── VariableDeclarationList.md
│           │   ├── VariableStatement.md
│           │   ├── VoidExpression.md
│           │   ├── Watch.md
│           │   ├── WatchCompilerHost.md
│           │   ├── WatchCompilerHostOfConfigFile.md
│           │   ├── WatchCompilerHostOfFilesAndCompilerOptions.md
│           │   ├── WatchHost.md
│           │   ├── WatchOfConfigFile.md
│           │   ├── WatchOfFilesAndCompilerOptions.md
│           │   ├── WatchOptions.md
│           │   ├── WhileStatement.md
│           │   ├── WithStatement.md
│           │   ├── WriteFileCallbackData.md
│           │   └── YieldExpression.md
│           ├── namespaces
│           │   ├── ArkTSLinter_1_0
│           │   │   ├── classes
│           │   │   │   ├── LinterConfig.md
│           │   │   │   ├── TSCCompiledProgram.md
│           │   │   │   └── TypeScriptLinter.md
│           │   │   ├── functions
│           │   │   │   ├── runArkTSLinter.md
│           │   │   │   └── translateDiag.md
│           │   │   ├── interfaces
│           │   │   │   └── ProblemInfo.md
│           │   │   ├── namespaces
│           │   │   │   ├── Autofixer
│           │   │   │   │   ├── functions
│           │   │   │   │   │   ├── fixCtorParameterProperties.md
│           │   │   │   │   │   ├── fixFunctionExpression.md
│           │   │   │   │   │   ├── fixLiteralAsPropertyName.md
│           │   │   │   │   │   ├── fixPropertyAccessByIndex.md
│           │   │   │   │   │   ├── fixReturnType.md
│           │   │   │   │   │   └── shouldAutofix.md
│           │   │   │   │   ├── interfaces
│           │   │   │   │   │   └── Autofix.md
│           │   │   │   │   ├── README.md
│           │   │   │   │   └── variables
│           │   │   │   │       ├── AUTOFIX_ALL.md
│           │   │   │   │       └── autofixInfo.md
│           │   │   │   ├── Common
│           │   │   │   │   ├── interfaces
│           │   │   │   │   │   ├── AutofixInfo.md
│           │   │   │   │   │   ├── CommandLineOptions.md
│           │   │   │   │   │   └── LintOptions.md
│           │   │   │   │   └── README.md
│           │   │   │   ├── DiagnosticCheckerNamespace
│           │   │   │   │   ├── interfaces
│           │   │   │   │   │   └── DiagnosticChecker.md
│           │   │   │   │   └── README.md
│           │   │   │   ├── LibraryTypeCallDiagnosticCheckerNamespace
│           │   │   │   │   ├── classes
│           │   │   │   │   │   └── LibraryTypeCallDiagnosticChecker.md
│           │   │   │   │   ├── README.md
│           │   │   │   │   └── variables
│           │   │   │   │       ├── ARGUMENT_OF_TYPE_0_IS_NOT_ASSIGNABLE_TO_PARAMETER_OF_TYPE_1_ERROR_CODE.md
│           │   │   │   │       ├── ARGUMENT_OF_TYPE_NULL_IS_NOT_ASSIGNABLE_TO_PARAMETER_OF_TYPE_1_RE.md
│           │   │   │   │       ├── ARGUMENT_OF_TYPE_UNDEFINED_IS_NOT_ASSIGNABLE_TO_PARAMETER_OF_TYPE_1_RE.md
│           │   │   │   │       ├── NO_OVERLOAD_MATCHES_THIS_CALL_ERROR_CODE.md
│           │   │   │   │       ├── TYPE_0_IS_NOT_ASSIGNABLE_TO_TYPE_1_ERROR_CODE.md
│           │   │   │   │       ├── TYPE_NULL_IS_NOT_ASSIGNABLE_TO_TYPE_1_RE.md
│           │   │   │   │       ├── TYPE_UNDEFINED_IS_NOT_ASSIGNABLE_TO_TYPE_1_RE.md
│           │   │   │   │       └── TYPE_UNKNOWN_IS_NOT_ASSIGNABLE_TO_TYPE_1_RE.md
│           │   │   │   ├── Problems
│           │   │   │   │   ├── classes
│           │   │   │   │   │   └── FaultAttributs.md
│           │   │   │   │   ├── enumerations
│           │   │   │   │   │   └── FaultID.md
│           │   │   │   │   ├── README.md
│           │   │   │   │   └── variables
│           │   │   │   │       └── faultsAttrs.md
│           │   │   │   └── Utils
│           │   │   │       ├── enumerations
│           │   │   │       │   ├── CheckType.md
│           │   │   │       │   └── ProblemSeverity.md
│           │   │   │       ├── functions
│           │   │   │       │   ├── clearTrueSymbolAtLocationCache.md
│           │   │   │       │   ├── clearTypeChecker.md
│           │   │   │       │   ├── decodeAutofixInfo.md
│           │   │   │       │   ├── encodeProblemInfo.md
│           │   │   │       │   ├── entityNameToString.md
│           │   │   │       │   ├── findParentIf.md
│           │   │   │       │   ├── followIfAliased.md
│           │   │   │       │   ├── getAccessModifier.md
│           │   │   │       │   ├── getDeclaration.md
│           │   │   │       │   ├── getEndPos.md
│           │   │   │       │   ├── getModifier.md
│           │   │   │       │   ├── getParentSymbolName.md
│           │   │   │       │   ├── getScriptKind.md
│           │   │   │       │   ├── getStartPos.md
│           │   │   │       │   ├── getSymbolDeclarationTypeNode.md
│           │   │   │       │   ├── getSymbolOfCallExpression.md
│           │   │   │       │   ├── getVariableDeclarationTypeNode.md
│           │   │   │       │   ├── hasAccessModifier.md
│           │   │   │       │   ├── hasEsObjectType.md
│           │   │   │       │   ├── hasLibraryType.md
│           │   │   │       │   ├── hasMethods.md
│           │   │   │       │   ├── hasModifier.md
│           │   │   │       │   ├── hasPredecessor.md
│           │   │   │       │   ├── isAnonymousType.md
│           │   │   │       │   ├── isAnyType.md
│           │   │   │       │   ├── isAssignmentOperator.md
│           │   │   │       │   ├── isBooleanType.md
│           │   │   │       │   ├── isCallToFunctionWithOmittedReturnType.md
│           │   │   │       │   ├── isCompileTimeExpression.md
│           │   │   │       │   ├── isConst.md
│           │   │   │       │   ├── isDefaultImport.md
│           │   │   │       │   ├── isDerivedFrom.md
│           │   │   │       │   ├── isDestructuringAssignmentLHS.md
│           │   │   │       │   ├── isDynamicLiteralInitializer.md
│           │   │   │       │   ├── isDynamicType.md
│           │   │   │       │   ├── isEnumMemberType.md
│           │   │   │       │   ├── isEnumType.md
│           │   │   │       │   ├── isEsObjectPossiblyAllowed.md
│           │   │   │       │   ├── isEsObjectSymbol.md
│           │   │   │       │   ├── isEsObjectType.md
│           │   │   │       │   ├── isExpressionAssignableToType.md
│           │   │   │       │   ├── isFunctionOrMethod.md
│           │   │   │       │   ├── isFunctionSymbol.md
│           │   │   │       │   ├── isGenericArrayType.md
│           │   │   │       │   ├── isGlobalSymbol.md
│           │   │   │       │   ├── isInsideBlock.md
│           │   │   │       │   ├── isIntegerConstantValue.md
│           │   │   │       │   ├── isInterfaceType.md
│           │   │   │       │   ├── isIntrinsicObjectType.md
│           │   │   │       │   ├── isLibrarySymbol.md
│           │   │   │       │   ├── isLibraryType.md
│           │   │   │       │   ├── isLiteralType.md
│           │   │   │       │   ├── isMethodAssignment.md
│           │   │   │       │   ├── isNullType.md
│           │   │   │       │   ├── isNumberConstantValue.md
│           │   │   │       │   ├── isNumberLikeType.md
│           │   │   │       │   ├── isNumberType.md
│           │   │   │       │   ├── isObjectLiteralType.md
│           │   │   │       │   ├── isObjectType.md
│           │   │   │       │   ├── isPrimitiveEnumMemberType.md
│           │   │   │       │   ├── isPrimitiveEnumType.md
│           │   │   │       │   ├── isPrimitiveType.md
│           │   │   │       │   ├── isPrototypeSymbol.md
│           │   │   │       │   ├── isReferenceType.md
│           │   │   │       │   ├── isStdLibrarySymbol.md
│           │   │   │       │   ├── isStdLibraryType.md
│           │   │   │       │   ├── isStdPartialType.md
│           │   │   │       │   ├── isStdReadonlyType.md
│           │   │   │       │   ├── isStdRecordType.md
│           │   │   │       │   ├── isStdRequiredType.md
│           │   │   │       │   ├── isStdSymbol.md
│           │   │   │       │   ├── isStringConstantValue.md
│           │   │   │       │   ├── isStringLikeType.md
│           │   │   │       │   ├── isStringType.md
│           │   │   │       │   ├── isStruct.md
│           │   │   │       │   ├── isStructDeclaration.md
│           │   │   │       │   ├── isStructDeclarationKind.md
│           │   │   │       │   ├── isStructObjectInitializer.md
│           │   │   │       │   ├── isSupportedType.md
│           │   │   │       │   ├── isSymbolAPI.md
│           │   │   │       │   ├── isSymbolIterator.md
│           │   │   │       │   ├── isThisOrSuperExpr.md
│           │   │   │       │   ├── isType.md
│           │   │   │       │   ├── isTypedArray.md
│           │   │   │       │   ├── isTypeDeclSyntaxKind.md
│           │   │   │       │   ├── isTypeReference.md
│           │   │   │       │   ├── isTypeSymbol.md
│           │   │   │       │   ├── isUnknownType.md
│           │   │   │       │   ├── isUnsupportedType.md
│           │   │   │       │   ├── isUnsupportedUnionType.md
│           │   │   │       │   ├── isValidEnumMemberInit.md
│           │   │   │       │   ├── isValueAssignableToESObject.md
│           │   │   │       │   ├── logTscDiagnostic.md
│           │   │   │       │   ├── needToDeduceStructuralIdentity.md
│           │   │   │       │   ├── pathContainsDirectory.md
│           │   │   │       │   ├── processParentTypes.md
│           │   │   │       │   ├── processParentTypesCheck.md
│           │   │   │       │   ├── relatedByInheritanceOrIdentical.md
│           │   │   │       │   ├── setTestMode.md
│           │   │   │       │   ├── setTypeChecker.md
│           │   │   │       │   ├── symbolHasDuplicateName.md
│           │   │   │       │   ├── symbolHasEsObjectType.md
│           │   │   │       │   ├── trueSymbolAtLocation.md
│           │   │   │       │   ├── typeIsRecursive.md
│           │   │   │       │   ├── unwrapParenthesized.md
│           │   │   │       │   ├── unwrapParenthesizedType.md
│           │   │   │       │   ├── validateFields.md
│           │   │   │       │   └── validateObjectLiteralType.md
│           │   │   │       ├── README.md
│           │   │   │       └── variables
│           │   │   │           ├── ALLOWED_STD_SYMBOL_API.md
│           │   │   │           ├── ARKTS_IGNORE_DIRS.md
│           │   │   │           ├── ARKTS_IGNORE_FILES.md
│           │   │   │           ├── ARKUI_DECORATORS.md
│           │   │   │           ├── ES_OBJECT.md
│           │   │   │           ├── FUNCTION_HAS_NO_RETURN_ERROR_CODE.md
│           │   │   │           ├── LIMITED_STANDARD_UTILITY_TYPES.md
│           │   │   │           ├── LIMITED_STD_GLOBAL_FUNC.md
│           │   │   │           ├── LIMITED_STD_OBJECT_API.md
│           │   │   │           ├── LIMITED_STD_PROXYHANDLER_API.md
│           │   │   │           ├── LIMITED_STD_REFLECT_API.md
│           │   │   │           ├── NON_INITIALIZABLE_PROPERTY_ClASS_DECORATORS.md
│           │   │   │           ├── NON_INITIALIZABLE_PROPERTY_DECORATORS.md
│           │   │   │           ├── NON_RETURN_FUNCTION_DECORATORS.md
│           │   │   │           ├── PROPERTY_HAS_NO_INITIALIZER_ERROR_CODE.md
│           │   │   │           ├── STANDARD_LIBRARIES.md
│           │   │   │           └── TYPED_ARRAYS.md
│           │   │   ├── README.md
│           │   │   └── variables
│           │   │       ├── cookBookMsg.md
│           │   │       └── cookBookTag.md
│           │   ├── ArkTSLinter_1_1
│           │   │   ├── classes
│           │   │   │   ├── InteropTypescriptLinter.md
│           │   │   │   ├── LinterConfig.md
│           │   │   │   ├── TSCCompiledProgram.md
│           │   │   │   └── TypeScriptLinter.md
│           │   │   ├── functions
│           │   │   │   ├── runArkTSLinter.md
│           │   │   │   └── translateDiag.md
│           │   │   ├── interfaces
│           │   │   │   ├── KitInfo.md
│           │   │   │   ├── KitSymbol.md
│           │   │   │   └── ProblemInfo.md
│           │   │   ├── namespaces
│           │   │   │   ├── Autofixer
│           │   │   │   │   ├── functions
│           │   │   │   │   │   ├── fixCtorParameterProperties.md
│           │   │   │   │   │   ├── fixFunctionExpression.md
│           │   │   │   │   │   ├── fixLiteralAsPropertyName.md
│           │   │   │   │   │   ├── fixPropertyAccessByIndex.md
│           │   │   │   │   │   ├── fixReturnType.md
│           │   │   │   │   │   └── shouldAutofix.md
│           │   │   │   │   ├── interfaces
│           │   │   │   │   │   └── Autofix.md
│           │   │   │   │   ├── README.md
│           │   │   │   │   └── variables
│           │   │   │   │       ├── AUTOFIX_ALL.md
│           │   │   │   │       └── autofixInfo.md
│           │   │   │   ├── Common
│           │   │   │   │   ├── enumerations
│           │   │   │   │   │   └── ProblemSeverity.md
│           │   │   │   │   ├── interfaces
│           │   │   │   │   │   ├── AutofixInfo.md
│           │   │   │   │   │   ├── CommandLineOptions.md
│           │   │   │   │   │   └── LintOptions.md
│           │   │   │   │   └── README.md
│           │   │   │   ├── DiagnosticCheckerNamespace
│           │   │   │   │   ├── interfaces
│           │   │   │   │   │   └── DiagnosticChecker.md
│           │   │   │   │   └── README.md
│           │   │   │   ├── LibraryTypeCallDiagnosticCheckerNamespace
│           │   │   │   │   ├── classes
│           │   │   │   │   │   └── LibraryTypeCallDiagnosticChecker.md
│           │   │   │   │   ├── enumerations
│           │   │   │   │   │   └── ErrorType.md
│           │   │   │   │   ├── README.md
│           │   │   │   │   └── variables
│           │   │   │   │       ├── ARGUMENT_OF_TYPE_0_IS_NOT_ASSIGNABLE_TO_PARAMETER_OF_TYPE_1_ERROR_CODE.md
│           │   │   │   │       ├── ARGUMENT_OF_TYPE_NULL_IS_NOT_ASSIGNABLE_TO_PARAMETER_OF_TYPE_1_RE.md
│           │   │   │   │       ├── ARGUMENT_OF_TYPE_UNDEFINED_IS_NOT_ASSIGNABLE_TO_PARAMETER_OF_TYPE_1_RE.md
│           │   │   │   │       ├── ARGUMENT_OF_TYPE.md
│           │   │   │   │       ├── IS_NOT_ASSIGNABLE_TO_PARAMETER_OF_TYPE.md
│           │   │   │   │       ├── IS_NOT_ASSIGNABLE_TO_TYPE.md
│           │   │   │   │       ├── NO_OVERLOAD_MATCHES_THIS_CALL_ERROR_CODE.md
│           │   │   │   │       ├── TYPE_0_IS_NOT_ASSIGNABLE_TO_TYPE_1_ERROR_CODE.md
│           │   │   │   │       ├── TYPE_NULL_IS_NOT_ASSIGNABLE_TO_TYPE_1_RE.md
│           │   │   │   │       ├── TYPE_UNDEFINED_IS_NOT_ASSIGNABLE_TO_TYPE_1_RE.md
│           │   │   │   │       ├── TYPE_UNKNOWN_IS_NOT_ASSIGNABLE_TO_TYPE_1_RE.md
│           │   │   │   │       └── TYPE.md
│           │   │   │   ├── Problems
│           │   │   │   │   ├── classes
│           │   │   │   │   │   └── FaultAttributes.md
│           │   │   │   │   ├── enumerations
│           │   │   │   │   │   └── FaultID.md
│           │   │   │   │   ├── README.md
│           │   │   │   │   └── variables
│           │   │   │   │       └── faultsAttrs.md
│           │   │   │   └── Utils
│           │   │   │       ├── functions
│           │   │   │       │   ├── checkTypeSet.md
│           │   │   │       │   ├── clearTrueSymbolAtLocationCache.md
│           │   │   │       │   ├── clearTypeChecker.md
│           │   │   │       │   ├── decodeAutofixInfo.md
│           │   │   │       │   ├── encodeProblemInfo.md
│           │   │   │       │   ├── entityNameToString.md
│           │   │   │       │   ├── findParentIf.md
│           │   │   │       │   ├── followIfAliased.md
│           │   │   │       │   ├── getAccessModifier.md
│           │   │   │       │   ├── getCatchWithUnsupportedTypeHighlightRange.md
│           │   │   │       │   ├── getClassExpressionHighlightRange.md
│           │   │   │       │   ├── getConstAssertionHighlightRange.md
│           │   │   │       │   ├── getDeclaration.md
│           │   │   │       │   ├── getDeclarationNode.md
│           │   │   │       │   ├── getDeclWithDuplicateNameHighlightRange.md
│           │   │   │       │   ├── getDecoratorName.md
│           │   │   │       │   ├── getDecoratorsIfInSendableClass.md
│           │   │   │       │   ├── getDeleteOperatorHighlightRange.md
│           │   │   │       │   ├── getEndPos.md
│           │   │   │       │   ├── getForInStatementHighlightRange.md
│           │   │   │       │   ├── getFunctionApplyCallHighlightRange.md
│           │   │   │       │   ├── getHighlightRange.md
│           │   │   │       │   ├── getInstanceofUnsupportedHighlightRange.md
│           │   │   │       │   ├── getKeywordHighlightRange.md
│           │   │   │       │   ├── getLimitedReturnTypeInferenceHighlightRange.md
│           │   │   │       │   ├── getLocalFunctionHighlightRange.md
│           │   │   │       │   ├── getModifier.md
│           │   │   │       │   ├── getMultipleStaticBlocksHighlightRange.md
│           │   │   │       │   ├── getNonNullableType.md
│           │   │   │       │   ├── getNonSendableDecorators.md
│           │   │   │       │   ├── getObjectLiteralNoContextTypeHighlightRange.md
│           │   │   │       │   ├── getParentSymbolName.md
│           │   │   │       │   ├── getScriptKind.md
│           │   │   │       │   ├── getSendableDecorator.md
│           │   │   │       │   ├── getSendableDefiniteAssignmentHighlightRange.md
│           │   │   │       │   ├── getStartPos.md
│           │   │   │       │   ├── getSymbolDeclarationTypeNode.md
│           │   │   │       │   ├── getSymbolOfCallExpression.md
│           │   │   │       │   ├── getTypeOrTypeConstraintAtLocation.md
│           │   │   │       │   ├── getTypeQueryHighlightRange.md
│           │   │   │       │   ├── getVarDeclarationHighlightRange.md
│           │   │   │       │   ├── getVariableDeclarationTypeNode.md
│           │   │   │       │   ├── getWithStatementHighlightRange.md
│           │   │   │       │   ├── hasAccessModifier.md
│           │   │   │       │   ├── hasEsObjectType.md
│           │   │   │       │   ├── hasLibraryType.md
│           │   │   │       │   ├── hasMethods.md
│           │   │   │       │   ├── hasModifier.md
│           │   │   │       │   ├── hasPredecessor.md
│           │   │   │       │   ├── hasSendableDecorator.md
│           │   │   │       │   ├── hasSendableDecoratorFunctionOverload.md
│           │   │   │       │   ├── hasSendableTypeAlias.md
│           │   │   │       │   ├── isAllowedIndexSignature.md
│           │   │   │       │   ├── isAnonymous.md
│           │   │   │       │   ├── isAnonymousType.md
│           │   │   │       │   ├── isAnyType.md
│           │   │   │       │   ├── isArkTSCollectionsArrayLikeType.md
│           │   │   │       │   ├── isArkTSCollectionsClassOrInterfaceDeclaration.md
│           │   │   │       │   ├── isArray.md
│           │   │   │       │   ├── isAssignmentOperator.md
│           │   │   │       │   ├── isBooleanLikeType.md
│           │   │   │       │   ├── isCallToFunctionWithOmittedReturnType.md
│           │   │   │       │   ├── isCompileTimeExpression.md
│           │   │   │       │   ├── isConst.md
│           │   │   │       │   ├── isConstEnum.md
│           │   │   │       │   ├── isDefaultImport.md
│           │   │   │       │   ├── isDestructuringAssignmentLHS.md
│           │   │   │       │   ├── isDynamicLiteralInitializer.md
│           │   │   │       │   ├── isDynamicType.md
│           │   │   │       │   ├── isEnum.md
│           │   │   │       │   ├── isEnumMemberType.md
│           │   │   │       │   ├── isEnumStringLiteral.md
│           │   │   │       │   ├── isEnumType.md
│           │   │   │       │   ├── isEsObjectPossiblyAllowed.md
│           │   │   │       │   ├── isEsObjectSymbol.md
│           │   │   │       │   ├── isEsObjectType.md
│           │   │   │       │   ├── isFunctionOrMethod.md
│           │   │   │       │   ├── isFunctionSymbol.md
│           │   │   │       │   ├── isGenericArrayType.md
│           │   │   │       │   ├── isGlobalSymbol.md
│           │   │   │       │   ├── isInImportWhiteList.md
│           │   │   │       │   ├── isInsideBlock.md
│           │   │   │       │   ├── isIntegerConstantValue.md
│           │   │   │       │   ├── isInterfaceType.md
│           │   │   │       │   ├── isIntrinsicObjectType.md
│           │   │   │       │   ├── isISendableInterface.md
│           │   │   │       │   ├── isLibrarySymbol.md
│           │   │   │       │   ├── isLibraryType.md
│           │   │   │       │   ├── isLiteralType.md
│           │   │   │       │   ├── isMethodAssignment.md
│           │   │   │       │   ├── isNonSendableFunctionTypeAlias.md
│           │   │   │       │   ├── isNullType.md
│           │   │   │       │   ├── isNumberConstantValue.md
│           │   │   │       │   ├── isNumberLikeType.md
│           │   │   │       │   ├── isObject.md
│           │   │   │       │   ├── isObjectLiteralAssignable.md
│           │   │   │       │   ├── isObjectLiteralType.md
│           │   │   │       │   ├── isObjectType.md
│           │   │   │       │   ├── isOrDerivedFrom.md
│           │   │   │       │   ├── isPrimitiveEnumMemberType.md
│           │   │   │       │   ├── isPrimitiveLiteralType.md
│           │   │   │       │   ├── isPrimitiveType.md
│           │   │   │       │   ├── isPrototypeSymbol.md
│           │   │   │       │   ├── isPurePrimitiveLiteralType.md
│           │   │   │       │   ├── isReadonlyArrayType.md
│           │   │   │       │   ├── isReferenceType.md
│           │   │   │       │   ├── isSendableClassOrInterface.md
│           │   │   │       │   ├── isSendableClassOrInterfaceEntity.md
│           │   │   │       │   ├── isSendableFunction.md
│           │   │   │       │   ├── isSendableType.md
│           │   │   │       │   ├── isSendableTypeAlias.md
│           │   │   │       │   ├── isSendableTypeNode.md
│           │   │   │       │   ├── isSendableUnionType.md
│           │   │   │       │   ├── isShareableEntity.md
│           │   │   │       │   ├── isShareableType.md
│           │   │   │       │   ├── isSharedModule.md
│           │   │   │       │   ├── isStdBigIntType.md
│           │   │   │       │   ├── isStdBooleanType.md
│           │   │   │       │   ├── isStdErrorType.md
│           │   │   │       │   ├── isStdLibrarySymbol.md
│           │   │   │       │   ├── isStdLibraryType.md
│           │   │   │       │   ├── isStdMapType.md
│           │   │   │       │   ├── isStdNumberType.md
│           │   │   │       │   ├── isStdPartialType.md
│           │   │   │       │   ├── isStdReadonlyType.md
│           │   │   │       │   ├── isStdRecordType.md
│           │   │   │       │   ├── isStdRequiredType.md
│           │   │   │       │   ├── isStdSymbol.md
│           │   │   │       │   ├── isStringConstantValue.md
│           │   │   │       │   ├── isStringLikeType.md
│           │   │   │       │   ├── isStringType.md
│           │   │   │       │   ├── isStruct.md
│           │   │   │       │   ├── isStructDeclaration.md
│           │   │   │       │   ├── isStructDeclarationKind.md
│           │   │   │       │   ├── isStructObjectInitializer.md
│           │   │   │       │   ├── isSupportedType.md
│           │   │   │       │   ├── isSymbolAPI.md
│           │   │   │       │   ├── isSymbolIterator.md
│           │   │   │       │   ├── isSymbolIteratorExpression.md
│           │   │   │       │   ├── isThisOrSuperExpr.md
│           │   │   │       │   ├── isTuple.md
│           │   │   │       │   ├── isType.md
│           │   │   │       │   ├── isTypedArray.md
│           │   │   │       │   ├── isTypeDeclSyntaxKind.md
│           │   │   │       │   ├── isTypeReference.md
│           │   │   │       │   ├── isTypeSymbol.md
│           │   │   │       │   ├── isUnknownType.md
│           │   │   │       │   ├── isUnsupportedType.md
│           │   │   │       │   ├── isUnsupportedUnionType.md
│           │   │   │       │   ├── isValidComputedPropertyName.md
│           │   │   │       │   ├── isValidEnumMemberInit.md
│           │   │   │       │   ├── isValueAssignableToESObject.md
│           │   │   │       │   ├── isWrongSendableFunctionAssignment.md
│           │   │   │       │   ├── logTscDiagnostic.md
│           │   │   │       │   ├── needStrictMatchType.md
│           │   │   │       │   ├── needToDeduceStructuralIdentity.md
│           │   │   │       │   ├── pathContainsDirectory.md
│           │   │   │       │   ├── processParentTypes.md
│           │   │   │       │   ├── reduceReference.md
│           │   │   │       │   ├── relatedByInheritanceOrIdentical.md
│           │   │   │       │   ├── searchFileExportDecl.md
│           │   │   │       │   ├── setTestMode.md
│           │   │   │       │   ├── setTypeChecker.md
│           │   │   │       │   ├── symbolHasDuplicateName.md
│           │   │   │       │   ├── symbolHasEsObjectType.md
│           │   │   │       │   ├── trueSymbolAtLocation.md
│           │   │   │       │   ├── typeContainsNonSendableClassOrInterface.md
│           │   │   │       │   ├── typeContainsSendableClassOrInterface.md
│           │   │   │       │   ├── typeIsRecursive.md
│           │   │   │       │   ├── unwrapParenthesized.md
│           │   │   │       │   ├── unwrapParenthesizedType.md
│           │   │   │       │   ├── unwrapParenthesizedTypeNode.md
│           │   │   │       │   ├── validateFields.md
│           │   │   │       │   └── validateObjectLiteralType.md
│           │   │   │       ├── README.md
│           │   │   │       ├── type-aliases
│           │   │   │       │   └── CheckType.md
│           │   │   │       └── variables
│           │   │   │           ├── ALLOWED_STD_SYMBOL_API.md
│           │   │   │           ├── ARKTS_COLLECTIONS_D_ETS.md
│           │   │   │           ├── ARKTS_IGNORE_DIRS.md
│           │   │   │           ├── ARKTS_IGNORE_FILES.md
│           │   │   │           ├── ARKTS_LANG_D_ETS.md
│           │   │   │           ├── COLLECTIONS_NAMESPACE.md
│           │   │   │           ├── D_TS.md
│           │   │   │           ├── ES_OBJECT.md
│           │   │   │           ├── FUNCTION_HAS_NO_RETURN_ERROR_CODE.md
│           │   │   │           ├── ISENDABLE_TYPE.md
│           │   │   │           ├── LANG_NAMESPACE.md
│           │   │   │           ├── LIMITED_STANDARD_UTILITY_TYPES.md
│           │   │   │           ├── LIMITED_STD_GLOBAL_FUNC.md
│           │   │   │           ├── LIMITED_STD_OBJECT_API.md
│           │   │   │           ├── LIMITED_STD_PROXYHANDLER_API.md
│           │   │   │           ├── LIMITED_STD_REFLECT_API.md
│           │   │   │           ├── NON_INITIALIZABLE_PROPERTY_CLASS_DECORATORS.md
│           │   │   │           ├── NON_INITIALIZABLE_PROPERTY_DECORATORS.md
│           │   │   │           ├── NON_RETURN_FUNCTION_DECORATORS.md
│           │   │   │           ├── PROPERTY_HAS_NO_INITIALIZER_ERROR_CODE.md
│           │   │   │           ├── SENDABLE_CLOSURE_DECLS.md
│           │   │   │           ├── SENDABLE_DECORATOR_NODES.md
│           │   │   │           ├── SENDABLE_DECORATOR.md
│           │   │   │           ├── SENDABLE_INTERFACE.md
│           │   │   │           ├── STANDARD_LIBRARIES.md
│           │   │   │           ├── TYPED_ARRAYS.md
│           │   │   │           └── USE_SHARED.md
│           │   │   ├── README.md
│           │   │   ├── type-aliases
│           │   │   │   └── KitSymbols.md
│           │   │   └── variables
│           │   │       ├── cookBookMsg.md
│           │   │       └── cookBookTag.md
│           │   ├── ScriptSnapshot
│           │   │   ├── functions
│           │   │   │   └── fromString.md
│           │   │   └── README.md
│           │   └── server
│           │       ├── interfaces
│           │       │   ├── BeginInstallTypes.md
│           │       │   ├── CloseProject.md
│           │       │   ├── DiscoverTypings.md
│           │       │   ├── EndInstallTypes.md
│           │       │   ├── InitializationFailedResponse.md
│           │       │   ├── InstallPackageRequest.md
│           │       │   ├── InstallTypes.md
│           │       │   ├── InvalidateCachedTypings.md
│           │       │   ├── PackageInstalledResponse.md
│           │       │   ├── ProjectResponse.md
│           │       │   ├── SetTypings.md
│           │       │   ├── TypesRegistryRequest.md
│           │       │   ├── TypingInstallerRequestWithProjectName.md
│           │       │   └── TypingInstallerResponse.md
│           │       ├── README.md
│           │       └── type-aliases
│           │           ├── ActionInvalidate.md
│           │           ├── ActionPackageInstalled.md
│           │           ├── ActionSet.md
│           │           ├── EventBeginInstallTypes.md
│           │           ├── EventEndInstallTypes.md
│           │           ├── EventInitializationFailed.md
│           │           └── EventTypesRegistry.md
│           ├── README.md
│           ├── type-aliases
│           │   ├── AbstractKeyword.md
│           │   ├── AccessExpression.md
│           │   ├── AccessibilityModifier.md
│           │   ├── AccessorDeclaration.md
│           │   ├── AccessorKeyword.md
│           │   ├── AdditiveOperator.md
│           │   ├── AdditiveOperatorOrHigher.md
│           │   ├── AffectedFileResult.md
│           │   ├── ArrayBindingElement.md
│           │   ├── ArrayBindingOrAssignmentElement.md
│           │   ├── ArrayBindingOrAssignmentPattern.md
│           │   ├── AssertionExpression.md
│           │   ├── AssertionKey.md
│           │   ├── AssertKeyword.md
│           │   ├── AssertsKeyword.md
│           │   ├── AssertsToken.md
│           │   ├── AssignmentOperator.md
│           │   ├── AssignmentOperatorOrHigher.md
│           │   ├── AssignmentOperatorToken.md
│           │   ├── AssignmentPattern.md
│           │   ├── AsteriskToken.md
│           │   ├── AsyncKeyword.md
│           │   ├── AwaitKeyword.md
│           │   ├── AwaitKeywordToken.md
│           │   ├── BaseType.md
│           │   ├── BinaryOperator.md
│           │   ├── BinaryOperatorToken.md
│           │   ├── BindingName.md
│           │   ├── BindingOrAssignmentElement.md
│           │   ├── BindingOrAssignmentElementRestIndicator.md
│           │   ├── BindingOrAssignmentElementTarget.md
│           │   ├── BindingOrAssignmentPattern.md
│           │   ├── BindingPattern.md
│           │   ├── BitwiseOperator.md
│           │   ├── BitwiseOperatorOrHigher.md
│           │   ├── BlockLike.md
│           │   ├── BooleanLiteral.md
│           │   ├── BreakOrContinueStatement.md
│           │   ├── CallLikeExpression.md
│           │   ├── CaseOrDefaultClause.md
│           │   ├── ClassLikeDeclaration.md
│           │   ├── ClassMemberModifier.md
│           │   ├── CodeActionCommand.md
│           │   ├── ColonToken.md
│           │   ├── CommentKind.md
│           │   ├── CompilerOptionsValue.md
│           │   ├── CompletionEntryData.md
│           │   ├── CompletionsTriggerCharacter.md
│           │   ├── CompoundAssignmentOperator.md
│           │   ├── ConciseBody.md
│           │   ├── ConstKeyword.md
│           │   ├── CreateProgram.md
│           │   ├── CustomTransformerFactory.md
│           │   ├── DeclarationName.md
│           │   ├── DeclarationWithTypeParameterChildren.md
│           │   ├── DeclarationWithTypeParameters.md
│           │   ├── DeclareKeyword.md
│           │   ├── DefaultKeyword.md
│           │   ├── DestructuringAssignment.md
│           │   ├── DestructuringPattern.md
│           │   ├── DiagnosticReporter.md
│           │   ├── DirectoryWatcherCallback.md
│           │   ├── DocumentRegistryBucketKey.md
│           │   ├── DotDotDotToken.md
│           │   ├── DotToken.md
│           │   ├── EmitHelper.md
│           │   ├── EmitHelperUniqueNameCallback.md
│           │   ├── EndOfFileToken.md
│           │   ├── EntityName.md
│           │   ├── EntityNameExpression.md
│           │   ├── EntityNameOrEntityNameExpression.md
│           │   ├── EqualityOperator.md
│           │   ├── EqualityOperatorOrHigher.md
│           │   ├── EqualsGreaterThanToken.md
│           │   ├── EqualsToken.md
│           │   ├── ErrorCallback.md
│           │   ├── ExclamationToken.md
│           │   ├── ExponentiationOperator.md
│           │   ├── ExportKeyword.md
│           │   ├── FileWatcherCallback.md
│           │   ├── FlowNode.md
│           │   ├── FlowType.md
│           │   ├── ForInitializer.md
│           │   ├── ForInOrOfStatement.md
│           │   ├── FunctionBody.md
│           │   ├── FunctionLike.md
│           │   ├── FunctionLikeDeclaration.md
│           │   ├── FunctionOrConstructorTypeNode.md
│           │   ├── HasDecorators.md
│           │   ├── HasExpressionInitializer.md
│           │   ├── HasIllegalDecorators.md
│           │   ├── HasInitializer.md
│           │   ├── HasJSDoc.md
│           │   ├── HasModifiers.md
│           │   ├── HasType.md
│           │   ├── HasTypeArguments.md
│           │   ├── ImportOrExportSpecifier.md
│           │   ├── IncrementExpression.md
│           │   ├── InKeyword.md
│           │   ├── InvalidatedProject.md
│           │   ├── JSDocComment.md
│           │   ├── JSDocNamespaceBody.md
│           │   ├── JSDocSyntaxKind.md
│           │   ├── JSDocTypeReferencingNode.md
│           │   ├── JsFileExtensionInfo.md
│           │   ├── JsonObjectExpression.md
│           │   ├── JsxAttributeLike.md
│           │   ├── JsxAttributeValue.md
│           │   ├── JsxChild.md
│           │   ├── JsxOpeningLikeElement.md
│           │   ├── JsxTagNameExpression.md
│           │   ├── JsxTokenSyntaxKind.md
│           │   ├── KeywordSyntaxKind.md
│           │   ├── KeywordTypeSyntaxKind.md
│           │   ├── LiteralSyntaxKind.md
│           │   ├── LiteralToken.md
│           │   ├── LogicalOperator.md
│           │   ├── LogicalOperatorOrHigher.md
│           │   ├── LogicalOrCoalescingAssignmentOperator.md
│           │   ├── MemberName.md
│           │   ├── MinusToken.md
│           │   ├── Modifier.md
│           │   ├── ModifierLike.md
│           │   ├── ModifiersArray.md
│           │   ├── ModifierSyntaxKind.md
│           │   ├── ModuleBody.md
│           │   ├── ModuleName.md
│           │   ├── ModuleReference.md
│           │   ├── MultiplicativeOperator.md
│           │   ├── MultiplicativeOperatorOrHigher.md
│           │   ├── NamedExportBindings.md
│           │   ├── NamedImportBindings.md
│           │   ├── NamedImportsOrExports.md
│           │   ├── NamespaceBody.md
│           │   ├── ObjectBindingOrAssignmentElement.md
│           │   ├── ObjectBindingOrAssignmentPattern.md
│           │   ├── ObjectLiteralElementLike.md
│           │   ├── ObjectTypeDeclaration.md
│           │   ├── OptionalChain.md
│           │   ├── OutKeyword.md
│           │   ├── OverrideKeyword.md
│           │   ├── ParameterPropertyDeclaration.md
│           │   ├── ParameterPropertyModifier.md
│           │   ├── Path.md
│           │   ├── PlusToken.md
│           │   ├── PostfixUnaryOperator.md
│           │   ├── PrefixUnaryOperator.md
│           │   ├── PrivateKeyword.md
│           │   ├── PropertyName.md
│           │   ├── PropertyNameLiteral.md
│           │   ├── ProtectedKeyword.md
│           │   ├── PseudoLiteralSyntaxKind.md
│           │   ├── PseudoLiteralToken.md
│           │   ├── PublicKeyword.md
│           │   ├── PunctuationSyntaxKind.md
│           │   ├── QuestionDotToken.md
│           │   ├── QuestionToken.md
│           │   ├── ReadonlyKeyword.md
│           │   ├── ReadonlyToken.md
│           │   ├── RedirectTargetsMap.md
│           │   ├── RefactorTriggerReason.md
│           │   ├── RelationalOperator.md
│           │   ├── RelationalOperatorOrHigher.md
│           │   ├── RenameInfo.md
│           │   ├── ReportEmitErrorSummary.md
│           │   ├── ResolvedConfigFileName.md
│           │   ├── ShiftOperator.md
│           │   ├── ShiftOperatorOrHigher.md
│           │   ├── SignatureDeclaration.md
│           │   ├── SignatureHelpRetriggerCharacter.md
│           │   ├── SignatureHelpTriggerCharacter.md
│           │   ├── SignatureHelpTriggerReason.md
│           │   ├── StaticKeyword.md
│           │   ├── String.md
│           │   ├── StringLiteralLike.md
│           │   ├── StructuredType.md
│           │   ├── SuperProperty.md
│           │   ├── SymbolTable.md
│           │   ├── TemplateLiteral.md
│           │   ├── TemplateLiteralToken.md
│           │   ├── TokenSyntaxKind.md
│           │   ├── Transformer.md
│           │   ├── TransformerFactory.md
│           │   ├── TriviaSyntaxKind.md
│           │   ├── TypeOfTag.md
│           │   ├── TypeOnlyAliasDeclaration.md
│           │   ├── TypeOnlyCompatibleAliasDeclaration.md
│           │   ├── TypePredicate.md
│           │   ├── TypeReferenceType.md
│           │   ├── TypeVariable.md
│           │   ├── UnionOrIntersectionTypeNode.md
│           │   ├── UnparsedNode.md
│           │   ├── UnparsedSourceText.md
│           │   ├── VariableLikeDeclaration.md
│           │   ├── Visitor.md
│           │   ├── VisitResult.md
│           │   ├── WatchStatusReporter.md
│           │   ├── WithMetadata.md
│           │   └── WriteFileCallback.md
│           └── variables
│               ├── createAdd.md
│               ├── createArrayBindingPattern.md
│               ├── createArrayLiteral.md
│               ├── createArrayTypeNode.md
│               ├── createArrowFunction.md
│               ├── createAsExpression.md
│               ├── createAssignment.md
│               ├── createAwait.md
│               ├── createBigIntLiteral.md
│               ├── createBinary.md
│               ├── createBindingElement.md
│               ├── createBlock.md
│               ├── createBreak.md
│               ├── createBundle.md
│               ├── createCall.md
│               ├── createCallChain.md
│               ├── createCallSignature.md
│               ├── createCaseBlock.md
│               ├── createCaseClause.md
│               ├── createCatchClause.md
│               ├── createClassDeclaration.md
│               ├── createClassExpression.md
│               ├── createComma.md
│               ├── createCommaList.md
│               ├── createComputedPropertyName.md
│               ├── createConditional.md
│               ├── createConditionalTypeNode.md
│               ├── createConstructor.md
│               ├── createConstructorTypeNode.md
│               ├── createConstructSignature.md
│               ├── createContinue.md
│               ├── createDebuggerStatement.md
│               ├── createDecorator.md
│               ├── createDefaultClause.md
│               ├── createDelete.md
│               ├── createDo.md
│               ├── createElementAccess.md
│               ├── createElementAccessChain.md
│               ├── createEmptyStatement.md
│               ├── createEnumDeclaration.md
│               ├── createEnumMember.md
│               ├── createExportAssignment.md
│               ├── createExportDeclaration.md
│               ├── createExportDefault.md
│               ├── createExportSpecifier.md
│               ├── createExpressionStatement.md
│               ├── createExpressionWithTypeArguments.md
│               ├── createExternalModuleExport.md
│               ├── createExternalModuleReference.md
│               ├── createFalse.md
│               ├── createFileLevelUniqueName.md
│               ├── createFor.md
│               ├── createForIn.md
│               ├── createForOf.md
│               ├── createFunctionDeclaration.md
│               ├── createFunctionExpression.md
│               ├── createFunctionTypeNode.md
│               ├── createGetAccessor.md
│               ├── createHeritageClause.md
│               ├── createIdentifier.md
│               ├── createIf.md
│               ├── createImmediatelyInvokedArrowFunction.md
│               ├── createImmediatelyInvokedFunctionExpression.md
│               ├── createImportClause.md
│               ├── createImportDeclaration.md
│               ├── createImportEqualsDeclaration.md
│               ├── createImportSpecifier.md
│               ├── createImportTypeNode.md
│               ├── createIndexedAccessTypeNode.md
│               ├── createIndexSignature.md
│               ├── createInferTypeNode.md
│               ├── createInterfaceDeclaration.md
│               ├── createIntersectionTypeNode.md
│               ├── createJSDocAugmentsTag.md
│               ├── createJSDocAuthorTag.md
│               ├── createJSDocCallbackTag.md
│               ├── createJSDocClassTag.md
│               ├── createJSDocComment.md
│               ├── createJSDocEnumTag.md
│               ├── createJSDocImplementsTag.md
│               ├── createJSDocParameterTag.md
│               ├── createJSDocParamTag.md
│               ├── createJSDocPrivateTag.md
│               ├── createJSDocPropertyTag.md
│               ├── createJSDocProtectedTag.md
│               ├── createJSDocPublicTag.md
│               ├── createJSDocReadonlyTag.md
│               ├── createJSDocReturnTag.md
│               ├── createJSDocSignature.md
│               ├── createJSDocTag.md
│               ├── createJSDocTemplateTag.md
│               ├── createJSDocThisTag.md
│               ├── createJSDocTypedefTag.md
│               ├── createJSDocTypeExpression.md
│               ├── createJSDocTypeLiteral.md
│               ├── createJSDocTypeTag.md
│               ├── createJsxAttribute.md
│               ├── createJsxAttributes.md
│               ├── createJsxClosingElement.md
│               ├── createJsxElement.md
│               ├── createJsxExpression.md
│               ├── createJsxFragment.md
│               ├── createJsxJsxClosingFragment.md
│               ├── createJsxOpeningElement.md
│               ├── createJsxOpeningFragment.md
│               ├── createJsxSelfClosingElement.md
│               ├── createJsxSpreadAttribute.md
│               ├── createJsxText.md
│               ├── createKeywordTypeNode.md
│               ├── createLabel.md
│               ├── createLessThan.md
│               ├── createLiteral.md
│               ├── createLiteralTypeNode.md
│               ├── createLogicalAnd.md
│               ├── createLogicalNot.md
│               ├── createLogicalOr.md
│               ├── createLoopVariable.md
│               ├── createMappedTypeNode.md
│               ├── createMetaProperty.md
│               ├── createMethod.md
│               ├── createMethodSignature.md
│               ├── createModifier.md
│               ├── createModifiersFromModifierFlags.md
│               ├── createModuleBlock.md
│               ├── createModuleDeclaration.md
│               ├── createNamedExports.md
│               ├── createNamedImports.md
│               ├── createNamespaceExport.md
│               ├── createNamespaceExportDeclaration.md
│               ├── createNamespaceImport.md
│               ├── createNew.md
│               ├── createNode.md
│               ├── createNodeArray.md
│               ├── createNonNullChain.md
│               ├── createNonNullExpression.md
│               ├── createNoSubstitutionTemplateLiteral.md
│               ├── createNotEmittedStatement.md
│               ├── createNull.md
│               ├── createNumericLiteral.md
│               ├── createObjectBindingPattern.md
│               ├── createObjectLiteral.md
│               ├── createOmittedExpression.md
│               ├── createOptimisticUniqueName.md
│               ├── createOptionalTypeNode.md
│               ├── createParameter.md
│               ├── createParen.md
│               ├── createParenthesizedType.md
│               ├── createPartiallyEmittedExpression.md
│               ├── createPostfix.md
│               ├── createPostfixIncrement.md
│               ├── createPrefix.md
│               ├── createPrivateIdentifier.md
│               ├── createProperty.md
│               ├── createPropertyAccess.md
│               ├── createPropertyAccessChain.md
│               ├── createPropertyAssignment.md
│               ├── createPropertySignature.md
│               ├── createQualifiedName.md
│               ├── createRegularExpressionLiteral.md
│               ├── createRestTypeNode.md
│               ├── createReturn.md
│               ├── createSemicolonClassElement.md
│               ├── createSetAccessor.md
│               ├── createShorthandPropertyAssignment.md
│               ├── createSpread.md
│               ├── createSpreadAssignment.md
│               ├── createStatement.md
│               ├── createStrictEquality.md
│               ├── createStrictInequality.md
│               ├── createStringLiteral.md
│               ├── createStringLiteralFromNode.md
│               ├── createSubtract.md
│               ├── createSuper.md
│               ├── createSwitch.md
│               ├── createTaggedTemplate.md
│               ├── createTemplateExpression.md
│               ├── createTemplateHead.md
│               ├── createTemplateMiddle.md
│               ├── createTemplateSpan.md
│               ├── createTemplateTail.md
│               ├── createTempVariable.md
│               ├── createThis.md
│               ├── createThisTypeNode.md
│               ├── createThrow.md
│               ├── createToken.md
│               ├── createTrue.md
│               ├── createTry.md
│               ├── createTupleTypeNode.md
│               ├── createTypeAliasDeclaration.md
│               ├── createTypeAssertion.md
│               ├── createTypeLiteralNode.md
│               ├── createTypeOf.md
│               ├── createTypeOperatorNode.md
│               ├── createTypeParameterDeclaration.md
│               ├── createTypePredicateNode.md
│               ├── createTypePredicateNodeWithModifier.md
│               ├── createTypeQueryNode.md
│               ├── createTypeReferenceNode.md
│               ├── createUnionTypeNode.md
│               ├── createUniqueName.md
│               ├── createVariableDeclaration.md
│               ├── createVariableDeclarationList.md
│               ├── createVariableStatement.md
│               ├── createVoid.md
│               ├── createVoidZero.md
│               ├── createWhile.md
│               ├── createWith.md
│               ├── createYield.md
│               ├── factory.md
│               ├── getGeneratedNameForNode.md
│               ├── getMutableClone.md
│               ├── isIdentifierOrPrivateIdentifier.md
│               ├── isTypeAssertion.md
│               ├── ohModulesPathPart.md
│               ├── servicesVersion.md
│               ├── sys.md
│               ├── unchangedTextChangeRange.md
│               ├── updateArrayBindingPattern.md
│               ├── updateArrayLiteral.md
│               ├── updateArrayTypeNode.md
│               ├── updateArrowFunction.md
│               ├── updateAsExpression.md
│               ├── updateAwait.md
│               ├── updateBinary.md
│               ├── updateBindingElement.md
│               ├── updateBlock.md
│               ├── updateBreak.md
│               ├── updateBundle.md
│               ├── updateCall.md
│               ├── updateCallChain.md
│               ├── updateCallSignature.md
│               ├── updateCaseBlock.md
│               ├── updateCaseClause.md
│               ├── updateCatchClause.md
│               ├── updateClassDeclaration.md
│               ├── updateClassExpression.md
│               ├── updateCommaList.md
│               ├── updateComputedPropertyName.md
│               ├── updateConditional.md
│               ├── updateConditionalTypeNode.md
│               ├── updateConstructor.md
│               ├── updateConstructorTypeNode.md
│               ├── updateConstructSignature.md
│               ├── updateContinue.md
│               ├── updateDecorator.md
│               ├── updateDefaultClause.md
│               ├── updateDelete.md
│               ├── updateDo.md
│               ├── updateElementAccess.md
│               ├── updateElementAccessChain.md
│               ├── updateEnumDeclaration.md
│               ├── updateEnumMember.md
│               ├── updateExportAssignment.md
│               ├── updateExportDeclaration.md
│               ├── updateExportSpecifier.md
│               ├── updateExpressionStatement.md
│               ├── updateExpressionWithTypeArguments.md
│               ├── updateExternalModuleReference.md
│               ├── updateFor.md
│               ├── updateForIn.md
│               ├── updateForOf.md
│               ├── updateFunctionDeclaration.md
│               ├── updateFunctionExpression.md
│               ├── updateFunctionTypeNode.md
│               ├── updateGetAccessor.md
│               ├── updateHeritageClause.md
│               ├── updateIf.md
│               ├── updateImportClause.md
│               ├── updateImportDeclaration.md
│               ├── updateImportEqualsDeclaration.md
│               ├── updateImportSpecifier.md
│               ├── updateImportTypeNode.md
│               ├── updateIndexedAccessTypeNode.md
│               ├── updateIndexSignature.md
│               ├── updateInferTypeNode.md
│               ├── updateInterfaceDeclaration.md
│               ├── updateIntersectionTypeNode.md
│               ├── updateJsxAttribute.md
│               ├── updateJsxAttributes.md
│               ├── updateJsxClosingElement.md
│               ├── updateJsxElement.md
│               ├── updateJsxExpression.md
│               ├── updateJsxFragment.md
│               ├── updateJsxOpeningElement.md
│               ├── updateJsxSelfClosingElement.md
│               ├── updateJsxSpreadAttribute.md
│               ├── updateJsxText.md
│               ├── updateLabel.md
│               ├── updateLiteralTypeNode.md
│               ├── updateMappedTypeNode.md
│               ├── updateMetaProperty.md
│               ├── updateMethod.md
│               ├── updateMethodSignature.md
│               ├── updateModuleBlock.md
│               ├── updateModuleDeclaration.md
│               ├── updateNamedExports.md
│               ├── updateNamedImports.md
│               ├── updateNamespaceExport.md
│               ├── updateNamespaceExportDeclaration.md
│               ├── updateNamespaceImport.md
│               ├── updateNew.md
│               ├── updateNonNullChain.md
│               ├── updateNonNullExpression.md
│               ├── updateObjectBindingPattern.md
│               ├── updateObjectLiteral.md
│               ├── updateOptionalTypeNode.md
│               ├── updateParameter.md
│               ├── updateParen.md
│               ├── updateParenthesizedType.md
│               ├── updatePartiallyEmittedExpression.md
│               ├── updatePostfix.md
│               ├── updatePrefix.md
│               ├── updateProperty.md
│               ├── updatePropertyAccess.md
│               ├── updatePropertyAccessChain.md
│               ├── updatePropertyAssignment.md
│               ├── updatePropertySignature.md
│               ├── updateQualifiedName.md
│               ├── updateRestTypeNode.md
│               ├── updateReturn.md
│               ├── updateSetAccessor.md
│               ├── updateShorthandPropertyAssignment.md
│               ├── updateSourceFileNode.md
│               ├── updateSpread.md
│               ├── updateSpreadAssignment.md
│               ├── updateStatement.md
│               ├── updateSwitch.md
│               ├── updateTaggedTemplate.md
│               ├── updateTemplateExpression.md
│               ├── updateTemplateSpan.md
│               ├── updateThrow.md
│               ├── updateTry.md
│               ├── updateTupleTypeNode.md
│               ├── updateTypeAliasDeclaration.md
│               ├── updateTypeAssertion.md
│               ├── updateTypeLiteralNode.md
│               ├── updateTypeOf.md
│               ├── updateTypeOperatorNode.md
│               ├── updateTypeParameterDeclaration.md
│               ├── updateTypePredicateNode.md
│               ├── updateTypePredicateNodeWithModifier.md
│               ├── updateTypeQueryNode.md
│               ├── updateTypeReferenceNode.md
│               ├── updateUnionTypeNode.md
│               ├── updateVariableDeclaration.md
│               ├── updateVariableDeclarationList.md
│               ├── updateVariableStatement.md
│               ├── updateVoid.md
│               ├── updateWhile.md
│               ├── updateWith.md
│               ├── updateYield.md
│               ├── version.md
│               └── versionMajorMinor.md
├── classes
│   ├── AbstractAnalysis.md
│   ├── AbstractBinopExpr.md
│   ├── AbstractExpr.md
│   ├── AbstractFieldRef.md
│   ├── AbstractInvokeExpr.md
│   ├── AbstractRef.md
│   ├── AddrPagEdge.md
│   ├── AliasClassSignature.md
│   ├── AliasType.md
│   ├── AliasTypeExpr.md
│   ├── AliasTypeSignature.md
│   ├── AnnotationNamespaceType.md
│   ├── AnnotationType.md
│   ├── AnnotationTypeQueryType.md
│   ├── AnyType.md
│   ├── ArkAliasTypeDefineStmt.md
│   ├── ArkArrayRef.md
│   ├── ArkAssignStmt.md
│   ├── ArkAwaitExpr.md
│   ├── ArkBody.md
│   ├── ArkCastExpr.md
│   ├── ArkCaughtExceptionRef.md
│   ├── ArkClass.md
│   ├── ArkConditionExpr.md
│   ├── ArkDeleteExpr.md
│   ├── ArkField.md
│   ├── ArkFile.md
│   ├── ArkIfStmt.md
│   ├── ArkInstanceFieldRef.md
│   ├── ArkInstanceInvokeExpr.md
│   ├── ArkInstanceOfExpr.md
│   ├── ArkInvokeStmt.md
│   ├── ArkMethod.md
│   ├── ArkNamespace.md
│   ├── ArkNewArrayExpr.md
│   ├── ArkNewExpr.md
│   ├── ArkNormalBinopExpr.md
│   ├── ArkParameterRef.md
│   ├── ArkPhiExpr.md
│   ├── ArkPtrInvokeExpr.md
│   ├── ArkReturnStmt.md
│   ├── ArkReturnVoidStmt.md
│   ├── ArkSignatureBuilder.md
│   ├── ArkStaticFieldRef.md
│   ├── ArkStaticInvokeExpr.md
│   ├── ArkThisRef.md
│   ├── ArkThrowStmt.md
│   ├── ArkTypeOfExpr.md
│   ├── ArkUnopExpr.md
│   ├── ArkYieldExpr.md
│   ├── ArrayType.md
│   ├── AstTreeUtils.md
│   ├── BaseEdge.md
│   ├── BaseExplicitGraph.md
│   ├── BaseNode.md
│   ├── BasicBlock.md
│   ├── BigIntType.md
│   ├── BooleanType.md
│   ├── CallGraph.md
│   ├── CallGraphBuilder.md
│   ├── CallGraphEdge.md
│   ├── CallGraphNode.md
│   ├── CallSite.md
│   ├── Cfg.md
│   ├── CGStat.md
│   ├── ClassHierarchyAnalysis.md
│   ├── ClassSignature.md
│   ├── ClassType.md
│   ├── ClosureFieldRef.md
│   ├── ClosureType.md
│   ├── Constant.md
│   ├── CopyPagEdge.md
│   ├── CSFuncID.md
│   ├── DataflowProblem.md
│   ├── DataflowResult.md
│   ├── DataflowSolver.md
│   ├── Decorator.md
│   ├── DefUseChain.md
│   ├── DiffPTData.md
│   ├── DominanceFinder.md
│   ├── DominanceTree.md
│   ├── DotClassPrinter.md
│   ├── DotFilePrinter.md
│   ├── DotMethodPrinter.md
│   ├── DotNamespacePrinter.md
│   ├── DummyCallCreator.md
│   ├── DummyMainCreater.md
│   ├── DVFG.md
│   ├── DVFGBuilder.md
│   ├── DynCallSite.md
│   ├── EnumValueType.md
│   ├── ExportInfo.md
│   ├── ExprUseReplacer.md
│   ├── Fact.md
│   ├── FieldSignature.md
│   ├── FileSignature.md
│   ├── FileUtils.md
│   ├── FullPosition.md
│   ├── FuncPag.md
│   ├── FunctionType.md
│   ├── GenericType.md
│   ├── GlobalRef.md
│   ├── GraphPrinter.md
│   ├── ImportInfo.md
│   ├── InterFuncPag.md
│   ├── IntersectionType.md
│   ├── IRUtils.md
│   ├── JsonPrinter.md
│   ├── KLimitedContextSensitive.md
│   ├── LexicalEnvType.md
│   ├── LineColPosition.md
│   ├── LiteralType.md
│   ├── LoadPagEdge.md
│   ├── Local.md
│   ├── LocalSignature.md
│   ├── Logger.md
│   ├── MethodSignature.md
│   ├── MethodSignatureManager.md
│   ├── MethodSubSignature.md
│   ├── ModelUtils.md
│   ├── ModulePath.md
│   ├── NamespaceSignature.md
│   ├── NeverType.md
│   ├── NullType.md
│   ├── NumberType.md
│   ├── Pag.md
│   ├── PagArrayNode.md
│   ├── PagBuilder.md
│   ├── PagEdge.md
│   ├── PagFuncNode.md
│   ├── PagGlobalThisNode.md
│   ├── PagInstanceFieldNode.md
│   ├── PagLocalNode.md
│   ├── PagNewContainerExprNode.md
│   ├── PagNewExprNode.md
│   ├── PagNode.md
│   ├── PagParamNode.md
│   ├── PAGStat.md
│   ├── PagStaticFieldNode.md
│   ├── PagThisRefNode.md
│   ├── PathEdge.md
│   ├── PathEdgePoint.md
│   ├── PointerAnalysis.md
│   ├── PointerAnalysisConfig.md
│   ├── PrimitiveType.md
│   ├── Printer.md
│   ├── PrinterBuilder.md
│   ├── PTAStat.md
│   ├── PtsSet.md
│   ├── RapidTypeAnalysis.md
│   ├── RefUseReplacer.md
│   ├── SCCDetection.md
│   ├── Scene.md
│   ├── SceneConfig.md
│   ├── SceneManager.md
│   ├── Scope.md
│   ├── SourceClassPrinter.md
│   ├── SourceFilePrinter.md
│   ├── SourceMethodPrinter.md
│   ├── SourceNamespacePrinter.md
│   ├── StaticSingleAssignmentFormer.md
│   ├── Stmt.md
│   ├── StmtUseReplacer.md
│   ├── StringType.md
│   ├── ThisPagEdge.md
│   ├── TupleType.md
│   ├── Type.md
│   ├── TypeInference.md
│   ├── UnclearReferenceType.md
│   ├── UndefinedType.md
│   ├── UndefinedVariableChecker.md
│   ├── UndefinedVariableSolver.md
│   ├── UnionType.md
│   ├── UnknownType.md
│   ├── ValueUtil.md
│   ├── ViewTreePrinter.md
│   ├── VisibleValue.md
│   ├── VoidType.md
│   └── WritePagEdge.md
├── enumerations
│   ├── CallGraphNodeKind.md
│   ├── LOG_LEVEL.md
│   ├── LOG_MODULE_TYPE.md
│   ├── NormalBinaryOperator.md
│   ├── PagEdgeKind.md
│   ├── PagNodeKind.md
│   ├── RelationalBinaryOperator.md
│   ├── StorageLinkEdgeType.md
│   ├── StorageType.md
│   └── UnaryOperator.md
├── functions
│   ├── addCfg2Stmt.md
│   ├── classSignatureCompare.md
│   ├── extractLastBracketContent.md
│   ├── fetchDependenciesFromFile.md
│   ├── fieldSignatureCompare.md
│   ├── fileSignatureCompare.md
│   ├── genSignature4ImportClause.md
│   ├── getAllFiles.md
│   ├── getCallbackMethodFromStmt.md
│   ├── getFileRecursively.md
│   ├── isEtsAtomicComponent.md
│   ├── isEtsContainerComponent.md
│   ├── isEtsSystemComponent.md
│   ├── isItemRegistered.md
│   ├── methodSignatureCompare.md
│   ├── methodSubSignatureCompare.md
│   ├── parseJsonText.md
│   ├── printCallGraphDetails.md
│   ├── splitStringWithRegex.md
│   └── transfer2UnixPath.md
├── globals.md
├── interfaces
│   ├── AbilityMessage.md
│   ├── ArkSignature.md
│   ├── FlowFunction.md
│   ├── ICallSite.md
│   ├── Value.md
│   ├── ViewTree.md
│   └── ViewTreeNode.md
├── README.md
├── tree.md
├── type-aliases
│   ├── AliasTypeOriginalModel.md
│   ├── BaseSignature.md
│   ├── BinaryOperator.md
│   ├── FuncID.md
│   ├── InterProceduralEdge.md
│   ├── InterProceduralSrcType.md
│   ├── IntraProceduralEdge.md
│   ├── Kind.md
│   ├── Method.md
│   ├── NodeID.md
│   ├── PagNodeType.md
│   └── Signature.md
└── variables
    ├── ALL.md
    ├── ANONYMOUS_CLASS_DELIMITER.md
    ├── ANONYMOUS_CLASS_PREFIX.md
    ├── ANONYMOUS_METHOD_PREFIX.md
    ├── ANY_KEYWORD.md
    ├── ARKTS_STATIC_MARK.md
    ├── BIGINT_KEYWORD.md
    ├── BOOLEAN_KEYWORD.md
    ├── BUILD_PROFILE_JSON5.md
    ├── BUILDER_DECORATOR.md
    ├── BUILDER_PARAM_DECORATOR.md
    ├── BUILDIN_ATOMIC_COMPONENT.md
    ├── BUILDIN_SYSTEM_COMPONENT.md
    ├── CALL_BACK.md
    ├── CALL_SIGNATURE_NAME.md
    ├── CALLBACK_METHOD_NAME.md
    ├── COMPONENT_ATTRIBUTE.md
    ├── COMPONENT_BRANCH_FUNCTION.md
    ├── COMPONENT_BUILD_FUNCTION.md
    ├── COMPONENT_COMMON.md
    ├── COMPONENT_CREATE_FUNCTION.md
    ├── COMPONENT_CUSTOMVIEW.md
    ├── COMPONENT_DECORATOR.md
    ├── COMPONENT_FOR_EACH.md
    ├── COMPONENT_IF_BRANCH.md
    ├── COMPONENT_IF.md
    ├── COMPONENT_INSTANCE.md
    ├── COMPONENT_LAZY_FOR_EACH.md
    ├── COMPONENT_LIFECYCLE_METHOD_NAME.md
    ├── COMPONENT_POP_FUNCTION.md
    ├── COMPONENT_REPEAT.md
    ├── CONSTRUCTOR_NAME.md
    ├── DECLARE_KEYWORD.md
    ├── DEFAULT_ARK_CLASS_NAME.md
    ├── DEFAULT_ARK_METHOD_NAME.md
    ├── DEFAULT_NAME.md
    ├── DEFAULT.md
    ├── ENTRY_DECORATOR.md
    ├── ETS_COMPILER_OPTIONS.md
    ├── FUNCTION.md
    ├── GLOBAL_THIS_NAME.md
    ├── IMPORT.md
    ├── INSTANCE_INIT_METHOD_NAME.md
    ├── LEXICAL_ENV_NAME_PREFIX.md
    ├── LIFECYCLE_METHOD_NAME.md
    ├── NAME_DELIMITER.md
    ├── NAME_PREFIX.md
    ├── NEVER_KEYWORD.md
    ├── NULL_KEYWORD.md
    ├── NUMBER_KEYWORD.md
    ├── OH_PACKAGE_JSON5.md
    ├── ON_OFF.md
    ├── PROMISE.md
    ├── SPECIAL_CONTAINER_COMPONENT.md
    ├── STATIC_BLOCK_METHOD_NAME_PREFIX.md
    ├── STATIC_INIT_METHOD_NAME.md
    ├── STRING_KEYWORD.md
    ├── SUPER_NAME.md
    ├── TEMP_LOCAL_PREFIX.md
    ├── THIS_NAME.md
    ├── TSCONFIG_JSON.md
    ├── UNDEFINED_KEYWORD.md
    ├── UNKNOWN_CLASS_NAME.md
    ├── UNKNOWN_FIELD_NAME.md
    ├── UNKNOWN_FILE_NAME.md
    ├── UNKNOWN_KEYWORD.md
    ├── UNKNOWN_METHOD_NAME.md
    ├── UNKNOWN_NAME.md
    ├── UNKNOWN_NAMESPACE_NAME.md
    ├── UNKNOWN_PROJECT_NAME.md
    └── VOID_KEYWORD.md

76 directories, 2373 files




============================================================
## FILE: `type-aliases/AliasTypeOriginalModel.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / AliasTypeOriginalModel

# Type Alias: AliasTypeOriginalModel

> **AliasTypeOriginalModel** = [`Type`](../classes/Type.md) \| [`ImportInfo`](../classes/ImportInfo.md) \| [`Local`](../classes/Local.md) \| [`ArkClass`](../classes/ArkClass.md) \| [`ArkMethod`](../classes/ArkMethod.md) \| [`ArkField`](../classes/ArkField.md)

Defined in: src/core/base/Expr.ts:1007




============================================================
## FILE: `type-aliases/BaseSignature.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BaseSignature

# Type Alias: BaseSignature

> **BaseSignature** = [`ClassSignature`](../classes/ClassSignature.md) \| [`NamespaceSignature`](../classes/NamespaceSignature.md)

Defined in: src/core/model/ArkSignature.ts:215




============================================================
## FILE: `type-aliases/BinaryOperator.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BinaryOperator

# Type Alias: BinaryOperator

> **BinaryOperator** = [`NormalBinaryOperator`](../enumerations/NormalBinaryOperator.md) \| [`RelationalBinaryOperator`](../enumerations/RelationalBinaryOperator.md)

Defined in: src/core/base/Expr.ts:576




============================================================
## FILE: `type-aliases/FuncID.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / FuncID

# Type Alias: FuncID

> **FuncID** = `number`

Defined in: src/callgraph/model/CallGraph.ts:28




============================================================
## FILE: `type-aliases/InterProceduralEdge.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / InterProceduralEdge

# Type Alias: InterProceduralEdge

> **InterProceduralEdge** = `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1047

## Properties

### dst

> **dst**: [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1049

***

### kind

> **kind**: [`PagEdgeKind`](../enumerations/PagEdgeKind.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1050

***

### src

> **src**: [`InterProceduralSrcType`](InterProceduralSrcType.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1048




============================================================
## FILE: `type-aliases/InterProceduralSrcType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / InterProceduralSrcType

# Type Alias: InterProceduralSrcType

> **InterProceduralSrcType** = [`Local`](../classes/Local.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1040




============================================================
## FILE: `type-aliases/IntraProceduralEdge.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / IntraProceduralEdge

# Type Alias: IntraProceduralEdge

> **IntraProceduralEdge** = `object`

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1041

## Properties

### dst

> **dst**: [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1043

***

### kind

> **kind**: [`PagEdgeKind`](../enumerations/PagEdgeKind.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1044

***

### src

> **src**: [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1042

***

### stmt

> **stmt**: [`Stmt`](../classes/Stmt.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:1045




============================================================
## FILE: `type-aliases/Kind.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Kind

# Type Alias: Kind

> **Kind** = `number`

Defined in: src/core/graph/GraphTraits.ts:17




============================================================
## FILE: `type-aliases/Method.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Method

# Type Alias: Method

> **Method** = [`MethodSignature`](../classes/MethodSignature.md)

Defined in: src/callgraph/model/CallGraph.ts:27




============================================================
## FILE: `type-aliases/NodeID.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / NodeID

# Type Alias: NodeID

> **NodeID** = `number`

Defined in: src/core/graph/GraphTraits.ts:16




============================================================
## FILE: `type-aliases/PagNodeType.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PagNodeType

# Type Alias: PagNodeType

> **PagNodeType** = [`Value`](../interfaces/Value.md)

Defined in: src/callgraph/pointerAnalysis/Pag.ts:37




============================================================
## FILE: `type-aliases/Signature.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / Signature

# Type Alias: Signature

> **Signature** = [`FileSignature`](../classes/FileSignature.md) \| [`NamespaceSignature`](../classes/NamespaceSignature.md) \| [`ClassSignature`](../classes/ClassSignature.md) \| [`MethodSignature`](../classes/MethodSignature.md) \| [`FieldSignature`](../classes/FieldSignature.md) \| [`LocalSignature`](../classes/LocalSignature.md) \| [`AliasTypeSignature`](../classes/AliasTypeSignature.md)

Defined in: src/core/model/ArkSignature.ts:31




============================================================
## FILE: `variables/ALL.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ALL

# Variable: ALL

> `const` **ALL**: `"*"` = `'*'`

Defined in: src/core/common/TSConst.ts:23




============================================================
## FILE: `variables/ANONYMOUS_CLASS_DELIMITER.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ANONYMOUS\_CLASS\_DELIMITER

# Variable: ANONYMOUS\_CLASS\_DELIMITER

> `const` **ANONYMOUS\_CLASS\_DELIMITER**: `"$"` = `NAME_DELIMITER`

Defined in: src/core/common/Const.ts:25




============================================================
## FILE: `variables/ANONYMOUS_CLASS_PREFIX.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ANONYMOUS\_CLASS\_PREFIX

# Variable: ANONYMOUS\_CLASS\_PREFIX

> `const` **ANONYMOUS\_CLASS\_PREFIX**: `string`

Defined in: src/core/common/Const.ts:24




============================================================
## FILE: `variables/ANONYMOUS_METHOD_PREFIX.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ANONYMOUS\_METHOD\_PREFIX

# Variable: ANONYMOUS\_METHOD\_PREFIX

> `const` **ANONYMOUS\_METHOD\_PREFIX**: `string`

Defined in: src/core/common/Const.ts:32




============================================================
## FILE: `variables/ANY_KEYWORD.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ANY\_KEYWORD

# Variable: ANY\_KEYWORD

> `const` **ANY\_KEYWORD**: `"any"` = `'any'`

Defined in: src/core/common/TSConst.ts:33




============================================================
## FILE: `variables/ARKTS_STATIC_MARK.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ARKTS\_STATIC\_MARK

# Variable: ARKTS\_STATIC\_MARK

> `const` **ARKTS\_STATIC\_MARK**: `"use static"` = `'use static'`

Defined in: src/core/common/Const.ts:48




============================================================
## FILE: `variables/BIGINT_KEYWORD.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BIGINT\_KEYWORD

# Variable: BIGINT\_KEYWORD

> `const` **BIGINT\_KEYWORD**: `"bigint"` = `'bigint'`

Defined in: src/core/common/TSConst.ts:40




============================================================
## FILE: `variables/BOOLEAN_KEYWORD.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BOOLEAN\_KEYWORD

# Variable: BOOLEAN\_KEYWORD

> `const` **BOOLEAN\_KEYWORD**: `"boolean"` = `'boolean'`

Defined in: src/core/common/TSConst.ts:35




============================================================
## FILE: `variables/BUILDER_DECORATOR.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BUILDER\_DECORATOR

# Variable: BUILDER\_DECORATOR

> `const` **BUILDER\_DECORATOR**: `string` = `'Builder'`

Defined in: src/core/common/EtsConst.ts:985




============================================================
## FILE: `variables/BUILDER_PARAM_DECORATOR.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BUILDER\_PARAM\_DECORATOR

# Variable: BUILDER\_PARAM\_DECORATOR

> `const` **BUILDER\_PARAM\_DECORATOR**: `string` = `'BuilderParam'`

Defined in: src/core/common/EtsConst.ts:986




============================================================
## FILE: `variables/BUILDIN_ATOMIC_COMPONENT.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BUILDIN\_ATOMIC\_COMPONENT

# Variable: BUILDIN\_ATOMIC\_COMPONENT

> `const` **BUILDIN\_ATOMIC\_COMPONENT**: `Set`\<`string`\>

Defined in: src/core/common/EtsConst.ts:928




============================================================
## FILE: `variables/BUILDIN_SYSTEM_COMPONENT.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BUILDIN\_SYSTEM\_COMPONENT

# Variable: BUILDIN\_SYSTEM\_COMPONENT

> `const` **BUILDIN\_SYSTEM\_COMPONENT**: `Set`\<`string`\>

Defined in: src/core/common/EtsConst.ts:926




============================================================
## FILE: `variables/BUILD_PROFILE_JSON5.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / BUILD\_PROFILE\_JSON5

# Variable: BUILD\_PROFILE\_JSON5

> `const` **BUILD\_PROFILE\_JSON5**: `"build-profile.json5"` = `'build-profile.json5'`

Defined in: src/core/common/EtsConst.ts:1020




============================================================
## FILE: `variables/CALLBACK_METHOD_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / CALLBACK\_METHOD\_NAME

# Variable: CALLBACK\_METHOD\_NAME

> `const` **CALLBACK\_METHOD\_NAME**: `string`[]

Defined in: src/utils/entryMethodUtils.ts:49




============================================================
## FILE: `variables/CALL_BACK.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / CALL\_BACK

# Variable: CALL\_BACK

> `const` **CALL\_BACK**: `string` = `'Callback'`

Defined in: src/core/common/EtsConst.ts:1016




============================================================
## FILE: `variables/CALL_SIGNATURE_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / CALL\_SIGNATURE\_NAME

# Variable: CALL\_SIGNATURE\_NAME

> `const` **CALL\_SIGNATURE\_NAME**: `"create"` = `'create'`

Defined in: src/core/common/Const.ts:33




============================================================
## FILE: `variables/COMPONENT_ATTRIBUTE.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_ATTRIBUTE

# Variable: COMPONENT\_ATTRIBUTE

> `const` **COMPONENT\_ATTRIBUTE**: `string` = `'Attribute'`

Defined in: src/core/common/EtsConst.ts:1015




============================================================
## FILE: `variables/COMPONENT_BRANCH_FUNCTION.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_BRANCH\_FUNCTION

# Variable: COMPONENT\_BRANCH\_FUNCTION

> `const` **COMPONENT\_BRANCH\_FUNCTION**: `string` = `'branch'`

Defined in: src/core/common/EtsConst.ts:1007




============================================================
## FILE: `variables/COMPONENT_BUILD_FUNCTION.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_BUILD\_FUNCTION

# Variable: COMPONENT\_BUILD\_FUNCTION

> `const` **COMPONENT\_BUILD\_FUNCTION**: `string` = `'build'`

Defined in: src/core/common/EtsConst.ts:1008




============================================================
## FILE: `variables/COMPONENT_COMMON.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_COMMON

# Variable: COMPONENT\_COMMON

> `const` **COMPONENT\_COMMON**: `string` = `'Common'`

Defined in: src/core/common/EtsConst.ts:1012




============================================================
## FILE: `variables/COMPONENT_CREATE_FUNCTION.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_CREATE\_FUNCTION

# Variable: COMPONENT\_CREATE\_FUNCTION

> `const` **COMPONENT\_CREATE\_FUNCTION**: `string` = `'create'`

Defined in: src/core/common/EtsConst.ts:1000




============================================================
## FILE: `variables/COMPONENT_CUSTOMVIEW.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_CUSTOMVIEW

# Variable: COMPONENT\_CUSTOMVIEW

> `const` **COMPONENT\_CUSTOMVIEW**: `string` = `'View'`

Defined in: src/core/common/EtsConst.ts:1002




============================================================
## FILE: `variables/COMPONENT_DECORATOR.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_DECORATOR

# Variable: COMPONENT\_DECORATOR

> `const` **COMPONENT\_DECORATOR**: `Set`\<`string`\>

Defined in: src/core/common/EtsConst.ts:983




============================================================
## FILE: `variables/COMPONENT_FOR_EACH.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_FOR\_EACH

# Variable: COMPONENT\_FOR\_EACH

> `const` **COMPONENT\_FOR\_EACH**: `string` = `'ForEach'`

Defined in: src/core/common/EtsConst.ts:923




============================================================
## FILE: `variables/COMPONENT_IF.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_IF

# Variable: COMPONENT\_IF

> `const` **COMPONENT\_IF**: `string` = `'If'`

Defined in: src/core/common/EtsConst.ts:1005




============================================================
## FILE: `variables/COMPONENT_IF_BRANCH.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_IF\_BRANCH

# Variable: COMPONENT\_IF\_BRANCH

> `const` **COMPONENT\_IF\_BRANCH**: `string` = `'IfBranch'`

Defined in: src/core/common/EtsConst.ts:1006




============================================================
## FILE: `variables/COMPONENT_INSTANCE.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_INSTANCE

# Variable: COMPONENT\_INSTANCE

> `const` **COMPONENT\_INSTANCE**: `string` = `'Instance'`

Defined in: src/core/common/EtsConst.ts:1013




============================================================
## FILE: `variables/COMPONENT_LAZY_FOR_EACH.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_LAZY\_FOR\_EACH

# Variable: COMPONENT\_LAZY\_FOR\_EACH

> `const` **COMPONENT\_LAZY\_FOR\_EACH**: `string` = `'LazyForEach'`

Defined in: src/core/common/EtsConst.ts:924




============================================================
## FILE: `variables/COMPONENT_LIFECYCLE_METHOD_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_LIFECYCLE\_METHOD\_NAME

# Variable: COMPONENT\_LIFECYCLE\_METHOD\_NAME

> `const` **COMPONENT\_LIFECYCLE\_METHOD\_NAME**: `string`[]

Defined in: src/utils/entryMethodUtils.ts:68




============================================================
## FILE: `variables/COMPONENT_POP_FUNCTION.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_POP\_FUNCTION

# Variable: COMPONENT\_POP\_FUNCTION

> `const` **COMPONENT\_POP\_FUNCTION**: `string` = `'pop'`

Defined in: src/core/common/EtsConst.ts:1001




============================================================
## FILE: `variables/COMPONENT_REPEAT.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / COMPONENT\_REPEAT

# Variable: COMPONENT\_REPEAT

> `const` **COMPONENT\_REPEAT**: `string` = `'Repeat'`

Defined in: src/core/common/EtsConst.ts:1003




============================================================
## FILE: `variables/CONSTRUCTOR_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / CONSTRUCTOR\_NAME

# Variable: CONSTRUCTOR\_NAME

> `const` **CONSTRUCTOR\_NAME**: `"constructor"` = `'constructor'`

Defined in: src/core/common/TSConst.ts:16




============================================================
## FILE: `variables/DECLARE_KEYWORD.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DECLARE\_KEYWORD

# Variable: DECLARE\_KEYWORD

> `const` **DECLARE\_KEYWORD**: `"DeclareKeyword"` = `'DeclareKeyword'`

Defined in: src/core/common/TSConst.ts:30




============================================================
## FILE: `variables/DEFAULT.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DEFAULT

# Variable: DEFAULT

> `const` **DEFAULT**: `"default"` = `'default'`

Defined in: src/core/common/TSConst.ts:21




============================================================
## FILE: `variables/DEFAULT_ARK_CLASS_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DEFAULT\_ARK\_CLASS\_NAME

# Variable: DEFAULT\_ARK\_CLASS\_NAME

> `const` **DEFAULT\_ARK\_CLASS\_NAME**: `string`

Defined in: src/core/common/Const.ts:23




============================================================
## FILE: `variables/DEFAULT_ARK_METHOD_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DEFAULT\_ARK\_METHOD\_NAME

# Variable: DEFAULT\_ARK\_METHOD\_NAME

> `const` **DEFAULT\_ARK\_METHOD\_NAME**: `string`

Defined in: src/core/common/Const.ts:28




============================================================
## FILE: `variables/DEFAULT_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / DEFAULT\_NAME

# Variable: DEFAULT\_NAME

> `const` **DEFAULT\_NAME**: `"dflt"` = `'dflt'`

Defined in: src/core/common/Const.ts:20




============================================================
## FILE: `variables/ENTRY_DECORATOR.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ENTRY\_DECORATOR

# Variable: ENTRY\_DECORATOR

> `const` **ENTRY\_DECORATOR**: `string` = `'Entry'`

Defined in: src/core/common/EtsConst.ts:984




============================================================
## FILE: `variables/ETS_COMPILER_OPTIONS.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ETS\_COMPILER\_OPTIONS

# Variable: ETS\_COMPILER\_OPTIONS

> `const` **ETS\_COMPILER\_OPTIONS**: `object`

Defined in: src/core/common/EtsConst.ts:16

## Type declaration

### ets

> **ets**: `object`

#### ets.components

> **components**: `string`[]

#### ets.concurrent

> **concurrent**: `object`

#### ets.concurrent.decorator

> **decorator**: `string` = `'Concurrent'`

#### ets.customComponent

> **customComponent**: `string` = `'CustomComponent'`

#### ets.emitDecorators

> **emitDecorators**: `object`[]

#### ets.extend

> **extend**: `object`

#### ets.extend.components

> **components**: `object`[]

#### ets.extend.decorator

> **decorator**: `string`[]

#### ets.libs

> **libs**: `never`[] = `[]`

#### ets.propertyDecorators

> **propertyDecorators**: `object`[]

#### ets.render

> **render**: `object`

#### ets.render.decorator

> **decorator**: `string`[]

#### ets.render.method

> **method**: `string`[]

#### ets.styles

> **styles**: `object`

#### ets.styles.component

> **component**: `object`

#### ets.styles.component.instance

> **instance**: `string` = `'CommonInstance'`

#### ets.styles.component.name

> **name**: `string` = `'Common'`

#### ets.styles.component.type

> **type**: `string` = `'T'`

#### ets.styles.decorator

> **decorator**: `string` = `'Styles'`

#### ets.styles.property

> **property**: `string` = `'stateStyles'`

#### ets.syntaxComponents

> **syntaxComponents**: `object`

#### ets.syntaxComponents.attrUICallback

> **attrUICallback**: `object`[]

#### ets.syntaxComponents.paramsUICallback

> **paramsUICallback**: `string`[]




============================================================
## FILE: `variables/FUNCTION.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / FUNCTION

# Variable: FUNCTION

> `const` **FUNCTION**: `"Function"` = `'Function'`

Defined in: src/core/common/TSConst.ts:27




============================================================
## FILE: `variables/GLOBAL_THIS_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / GLOBAL\_THIS\_NAME

# Variable: GLOBAL\_THIS\_NAME

> `const` **GLOBAL\_THIS\_NAME**: `string` = `'globalThis'`

Defined in: src/core/common/TSConst.ts:19




============================================================
## FILE: `variables/IMPORT.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / IMPORT

# Variable: IMPORT

> `const` **IMPORT**: `"import"` = `'import'`

Defined in: src/core/common/TSConst.ts:25




============================================================
## FILE: `variables/INSTANCE_INIT_METHOD_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / INSTANCE\_INIT\_METHOD\_NAME

# Variable: INSTANCE\_INIT\_METHOD\_NAME

> `const` **INSTANCE\_INIT\_METHOD\_NAME**: `string`

Defined in: src/core/common/Const.ts:29




============================================================
## FILE: `variables/LEXICAL_ENV_NAME_PREFIX.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / LEXICAL\_ENV\_NAME\_PREFIX

# Variable: LEXICAL\_ENV\_NAME\_PREFIX

> `const` **LEXICAL\_ENV\_NAME\_PREFIX**: `string`

Defined in: src/core/common/Const.ts:45




============================================================
## FILE: `variables/LIFECYCLE_METHOD_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / LIFECYCLE\_METHOD\_NAME

# Variable: LIFECYCLE\_METHOD\_NAME

> `const` **LIFECYCLE\_METHOD\_NAME**: `string`[]

Defined in: src/utils/entryMethodUtils.ts:21




============================================================
## FILE: `variables/NAME_DELIMITER.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / NAME\_DELIMITER

# Variable: NAME\_DELIMITER

> `const` **NAME\_DELIMITER**: `"$"` = `'$'`

Defined in: src/core/common/Const.ts:17




============================================================
## FILE: `variables/NAME_PREFIX.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / NAME\_PREFIX

# Variable: NAME\_PREFIX

> `const` **NAME\_PREFIX**: `"%"` = `'%'`

Defined in: src/core/common/Const.ts:18




============================================================
## FILE: `variables/NEVER_KEYWORD.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / NEVER\_KEYWORD

# Variable: NEVER\_KEYWORD

> `const` **NEVER\_KEYWORD**: `"never"` = `'never'`

Defined in: src/core/common/TSConst.ts:39




============================================================
## FILE: `variables/NULL_KEYWORD.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / NULL\_KEYWORD

# Variable: NULL\_KEYWORD

> `const` **NULL\_KEYWORD**: `"null"` = `'null'`

Defined in: src/core/common/TSConst.ts:31




============================================================
## FILE: `variables/NUMBER_KEYWORD.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / NUMBER\_KEYWORD

# Variable: NUMBER\_KEYWORD

> `const` **NUMBER\_KEYWORD**: `"number"` = `'number'`

Defined in: src/core/common/TSConst.ts:36




============================================================
## FILE: `variables/OH_PACKAGE_JSON5.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / OH\_PACKAGE\_JSON5

# Variable: OH\_PACKAGE\_JSON5

> `const` **OH\_PACKAGE\_JSON5**: `"oh-package.json5"` = `'oh-package.json5'`

Defined in: src/core/common/EtsConst.ts:1019




============================================================
## FILE: `variables/ON_OFF.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / ON\_OFF

# Variable: ON\_OFF

> `const` **ON\_OFF**: `Set`\<`string`\>

Defined in: src/core/common/EtsConst.ts:1017




============================================================
## FILE: `variables/PROMISE.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / PROMISE

# Variable: PROMISE

> `const` **PROMISE**: `"Promise"` = `'Promise'`

Defined in: src/core/common/TSConst.ts:26




============================================================
## FILE: `variables/SPECIAL_CONTAINER_COMPONENT.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / SPECIAL\_CONTAINER\_COMPONENT

# Variable: SPECIAL\_CONTAINER\_COMPONENT

> `const` **SPECIAL\_CONTAINER\_COMPONENT**: `Set`\<`string`\>

Defined in: src/core/common/EtsConst.ts:1010




============================================================
## FILE: `variables/STATIC_BLOCK_METHOD_NAME_PREFIX.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / STATIC\_BLOCK\_METHOD\_NAME\_PREFIX

# Variable: STATIC\_BLOCK\_METHOD\_NAME\_PREFIX

> `const` **STATIC\_BLOCK\_METHOD\_NAME\_PREFIX**: `string`

Defined in: src/core/common/Const.ts:31




============================================================
## FILE: `variables/STATIC_INIT_METHOD_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / STATIC\_INIT\_METHOD\_NAME

# Variable: STATIC\_INIT\_METHOD\_NAME

> `const` **STATIC\_INIT\_METHOD\_NAME**: `string`

Defined in: src/core/common/Const.ts:30




============================================================
## FILE: `variables/STRING_KEYWORD.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / STRING\_KEYWORD

# Variable: STRING\_KEYWORD

> `const` **STRING\_KEYWORD**: `"string"` = `'string'`

Defined in: src/core/common/TSConst.ts:37




============================================================
## FILE: `variables/SUPER_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / SUPER\_NAME

# Variable: SUPER\_NAME

> `const` **SUPER\_NAME**: `"super"` = `'super'`

Defined in: src/core/common/TSConst.ts:17




============================================================
## FILE: `variables/TEMP_LOCAL_PREFIX.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / TEMP\_LOCAL\_PREFIX

# Variable: TEMP\_LOCAL\_PREFIX

> `const` **TEMP\_LOCAL\_PREFIX**: `"%"` = `NAME_PREFIX`

Defined in: src/core/common/Const.ts:44




============================================================
## FILE: `variables/THIS_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / THIS\_NAME

# Variable: THIS\_NAME

> `const` **THIS\_NAME**: `"this"` = `'this'`

Defined in: src/core/common/TSConst.ts:18




============================================================
## FILE: `variables/TSCONFIG_JSON.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / TSCONFIG\_JSON

# Variable: TSCONFIG\_JSON

> `const` **TSCONFIG\_JSON**: `"tsconfig.json"` = `'tsconfig.json'`

Defined in: src/core/common/TSConst.ts:41




============================================================
## FILE: `variables/UNDEFINED_KEYWORD.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UNDEFINED\_KEYWORD

# Variable: UNDEFINED\_KEYWORD

> `const` **UNDEFINED\_KEYWORD**: `"undefined"` = `'undefined'`

Defined in: src/core/common/TSConst.ts:32




============================================================
## FILE: `variables/UNKNOWN_CLASS_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UNKNOWN\_CLASS\_NAME

# Variable: UNKNOWN\_CLASS\_NAME

> `const` **UNKNOWN\_CLASS\_NAME**: `""` = `''`

Defined in: src/core/common/Const.ts:39




============================================================
## FILE: `variables/UNKNOWN_FIELD_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UNKNOWN\_FIELD\_NAME

# Variable: UNKNOWN\_FIELD\_NAME

> `const` **UNKNOWN\_FIELD\_NAME**: `""` = `''`

Defined in: src/core/common/Const.ts:40




============================================================
## FILE: `variables/UNKNOWN_FILE_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UNKNOWN\_FILE\_NAME

# Variable: UNKNOWN\_FILE\_NAME

> `const` **UNKNOWN\_FILE\_NAME**: `string`

Defined in: src/core/common/Const.ts:37




============================================================
## FILE: `variables/UNKNOWN_KEYWORD.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UNKNOWN\_KEYWORD

# Variable: UNKNOWN\_KEYWORD

> `const` **UNKNOWN\_KEYWORD**: `"unknown"` = `'unknown'`

Defined in: src/core/common/TSConst.ts:34




============================================================
## FILE: `variables/UNKNOWN_METHOD_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UNKNOWN\_METHOD\_NAME

# Variable: UNKNOWN\_METHOD\_NAME

> `const` **UNKNOWN\_METHOD\_NAME**: `""` = `''`

Defined in: src/core/common/Const.ts:41




============================================================
## FILE: `variables/UNKNOWN_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UNKNOWN\_NAME

# Variable: UNKNOWN\_NAME

> `const` **UNKNOWN\_NAME**: `"unk"` = `'unk'`

Defined in: src/core/common/Const.ts:19




============================================================
## FILE: `variables/UNKNOWN_NAMESPACE_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UNKNOWN\_NAMESPACE\_NAME

# Variable: UNKNOWN\_NAMESPACE\_NAME

> `const` **UNKNOWN\_NAMESPACE\_NAME**: `string`

Defined in: src/core/common/Const.ts:38




============================================================
## FILE: `variables/UNKNOWN_PROJECT_NAME.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / UNKNOWN\_PROJECT\_NAME

# Variable: UNKNOWN\_PROJECT\_NAME

> `const` **UNKNOWN\_PROJECT\_NAME**: `string`

Defined in: src/core/common/Const.ts:36




============================================================
## FILE: `variables/VOID_KEYWORD.md`
============================================================

[**ArkAnalyzer**](../README.md)

***

[ArkAnalyzer](../globals.md) / VOID\_KEYWORD

# Variable: VOID\_KEYWORD

> `const` **VOID\_KEYWORD**: `"void"` = `'void'`

Defined in: src/core/common/TSConst.ts:38




============================================================
## FILE: `项目背景.md`
============================================================


api_docs已在github上开源，地址:https://github.com/z652011350/api_docs/blob/main/globals.md
全局api索引信息：https://github.com/z652011350/api_docs/blob/main/globals.md
每个api均在该代码仓库中，可以直接查询


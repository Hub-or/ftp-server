<h1 align="center"> FTP server side program 🐞</h1>

<p align="center">
  <a href="https://github.com/ZhelinCheng/mint-filter" target="_blank">
    <img alt="GitHub package.json version" src="https://img.shields.io/github/package-json/v/ZhelinCheng/mint-filter.svg">
  </a>

  <a href="https://www.npmjs.com/package/mint-filter" target="_blank">
    <img alt="Version" src="https://img.shields.io/npm/v/mint-filter.svg">
  </a>

  <a href="https://www.npmjs.com/package/mint-filter" target="_blank">
    <img alt="Download" src="https://img.shields.io/npm/dm/mint-filter.svg">
  </a>

  <a href="https://coveralls.io/github/ZhelinCheng/mint-filter?branch=master" target="_blank">
    <img alt="Coverage" src="https://coveralls.io/repos/github/ZhelinCheng/mint-filter/badge.svg?branch=master">
  </a>

  <br/>

  <a href="https://github.com/ZhelinCheng/mint-filter/actions" target="_blank">
    <img alt="Coverage" src="https://github.com/ZhelinCheng/mint-filter/workflows/CI/badge.svg">
  </a>

  <a href="https://github.com/ZhelinCheng/mint-filter#readme" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/ZhelinCheng/mint-filter/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://github.com/ZhelinCheng/mint-filter/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/github/license/ZhelinCheng/mint-filter" />
  </a>
</p>


> Sensitive word filtering scheme based on the Aho–Corasick algorithm. The Aho–Corasick algorithm is a string search algorithm invented by Alfred V. Aho and Margaret J.Corasick. It is used to match a limited set of "dictionaries" in an input string. " substring in ". It differs from ordinary string matching in that it matches all dictionary strings at the same time. The algorithm has an approximately linear time complexity when amortized, which is approximately the length of the string plus the number of all matches.

## 1. Package


## 1. Install

```sh
yarn add mint-filter
```



## 2. Use

### CommonJS Import
```javascript
const { Mint } = require('mint-filter')
```

### TypeScript / ES Module Reference

```typescript
import Mint from 'mint-filter'
const mint = new Mint(['/n', 'text'])

// Basic use
mint.filter(`
Text to be checked.`)
```



## 3. Constructor

• **new Mint**(`Keys to be check.`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `Keys to be check.` | `string`[] |

#### Define on

[index.ts:26](https://github.com/ZhelinCheng/mint-filter/blob/f25e001/src/index.ts#L26)



## 4.Methods (Functions)

### Add key word

▸ **add**(`key`, `build?`): `boolean`

**`Example`**

```typescript
const status = mint.add('Text')
```

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `key` | `string` | `undefined` | Key word |
| `build` | `boolean` | `true` | Whether to build a tree, no need to pass by default |

#### Returns

`boolean` (status)

#### Define on

[index.ts:233](https://github.com/ZhelinCheng/mint-filter/blob/f25e001/src/index.ts#L233)

___

### Delete key word

▸ **delete**(`key`): ``"update"`` \| ``"delete"``

**`Example`**

```typescript
const status = mint.delete('key')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `key` | `string` | Key word |

#### Returns

``"update"`` \| ``"delete"``

Status (update | delete), informs the user whether the node in the tree has been deleted or simply updated.

#### Define on

[index.ts:169](https://github.com/ZhelinCheng/mint-filter/blob/f25e001/src/index.ts#L169)

___

### Filter text

▸ **filter**(`text`, `options?`): `FilterData`

**`Example`**

```typescript
mint.add('unpassable')
let status = mint.filter('An unpassable text.')
console.log(status) // { words: ["unpassable"], text: "An ********** text." }

status = mint.filter('An unpassable text.', { replace: false })
console.log(status) // { words: ["unpassable"], text: "An unpassable text." }
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `text` | `string` | Text content |
| `options?` | `Pick`<`FilterOptions`, ``"replace"``\> | - |

#### Returns

`FilterData`

#### Define on

[index.ts:134](https://github.com/ZhelinCheng/mint-filter/blob/f25e001/src/index.ts#L134)

___

### Check whether the text passes validation

▸ **verify**(`text`): `boolean`


**`Example`**

```typescript
mint.add('unpassable')
const status = mint.verify('An unpassable text.')
console.log(status) // false
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `text` | `string` | Text content |

#### Returns

`boolean`

#### Define on

[index.ts:152](https://github.com/ZhelinCheng/mint-filter/blob/f25e001/src/index.ts#L152)



## 5. Test script

```sh
yarn run test
```


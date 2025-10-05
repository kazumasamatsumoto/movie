# #015 「バックスラッシュのエスケープ - \\」

## 概要
TypeScript v5.9のバックスラッシュエスケープについて学習します。バックスラッシュ文字自体を表現する方法を理解します。

## 学習目標
- バックスラッシュエスケープの基本を理解する
- ファイルパスでの使用方法を理解する
- 正規表現での活用方法を理解する

## 画面表示用コード

```typescript
// バックスラッシュのエスケープ
let windowsPath: string = "C:\\Users\\Documents\\file.txt";
let unixPath: string = "/home/user/documents/file.txt";
let regexPattern: string = "\\d+\\s+\\w+";

// 実用的な例
let configPath: string = "C:\\Program Files\\MyApp\\config.json";
let logPath: string = "D:\\Logs\\application.log";
let assetPath: string = "assets\\images\\logo.png";

// 正規表現での使用
let phonePattern: string = "\\d{3}-\\d{4}-\\d{4}";
let emailPattern: string = "\\w+@\\w+\\.\\w+";
```

## 重要なポイント
1. **バックスラッシュ**: \\でバックスラッシュ文字を表現
2. **ファイルパス**: Windowsのファイルパスで必要
3. **正規表現**: 正規表現パターンで特殊文字をエスケープ

## 次のステップ
次回は、改行のエスケープについて学習します。
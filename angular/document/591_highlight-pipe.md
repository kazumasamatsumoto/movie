# #591 「Highlight Pipe - テキストハイライト」

## 概要
HighlightPipeは文字列内のキーワードをハイライト用タグ（例: `<mark>`）に置き換え、検索結果やマッチ箇所を強調表示するカスタムPipe。

## 学習目標
- HighlightPipeの用途と実装手順を理解する
- 正規表現でキーワードをハイライトする方法を学ぶ
- HTML変換後のサニタイズについて把握する

## 技術ポイント
- `transform(text: string, keyword: string): string`
- 正規表現でキーワード検出し`<mark>`タグで囲む
- `DomSanitizer.bypassSecurityTrustHtml`でサニタイズ

## 📺 画面表示用コード（動画用）
```typescript
transform(value: string, keyword: string): string {
  if (!keyword) return value;
  const pattern = new RegExp(keyword, 'gi');
  return value.replace(pattern, match => `<mark>${match}</mark>`);
}
```

## 💻 詳細実装例（学習用）
```typescript
@Pipe({
  name: 'highlight',
  standalone: true
})
export class HighlightPipe implements PipeTransform {
  constructor(private readonly sanitizer: DomSanitizer) {}

  transform(value: string, keyword: string): SafeHtml {
    if (!value || !keyword) return value;
    const pattern = new RegExp(`(${keyword.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
    const highlighted = value.replace(pattern, '<mark>$1</mark>');
    return this.sanitizer.bypassSecurityTrustHtml(highlighted);
  }
}
```

## ベストプラクティス
- 正規表現でキーワードをエスケープし、誤検出を防ぐ
- HTMLを生成するため `DomSanitizer` で信頼できるHTMLとしてマーキング
- Sass/CSSで`mark`タグにスタイルを当てて視認性を調整

## 注意点
- HTMLタグを生成するためXSS対策が必須
- 大文字小文字を区別しない検索時は`gi`フラグを利用
- null/undefinedに対応し、Pipeが例外を投げないようにする

## 関連技術
- PipeTransform
- DomSanitizer
- 正規表現による文字列置換

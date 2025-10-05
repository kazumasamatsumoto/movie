# #155 「ElementRef の注意点とリスク」

## 概要
Angular v20におけるElementRefの使用時の注意点とリスク。セキュリティ、プラットフォーム互換性、SSRでの問題など、ElementRefを使用する際に考慮すべき重要なポイントを学ぶ。

## 学習目標
- ElementRefの使用リスクを理解する
- セキュリティ問題を学ぶ
- 安全な実装方法を把握する

## 技術ポイント
- XSS攻撃のリスク
- SSRでの問題
- プラットフォーム依存のリスク
- 安全な代替手段

## 📺 画面表示用コード

### リスクのある実装例
```typescript
@Component({
  selector: 'app-risky',
  template: `
    <div #dangerousElement>危険な要素</div>
    <button (click)="dangerousOperation()">危険な操作</button>
  `
})
export class RiskyComponent {
  @ViewChild('dangerousElement') dangerousElement!: ElementRef;

  dangerousOperation() {
    // ❌ 危険: ユーザー入力の直接挿入
    const userInput = '<script>alert("XSS")</script>';
    this.dangerousElement.nativeElement.innerHTML = userInput;
    
    // ❌ 危険: 未検証のHTML挿入
    this.dangerousElement.nativeElement.outerHTML = '<div onclick="malicious()">Click me</div>';
  }
}
```

### 安全な実装例
```typescript
@Component({
  selector: 'app-safe',
  template: `
    <div #safeElement>安全な要素</div>
    <button (click)="safeOperation()">安全な操作</button>
  `
})
export class SafeComponent {
  @ViewChild('safeElement') safeElement!: ElementRef;

  safeOperation() {
    // ✅ 安全: textContentを使用
    const safeText = '安全なテキスト';
    this.safeElement.nativeElement.textContent = safeText;
    
    // ✅ 安全: 属性の直接設定
    this.safeElement.nativeElement.setAttribute('data-safe', 'true');
  }
}
```

## 実践的な活用例
- セキュアなDOM操作
- 安全なデータ表示
- 適切な検証の実装

## ベストプラクティス
- ユーザー入力の検証
- innerHTMLの回避
- Renderer2の使用推奨

## 注意点
- XSS攻撃の防止
- SSRでの動作確認
- セキュリティテストの実施

## 関連技術
- セキュリティ
- DOM操作
- XSS対策

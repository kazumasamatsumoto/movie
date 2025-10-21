# #383 「オブジェクトでのスタイル指定」

## 概要
`[ngStyle]`にオブジェクトを渡すと、プロパティごとにスタイルを指定でき、条件付きスタイルや複数プロパティの同時制御が容易になる。

## 学習目標
- オブジェクト形式の利点を理解する
- Falsy値でスタイルを削除する仕組みを把握する
- コンポーネントでスタイルオブジェクトを生成する手法を学ぶ

## 技術ポイント
- `Record<string, string | null>`を返す実装が一般的
- null/undefinedを許容してスタイルを外す
- 連動するスタイルは同じオブジェクトでまとめて管理

## 📺 画面表示用コード（動画用）
```html
<section [ngStyle]="{ background: theme.bg, color: theme.fg }">テーマパネル</section>
```

## 💻 詳細実装例（学習用）
```typescript
interface Theme {
  bg: string;
  fg: string;
}

@Component({
  selector: 'app-ngstyle-object-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section [ngStyle]="styles()">
      <h2>テーマ</h2>
      <p>現在のテーマ色に合わせてスタイルを適用。</p>
    </section>
  `
})
export class NgStyleObjectDemoComponent {
  private readonly theme = signal<Theme>({ bg: '#e0f2fe', fg: '#0f172a' });
  protected readonly styles = computed(() => ({
    background: this.theme().bg,
    color: this.theme().fg,
    padding: '1.5rem',
    borderRadius: '1rem'
  }));
}
```

## ベストプラクティス
- computedを活用してスタイルを再利用し、不要な再計算を避ける
- テーマやダークモードなど状態管理はサービスやSignalsで管理
- スタイルプロパティは型で管理して意図しない値を防止

## 注意点
- スタイル数が増えるとオブジェクトが肥大化するため、重要な差分だけ保持
- `null`を返したプロパティは削除されるが、期待と違う場合は空文字などで調整
- 重要なスタイルはCSSクラス化し、ngStyleは例外的な上書きに限定

## 関連技術
- Angular Signals
- Theme Service
- CSS変数

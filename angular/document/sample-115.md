# #115 「祖先-子孫間の通信戦略」

## 概要
Angular v20における祖先と子孫コンポーネント間の効率的な通信方法。createContext()とinject()を活用したContext APIを使用して、プロパティドリリングを回避した通信を実現する。

## 学習目標
- Context APIの基本的な使い方を理解する
- 祖先-子孫間通信の効率的なパターンを学ぶ
- プロパティドリリングの回避方法を把握する

## 技術ポイント
- createContext()によるコンテキスト作成
- inject()によるコンテキスト参照
- プロパティドリリングの回避
- 型安全なコンテキスト実装

## 📺 画面表示用コード

### Context の作成
```typescript
export interface ThemeContext {
  theme: string;
  toggleTheme: () => void;
}

export const THEME_CONTEXT = createContext<ThemeContext>({
  theme: 'light',
  toggleTheme: () => {}
});
```

### 祖先コンポーネント
```typescript
@Component({
  template: `
    <div [class]="theme">
      <app-parent>
        <app-child>
          <app-grandchild></app-grandchild>
        </app-child>
      </app-parent>
    </div>
  `
})
export class AncestorComponent {
  theme = 'light';

  toggleTheme() {
    this.theme = this.theme === 'light' ? 'dark' : 'light';
  }

  provide() {
    return {
      theme: this.theme,
      toggleTheme: () => this.toggleTheme()
    };
  }
}
```

### 子孫コンポーネント
```typescript
@Component({
  selector: 'app-grandchild',
  template: `
    <button (click)="toggleTheme()">
      テーマ切り替え: {{ theme }}
    </button>
  `
})
export class GrandchildComponent {
  themeContext = inject(THEME_CONTEXT);
  
  get theme() {
    return this.themeContext.theme;
  }

  toggleTheme() {
    this.themeContext.toggleTheme();
  }
}
```

## 実践的な活用例
- テーマ切り替え機能
- ユーザー認証状態の共有
- 言語設定の管理

## ベストプラクティス
- コンテキストの責任範囲を明確にする
- 型安全性を保った実装を行う
- 不要な再レンダリングを防ぐ

## 注意点
- コンテキストの過度な使用を避ける
- メモリリークを防ぐため、適切なクリーンアップを行う
- パフォーマンスを考慮した実装

## 関連技術
- Context API
- Dependency Injection
- 状態管理
- コンポーネント設計パターン

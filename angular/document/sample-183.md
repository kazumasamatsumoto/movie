# #183 「CSS Modules の活用」

## 概要
Angular v20におけるCSS Modulesの活用方法。コンポーネント固有のクラス名を自動生成し、スタイルの競合を回避しながら保守性の高いスタイル管理を実現する。

## 学習目標
- CSS Modulesの概念を理解する
- 自動スコープ化の仕組みを学ぶ
- 大規模アプリケーションでの活用を把握する

## 技術ポイント
- CSS Modulesの設定
- 自動的なクラス名生成
- スコープ化の仕組み
- 競合回避

## 📺 画面表示用コード

### CSS Modulesの基本的な使用
```typescript
@Component({
  selector: 'app-css-modules',
  template: `
    <div class="container">
      <h2>CSS Modules</h2>
      
      <div class="card">
        <h3>カードタイトル</h3>
        <p>CSS Modulesにより自動的にスコープ化されます</p>
        <button class="button primary">プライマリボタン</button>
        <button class="button secondary">セカンダリボタン</button>
      </div>
      
      <div class="list">
        <div class="list-item" *ngFor="let item of items">
          {{ item }}
        </div>
      </div>
    </div>
  `,
  styleUrls: ['./css-modules.component.css']
})
export class CssModulesComponent {
  items = ['項目1', '項目2', '項目3'];
}
```

### CSS Modules設定例
```css
/* css-modules.component.css */
.container {
  padding: 20px;
  max-width: 600px;
  margin: 0 auto;
}

.card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  margin: 15px 0;
}

.card h3 {
  color: #333;
  margin-bottom: 15px;
}

.button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin: 5px;
  transition: all 0.3s ease;
}

.button.primary {
  background: #007bff;
  color: white;
}

.button.secondary {
  background: #6c757d;
  color: white;
}

.list {
  margin-top: 20px;
}

.list-item {
  padding: 10px;
  border-bottom: 1px solid #eee;
  transition: background 0.3s ease;
}

.list-item:hover {
  background: #f8f9fa;
}
```

## 実践的な活用例
- 大規模アプリケーションのスタイル管理
- コンポーネント間のスタイル競合回避
- 保守性の向上

## ベストプラクティス
- 適切なモジュール設定
- 明確なクラス命名
- スコープの理解

## 注意点
- 設定の複雑さ
- デバッグの難しさ
- 学習コスト

## 関連技術
- CSS Modules
- 自動スコープ化
- スタイル競合回避

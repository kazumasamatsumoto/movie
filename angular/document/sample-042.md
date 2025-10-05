# #042 「(click) クリックイベント」台本

四国めたん「(click) クリックイベントについて解説します！」
ずんだもん「一番よく使うイベントだね」
四国めたん「はい！ボタンクリックや要素のタップで処理を実行できます」
ずんだもん「引数も渡せるの？」
四国めたん「はい！メソッドに値を渡すことも可能です」
ずんだもん「複数の処理も実行できる？」
四国めたん「メソッド内で複数の処理を組み合わせることができます」

---

## 📺 画面表示用コード

// 基本的なクリックイベント
```typescript
@Component({
  selector: 'app-click-basic',
  standalone: true,
  template: `
    <div class="click-demo">
      <h2>基本的なクリックイベント</h2>
      <button (click)="increment()">カウントアップ</button>
      <p>カウント: {{count}}</p>
    </div>
  `,
  styles: [`
    .click-demo {
      padding: 20px;
      text-align: center;
    }
    button {
      padding: 10px 20px;
      font-size: 16px;
    }
  `]
})
export class ClickBasicComponent {
  count = 0;
  
  increment() {
    this.count++;
  }
}
```

// 引数付きクリックイベント
```typescript
@Component({
  selector: 'app-click-with-args',
  standalone: true,
  template: `
    <div class="click-args-demo">
      <h2>引数付きクリックイベント</h2>
      <button (click)="selectItem('item1')">アイテム1</button>
      <button (click)="selectItem('item2')">アイテム2</button>
      <button (click)="selectItem('item3')">アイテム3</button>
      <p>選択中: {{selectedItem}}</p>
    </div>
  `,
  styles: [`
    .click-args-demo {
      padding: 20px;
    }
    button {
      margin: 5px;
      padding: 8px 16px;
    }
  `]
})
export class ClickWithArgsComponent {
  selectedItem = 'なし';
  
  selectItem(item: string) {
    this.selectedItem = item;
    console.log(`${item}が選択されました`);
  }
}
```

// 複数処理のクリックイベント
```typescript
@Component({
  selector: 'app-click-multiple',
  standalone: true,
  template: `
    <div class="click-multiple-demo">
      <h2>複数処理のクリックイベント</h2>
      <button (click)="processData()">データ処理</button>
      <p>処理回数: {{processCount}}</p>
      <p>最後の処理時刻: {{lastProcessTime}}</p>
    </div>
  `,
  styles: [`
    .click-multiple-demo {
      padding: 20px;
    }
    button {
      padding: 10px 20px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
    }
  `]
})
export class ClickMultipleComponent {
  processCount = 0;
  lastProcessTime = '';
  
  processData() {
    // 複数の処理を実行
    this.processCount++;
    this.lastProcessTime = new Date().toLocaleTimeString();
    
    // ログ出力
    console.log('データ処理を実行しました');
    
    // 外部API呼び出し（模擬）
    this.callExternalAPI();
  }
  
  private callExternalAPI() {
    // 実際のAPI呼び出し処理
    console.log('外部APIを呼び出しました');
  }
}
```

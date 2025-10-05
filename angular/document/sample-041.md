# #041 「(event) イベントバインディング基礎」台本

四国めたん「(event) イベントバインディング基礎について学びましょう！」
ずんだもん「イベントバインディングって何？」
四国めたん「ユーザーの操作に応じてComponentのメソッドを実行する仕組みです」
ずんだもん「どんな操作に対応できるの？」
四国めたん「クリック、入力、キーボード、マウスなど、様々なイベントに対応できます」
ずんだもん「どうやって使うの？」
四国めたん「括弧()でイベント名を囲み、メソッド名を指定します」

---

## 📺 画面表示用コード

// 基本的なイベントバインディング
```typescript
@Component({
  selector: 'app-event-basic',
  standalone: true,
  template: `
    <div class="event-demo">
      <h2>基本的なイベントバインディング</h2>
      <button (click)="onClick()">クリック</button>
      <p>クリック回数: {{clickCount}}</p>
    </div>
  `,
  styles: [`
    .event-demo {
      padding: 20px;
      text-align: center;
    }
    button {
      padding: 10px 20px;
      font-size: 16px;
    }
  `]
})
export class EventBasicComponent {
  clickCount = 0;
  
  onClick() {
    this.clickCount++;
    console.log('ボタンがクリックされました');
  }
}
```

// 複数のイベントハンドリング
```typescript
@Component({
  selector: 'app-multiple-events',
  standalone: true,
  template: `
    <div class="multiple-demo">
      <h2>複数のイベントハンドリング</h2>
      <div (mouseenter)="onMouseEnter()" 
           (mouseleave)="onMouseLeave()"
           [class.highlighted]="isHighlighted">
        マウスをホバー
      </div>
      <p>状態: {{status}}</p>
    </div>
  `,
  styles: [`
    .multiple-demo {
      padding: 20px;
    }
    div {
      padding: 20px;
      border: 2px solid #ccc;
      margin: 10px 0;
      transition: background-color 0.3s;
    }
    .highlighted {
      background-color: #ffffcc;
    }
  `]
})
export class MultipleEventsComponent {
  isHighlighted = false;
  status = '通常状態';
  
  onMouseEnter() {
    this.isHighlighted = true;
    this.status = 'ホバー中';
  }
  
  onMouseLeave() {
    this.isHighlighted = false;
    this.status = '通常状態';
  }
}
```

// カスタムイベントハンドラー
```typescript
@Component({
  selector: 'app-custom-handler',
  standalone: true,
  template: `
    <div class="custom-demo">
      <h2>カスタムイベントハンドラー</h2>
      <button (click)="handleClick('ボタン1')">ボタン1</button>
      <button (click)="handleClick('ボタン2')">ボタン2</button>
      <p>最後にクリックされた: {{lastClicked}}</p>
    </div>
  `,
  styles: [`
    .custom-demo {
      padding: 20px;
    }
    button {
      margin: 5px;
      padding: 8px 16px;
    }
  `]
})
export class CustomHandlerComponent {
  lastClicked = 'なし';
  
  handleClick(buttonName: string) {
    this.lastClicked = buttonName;
    console.log(`${buttonName}がクリックされました`);
  }
}
```

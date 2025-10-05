# #049 「$event オブジェクトの活用」台本

四国めたん「$event オブジェクトの活用について学びましょう！」
ずんだもん「$eventって何？」
四国めたん「イベント発生時の詳細情報が含まれたオブジェクトです」
ずんだもん「どんな情報が取得できるの？」
四国めたん「イベントの種類、ターゲット要素、座標、キー情報などが取得できます」
ずんだもん「どうやって使うの？」
四国めたん「メソッドの引数として$eventを受け取り、必要な情報を抽出します」

---

## 📺 画面表示用コード

// 基本的な$eventの使用
```typescript
@Component({
  selector: 'app-event-basic',
  standalone: true,
  template: `
    <div class="event-demo">
      <h2>基本的な$eventの使用</h2>
      <button (click)="onClick($event)">クリック</button>
      <p>イベントタイプ: {{eventType}}</p>
      <p>ターゲット: {{targetElement}}</p>
    </div>
  `,
  styles: [`
    .event-demo {
      padding: 20px;
    }
    button {
      padding: 10px 20px;
      margin: 10px 0;
    }
  `]
})
export class EventBasicComponent {
  eventType = '';
  targetElement = '';
  
  onClick(event: Event) {
    this.eventType = event.type;
    this.targetElement = (event.target as HTMLElement).tagName;
    console.log('イベント詳細:', event);
  }
}
```

// マウスイベントでの座標取得
```typescript
@Component({
  selector: 'app-mouse-event',
  standalone: true,
  template: `
    <div class="mouse-event-demo">
      <h2>マウスイベントでの座標取得</h2>
      <div (click)="onClick($event)" class="click-area">
        クリックしてください
      </div>
      <p>クリック座標: X={{clickX}}, Y={{clickY}}</p>
      <p>ページ座標: X={{pageX}}, Y={{pageY}}</p>
    </div>
  `,
  styles: [`
    .mouse-event-demo {
      padding: 20px;
    }
    .click-area {
      width: 200px;
      height: 100px;
      border: 2px solid #007bff;
      background-color: #e7f3ff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      margin: 10px 0;
    }
  `]
})
export class MouseEventComponent {
  clickX = 0;
  clickY = 0;
  pageX = 0;
  pageY = 0;
  
  onClick(event: MouseEvent) {
    this.clickX = event.offsetX;
    this.clickY = event.offsetY;
    this.pageX = event.pageX;
    this.pageY = event.pageY;
    console.log('マウスイベント詳細:', event);
  }
}
```

// キーボードイベントでの詳細情報
```typescript
@Component({
  selector: 'app-keyboard-event',
  standalone: true,
  template: `
    <div class="keyboard-event-demo">
      <h2>キーボードイベントでの詳細情報</h2>
      <input (keydown)="onKeyDown($event)" 
             placeholder="キーを押してください">
      <div class="key-info">
        <p>キー: {{key}}</p>
        <p>キーコード: {{keyCode}}</p>
        <p>Ctrlキー: {{ctrlKey}}</p>
        <p>Shiftキー: {{shiftKey}}</p>
      </div>
    </div>
  `,
  styles: [`
    .keyboard-event-demo {
      padding: 20px;
    }
    input {
      padding: 8px;
      margin: 10px 0;
      width: 300px;
    }
    .key-info {
      background-color: #f8f9fa;
      padding: 10px;
      border-radius: 4px;
      margin-top: 10px;
    }
  `]
})
export class KeyboardEventComponent {
  key = '';
  keyCode = 0;
  ctrlKey = false;
  shiftKey = false;
  
  onKeyDown(event: KeyboardEvent) {
    this.key = event.key;
    this.keyCode = event.keyCode;
    this.ctrlKey = event.ctrlKey;
    this.shiftKey = event.shiftKey;
    console.log('キーボードイベント詳細:', event);
  }
}
```

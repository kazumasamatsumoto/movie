# #046 「(keyup) キーボードイベント」台本

四国めたん「(keyup) キーボードイベントについて解説します！」
ずんだもん「キーボードの操作に反応するの？」
四国めたん「はい！特定のキーが押された時に処理を実行できます」
ずんだもん「どのキーが押されたか分かるの？」
四国めたん「$event.keyCodeや$event.keyで押されたキーを判定できます」
ずんだもん「よく使うキーは？」
四国めたん「Enter、Escape、Space、方向キーなどがよく使われます」

---

## 📺 画面表示用コード

// 基本的なキーボードイベント
```typescript
@Component({
  selector: 'app-keyup-basic',
  standalone: true,
  template: `
    <div class="keyup-demo">
      <h2>基本的なキーボードイベント</h2>
      <input (keyup)="onKeyUp($event)" placeholder="キーを押してください">
      <p>最後に押されたキー: {{lastKey}}</p>
    </div>
  `,
  styles: [`
    .keyup-demo {
      padding: 20px;
    }
    input {
      padding: 8px;
      margin: 10px 0;
      width: 300px;
    }
  `]
})
export class KeyupBasicComponent {
  lastKey = '';
  
  onKeyUp(event: KeyboardEvent) {
    this.lastKey = event.key;
    console.log('キーが押されました:', event.key);
  }
}
```

// Enterキーでの送信
```typescript
@Component({
  selector: 'app-enter-submit',
  standalone: true,
  template: `
    <div class="enter-submit-demo">
      <h2>Enterキーでの送信</h2>
      <input (keyup.enter)="onEnterSubmit($event)" 
             placeholder="Enterキーで送信">
      <p>送信されたメッセージ: {{submittedMessage}}</p>
    </div>
  `,
  styles: [`
    .enter-submit-demo {
      padding: 20px;
    }
    input {
      padding: 8px;
      margin: 10px 0;
      width: 300px;
    }
  `]
})
export class EnterSubmitComponent {
  submittedMessage = '';
  
  onEnterSubmit(event: KeyboardEvent) {
    const target = event.target as HTMLInputElement;
    this.submittedMessage = target.value;
    target.value = ''; // 入力欄をクリア
    console.log('Enterで送信:', this.submittedMessage);
  }
}
```

// 特定キーの検知
```typescript
@Component({
  selector: 'app-specific-keys',
  standalone: true,
  template: `
    <div class="specific-keys-demo">
      <h2>特定キーの検知</h2>
      <input (keyup)="onSpecificKey($event)" 
             placeholder="Escape、Space、矢印キーを試してください">
      <div class="key-info">
        <p>Escapeキー: {{escapeCount}}回</p>
        <p>Spaceキー: {{spaceCount}}回</p>
        <p>矢印キー: {{arrowCount}}回</p>
      </div>
    </div>
  `,
  styles: [`
    .specific-keys-demo {
      padding: 20px;
    }
    input {
      padding: 8px;
      margin: 10px 0;
      width: 300px;
    }
    .key-info {
      margin-top: 15px;
    }
  `]
})
export class SpecificKeysComponent {
  escapeCount = 0;
  spaceCount = 0;
  arrowCount = 0;
  
  onSpecificKey(event: KeyboardEvent) {
    switch (event.key) {
      case 'Escape':
        this.escapeCount++;
        console.log('Escapeキーが押されました');
        break;
      case ' ':
        this.spaceCount++;
        console.log('Spaceキーが押されました');
        break;
      case 'ArrowUp':
      case 'ArrowDown':
      case 'ArrowLeft':
      case 'ArrowRight':
        this.arrowCount++;
        console.log('矢印キーが押されました:', event.key);
        break;
    }
  }
}
```

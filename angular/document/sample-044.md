# #044 「(change) 変更イベント」台本

四国めたん「(change) 変更イベントについて解説します！」
ずんだもん「inputイベントと何が違うの？」
四国めたん「changeは入力が確定した時、inputは入力中の毎回発生します」
ずんだもん「どんな要素で使えるの？」
四国めたん「select、input、textarea、checkbox、radioなどで使用できます」
ずんだもん「フォームの値変更検知に使う？」
四国めたん「はい！ユーザーが入力を完了した時点で処理を実行できます」

---

## 📺 画面表示用コード

// 基本的な変更イベント
```typescript
@Component({
  selector: 'app-change-basic',
  standalone: true,
  template: `
    <div class="change-demo">
      <h2>基本的な変更イベント</h2>
      <input (change)="onChange($event)" placeholder="入力後にフォーカスを外してください">
      <p>最終値: {{finalValue}}</p>
    </div>
  `,
  styles: [`
    .change-demo {
      padding: 20px;
    }
    input {
      padding: 8px;
      margin: 10px 0;
      width: 300px;
    }
  `]
})
export class ChangeBasicComponent {
  finalValue = '';
  
  onChange(event: Event) {
    const target = event.target as HTMLInputElement;
    this.finalValue = target.value;
    console.log('値が確定しました:', this.finalValue);
  }
}
```

// select要素での変更イベント
```typescript
@Component({
  selector: 'app-select-change',
  standalone: true,
  template: `
    <div class="select-demo">
      <h2>select要素での変更イベント</h2>
      <select (change)="onSelectChange($event)">
        <option value="">選択してください</option>
        <option value="angular">Angular</option>
        <option value="react">React</option>
        <option value="vue">Vue</option>
      </select>
      <p>選択されたフレームワーク: {{selectedFramework}}</p>
    </div>
  `,
  styles: [`
    .select-demo {
      padding: 20px;
    }
    select {
      padding: 8px;
      margin: 10px 0;
      width: 200px;
    }
  `]
})
export class SelectChangeComponent {
  selectedFramework = '';
  
  onSelectChange(event: Event) {
    const target = event.target as HTMLSelectElement;
    this.selectedFramework = target.value;
    console.log('フレームワークが選択されました:', this.selectedFramework);
  }
}
```

// checkboxでの変更イベント
```typescript
@Component({
  selector: 'app-checkbox-change',
  standalone: true,
  template: `
    <div class="checkbox-demo">
      <h2>checkboxでの変更イベント</h2>
      <label>
        <input type="checkbox" 
               (change)="onCheckboxChange($event)">
        同意する
      </label>
      <p>同意状態: {{isAgreed ? '同意済み' : '未同意'}}</p>
    </div>
  `,
  styles: [`
    .checkbox-demo {
      padding: 20px;
    }
    label {
      display: flex;
      align-items: center;
      margin: 10px 0;
    }
    input[type="checkbox"] {
      margin-right: 8px;
    }
  `]
})
export class CheckboxChangeComponent {
  isAgreed = false;
  
  onCheckboxChange(event: Event) {
    const target = event.target as HTMLInputElement;
    this.isAgreed = target.checked;
    console.log('同意状態が変更されました:', this.isAgreed);
  }
}
```

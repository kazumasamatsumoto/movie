# #050 「イベント修飾子 - .preventDefault()」台本

四国めたん「イベント修飾子 - .preventDefault()について解説します！」
ずんだもん「イベント修飾子って何？」
四国めたん「イベントの動作を変更するためのキーワードです」
ずんだもん「preventDefault()の役割は？」
四国めたん「デフォルトの動作を防ぐことができます。リンクの遷移やフォーム送信を止められます」
ずんだもん「他にも修飾子があるの？」
四国めたん「stopPropagation()でイベントの伝播を止めたり、.once()で一度だけ実行できます」

---

## 📺 画面表示用コード

// 基本的なpreventDefault
```typescript
@Component({
  selector: 'app-prevent-default',
  standalone: true,
  template: `
    <div class="prevent-demo">
      <h2>基本的なpreventDefault</h2>
      <a href="https://angular.io" (click)="onLinkClick($event)">
        クリックしても遷移しません
      </a>
      <p>クリック回数: {{clickCount}}</p>
    </div>
  `,
  styles: [`
    .prevent-demo {
      padding: 20px;
    }
    a {
      color: #007bff;
      text-decoration: none;
      display: block;
      margin: 10px 0;
    }
    a:hover {
      text-decoration: underline;
    }
  `]
})
export class PreventDefaultComponent {
  clickCount = 0;
  
  onLinkClick(event: Event) {
    event.preventDefault(); // デフォルトの遷移を防ぐ
    this.clickCount++;
    console.log('リンクがクリックされましたが遷移しません');
  }
}
```

// フォーム送信の制御
```typescript
@Component({
  selector: 'app-form-prevent',
  standalone: true,
  template: `
    <div class="form-prevent-demo">
      <h2>フォーム送信の制御</h2>
      <form (submit)="onSubmit($event)">
        <input type="text" placeholder="名前" required>
        <button type="submit">送信</button>
      </form>
      <p>送信回数: {{submitCount}}</p>
      <p>送信メッセージ: {{submitMessage}}</p>
    </div>
  `,
  styles: [`
    .form-prevent-demo {
      padding: 20px;
    }
    form {
      display: flex;
      gap: 10px;
      margin: 10px 0;
    }
    input, button {
      padding: 8px;
    }
  `]
})
export class FormPreventComponent {
  submitCount = 0;
  submitMessage = '';
  
  onSubmit(event: Event) {
    event.preventDefault(); // デフォルトの送信を防ぐ
    this.submitCount++;
    this.submitMessage = `カスタム送信処理を実行しました (${this.submitCount}回目)`;
    console.log('カスタム送信処理が実行されました');
  }
}
```

// 複数の修飾子の組み合わせ
```typescript
@Component({
  selector: 'app-multiple-modifiers',
  standalone: true,
  template: `
    <div class="modifiers-demo">
      <h2>複数の修飾子の組み合わせ</h2>
      <div (click)="onParentClick()" class="parent">
        親要素
        <button (click)="onChildClick($event)" class="child">
          子要素（伝播停止）
        </button>
      </div>
      <p>親要素クリック: {{parentClickCount}}</p>
      <p>子要素クリック: {{childClickCount}}</p>
    </div>
  `,
  styles: [`
    .modifiers-demo {
      padding: 20px;
    }
    .parent {
      padding: 20px;
      border: 2px solid #007bff;
      background-color: #e7f3ff;
      margin: 10px 0;
    }
    .child {
      padding: 8px 16px;
      background-color: #dc3545;
      color: white;
      border: none;
      border-radius: 4px;
    }
  `]
})
export class MultipleModifiersComponent {
  parentClickCount = 0;
  childClickCount = 0;
  
  onParentClick() {
    this.parentClickCount++;
    console.log('親要素がクリックされました');
  }
  
  onChildClick(event: Event) {
    event.stopPropagation(); // イベントの伝播を停止
    event.preventDefault(); // デフォルト動作を防止
    this.childClickCount++;
    console.log('子要素がクリックされました（伝播停止）');
  }
}
```

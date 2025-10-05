# #005 「template - インラインテンプレート」台本

四国めたん「template - インラインテンプレートについて学びましょう！」
ずんだもん「インラインテンプレートって何？」
四国めたん「Componentクラス内に直接HTMLを記述する方法です」
ずんだもん「外部ファイルとどっちがいいの？」
四国めたん「短いテンプレートはインライン、長いテンプレートは外部ファイルがおすすめです」
ずんだもん「どんな時に使うの？」
四国めたん「シンプルなComponentや、テンプレートが短い場合に便利です」

---

## 📺 画面表示用コード

// 基本的なインラインテンプレート
```typescript
@Component({
  selector: 'app-simple',
  template: '<h1>Hello Angular!</h1>'
})
export class SimpleComponent {
  // シンプルなテンプレート
}
```

// 複数行のインラインテンプレート
```typescript
@Component({
  selector: 'app-multiline',
  template: `
    <div class="container">
      <h2>{{title}}</h2>
      <p>{{description}}</p>
      <button (click)="onClick()">クリック</button>
    </div>
  `
})
export class MultilineComponent {
  title = 'マルチライン';
  description = '複数行のテンプレートです';
  
  onClick() {
    console.log('ボタンがクリックされました');
  }
}
```

// バッククォートを使ったテンプレート
```typescript
@Component({
  selector: 'app-backtick',
  template: `
    <div>
      <h3>バッククォートテンプレート</h3>
      <ul>
        <li *ngFor="let item of items">{{item}}</li>
      </ul>
    </div>
  `
})
export class BacktickComponent {
  items = ['項目1', '項目2', '項目3'];
}
```

// 条件分岐を含むテンプレート
```typescript
@Component({
  selector: 'app-conditional',
  template: `
    <div>
      <h4>条件分岐テンプレート</h4>
      <p *ngIf="isVisible">表示中</p>
      <p *ngIf="!isVisible">非表示</p>
      <button (click)="toggle()">切り替え</button>
    </div>
  `
})
export class ConditionalComponent {
  isVisible = true;
  
  toggle() {
    this.isVisible = !this.isVisible;
  }
}
```

// フォームを含むテンプレート
```typescript
@Component({
  selector: 'app-form',
  template: `
    <form (ngSubmit)="onSubmit()">
      <div>
        <label>名前:</label>
        <input [(ngModel)]="name" name="name" required>
      </div>
      <div>
        <label>メール:</label>
        <input [(ngModel)]="email" name="email" type="email" required>
      </div>
      <button type="submit">送信</button>
    </form>
  `
})
export class FormComponent {
  name = '';
  email = '';
  
  onSubmit() {
    console.log('送信:', { name: this.name, email: this.email });
  }
}
```

// インラインテンプレートの利点
```typescript
@Component({
  selector: 'app-advantages',
  template: `
    <div>
      <h5>インラインテンプレートの利点</h5>
      <ul>
        <li>ファイル数が少ない</li>
        <li>IDEの補完が効く</li>
        <li>リファクタリングが簡単</li>
        <li>TypeScriptとHTMLが同じファイル</li>
      </ul>
    </div>
  `
})
export class AdvantagesComponent {
  // 短いテンプレートには最適
}
```

// インラインテンプレートの注意点
```typescript
@Component({
  selector: 'app-notes',
  template: `
    <div>
      <h6>注意点</h6>
      <p>長いテンプレートは可読性が下がる</p>
      <p>HTMLエディタの機能が制限される</p>
      <p>チーム開発では統一が必要</p>
    </div>
  `
})
export class NotesComponent {
  // 適切な使い分けが重要
}
```

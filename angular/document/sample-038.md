# #038 「[class] クラスバインディング」台本

四国めたん「[class] クラスバインディングについて解説します！」
ずんだもん「CSSクラスを動的に変更できるの？」
四国めたん「はい！プロパティバインディングでCSSクラスを動的に追加・削除できます」
ずんだもん「どんな場面で使うの？」
四国めたん「状態に応じたスタイル変更、テーマ切り替え、アニメーションなどです」
ずんだもん「複数のクラスも制御できる？」
四国めたん「ngClassディレクティブを使うとより柔軟に制御できます」

---

## 📺 画面表示用コード

// 基本的なクラスバインディング
```typescript
@Component({
  selector: 'app-class-basic',
  standalone: true,
  template: `
    <div class="class-demo">
      <h2>基本的なクラスバインディング</h2>
      <div [class.active]="isActive" 
           [class.highlighted]="isHighlighted">
        動的なクラス適用
      </div>
      <button (click)="toggleActive()">Active切り替え</button>
      <button (click)="toggleHighlight()">Highlight切り替え</button>
    </div>
  `,
  styles: [`
    .class-demo {
      padding: 20px;
    }
    div {
      padding: 20px;
      border: 2px solid #ccc;
      margin: 10px 0;
    }
    .active {
      background-color: #007bff;
      color: white;
    }
    .highlighted {
      border-color: #ffc107;
      box-shadow: 0 0 10px #ffc107;
    }
  `]
})
export class ClassBasicComponent {
  isActive = false;
  isHighlighted = false;
  
  toggleActive() {
    this.isActive = !this.isActive;
  }
  
  toggleHighlight() {
    this.isHighlighted = !this.isHighlighted;
  }
}
```

// 条件に応じたクラス設定
```typescript
@Component({
  selector: 'app-conditional-class',
  standalone: true,
  template: `
    <div class="conditional-demo">
      <h2>条件に応じたクラス設定</h2>
      <div [class]="getStatusClass()">
        ステータス: {{status}}
      </div>
      <button (click)="changeStatus()">ステータス変更</button>
    </div>
  `,
  styles: [`
    .conditional-demo {
      padding: 20px;
    }
    div {
      padding: 15px;
      margin: 10px 0;
      border-radius: 5px;
    }
    .status-success {
      background-color: #d4edda;
      color: #155724;
    }
    .status-warning {
      background-color: #fff3cd;
      color: #856404;
    }
    .status-error {
      background-color: #f8d7da;
      color: #721c24;
    }
  `]
})
export class ConditionalClassComponent {
  status = 'success';
  statuses = ['success', 'warning', 'error'];
  index = 0;
  
  getStatusClass(): string {
    return `status-${this.status}`;
  }
  
  changeStatus() {
    this.index = (this.index + 1) % this.statuses.length;
    this.status = this.statuses[this.index];
  }
}
```

// ngClassを使った複雑な制御
```typescript
@Component({
  selector: 'app-ngclass-demo',
  standalone: true,
  imports: [NgClass],
  template: `
    <div class="ngclass-demo">
      <h2>ngClassを使った複雑な制御</h2>
      <div [ngClass]="getClasses()">
        ngClassで制御
      </div>
      <button (click)="toggleStates()">状態変更</button>
    </div>
  `,
  styles: [`
    .ngclass-demo {
      padding: 20px;
    }
    div {
      padding: 20px;
      margin: 10px 0;
      border: 2px solid #ccc;
      transition: all 0.3s;
    }
    .primary { background-color: #007bff; color: white; }
    .large { font-size: 1.2em; }
    .rounded { border-radius: 10px; }
  `]
})
export class NgClassDemoComponent {
  isPrimary = true;
  isLarge = false;
  isRounded = true;
  
  getClasses() {
    return {
      'primary': this.isPrimary,
      'large': this.isLarge,
      'rounded': this.isRounded
    };
  }
  
  toggleStates() {
    this.isPrimary = !this.isPrimary;
    this.isLarge = !this.isLarge;
    this.isRounded = !this.isRounded;
  }
}
```

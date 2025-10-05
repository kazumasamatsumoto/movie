# #034 「[property] プロパティバインディング基礎」台本

四国めたん「[property] プロパティバインディング基礎について解説します！」
ずんだもん「プロパティバインディングって何？」
四国めたん「Componentのプロパティ値を、HTML要素のプロパティに直接バインドする方法です」
ずんだもん「補間バインディングと何が違うの？」
四国めたん「属性値だけでなく、DOM要素のプロパティやディレクティブの入力にもバインドできます」
ずんだもん「どうやって使うの？」
四国めたん「角括弧[]でプロパティ名を囲み、値を代入します」

---

## 📺 画面表示用コード

// 基本的なプロパティバインディング
```typescript
@Component({
  selector: 'app-property-binding-basic',
  standalone: true,
  template: `
    <div class="property-demo">
      <h2>基本的なプロパティバインディング</h2>
      <div class="example">
        <h3>input要素のvalue</h3>
        <input [value]="inputValue" readonly>
        <p>バインドされた値: {{inputValue}}</p>
      </div>
      <div class="example">
        <h3>button要素のdisabled</h3>
        <button [disabled]="isDisabled">ボタン</button>
        <p>無効状態: {{isDisabled}}</p>
        <button (click)="toggleDisabled()">切り替え</button>
      </div>
    </div>
  `,
  styles: [`
    .property-demo {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
    }
    .example {
      margin: 20px 0;
      padding: 15px;
      border: 1px solid #007bff;
      border-radius: 8px;
      background-color: #e7f3ff;
    }
    input, button {
      padding: 8px 16px;
      margin: 5px;
      border: 1px solid #ced4da;
      border-radius: 4px;
    }
  `]
})
export class PropertyBindingBasicComponent {
  inputValue = 'プロパティバインディング';
  isDisabled = false;
  
  toggleDisabled(): void {
    this.isDisabled = !this.isDisabled;
  }
}
```

// 補間バインディングとの比較
```typescript
@Component({
  selector: 'app-interpolation-vs-property',
  standalone: true,
  template: `
    <div class="comparison-demo">
      <h2>補間バインディング vs プロパティバインディング</h2>
      
      <div class="example">
        <h3>補間バインディング {{ "{{" }}{{ "}}" }}</h3>
        <p>タイトル: {{title}}</p>
        <p>説明: {{description}}</p>
        <p>✅ テキストコンテンツに最適</p>
      </div>
      
      <div class="example">
        <h3>プロパティバインディング []</h3>
        <input [value]="title" readonly>
        <button [disabled]="isDisabled">ボタン</button>
        <img [src]="imageUrl" [alt]="imageAlt" width="100">
        <p>✅ DOM要素のプロパティに最適</p>
      </div>
      
      <div class="example">
        <h3>両方使える場合</h3>
        <p>補間: <span title="{{title}}">ホバーしてください</span></p>
        <p>プロパティ: <span [title]="title">ホバーしてください</span></p>
        <p>✅ どちらでも動作しますが、プロパティバインディングが推奨</p>
      </div>
    </div>
  `,
  styles: [`
    .comparison-demo {
      padding: 20px;
    }
    .example {
      margin: 20px 0;
      padding: 15px;
      border: 1px solid #28a745;
      border-radius: 8px;
      background-color: #d4edda;
    }
    input, button {
      display: block;
      margin: 10px 0;
      padding: 8px;
    }
    img {
      display: block;
      margin: 10px 0;
    }
  `]
})
export class InterpolationVsPropertyComponent {
  title = 'Angular';
  description = 'プロパティバインディングの例';
  isDisabled = false;
  imageUrl = 'https://angular.io/assets/images/logos/angular/angular.svg';
  imageAlt = 'Angular Logo';
}
```

// さまざまな要素のプロパティバインディング
```typescript
@Component({
  selector: 'app-various-properties',
  standalone: true,
  template: `
    <div class="various-demo">
      <h2>さまざまな要素のプロパティバインディング</h2>
      
      <div class="example">
        <h3>input要素</h3>
        <input [type]="inputType" [placeholder]="placeholder" [maxlength]="maxLength">
        <button (click)="changeInputType()">タイプ変更</button>
      </div>
      
      <div class="example">
        <h3>button要素</h3>
        <button [type]="buttonType" [disabled]="isDisabled">{{buttonText}}</button>
        <button (click)="toggleDisabled()">有効/無効切り替え</button>
      </div>
      
      <div class="example">
        <h3>div要素</h3>
        <div [hidden]="isHidden" class="content-box">
          このコンテンツは表示/非表示を切り替えできます
        </div>
        <button (click)="toggleHidden()">表示/非表示切り替え</button>
      </div>
      
      <div class="example">
        <h3>textarea要素</h3>
        <textarea [rows]="textareaRows" [cols]="textareaCols" [placeholder]="placeholder">
        </textarea>
      </div>
    </div>
  `,
  styles: [`
    .various-demo {
      padding: 20px;
    }
    .example {
      margin: 20px 0;
      padding: 15px;
      border: 1px solid #ffc107;
      border-radius: 8px;
      background-color: #fff3cd;
    }
    input, button, textarea {
      margin: 5px;
      padding: 8px;
    }
    .content-box {
      padding: 15px;
      background-color: #d1ecf1;
      border: 1px solid #bee5eb;
      border-radius: 4px;
      margin: 10px 0;
    }
  `]
})
export class VariousPropertiesComponent {
  inputType = 'text';
  placeholder = '入力してください';
  maxLength = 50;
  buttonType = 'button';
  buttonText = 'クリック';
  isDisabled = false;
  isHidden = false;
  textareaRows = 5;
  textareaCols = 40;
  
  changeInputType(): void {
    this.inputType = this.inputType === 'text' ? 'password' : 'text';
  }
  
  toggleDisabled(): void {
    this.isDisabled = !this.isDisabled;
  }
  
  toggleHidden(): void {
    this.isHidden = !this.isHidden;
  }
}
```

// カスタムComponentへのプロパティバインディング
```typescript
@Component({
  selector: 'app-child',
  standalone: true,
  template: `
    <div class="child-component">
      <h4>子Component</h4>
      <p>受け取ったタイトル: {{title}}</p>
      <p>受け取った値: {{value}}</p>
      <p>受け取ったオブジェクト: {{data.name}}</p>
    </div>
  `,
  styles: [`
    .child-component {
      padding: 15px;
      border: 2px dashed #6c757d;
      border-radius: 8px;
      background-color: #f8f9fa;
    }
  `]
})
export class ChildComponent {
  @Input() title = '';
  @Input() value = 0;
  @Input() data: any = {};
}

@Component({
  selector: 'app-parent',
  standalone: true,
  imports: [ChildComponent],
  template: `
    <div class="parent-demo">
      <h2>カスタムComponentへのプロパティバインディング</h2>
      <app-child
        [title]="parentTitle"
        [value]="parentValue"
        [data]="parentData">
      </app-child>
      <button (click)="updateValues()">値を更新</button>
    </div>
  `,
  styles: [`
    .parent-demo {
      padding: 20px;
    }
    button {
      margin-top: 15px;
      padding: 8px 16px;
    }
  `]
})
export class ParentComponent {
  parentTitle = '親からの値';
  parentValue = 100;
  parentData = { name: '田中太郎', age: 30 };
  
  updateValues(): void {
    this.parentTitle = '更新された値';
    this.parentValue++;
    this.parentData = { name: '佐藤花子', age: 25 };
  }
}
```

// 動的なプロパティバインディング
```typescript
@Component({
  selector: 'app-dynamic-property',
  standalone: true,
  template: `
    <div class="dynamic-demo">
      <h2>動的なプロパティバインディング</h2>
      
      <div class="example">
        <h3>条件に応じたプロパティ値</h3>
        <button [disabled]="count >= maxCount">
          カウント: {{count}} / {{maxCount}}
        </button>
        <button (click)="increment()">増加</button>
        <button (click)="reset()">リセット</button>
      </div>
      
      <div class="example">
        <h3>計算されたプロパティ値</h3>
        <input [value]="firstName + ' ' + lastName" readonly>
        <p>姓: {{firstName}}</p>
        <p>名: {{lastName}}</p>
      </div>
      
      <div class="example">
        <h3>メソッドの戻り値</h3>
        <div [hidden]="shouldHide()">
          この要素は条件に応じて表示/非表示されます
        </div>
        <button (click)="toggleCondition()">条件切り替え</button>
      </div>
    </div>
  `,
  styles: [`
    .dynamic-demo {
      padding: 20px;
    }
    .example {
      margin: 20px 0;
      padding: 15px;
      border: 1px solid #dc3545;
      border-radius: 8px;
      background-color: #f8d7da;
    }
    button, input {
      margin: 5px;
      padding: 8px 16px;
    }
    div[hidden] {
      display: none;
    }
  `]
})
export class DynamicPropertyComponent {
  count = 0;
  maxCount = 10;
  firstName = '田中';
  lastName = '太郎';
  condition = false;
  
  increment(): void {
    if (this.count < this.maxCount) {
      this.count++;
    }
  }
  
  reset(): void {
    this.count = 0;
  }
  
  shouldHide(): boolean {
    return this.condition;
  }
  
  toggleCondition(): void {
    this.condition = !this.condition;
  }
}
```

// プロパティバインディングのベストプラクティス
```typescript
@Component({
  selector: 'app-property-best-practices',
  standalone: true,
  template: `
    <div class="best-practices">
      <h2>プロパティバインディングのベストプラクティス</h2>
      
      <div class="practice-item">
        <h3>✅ DO: プロパティには[]を使用</h3>
        <code>&lt;input [value]="inputValue"&gt;</code>
        <p>DOM要素のプロパティにバインドする場合は[]を使用</p>
      </div>
      
      <div class="practice-item">
        <h3>✅ DO: 読み取り専用プロパティに使用</h3>
        <code>&lt;input [value]="value" readonly&gt;</code>
        <p>値を表示するだけの場合に使用</p>
      </div>
      
      <div class="practice-item">
        <h3>❌ DON'T: 副作用のあるメソッドを使用</h3>
        <code>&lt;input [value]="updateDatabase()"&gt;</code>
        <p>プロパティバインディング内で状態を変更しない</p>
      </div>
      
      <div class="practice-item">
        <h3>✅ DO: 単純な式を使用</h3>
        <code>&lt;button [disabled]="!isValid"&gt;</code>
        <p>複雑なロジックはComponentのメソッドやgetterに移動</p>
      </div>
    </div>
  `,
  styles: [`
    .best-practices {
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    .practice-item {
      margin: 20px 0;
      padding: 15px;
      border: 1px solid #17a2b8;
      border-radius: 8px;
      background-color: #d1ecf1;
    }
    code {
      display: block;
      padding: 10px;
      background-color: #f8f9fa;
      border-radius: 4px;
      margin: 10px 0;
      font-family: monospace;
    }
  `]
})
export class PropertyBestPracticesComponent {}
```

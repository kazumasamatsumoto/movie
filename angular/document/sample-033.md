# #033 「{{ }} 安全な補間 - XSS対策」台本

四国めたん「{{ }} 安全な補間 - XSS対策について学びましょう！」
ずんだもん「XSSって何？」
四国めたん「Cross-Site Scriptingの略で、悪意あるスクリプトを注入する攻撃です」
ずんだもん「Angularは対策してくれるの？」
四国めたん「はい！補間バインディングは自動的にHTMLをエスケープして、XSS攻撃を防ぎます」
ずんだもん「HTMLを表示したい時はどうするの？」
四国めたん「DomSanitizerを使って安全性を確認してから表示する必要があります」

---

## 📺 画面表示用コード

// 自動的なXSS対策
```typescript
@Component({
  selector: 'app-xss-protection',
  standalone: true,
  template: `
    <div class="xss-demo">
      <h2>自動的なXSS対策</h2>
      <div class="example">
        <h3>安全な表示（自動エスケープ）</h3>
        <p>入力値: {{userInput}}</p>
        <p>表示結果: {{userInput}}</p>
        <p class="note">スクリプトタグがそのまま文字列として表示されます</p>
      </div>
    </div>
  `,
  styles: [`
    .xss-demo {
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    .example {
      margin: 15px 0;
      padding: 15px;
      border: 1px solid #28a745;
      border-radius: 8px;
      background-color: #d4edda;
    }
    .note {
      color: #155724;
      font-weight: bold;
      margin-top: 10px;
    }
  `]
})
export class XssProtectionComponent {
  // 悪意のあるスクリプトを含む入力
  userInput = '<script>alert("XSS攻撃!")</script>';
  
  // Angularが自動的にエスケープするため、
  // スクリプトは実行されず、文字列として表示される
}
```

// HTMLエスケープの例
```typescript
@Component({
  selector: 'app-html-escape',
  standalone: true,
  template: `
    <div class="escape-demo">
      <h2>HTMLエスケープの例</h2>
      <div class="example-item">
        <h3>入力値1</h3>
        <p>元の値: {{htmlString1}}</p>
        <p>表示: {{htmlString1}}</p>
      </div>
      <div class="example-item">
        <h3>入力値2</h3>
        <p>元の値: {{htmlString2}}</p>
        <p>表示: {{htmlString2}}</p>
      </div>
      <div class="example-item">
        <h3>入力値3</h3>
        <p>元の値: {{htmlString3}}</p>
        <p>表示: {{htmlString3}}</p>
      </div>
    </div>
  `,
  styles: [`
    .escape-demo {
      padding: 20px;
    }
    .example-item {
      margin: 15px 0;
      padding: 15px;
      border: 1px solid #007bff;
      border-radius: 8px;
      background-color: #e7f3ff;
    }
  `]
})
export class HtmlEscapeComponent {
  htmlString1 = '<strong>太字</strong>';
  htmlString2 = '<img src="x" onerror="alert(\'XSS\')">';
  htmlString3 = '<a href="javascript:alert(\'XSS\')">リンク</a>';
  
  // すべてHTMLタグがエスケープされ、文字列として表示される
}
```

// 安全なHTML表示（DomSanitizer使用）
```typescript
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';

@Component({
  selector: 'app-safe-html',
  standalone: true,
  template: `
    <div class="safe-html-demo">
      <h2>安全なHTML表示</h2>
      <div class="warning">
        <p>⚠️ 注意: 信頼できるHTMLのみを使用してください</p>
      </div>
      <div class="example">
        <h3>元のHTML</h3>
        <pre>{{trustedHtml}}</pre>
      </div>
      <div class="example">
        <h3>サニタイズ後の表示</h3>
        <div [innerHTML]="safeHtml"></div>
      </div>
    </div>
  `,
  styles: [`
    .safe-html-demo {
      padding: 20px;
    }
    .warning {
      padding: 15px;
      background-color: #fff3cd;
      border: 1px solid #ffc107;
      border-radius: 8px;
      margin-bottom: 20px;
    }
    .example {
      margin: 15px 0;
      padding: 15px;
      border: 1px solid #6c757d;
      border-radius: 8px;
    }
    pre {
      background-color: #f8f9fa;
      padding: 10px;
      border-radius: 4px;
      overflow-x: auto;
    }
  `]
})
export class SafeHtmlComponent {
  trustedHtml = '<p>これは<strong>安全な</strong>HTMLです</p>';
  safeHtml: SafeHtml;
  
  constructor(private sanitizer: DomSanitizer) {
    // DomSanitizerを使って安全性を確認
    this.safeHtml = this.sanitizer.sanitize(
      1, // SecurityContext.HTML
      this.trustedHtml
    ) || '';
  }
}
```

// 危険なパターンと安全なパターン
```typescript
@Component({
  selector: 'app-xss-patterns',
  standalone: true,
  template: `
    <div class="patterns-demo">
      <h2>危険なパターンと安全なパターン</h2>
      
      <div class="pattern dangerous">
        <h3>❌ 危険なパターン</h3>
        <p>innerHTMLに直接バインド（避けるべき）</p>
        <code>&lt;div [innerHTML]="userInput"&gt;&lt;/div&gt;</code>
      </div>
      
      <div class="pattern safe">
        <h3>✅ 安全なパターン</h3>
        <p>補間バインディングを使用</p>
        <code>&lt;div&gt;{{ "{{userInput}}" }}&lt;/div&gt;</code>
      </div>
      
      <div class="pattern safe">
        <h3>✅ 安全なパターン（HTML表示が必要な場合）</h3>
        <p>DomSanitizerでサニタイズ</p>
        <code>&lt;div [innerHTML]="safeHtml"&gt;&lt;/div&gt;</code>
      </div>
    </div>
  `,
  styles: [`
    .patterns-demo {
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    .pattern {
      margin: 15px 0;
      padding: 15px;
      border-radius: 8px;
    }
    .pattern.dangerous {
      background-color: #f8d7da;
      border: 2px solid #dc3545;
    }
    .pattern.safe {
      background-color: #d4edda;
      border: 2px solid #28a745;
    }
    code {
      display: block;
      margin-top: 10px;
      padding: 10px;
      background-color: #f8f9fa;
      border-radius: 4px;
      font-family: monospace;
    }
  `]
})
export class XssPatternsComponent {}
```

// ユーザー入力の処理
```typescript
@Component({
  selector: 'app-user-input-handling',
  standalone: true,
  imports: [FormsModule],
  template: `
    <div class="input-demo">
      <h2>ユーザー入力の処理</h2>
      <div class="input-section">
        <h3>入力フォーム</h3>
        <textarea 
          [(ngModel)]="userInput" 
          placeholder="テキストを入力してください"
          rows="4">
        </textarea>
        <button (click)="clearInput()">クリア</button>
      </div>
      <div class="output-section">
        <h3>安全な表示（自動エスケープ）</h3>
        <div class="output-box">
          {{userInput}}
        </div>
      </div>
      <div class="info">
        <p>✅ HTMLタグを入力しても、文字列として表示されます</p>
        <p>✅ スクリプトタグも実行されません</p>
      </div>
    </div>
  `,
  styles: [`
    .input-demo {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
    }
    .input-section, .output-section {
      margin: 20px 0;
    }
    textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ced4da;
      border-radius: 4px;
      font-family: monospace;
    }
    button {
      margin-top: 10px;
      padding: 8px 16px;
      background-color: #dc3545;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .output-box {
      padding: 15px;
      background-color: #f8f9fa;
      border: 1px solid #dee2e6;
      border-radius: 4px;
      min-height: 50px;
      word-wrap: break-word;
    }
    .info {
      margin-top: 20px;
      padding: 15px;
      background-color: #d1ecf1;
      border: 1px solid #bee5eb;
      border-radius: 4px;
    }
    .info p {
      margin: 5px 0;
      color: #0c5460;
    }
  `]
})
export class UserInputHandlingComponent {
  userInput = '';
  
  clearInput(): void {
    this.userInput = '';
  }
}
```

// セキュリティのベストプラクティス
```typescript
@Component({
  selector: 'app-security-best-practices',
  standalone: true,
  template: `
    <div class="best-practices">
      <h2>セキュリティのベストプラクティス</h2>
      
      <div class="practice-item">
        <h3>1. 補間バインディングを優先</h3>
        <p>可能な限り{{ "{{" }}{{ "}}" }}を使用してください</p>
        <p>Angularが自動的にエスケープします</p>
      </div>
      
      <div class="practice-item">
        <h3>2. innerHTMLの使用を避ける</h3>
        <p>どうしても必要な場合はDomSanitizerを使用</p>
        <p>信頼できるソースのみを許可</p>
      </div>
      
      <div class="practice-item">
        <h3>3. ユーザー入力を信頼しない</h3>
        <p>すべてのユーザー入力を疑う</p>
        <p>バックエンドでも検証を行う</p>
      </div>
      
      <div class="practice-item">
        <h3>4. Content Security Policy (CSP)を設定</h3>
        <p>HTTPヘッダーでCSPを設定</p>
        <p>インラインスクリプトを制限</p>
      </div>
      
      <div class="practice-item">
        <h3>5. 定期的なセキュリティ監査</h3>
        <p>依存パッケージの更新</p>
        <p>セキュリティスキャンの実施</p>
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
      padding: 20px;
      border: 1px solid #007bff;
      border-radius: 8px;
      background-color: #e7f3ff;
    }
    .practice-item h3 {
      color: #004085;
      margin-top: 0;
    }
    .practice-item p {
      margin: 8px 0;
      color: #004085;
    }
  `]
})
export class SecurityBestPracticesComponent {}
```

// XSS攻撃の例と対策
```typescript
@Component({
  selector: 'app-xss-examples',
  standalone: true,
  template: `
    <div class="xss-examples">
      <h2>XSS攻撃の例と対策</h2>
      
      <div class="example-item">
        <h3>攻撃例1: スクリプトタグ</h3>
        <p class="attack">{{scriptAttack}}</p>
        <p class="defense">✅ Angularが自動的にエスケープ → 安全</p>
      </div>
      
      <div class="example-item">
        <h3>攻撃例2: イベントハンドラ</h3>
        <p class="attack">{{eventAttack}}</p>
        <p class="defense">✅ Angularが自動的にエスケープ → 安全</p>
      </div>
      
      <div class="example-item">
        <h3>攻撃例3: JavaScriptプロトコル</h3>
        <p class="attack">{{jsProtocolAttack}}</p>
        <p class="defense">✅ Angularが自動的にエスケープ → 安全</p>
      </div>
    </div>
  `,
  styles: [`
    .xss-examples {
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    .example-item {
      margin: 20px 0;
      padding: 15px;
      border: 1px solid #ffc107;
      border-radius: 8px;
      background-color: #fff3cd;
    }
    .attack {
      padding: 10px;
      background-color: #f8d7da;
      border: 1px solid #f5c6cb;
      border-radius: 4px;
      font-family: monospace;
      word-wrap: break-word;
    }
    .defense {
      margin-top: 10px;
      color: #155724;
      font-weight: bold;
    }
  `]
})
export class XssExamplesComponent {
  scriptAttack = '<script>alert("XSS")</script>';
  eventAttack = '<img src="x" onerror="alert(\'XSS\')">';
  jsProtocolAttack = '<a href="javascript:alert(\'XSS\')">クリック</a>';
  
  // すべてAngularによって自動的にエスケープされるため安全
}
```

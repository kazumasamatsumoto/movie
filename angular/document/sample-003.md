# #003 「Component デコレータ - @Component の役割」台本

四国めたん「Component デコレータ - @Component の役割について学びましょう！」
ずんだもん「@Componentって何をするものなの？」
四国めたん「@Componentは、TypeScriptクラスをAngular Componentとして認識させるメタデータを提供します」
ずんだもん「メタデータって具体的には？」
四国めたん「セレクタ、テンプレート、スタイルなどの設定情報です」
ずんだもん「これがないとComponentとして動かないんだね！」
四国めたん「その通りです！@ComponentデコレータがAngularの魔法を起こします」

---

## 📺 画面表示用コード

// @Componentデコレータの基本構文
```typescript
import { Component } from '@angular/core';

@Component({
  // メタデータオブジェクト
})
export class MyComponent {
  // Componentのロジック
}
```

// 基本的なメタデータプロパティ
```typescript
@Component({
  selector: 'app-hello',           // HTMLでの使用名
  templateUrl: './hello.component.html',  // テンプレートファイル
  styleUrls: ['./hello.component.css']    // スタイルファイル
})
export class HelloComponent {
  message = 'Hello Angular!';
}
```

// インラインテンプレートとスタイル
```typescript
@Component({
  selector: 'app-inline',
  template: `
    <div>
      <h1>{{title}}</h1>
      <p>{{description}}</p>
    </div>
  `,
  styles: [`
    div {
      padding: 20px;
      background-color: #f0f0f0;
    }
    h1 {
      color: #333;
      margin-bottom: 10px;
    }
  `]
})
export class InlineComponent {
  title = 'インラインComponent';
  description = 'テンプレートとスタイルが同じファイルにあります';
}
```

// 複数のスタイルファイル
```typescript
@Component({
  selector: 'app-multi-style',
  templateUrl: './multi-style.component.html',
  styleUrls: [
    './multi-style.component.css',
    './multi-style.theme.css',
    './multi-style.responsive.css'
  ]
})
export class MultiStyleComponent {
  // 複数のCSSファイルを組み合わせて使用
}
```

// デコレータなしのクラス（Componentとして認識されない）
```typescript
// ❌ これはComponentとして認識されない
export class NotAComponent {
  message = 'これはComponentではありません';
}
```

// デコレータありのクラス（Componentとして認識される）
```typescript
// ✅ これはComponentとして認識される
@Component({
  selector: 'app-valid',
  template: '<p>{{message}}</p>'
})
export class ValidComponent {
  message = 'これはComponentです！';
}
```

// 高度なメタデータ設定
```typescript
@Component({
  selector: 'app-advanced',
  templateUrl: './advanced.component.html',
  styleUrls: ['./advanced.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  encapsulation: ViewEncapsulation.Emulated,
  providers: [MyService]
})
export class AdvancedComponent {
  // 高度な設定を持つComponent
}
```

# #009 「Component クラスの基本構造」台本

四国めたん「Component クラスの基本構造について学びましょう！」
ずんだもん「Componentクラスってどんな構造なの？」
四国めたん「プロパティ、メソッド、ライフサイクルフックで構成されています」
ずんだもん「プロパティって何？」
四国めたん「データを保持する変数で、テンプレートで表示や操作に使用します」
ずんだもん「メソッドはどんなものがあるの？」
四国めたん「イベントハンドラやビジネスロジックを実装する関数です」

---

## 📺 画面表示用コード

// Componentクラスの基本構造
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-basic-structure',
  template: `
    <div>
      <h1>{{title}}</h1>
      <p>{{description}}</p>
      <button (click)="onButtonClick()">クリック</button>
    </div>
  `
})
export class BasicStructureComponent {
  // プロパティ（データ）
  title = '基本構造';
  description = 'Componentクラスの構造例';
  count = 0;
  
  // メソッド（機能）
  onButtonClick() {
    this.count++;
    console.log(`クリック回数: ${this.count}`);
  }
  
  // 計算プロパティ
  get displayCount() {
    return `カウント: ${this.count}`;
  }
}
```

// プロパティの種類
```typescript
@Component({
  selector: 'app-properties',
  template: `
    <div>
      <h2>プロパティの種類</h2>
      <p>文字列: {{stringProperty}}</p>
      <p>数値: {{numberProperty}}</p>
      <p>真偽値: {{booleanProperty}}</p>
      <p>配列: {{arrayProperty}}</p>
      <p>オブジェクト: {{objectProperty.name}}</p>
    </div>
  `
})
export class PropertiesComponent {
  // プリミティブ型のプロパティ
  stringProperty = '文字列プロパティ';
  numberProperty = 42;
  booleanProperty = true;
  
  // 配列プロパティ
  arrayProperty = ['項目1', '項目2', '項目3'];
  
  // オブジェクトプロパティ
  objectProperty = {
    name: '田中太郎',
    age: 30,
    email: 'tanaka@example.com'
  };
}
```

// メソッドの種類
```typescript
@Component({
  selector: 'app-methods',
  template: `
    <div>
      <h2>メソッドの種類</h2>
      <button (click)="onClick()">クリックイベント</button>
      <button (click)="onClickWithParam('パラメータ')">パラメータ付き</button>
      <p>{{result}}</p>
    </div>
  `
})
export class MethodsComponent {
  result = '';
  
  // イベントハンドラメソッド
  onClick() {
    this.result = 'ボタンがクリックされました';
  }
  
  // パラメータ付きメソッド
  onClickWithParam(param: string) {
    this.result = `パラメータ: ${param}`;
  }
  
  // ビジネスロジックメソッド
  calculateSum(a: number, b: number): number {
    return a + b;
  }
  
  // 非同期メソッド
  async fetchData() {
    try {
      const response = await fetch('/api/data');
      const data = await response.json();
      this.result = `データ取得: ${data.message}`;
    } catch (error) {
      this.result = 'エラーが発生しました';
    }
  }
}
```

// ライフサイクルフック
```typescript
import { Component, OnInit, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-lifecycle',
  template: `
    <div>
      <h2>ライフサイクルフック</h2>
      <p>初期化済み: {{isInitialized}}</p>
      <p>破棄済み: {{isDestroyed}}</p>
    </div>
  `
})
export class LifecycleComponent implements OnInit, OnDestroy {
  isInitialized = false;
  isDestroyed = false;
  
  // 初期化時の処理
  ngOnInit() {
    this.isInitialized = true;
    console.log('Componentが初期化されました');
  }
  
  // 破棄時の処理
  ngOnDestroy() {
    this.isDestroyed = true;
    console.log('Componentが破棄されました');
  }
}
```

// プライベートとパブリック
```typescript
@Component({
  selector: 'app-visibility',
  template: `
    <div>
      <h2>可視性</h2>
      <p>パブリックプロパティ: {{publicProperty}}</p>
      <button (click)="publicMethod()">パブリックメソッド</button>
    </div>
  `
})
export class VisibilityComponent {
  // パブリックプロパティ（デフォルト）
  publicProperty = 'パブリック';
  
  // プライベートプロパティ
  private privateProperty = 'プライベート';
  
  // パブリックメソッド
  publicMethod() {
    console.log('パブリックメソッドが呼ばれました');
    this.privateMethod();
  }
  
  // プライベートメソッド
  private privateMethod() {
    console.log('プライベートメソッドが呼ばれました');
  }
}
```

// ゲッターとセッター
```typescript
@Component({
  selector: 'app-getter-setter',
  template: `
    <div>
      <h2>ゲッターとセッター</h2>
      <input [(ngModel)]="name" placeholder="名前を入力">
      <p>表示名: {{displayName}}</p>
      <p>文字数: {{nameLength}}</p>
    </div>
  `
})
export class GetterSetterComponent {
  private _name = '';
  
  // セッター
  set name(value: string) {
    this._name = value.trim();
  }
  
  // ゲッター
  get name(): string {
    return this._name;
  }
  
  // 計算プロパティ（ゲッター）
  get displayName(): string {
    return this._name || '名前が入力されていません';
  }
  
  get nameLength(): number {
    return this._name.length;
  }
}
```

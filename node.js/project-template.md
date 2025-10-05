# 🟢 Node.js学習ショート動画 台本テンプレート
## 30秒構成（四国めたん：Node.js講師 / ずんだもん：バックエンド開発者）

---

## 基本設定
- **めたん**：標準語（です・ます調）、Node.js専門講師、実装重視
- **ずんだもん**：標準語（だね・だよ）、バックエンド開発者、実践派
- **動画時間**：30秒（28-32秒）
- **対象**：Node.js開発者、バックエンドエンジニア、JavaScript経験者

---

## プロジェクト概要

### シリーズ構成（全300本）
```json
{
  "project": {
    "name": "300本のショート動画で学ぶ実践Node.js開発",
    "description": "現場で使えるNode.js技術を30秒で習得",
    "totalVideos": 300,
    "targetAudience": "Node.js開発者、バックエンドエンジニア",
    "nodeVersion": "20+"
  }
}
```

### 章立て
1. **Node.js基礎** (1-50話): 非同期処理、モジュールシステム、npm
2. **Express.js & Web API** (51-100話): ルーティング、ミドルウェア、REST API
3. **データベース連携** (101-140話): MongoDB、PostgreSQL、ORM/ODM
4. **認証・セキュリティ** (141-170話): JWT、暗号化、セキュリティ対策
5. **ファイル・ストリーム処理** (171-200話): ファイル操作、ストリーム、バッファ
6. **リアルタイム通信** (201-230話): WebSocket、Socket.IO、SSE
7. **テスト&デバッグ** (231-260話): Jest、Supertest、プロファイリング
8. **パフォーマンス&スケール** (261-290話): クラスター、キャッシュ、最適化
9. **デプロイ&運用** (291-300話): Docker、AWS、CI/CD

---

## キャラクター設定

### 四国めたん（Node.js講師）
- **専門性**：Node.js公式ドキュメント準拠、ベストプラクティス重視
- **口調**：「です・ます調」で丁寧、技術的に正確
- **得意分野**：アーキテクチャ設計、パフォーマンス、新機能解説
- **セリフ例**：
  - 「Node.jsの[機能名]について学びましょう！」
  - 「実装のポイントは[重要事項]です」
  - 「この機能により[メリット]が実現できます」

### ずんだもん（バックエンド開発者）
- **立場**：現場のバックエンド開発者、実践経験豊富
- **口調**：「だね・だよ」で親しみやすい、開発者目線
- **得意分野**：実装の悩み、デバッグ、ライブラリ活用
- **セリフ例**：
  - 「実際のプロジェクトでどう使うの？」
  - 「これって[従来手法]より便利だね！」
  - 「開発効率が上がりそうだよ！」

---

## 動画タイプ別テンプレート

### TypeA: 新機能解説型（ES Modules、Worker Threads等）

```
オープニング（3-5秒）
めたん: 「今日は新機能『[機能名]』について学びましょう！」
ずんだもん: 「[機能名]？どんな機能だろう？」

メインコンテンツ（20-22秒）
めたん: 「[機能名]は[簡潔な定義]です。従来の[従来手法]と比べて[改善点]になります。」
ずんだもん: 「具体的にどう書くの？」
めたん: 「例えば『[コード例]』のように書きます。[実装のポイント]がコツです。」
ずんだもん: 「おー！[理解のコメント]だね！」

クロージング（3-5秒）
めたん: 「これで[機能名]の基本は完璧ですね！」
ずんだもん: 「早速プロジェクトで使ってみよう！」
```

### TypeB: 実装パターン型（API設計、エラーハンドリング等）

```
オープニング（3-5秒）
ずんだもん: 「[実装課題]で悩んでるんだ...」
めたん: 「それなら[解決手法]パターンを使いましょう！」

メインコンテンツ（20-22秒）
めたん: 「[解決手法]の実装は『[実装手順]』です。」
ずんだもん: 「なるほど！[理解確認]ということだね？」
めたん: 「その通りです。コード例は『[具体的なコード]』のようになります。[注意点]に気をつけてください。」
ずんだもん: 「これで[期待効果]が実現できそうだ！」

クロージング（3-5秒）
めたん: 「このパターンで開発効率が向上しますね！」
ずんだもん: 「実践的で助かるよ！」
```

### TypeC: 比較解説型（フレームワーク比較、手法比較等）

```
オープニング（3-5秒）
ずんだもん: 「[手法A]と[手法B]、どっちがいいの？」
めたん: 「用途によって使い分けましょう！」

メインコンテンツ（20-22秒）
めたん: 「[手法A]は[特徴A]で、[利用場面A]に適しています。[手法B]は[特徴B]で、[利用場面B]で活躍します。」
ずんだもん: 「つまり[理解した内容]ということだね？」
めたん: 「正解です！判断基準は[判断ポイント]です。」
ずんだもん: 「使い分けが大切なんだね！」

クロージング（3-5秒）
めたん: 「適切な選択で品質の高いAPIが作れますね！」
ずんだもん: 「プロジェクトに合わせて選ぼう！」
```

### TypeD: トラブルシューティング型（メモリリーク、パフォーマンス等）

```
オープニング（3-5秒）
ずんだもん: 「[問題内容]の問題が発生したんだ...」
めたん: 「よくある問題ですね！解決しましょう！」

メインコンテンツ（20-22秒）
めたん: 「この問題の原因は[原因]です。解決方法は『[解決手順]』です。」
ずんだもん: 「なるほど！[原因理解]だったんだね？」
めたん: 「その通りです。予防策として[予防策]を心がけてください。」
ずんだもん: 「今度から気をつけるよ！」

クロージング（3-5秒）
めたん: 「問題解決でスキルアップできましたね！」
ずんだもん: 「トラブルも学習の機会だね！」
```

---

## Node.js技術カテゴリー

### 🔧 Core機能
- **非同期処理**: async/await、Promise、callback
- **モジュールシステム**: CommonJS、ES Modules
- **イベントループ**: Event Loop、非ブロッキングI/O

### ⚡ Express.js & API
```javascript
// Express.jsの基本例
const express = require('express');
const app = express();

app.get('/api/users', async (req, res) => {
  const users = await User.findAll();
  res.json(users);
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

### 🗄️ データベース連携
- **MongoDB**: Mongoose、集約操作
- **PostgreSQL**: Sequelize、クエリ最適化
- **Redis**: キャッシュ、セッション管理

### 🛡️ セキュリティ & 認証
```javascript
// JWT認証の例
const jwt = require('jsonwebtoken');

const authenticateToken = (req, res, next) => {
  const token = req.header('Authorization')?.split(' ')[1];
  
  if (!token) {
    return res.status(401).json({ message: 'Access denied' });
  }
  
  try {
    const verified = jwt.verify(token, process.env.JWT_SECRET);
    req.user = verified;
    next();
  } catch (err) {
    res.status(400).json({ message: 'Invalid token' });
  }
};
```

### 🌐 リアルタイム & 通信
- **WebSocket**: ws、Socket.IO
- **HTTP/2**: http2モジュール
- **GraphQL**: Apollo Server、Relay

---

## 実装コード例テンプレート

### 非同期処理実装例
```javascript
// Promise chain vs async/await
// Promise chain (従来)
function fetchUserData(userId) {
  return fetch(`/api/users/${userId}`)
    .then(response => response.json())
    .then(user => fetch(`/api/posts/${user.id}`))
    .then(response => response.json());
}

// async/await (推奨)
async function fetchUserData(userId) {
  try {
    const userResponse = await fetch(`/api/users/${userId}`);
    const user = await userResponse.json();
    const postsResponse = await fetch(`/api/posts/${user.id}`);
    const posts = await postsResponse.json();
    return posts;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
}
```

### Express.jsミドルウェア実装例
```javascript
// カスタムミドルウェア
const rateLimiter = (maxRequests, windowMs) => {
  const requests = new Map();
  
  return (req, res, next) => {
    const key = req.ip;
    const now = Date.now();
    const windowStart = now - windowMs;
    
    if (!requests.has(key)) {
      requests.set(key, []);
    }
    
    const requestTimes = requests.get(key)
      .filter(time => time > windowStart);
    
    if (requestTimes.length >= maxRequests) {
      return res.status(429).json({ 
        message: 'Too many requests' 
      });
    }
    
    requestTimes.push(now);
    requests.set(key, requestTimes);
    next();
  };
};

// 使用例
app.use('/api', rateLimiter(100, 60 * 1000)); // 1分間に100リクエスト
```

---

## 動画制作ガイドライン

### ✅ Node.js特有のポイント
1. **非同期処理**: async/awaitを基本とした実装
2. **最新機能重視**: Node.js 20+の新機能を積極採用
3. **実践的内容**: 実プロジェクトで使える内容
4. **パフォーマンス**: メモリ効率、CPU最適化
5. **セキュリティ**: 脆弱性対策、ベストプラクティス

### 📋 品質チェックリスト

#### ✅ 技術面
- [ ] Node.js公式ドキュメントと整合性がある
- [ ] 最新のNode.jsバージョンに対応
- [ ] 実行可能なコード例
- [ ] エラーハンドリングが適切
- [ ] セキュリティ対策が考慮されている

#### ✅ 内容面
- [ ] 初心者〜中級者に適した説明レベル
- [ ] 実際の開発で使える実践的内容
- [ ] 30秒で理解できる適切な情報量
- [ ] 具体的なコード例が含まれている

#### ✅ 教育面
- [ ] 段階的理解が促進される構成
- [ ] 開発者の疑問に答える内容
- [ ] 実装の注意点が明記されている
- [ ] 次のステップが示されている

---

## 実例台本

### #078「async/awaitによる非同期処理」
```
オープニング（4秒）
めたん「今日はasync/awaitによる非同期処理について学びましょう！」
ずんだもん「Promiseより簡単って聞いたことあるよ！」

メインコンテンツ（22秒）
めたん「async/awaitは同期的な書き方で非同期処理ができます。asyncを関数に付けて、awaitで待機します。」
ずんだもん「具体的にはどう書くの？」
めたん「『async function getData() { const result = await fetch('/api/data'); return result.json(); }』このように書きます。」
ずんだもん「おー！Promiseのthenチェーンより読みやすいね！」

クロージング（4秒）
めたん「これで非同期処理がスッキリ書けますね！」
ずんだもん「早速APIを書き直してみよう！」
```

### #156「Express.js vs Fastify パフォーマンス比較」
```
オープニング（4秒）
ずんだもん「Express.jsとFastify、どっちが速いの？」
めたん「ベンチマークを見ながら比較しましょう！」

メインコンテンツ（22秒）
めたん「Fastifyは毎秒76,000リクエスト、Express.jsは毎秒34,000リクエストの処理能力があります。Fastifyの方が約2倍高速ですね。」
ずんだもん「すごい差だね！なんでそんなに速いの？」
めたん「Fastifyは内部でJSONスキーマコンパイルとルーティング最適化を行うからです。ただし、Express.jsは豊富なエコシステムが魅力です。」
ずんだもん「速度重視ならFastify、安定性ならExpressって感じだね！」

クロージング（4秒）
めたん「プロジェクトの要件に合わせて選択しましょう！」
ずんだもん「パフォーマンス要件を確認してから決めよう！」
```

---

## 出力形式

### ゆっくりムービーメーカー用
```
四国めたん「発話内容」
ずんだもん「発話内容」
```

### VS Code Live Share用（開発デモ）
```javascript
// デモコードをリアルタイム編集
const express = require('express');
const app = express();

// コード解説しながら実装
app.get('/api/example', async (req, res) => {
  // 実装内容を段階的に説明
});
```

---

## 継続学習パス

### 初級者向け（1-100話）
- Node.js基礎概念
- npm/yarn使い方
- Express.js入門
- 基本的な非同期処理

### 中級者向け（101-200話）
- データベース連携
- 認証システム構築
- RESTful API設計
- テスト実装

### 上級者向け（201-300話）
- マイクロサービス設計
- パフォーマンス最適化
- セキュリティ強化
- 本番運用ノウハウ

このテンプレートにより、Node.js開発者が現場で即戦力となるスキルを30秒動画で効率的に習得できます！